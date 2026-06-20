(function () {
    const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    const loginPage = 'admin-login.html';
    const invitePage = 'admin-accept-invite.html';
    const resetPage = 'admin-reset.html';
    const adminPage = 'admin.html';
    const currentPage = (window.location.pathname.split('/').pop() || '').toLowerCase();
    const isLoginPage = currentPage === loginPage;
    const isInvitePage = currentPage === invitePage;
    const isResetPage = currentPage === resetPage;
    const redirectParam = new URLSearchParams(window.location.search).get('redirect');
    let adminClaimWarningShown = false;
    let approvalCheckInFlight = false;

    function normalizeEmail(email) {
        return (email || '').trim().toLowerCase();
    }

    const supabaseClient = window.supabase.createClient(supabaseUrl, supabaseKey, {
        auth: {
            persistSession: true,
            autoRefreshToken: true,
            detectSessionInUrl: true
        }
    });

    function getRedirectTarget() {
        if (!redirectParam) {
            return adminPage;
        }

        if (/^https?:\/\//i.test(redirectParam)) {
            return adminPage;
        }

        return redirectParam;
    }

    function markReady() {
        if (document.body) {
            document.body.removeAttribute('data-auth-pending');
        }
    }

    function markPending() {
        if (document.body) {
            document.body.setAttribute('data-auth-pending', 'true');
        }
    }

    function redirectToLogin() {
        const currentPath = `${window.location.pathname.split('/').pop() || adminPage}${window.location.search}${window.location.hash}`;
        window.location.replace(`${loginPage}?redirect=${encodeURIComponent(currentPath)}`);
    }

    function redirectToUnauthorizedLogin() {
        const params = new URLSearchParams();

        if (!isLoginPage) {
            const currentPath = `${window.location.pathname.split('/').pop() || adminPage}${window.location.search}${window.location.hash}`;
            params.set('redirect', currentPath);
        }

        params.set('error', 'not-approved');
        window.location.replace(`${loginPage}?${params.toString()}`);
    }

    function broadcastAdminAuthState(session, approvedAdmin) {
        window.dispatchEvent(new CustomEvent('pyf-admin-auth-changed', {
            detail: {
                session: session || null,
                user: session?.user || null,
                approval: approvedAdmin || null
            }
        }));
    }

    async function claimAdminUser(session) {
        if (!session?.user) {
            return null;
        }

        const { data, error } = await supabaseClient.rpc('claim_admin_user');

        if (error) {
            const errorMessage = error.message || '';
            const missingFunction = error.code === 'PGRST202' || /claim_admin_user/i.test(errorMessage);

            if (!missingFunction && !adminClaimWarningShown) {
                console.warn('Failed to claim admin user row', error);
                adminClaimWarningShown = true;
            }

            return null;
        }

        return data || null;
    }

    async function ensureApprovedAdminSession(session, options) {
        const settings = Object.assign({
            signOutOnFailure: true,
            redirectOnFailure: false
        }, options || {});

        if (!session?.user) {
            return null;
        }

        const approvedAdmin = await claimAdminUser(session);

        if (approvedAdmin) {
            window.pyfAdminApproval = approvedAdmin;
            broadcastAdminAuthState(session, approvedAdmin);
            return approvedAdmin;
        }

        window.pyfAdminApproval = null;
        broadcastAdminAuthState(session, null);

        if (settings.signOutOnFailure) {
            await supabaseClient.auth.signOut();
        }

        if (settings.redirectOnFailure) {
            redirectToUnauthorizedLogin();
        }

        return null;
    }

    async function verifyCurrentApproval(options) {
        if (approvalCheckInFlight || isLoginPage || isInvitePage || isResetPage) {
            return null;
        }

        approvalCheckInFlight = true;

        try {
            const { data, error } = await supabaseClient.auth.getSession();

            if (error) {
                console.error('Failed to verify admin approval', error);
                return null;
            }

            const session = data?.session || null;

            if (!session?.user) {
                redirectToLogin();
                return null;
            }

            return await ensureApprovedAdminSession(session, Object.assign({
                signOutOnFailure: true,
                redirectOnFailure: true
            }, options || {}));
        } finally {
            approvalCheckInFlight = false;
        }
    }

    async function guardPage() {
        if (!isLoginPage && !isInvitePage && !isResetPage) {
            markPending();
        }

        const { data, error } = await supabaseClient.auth.getSession();
        if (error) {
            console.error('Failed to read admin session', error);
        }

        const session = data?.session || null;
        window.pyfAdminSession = session;
        window.pyfAdminUser = session?.user || null;
        window.pyfAdminApproval = null;

        if (!session) {
            if (isLoginPage || isInvitePage || isResetPage) {
                markReady();
                return null;
            }

            redirectToLogin();
            return null;
        }

        if (isLoginPage) {
            const approvedAdmin = await ensureApprovedAdminSession(session, {
                signOutOnFailure: true,
                redirectOnFailure: false
            });

            if (!approvedAdmin) {
                markReady();
                return null;
            }

            window.location.replace(getRedirectTarget());
            return session;
        }

        if (!isInvitePage && !isResetPage) {
            const approvedAdmin = await ensureApprovedAdminSession(session, {
                signOutOnFailure: true,
                redirectOnFailure: true
            });

            if (!approvedAdmin) {
                return null;
            }
        } else {
            await claimAdminUser(session);
        }

        markReady();
        return session;
    }

    window.PYF_SUPABASE_URL = supabaseUrl;
    window.PYF_SUPABASE_KEY = supabaseKey;
    window.pyfSupabase = supabaseClient;
    window.pyfAdminApproval = window.pyfAdminApproval || null;
    window.pyfGuardAdminPage = guardPage;
    window.pyfEnsureApprovedAdminSession = async function () {
        const { data, error } = await supabaseClient.auth.getSession();

        if (error) {
            return {
                ok: false,
                reason: 'session_error',
                error: error
            };
        }

        const session = data?.session || null;

        if (!session) {
            return {
                ok: false,
                reason: 'no_session'
            };
        }

        const approvedAdmin = await ensureApprovedAdminSession(session, {
            signOutOnFailure: true,
            redirectOnFailure: false
        });

        if (!approvedAdmin) {
            return {
                ok: false,
                reason: 'not_approved'
            };
        }

        return {
            ok: true,
            admin: approvedAdmin
        };
    };
    window.sendPasswordReset = async function (email) {
        const normalizedEmail = normalizeEmail(email);

        if (!normalizedEmail) {
            return {
                ok: false,
                error: 'Please enter your email address.'
            };
        }

        const response = await fetch(`${supabaseUrl}/functions/v1/admin-password-reset`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                apikey: supabaseKey,
                Authorization: `Bearer ${supabaseKey}`
            },
            body: JSON.stringify({
                email: normalizedEmail,
                redirectTo: `${window.location.origin}/admin-reset.html`
            })
        });

        const result = await response.json().catch(() => ({}));

        if (!response.ok) {
            return {
                ok: false,
                error: result.error || result.message || 'Unable to send password reset email.'
            };
        }

        return {
            ok: true,
            message: result.message || 'Password reset email sent.'
        };
    };
    window.pyfAdminLogout = async function () {
        await supabaseClient.auth.signOut();
        window.location.replace(loginPage);
    };

    supabaseClient.auth.onAuthStateChange(function (_event, session) {
        window.pyfAdminSession = session || null;
        window.pyfAdminUser = session?.user || null;
        if (!session) {
            window.pyfAdminApproval = null;
        }

        window.dispatchEvent(new CustomEvent('pyf-admin-auth-changed', {
            detail: {
                session: session || null,
                user: session?.user || null,
                approval: window.pyfAdminApproval || null
            }
        }));

        if (!session && !isLoginPage && !isInvitePage && !isResetPage) {
            redirectToLogin();
            return;
        }

        if (session?.user && !isInvitePage && !isResetPage) {
            ensureApprovedAdminSession(session, {
                signOutOnFailure: true,
                redirectOnFailure: !isLoginPage
            }).then(function (approvedAdmin) {
                if (approvedAdmin && isLoginPage) {
                    window.location.replace(getRedirectTarget());
                }
            });
        }

        if (isInvitePage || isResetPage) {
            markReady();
        }
    });

    document.addEventListener('DOMContentLoaded', function () {
        guardPage();

        if (!isLoginPage && !isInvitePage && !isResetPage) {
            window.setInterval(function () {
                verifyCurrentApproval();
            }, 15000);

            window.addEventListener('focus', function () {
                verifyCurrentApproval();
            });

            document.addEventListener('visibilitychange', function () {
                if (!document.hidden) {
                    verifyCurrentApproval();
                }
            });
        }
    });
})();
