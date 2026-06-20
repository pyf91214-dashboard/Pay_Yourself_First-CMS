(function () {
    const MAX_STORED_CHANGES = 8;
    const MAX_VALUE_LENGTH = 180;
    const ACTION_DRAFT_SAVED = 'content_draft_saved';
    const ACTION_PUBLISHED = 'content_published';
    const PAGE_LABELS = {
        home: 'Home',
        how_we_help_you: 'How We Help You',
        packages: 'Packages',
        tax: 'Tax Season Discount',
        support: 'Support',
        affiliate: 'Affiliate Plan',
        about_us: 'About Us',
        'purchase-power': 'Purchase Power',
        'dental-power': 'Dental Power',
        'doctor-power': 'Doctor Power',
        footer: 'Footer',
        'global-nav': 'Global Navigation',
        contact_us: 'Contact Us',
        business: 'Business Support Package',
        'business-support-package': 'Business Support Package'
    };

    function isPlainObject(value) {
        return Object.prototype.toString.call(value) === '[object Object]';
    }

    function normalizePageId(pageId) {
        return String(pageId || '')
            .trim()
            .toLowerCase();
    }

    function pageLabel(pageId) {
        const normalized = normalizePageId(pageId);
        return PAGE_LABELS[normalized] || normalized || 'Unknown Page';
    }

    function shortenText(value, maxLength) {
        if (value.length <= maxLength) {
            return value;
        }

        return `${value.slice(0, maxLength - 3)}...`;
    }

    function summarizeValue(value) {
        if (typeof value === 'undefined') {
            return '(empty)';
        }

        if (value === null) {
            return 'null';
        }

        if (typeof value === 'string') {
            const normalized = value.replace(/\s+/g, ' ').trim();
            return shortenText(normalized || '(empty)', MAX_VALUE_LENGTH);
        }

        if (typeof value === 'number' || typeof value === 'boolean') {
            return String(value);
        }

        try {
            return shortenText(JSON.stringify(value), MAX_VALUE_LENGTH);
        } catch (_error) {
            return shortenText(String(value), MAX_VALUE_LENGTH);
        }
    }

    function areEqual(left, right) {
        if (left === right) {
            return true;
        }

        if (typeof left !== typeof right) {
            return false;
        }

        if (Array.isArray(left) && Array.isArray(right)) {
            if (left.length !== right.length) {
                return false;
            }

            for (let index = 0; index < left.length; index += 1) {
                if (!areEqual(left[index], right[index])) {
                    return false;
                }
            }

            return true;
        }

        if (isPlainObject(left) && isPlainObject(right)) {
            const leftKeys = Object.keys(left).sort();
            const rightKeys = Object.keys(right).sort();

            if (leftKeys.length !== rightKeys.length) {
                return false;
            }

            for (let index = 0; index < leftKeys.length; index += 1) {
                const key = leftKeys[index];

                if (key !== rightKeys[index]) {
                    return false;
                }

                if (!areEqual(left[key], right[key])) {
                    return false;
                }
            }

            return true;
        }

        return false;
    }

    function pathToString(segments) {
        return segments.reduce((path, segment) => {
            if (typeof segment === 'number') {
                return `${path}[${segment}]`;
            }

            return path ? `${path}.${segment}` : segment;
        }, '');
    }

    function collectChanges(beforeValue, afterValue, pathSegments, state, limit) {
        if (areEqual(beforeValue, afterValue)) {
            return;
        }

        if (Array.isArray(beforeValue) && Array.isArray(afterValue)) {
            const maxLength = Math.max(beforeValue.length, afterValue.length);

            for (let index = 0; index < maxLength; index += 1) {
                collectChanges(beforeValue[index], afterValue[index], pathSegments.concat(index), state, limit);
            }

            return;
        }

        if (isPlainObject(beforeValue) && isPlainObject(afterValue)) {
            const keys = Array.from(new Set([
                ...Object.keys(beforeValue),
                ...Object.keys(afterValue)
            ])).sort();

            keys.forEach((key) => {
                collectChanges(beforeValue[key], afterValue[key], pathSegments.concat(key), state, limit);
            });

            return;
        }

        state.changeCount += 1;

        if (state.changes.length < limit) {
            state.changes.push({
                path: pathToString(pathSegments) || '(root)',
                before: summarizeValue(beforeValue),
                after: summarizeValue(afterValue)
            });
            return;
        }

        state.isTruncated = true;
    }

    function buildDiff(beforeValue, afterValue, limit = MAX_STORED_CHANGES) {
        const state = {
            changes: [],
            changeCount: 0,
            isTruncated: false
        };

        collectChanges(beforeValue, afterValue, [], state, limit);
        return state;
    }

    async function logChange(supabase, options) {
        if (!supabase || typeof supabase.rpc !== 'function') {
            return { logged: false, reason: 'missing_supabase_client' };
        }

        const mode = options?.mode === 'publish' ? 'publish' : 'draft';
        const normalizedPageId = normalizePageId(options?.pageId);
        const resolvedPageName = options?.pageName || pageLabel(normalizedPageId);
        const diff = mode === 'publish'
            ? buildDiff(options?.beforeLive, options?.afterLive, options?.maxStoredChanges)
            : buildDiff(options?.beforeDraft, options?.afterDraft, options?.maxStoredChanges);

        if (!diff.changeCount) {
            return { logged: false, reason: 'no_changes', diff };
        }

        const metadata = {
            page_id: normalizedPageId,
            page_name: resolvedPageName,
            change_scope: mode === 'publish' ? 'live' : 'draft',
            change_count: diff.changeCount,
            is_truncated: diff.isTruncated,
            changed_fields: diff.changes.map((change) => change.path),
            ...(options?.metadata && typeof options.metadata === 'object' ? options.metadata : {})
        };

        const { data, error } = await supabase.rpc('log_admin_content_change', {
            p_action: mode === 'publish' ? ACTION_PUBLISHED : ACTION_DRAFT_SAVED,
            p_page_id: normalizedPageId,
            p_page_name: resolvedPageName,
            p_status: 'success',
            p_changes: diff.changes,
            p_metadata: metadata
        });

        if (error) {
            console.error('Failed to write admin content audit log', error);
            return { logged: false, reason: 'rpc_error', error, diff };
        }

        return {
            logged: true,
            id: data || null,
            diff,
            action: mode === 'publish' ? ACTION_PUBLISHED : ACTION_DRAFT_SAVED,
            pageId: normalizedPageId,
            pageName: resolvedPageName
        };
    }

    window.pyfAdminContentAudit = {
        ACTION_DRAFT_SAVED,
        ACTION_PUBLISHED,
        buildDiff,
        isContentAction(action) {
            return action === ACTION_DRAFT_SAVED || action === ACTION_PUBLISHED;
        },
        logChange,
        normalizePageId,
        pageLabel
    };
})();
