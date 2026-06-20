(function () {
    const PERMANENT_ADMIN_EMAILS = new Set([
        "info@payyourselffirst.com"
    ]);
    const MANAGEABLE_ROLES = new Set([
        "admin",
        "super_admin"
    ]);

    function normalizeEmail(email) {
        return (email || '').trim().toLowerCase();
    }

    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function normalizeRole(role) {
        return String(role || 'admin').trim().toLowerCase() || 'admin';
    }

    function isPermanentAdminEmail(email) {
        return PERMANENT_ADMIN_EMAILS.has(normalizeEmail(email));
    }

    function isManageableRole(role) {
        return MANAGEABLE_ROLES.has(normalizeRole(role));
    }

    document.addEventListener('alpine:init', function () {
        Alpine.data('adminSettingsManager', function () {
            return {
                isLoading: true,
                isRefreshing: false,
                isSubmitting: false,
                hasLoadedOnce: false,
                removingAdminId: null,
                refreshPromise: null,
                updatingRoleId: null,
                showAdminPanel: false,
                currentUser: null,
                currentAdminRecord: null,
                admins: [],
                selectedRoles: {},
                auditLogs: [],
                authStateKey: '',
                statusMessage: '',
                errorMessage: '',
                successMessage: '',
                form: {
                    email: '',
                    role: 'admin'
                },

                async init() {
                    await this.refresh();

                    this.authStateKey = this.buildAuthStateKey();

                    window.addEventListener('pyf-admin-auth-changed', async (event) => {
                        const nextAuthStateKey = this.buildAuthStateKey(event.detail || {});

                        if (nextAuthStateKey === this.authStateKey) {
                            return;
                        }

                        this.authStateKey = nextAuthStateKey;
                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });
                    });
                },

                clearMessages() {
                    this.errorMessage = '';
                    this.successMessage = '';
                },

                buildAuthStateKey(detail) {
                    const authDetail = detail || {};
                    const sessionUserId = authDetail.session?.user?.id || authDetail.user?.id || '';
                    const approval = authDetail.approval || this.currentAdminRecord || window.pyfAdminApproval || null;

                    return JSON.stringify({
                        userId: sessionUserId || this.currentUser?.id || '',
                        approvalId: approval?.id || '',
                        approvalEmail: normalizeEmail(approval?.email || ''),
                        approvalRole: normalizeRole(approval?.role || '')
                    });
                },

                async getCurrentUser() {
                    const supabase = window.pyfSupabase;

                    if (!supabase) {
                        throw new Error('Supabase client is not available on this page.');
                    }

                    const { data, error } = await supabase.auth.getUser();

                    if (error) {
                        throw error;
                    }

                    return data?.user || null;
                },

                async refresh(options) {
                    const settings = Object.assign({
                        preserveVisibleState: false
                    }, options || {});

                    const preserveVisibleState = Boolean(settings.preserveVisibleState && this.hasLoadedOnce);
                    const previousState = preserveVisibleState ? {
                        showAdminPanel: this.showAdminPanel,
                        currentUser: this.currentUser,
                        currentAdminRecord: this.currentAdminRecord,
                        admins: this.admins,
                        selectedRoles: this.selectedRoles,
                        auditLogs: this.auditLogs,
                        statusMessage: this.statusMessage
                    } : null;

                    if (this.refreshPromise) {
                        return this.refreshPromise;
                    }

                    this.isLoading = !preserveVisibleState;
                    this.isRefreshing = preserveVisibleState;
                    this.clearMessages();
                    this.statusMessage = preserveVisibleState
                        ? (this.statusMessage || 'Refreshing admin access...')
                        : 'Checking admin access...';

                    this.refreshPromise = (async () => {
                        try {
                            this.currentUser = await this.getCurrentUser();

                            if (!this.currentUser) {
                                this.showAdminPanel = false;
                                this.currentAdminRecord = null;
                                this.admins = [];
                                this.auditLogs = [];
                                this.statusMessage = 'Sign in to manage admins.';
                                return;
                            }

                            console.log('Current Admin:', this.currentUser);

                            const { data, error } = await window.pyfSupabase
                                .from('admin_users')
                                .select('id, user_id, email, role, created_at, added_by, is_active, invite_status, last_invited_at, invite_sent_count, last_invite_error')
                                .order('created_at', { ascending: false });

                            if (error) {
                                throw error;
                            }

                            const rows = Array.isArray(data) ? data : [];
                            const currentEmail = normalizeEmail(this.currentUser.email);

                            this.admins = rows.map((row) => ({
                                ...row,
                                email: normalizeEmail(row.email),
                                role: normalizeRole(row.role),
                                invite_status: row.invite_status || (row.user_id ? 'active' : 'pending_auth'),
                                invite_sent_count: Number(row.invite_sent_count || 0),
                                accessLabel: row.user_id ? 'Active' : 'Pending Auth'
                            }));

                            this.selectedRoles = this.admins.reduce((accumulator, admin) => {
                                accumulator[this.adminKey(admin)] = normalizeRole(admin.role);
                                return accumulator;
                            }, {});

                            this.currentAdminRecord = this.admins.find((row) => {
                                return row.user_id === this.currentUser.id || normalizeEmail(row.email) === currentEmail;
                            }) || null;

                            this.showAdminPanel = Boolean(this.currentAdminRecord);

                            if (this.showAdminPanel) {
                                const { data: auditData, error: auditError } = await window.pyfSupabase
                                    .from('admin_audit_logs')
                                    .select('id, action, status, actor_user_id, actor_email, target_email, target_admin_user_id, details, created_at')
                                    .order('created_at', { ascending: false })
                                    .limit(100);

                                if (auditError) {
                                    throw auditError;
                                }

                                this.auditLogs = Array.isArray(auditData) ? auditData : [];
                            } else {
                                this.auditLogs = [];
                            }

                            this.statusMessage = this.showAdminPanel
                                ? (this.isSuperAdmin()
                                    ? 'Super admins can add, remove, and update admin roles here.'
                                    : 'Approved admins can review access here. Only super admins can add, remove, or change roles.')
                                : 'Your account is authenticated, but it is not approved in admin_users.';

                            this.hasLoadedOnce = true;
                            this.authStateKey = this.buildAuthStateKey();
                        } catch (error) {
                            console.error('Failed to load admin settings', error);

                            if (previousState) {
                                this.showAdminPanel = previousState.showAdminPanel;
                                this.currentUser = previousState.currentUser;
                                this.currentAdminRecord = previousState.currentAdminRecord;
                                this.admins = previousState.admins;
                                this.selectedRoles = previousState.selectedRoles;
                                this.auditLogs = previousState.auditLogs;
                                this.statusMessage = previousState.statusMessage;
                            } else {
                                this.showAdminPanel = false;
                                this.currentAdminRecord = null;
                                this.admins = [];
                                this.auditLogs = [];
                                this.statusMessage = 'Admin settings are unavailable until the latest Supabase SQL is applied.';
                            }

                            this.errorMessage = error.message || 'Unable to load admin settings.';
                        } finally {
                            this.isLoading = false;
                            this.isRefreshing = false;
                            this.refreshPromise = null;
                        }
                    })();

                    return this.refreshPromise;
                },

                async addAdmin() {
                    this.clearMessages();

                    const email = normalizeEmail(this.form.email);
                    const requestedRole = normalizeRole(this.form.role);
                    console.log('Adding Admin:', email);

                    if (!email || !isValidEmail(email)) {
                        this.errorMessage = 'Please enter a valid admin email.';
                        return;
                    }

                    if (!this.canManageAdminUsers()) {
                        this.errorMessage = 'Only super admins can manage admin access.';
                        return;
                    }

                    if (!isManageableRole(requestedRole)) {
                        this.errorMessage = 'Please choose a valid admin role.';
                        return;
                    }

                    this.isSubmitting = true;

                    try {
                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });

                        if (!this.currentUser) {
                            this.errorMessage = 'You must be signed in to manage admin access.';
                            return;
                        }

                        if (!this.showAdminPanel || !this.currentAdminRecord) {
                            this.errorMessage = 'Only approved admins can manage admin access.';
                            return;
                        }

                        const sessionResult = await window.pyfSupabase.auth.getSession();
                        const session = sessionResult.data?.session || null;

                        if (!session?.access_token) {
                            this.errorMessage = 'Your admin session expired. Please sign in again.';
                            return;
                        }

                        const response = await fetch(`${window.PYF_SUPABASE_URL}/functions/v1/admin-invite`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                apikey: window.PYF_SUPABASE_KEY,
                                Authorization: `Bearer ${session.access_token}`
                            },
                            body: JSON.stringify({
                                email: email,
                                role: requestedRole
                            })
                        });

                        const result = await response.json().catch(() => ({}));

                        if (!response.ok) {
                            this.errorMessage = result.error || result.message || `Unable to manage admin access (${response.status}).`;
                            return;
                        }

                        this.form.email = '';
                        this.form.role = 'admin';
                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });
                        this.successMessage = result.message || 'Admin email approved successfully.';
                    } catch (error) {
                        console.error('Failed to manage admin access', error);
                        this.errorMessage = error.message || 'Unable to manage admin access.';
                    } finally {
                        this.isSubmitting = false;
                    }
                },

                isCurrentAdmin(admin) {
                    if (!admin) {
                        return false;
                    }

                    const currentEmail = normalizeEmail(this.currentUser?.email);
                    return admin.user_id === this.currentUser?.id || normalizeEmail(admin.email) === currentEmail;
                },

                isProtectedAdmin(admin) {
                    return Boolean(admin && isPermanentAdminEmail(admin.email));
                },

                adminKey(admin) {
                    return admin?.id || normalizeEmail(admin?.email) || '';
                },

                isSuperAdmin() {
                    return Boolean(this.currentAdminRecord) && (
                        normalizeRole(this.currentAdminRecord.role) === 'super_admin'
                        || this.isProtectedAdmin(this.currentAdminRecord)
                    );
                },

                canManageAdminUsers() {
                    return Boolean(this.showAdminPanel && this.isSuperAdmin());
                },

                canRemoveAdmin(admin) {
                    return Boolean(this.canManageAdminUsers() && admin?.id && !this.isCurrentAdmin(admin) && !this.isProtectedAdmin(admin));
                },

                canChangeRole(admin) {
                    return Boolean(this.canManageAdminUsers() && admin?.id && !this.isCurrentAdmin(admin) && !this.isProtectedAdmin(admin));
                },

                selectedRoleFor(admin) {
                    return normalizeRole(this.selectedRoles[this.adminKey(admin)] || admin?.role || 'admin');
                },

                roleChanged(admin) {
                    return this.selectedRoleFor(admin) !== normalizeRole(admin?.role || 'admin');
                },

                setSelectedRole(admin, role) {
                    const key = this.adminKey(admin);
                    this.selectedRoles = {
                        ...this.selectedRoles,
                        [key]: normalizeRole(role)
                    };
                },

                formatRole(role) {
                    const normalized = normalizeRole(role);
                    const labels = {
                        admin: 'Admin',
                        super_admin: 'Super Admin',
                        editor: 'Editor',
                        publisher: 'Publisher'
                    };

                    return labels[normalized] || normalized;
                },

                removalDisabledLabel(admin) {
                    if (this.isCurrentAdmin(admin)) {
                        return 'Current account';
                    }

                    if (this.isProtectedAdmin(admin)) {
                        return 'Permanent admin';
                    }

                    if (!this.canManageAdminUsers()) {
                        return 'Super admin only';
                    }

                    return 'Protected';
                },

                roleDisabledLabel(admin) {
                    if (this.isCurrentAdmin(admin)) {
                        return 'Current role';
                    }

                    if (this.isProtectedAdmin(admin)) {
                        return 'Permanent super admin';
                    }

                    if (!this.canManageAdminUsers()) {
                        return 'Super admin only';
                    }

                    return 'Locked';
                },

                async removeAdmin(admin) {
                    this.clearMessages();

                    if (this.isProtectedAdmin(admin)) {
                        this.errorMessage = 'info@payyourselffirst.com is the permanent admin and cannot be removed.';
                        return;
                    }

                    if (!this.canRemoveAdmin(admin)) {
                        this.errorMessage = 'You cannot remove your own admin account from this screen.';
                        return;
                    }

                    const confirmed = window.confirm(`Remove admin access for ${admin.email || 'this admin'}? This will block CMS access until they are added again.`);

                    if (!confirmed) {
                        return;
                    }

                    this.removingAdminId = admin.id;

                    try {
                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });

                        if (!this.currentUser) {
                            this.errorMessage = 'You must be signed in to manage admin access.';
                            return;
                        }

                        if (!this.showAdminPanel || !this.currentAdminRecord) {
                            this.errorMessage = 'Only approved admins can manage admin access.';
                            return;
                        }

                        const sessionResult = await window.pyfSupabase.auth.getSession();
                        const session = sessionResult.data?.session || null;

                        if (!session?.access_token) {
                            this.errorMessage = 'Your admin session expired. Please sign in again.';
                            return;
                        }

                        const response = await fetch(`${window.PYF_SUPABASE_URL}/functions/v1/admin-remove`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                apikey: window.PYF_SUPABASE_KEY,
                                Authorization: `Bearer ${session.access_token}`
                            },
                            body: JSON.stringify({
                                id: admin.id,
                                email: admin.email
                            })
                        });

                        const result = await response.json().catch(() => ({}));

                        if (!response.ok) {
                            this.errorMessage = result.error || result.message || `Unable to remove admin access (${response.status}).`;
                            return;
                        }

                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });
                        this.successMessage = result.message || 'Admin access removed successfully.';
                    } catch (error) {
                        console.error('Failed to remove admin access', error);
                        this.errorMessage = error.message || 'Unable to remove admin access.';
                    } finally {
                        this.removingAdminId = null;
                    }
                },

                async updateAdminRole(admin) {
                    this.clearMessages();

                    if (!this.canChangeRole(admin)) {
                        this.errorMessage = 'Only super admins can change admin roles from this screen.';
                        return;
                    }

                    const requestedRole = this.selectedRoleFor(admin);

                    if (!isManageableRole(requestedRole)) {
                        this.errorMessage = 'Please choose a valid admin role.';
                        return;
                    }

                    if (!this.roleChanged(admin)) {
                        this.successMessage = 'That admin already has this role.';
                        return;
                    }

                    this.updatingRoleId = admin.id;

                    try {
                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });

                        if (!this.currentUser) {
                            this.errorMessage = 'You must be signed in to manage admin roles.';
                            return;
                        }

                        if (!this.canChangeRole(admin)) {
                            this.errorMessage = 'Only super admins can change admin roles from this screen.';
                            return;
                        }

                        const sessionResult = await window.pyfSupabase.auth.getSession();
                        const session = sessionResult.data?.session || null;

                        if (!session?.access_token) {
                            this.errorMessage = 'Your admin session expired. Please sign in again.';
                            return;
                        }

                        const refreshedAdmin = this.admins.find((row) => this.adminKey(row) === this.adminKey(admin)) || admin;
                        const response = await fetch(`${window.PYF_SUPABASE_URL}/functions/v1/admin-update-role`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                apikey: window.PYF_SUPABASE_KEY,
                                Authorization: `Bearer ${session.access_token}`
                            },
                            body: JSON.stringify({
                                id: refreshedAdmin.id,
                                email: refreshedAdmin.email,
                                role: requestedRole
                            })
                        });

                        const result = await response.json().catch(() => ({}));

                        if (!response.ok) {
                            this.errorMessage = result.error || result.message || `Unable to update admin role (${response.status}).`;
                            return;
                        }

                        await this.refresh({ preserveVisibleState: this.hasLoadedOnce });
                        this.successMessage = result.message || 'Admin role updated successfully.';
                    } catch (error) {
                        console.error('Failed to update admin role', error);
                        this.errorMessage = error.message || 'Unable to update admin role.';
                    } finally {
                        this.updatingRoleId = null;
                    }
                },

                inviteStatusClass(admin) {
                    if (admin?.user_id || admin?.invite_status === 'active') {
                        return 'bg-emerald-50 text-emerald-700';
                    }

                    return 'bg-amber-50 text-amber-700';
                },

                formatDate(value) {
                    if (!value) {
                        return '-';
                    }

                    const parsed = new Date(value);

                    if (Number.isNaN(parsed.getTime())) {
                        return value;
                    }

                    return parsed.toLocaleString();
                },

                resolveAddedBy(row) {
                    if (!row?.added_by) {
                        return 'System';
                    }

                    const matchingAdmin = this.admins.find((admin) => admin.user_id === row.added_by);

                    if (matchingAdmin?.email) {
                        return matchingAdmin.email;
                    }

                    if (this.currentUser?.id === row.added_by) {
                        return normalizeEmail(this.currentUser.email) || 'Current admin';
                    }

                    return row.added_by;
                },

                formatAuditAction(action) {
                    const labels = {
                        admin_access_created: 'Approved Admin Email Added',
                        admin_access_duplicate: 'Duplicate Admin Blocked',
                        admin_access_create_failed: 'Admin Approval Failed',
                        admin_role_updated: 'Admin Role Updated',
                        admin_role_update_blocked: 'Admin Role Change Blocked',
                        admin_role_update_failed: 'Admin Role Update Failed',
                        admin_access_removed: 'Admin Access Removed',
                        admin_access_remove_blocked: 'Admin Removal Blocked',
                        admin_access_remove_failed: 'Admin Removal Failed',
                        admin_self_register_created: 'Password Created',
                        admin_self_register_failed: 'Password Setup Failed',
                        admin_self_register_blocked: 'Password Setup Blocked',
                        admin_claim_activated: 'Pending Admin Activated',
                        content_draft_saved: 'Draft Saved',
                        content_published: 'Published Live'
                    };

                    return labels[action] || action || 'Unknown Action';
                },

                isContentAuditLog(log) {
                    const auditHelper = window.pyfAdminContentAudit;

                    if (auditHelper?.isContentAction) {
                        return auditHelper.isContentAction(log?.action);
                    }

                    return /^content_/i.test(log?.action || '');
                },

                contentAuditLogs() {
                    return this.auditLogs.filter((log) => this.isContentAuditLog(log));
                },

                adminAccessAuditLogs() {
                    return this.auditLogs.filter((log) => !this.isContentAuditLog(log));
                },

                auditStatusClass(status) {
                    const value = (status || '').toLowerCase();

                    if (value === 'success') {
                        return 'bg-emerald-50 text-emerald-700';
                    }

                    if (value === 'error') {
                        return 'bg-red-50 text-red-700';
                    }

                    if (value === 'blocked') {
                        return 'bg-amber-50 text-amber-700';
                    }

                    return 'bg-gray-100 text-gray-700';
                },

                describeAuditTarget(log) {
                    if (this.isContentAuditLog(log)) {
                        return this.resolveAuditPage(log);
                    }

                    if (log?.target_email) {
                        return log.target_email;
                    }

                    if (log?.target_admin_user_id) {
                        return log.target_admin_user_id;
                    }

                    return '-';
                },

                describeAuditActor(log) {
                    if (log?.actor_email) {
                        return log.actor_email;
                    }

                    if (log?.actor_user_id) {
                        return log.actor_user_id;
                    }

                    return 'System';
                },

                resolveAuditPage(log) {
                    const details = log?.details;

                    if (details?.page_name) {
                        return String(details.page_name);
                    }

                    if (details?.page_id) {
                        const auditHelper = window.pyfAdminContentAudit;

                        if (auditHelper?.pageLabel) {
                            return auditHelper.pageLabel(details.page_id);
                        }

                        return String(details.page_id);
                    }

                    return '-';
                },

                getAuditChanges(log) {
                    const changes = log?.details?.changes;
                    return Array.isArray(changes) ? changes : [];
                },

                contentAuditSummary(log) {
                    const details = log?.details || {};
                    const changeCount = Number(details.change_count || this.getAuditChanges(log).length || 0);

                    if (!changeCount) {
                        return 'No field-level differences were captured for this update.';
                    }

                    if (details.is_truncated) {
                        return `${this.getAuditChanges(log).length} of ${changeCount} field changes shown.`;
                    }

                    return `${changeCount} field change${changeCount === 1 ? '' : 's'} recorded.`;
                },

                formatAuditChangePath(path) {
                    if (!path) {
                        return 'Field';
                    }

                    return String(path)
                        .replace(/\.(\d+)/g, '[$1]')
                        .replace(/\./g, ' / ')
                        .replace(/_/g, ' ');
                },

                formatAuditValue(value) {
                    if (value === null || typeof value === 'undefined' || value === '') {
                        return '(empty)';
                    }

                    return String(value);
                },

                describeAuditDetails(log) {
                    const details = log?.details;

                    if (!details || typeof details !== 'object') {
                        return '-';
                    }

                    if (this.isContentAuditLog(log)) {
                        return this.contentAuditSummary(log);
                    }

                    if (details.error) {
                        return String(details.error);
                    }

                    if (details.reason) {
                        const reasonLabels = {
                            existing_active_admin: 'That email already has active admin access.',
                            pending_admin_already_exists: 'That email is already pending admin access.',
                            permanent_admin_protected: 'That admin email is permanent and cannot be removed.',
                            super_admin_required: 'Only super admins can manage admin access or change roles.',
                            self_role_change_attempt: 'Admins cannot change their own role from this screen.',
                            self_removal_attempt: 'Admins cannot remove their own account.',
                            target_not_found: 'The admin record no longer exists.'
                        };

                        return reasonLabels[details.reason] || String(details.reason);
                    }

                    if (details.message) {
                        return String(details.message);
                    }

                    if (details.previous_role || details.new_role || details.assigned_role) {
                        const parts = [];

                        if (details.previous_role) {
                            parts.push(`From ${this.formatRole(details.previous_role)}`);
                        }

                        if (details.new_role) {
                            parts.push(`To ${this.formatRole(details.new_role)}`);
                        }

                        if (details.assigned_role) {
                            parts.push(`Assigned ${this.formatRole(details.assigned_role)}`);
                        }

                        if (parts.length > 0) {
                            return parts.join(' | ');
                        }
                    }

                    if (typeof details.invite_sent_count !== 'undefined') {
                        return `Invite count: ${details.invite_sent_count}`;
                    }

                    if (details.source) {
                        return `Source: ${details.source}`;
                    }

                    return '-';
                },

                describeSetupState(admin) {
                    if (admin?.user_id || admin?.invite_status === 'active') {
                        return 'Password created and access active.';
                    }

                    if (admin?.invite_status === 'existing_auth') {
                        return 'Auth account exists. User can sign in to activate access.';
                    }

                    return 'Waiting for the approved admin to create a password from the login page.';
                }
            };
        });
    });
})();
