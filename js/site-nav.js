(function () {
    const SUPABASE_URL = 'https://nqwggnereuhphwmkqove.supabase.co';
    const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    const NAV_PAGE_ID = 'global-nav';

    function clone(value) {
        return JSON.parse(JSON.stringify(value));
    }

    function asText(value, fallback) {
        const result = typeof value === 'string' ? value.trim() : '';
        return result || (fallback || '');
    }

    function escapeHtml(value) {
        return String(value || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function getDefaultNavContent() {
        return {
            sections: [
                {
                    id: 'navbar',
                    type: 'navbar',
                    enabled: true,
                    order: 1,
                    content: {
                        links: [
                            { label: 'Home', url: 'index.html', visible: true },
                            { label: 'How We Help You', url: 'how-we-help-you.html', visible: true },
                            { label: 'Packages', url: 'packages.html', visible: true },
                            { label: 'Tax Season Discount', url: 'tax-season-discount.html', visible: true },
                            { label: 'Support', url: 'support.html', visible: true },
                            { label: 'About Us', url: 'about-us.html', visible: true },
                            { label: 'Contact Us', url: 'contact-us.html', visible: true },
                            { label: 'Business Support Package', url: 'business-support-package.html', visible: true }
                        ],
                        utility_links: [
                            { label: 'DISCOUNT PORTAL', url: 'https://payyourselffirst.benefithub.com/Welcome', icon: 'fa-dollar-sign', visible: true, newTab: true },
                            { label: 'AFFILIATE LOGIN', url: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login', icon: 'fa-user', visible: true, newTab: true }
                        ]
                    }
                }
            ]
        };
    }

    function normalizeLink(link, index) {
        return {
            id: asText(link && link.id, 'nav-link-' + index),
            label: asText(link && link.label, ''),
            url: asText(link && link.url, ''),
            visible: typeof link?.visible === 'boolean' ? link.visible : true
        };
    }

    function normalizeUtilityLink(link, index) {
        return {
            id: asText(link && link.id, 'utility-link-' + index),
            label: asText(link && link.label, ''),
            url: asText(link && link.url, ''),
            icon: asText(link && link.icon, ''),
            visible: typeof link?.visible === 'boolean' ? link.visible : true,
            newTab: typeof link?.newTab === 'boolean' ? link.newTab : true
        };
    }

    function normalizeNavContent(content) {
        const defaults = getDefaultNavContent();
        const source = content && typeof content === 'object' ? content : {};
        const sourceSection = Array.isArray(source.sections) ? source.sections[0] : null;
        const defaultSection = defaults.sections[0];
        const linkSource = sourceSection?.content?.links;
        const utilityLinkSource = sourceSection?.content?.utility_links;
        const links = Array.isArray(linkSource)
            ? linkSource.map(normalizeLink).filter((link) => link.label || link.url)
            : clone(defaultSection.content.links).map(normalizeLink);
        const utilityLinks = Array.isArray(utilityLinkSource)
            ? utilityLinkSource.map(normalizeUtilityLink).filter((link) => link.label || link.url)
            : clone(defaultSection.content.utility_links).map(normalizeUtilityLink);

        return {
            sections: [
                {
                    id: asText(sourceSection?.id, defaultSection.id),
                    type: 'navbar',
                    enabled: typeof sourceSection?.enabled === 'boolean' ? sourceSection.enabled : true,
                    order: Number.isFinite(sourceSection?.order) ? sourceSection.order : 1,
                    content: {
                        links,
                        utility_links: utilityLinks
                    }
                }
            ]
        };
    }

    function normalizePathname(pathname) {
        const raw = String(pathname || '').split('?')[0].split('#')[0].trim();
        if (!raw || raw === '/') {
            return 'index.html';
        }

        const segments = raw.split('/').filter(Boolean);
        return (segments[segments.length - 1] || 'index.html').toLowerCase();
    }

    function normalizeHref(url) {
        const raw = asText(url, '');
        if (!raw || raw === '/') {
            return 'index.html';
        }

        if (/^(https?:|mailto:|tel:|#)/i.test(raw)) {
            return raw;
        }

        return raw.replace(/^\//, '');
    }

    function isExternalUrl(url) {
        return /^(https?:|mailto:|tel:)/i.test(String(url || ''));
    }

    function isTaxUrl(url) {
        return normalizeHref(url) === 'tax-season-discount.html';
    }

    function isBusinessUrl(url) {
        return normalizeHref(url) === 'business-support-package.html';
    }

    function isActiveLink(url) {
        if (!url) return false;
        if (url === '/' || normalizeHref(url) === 'index.html') {
            return normalizePathname(window.location.pathname) === 'index.html';
        }

        if (isExternalUrl(url) || /^#/i.test(url)) {
            return false;
        }

        return normalizePathname(window.location.pathname) === normalizeHref(url).toLowerCase();
    }

    function getDesktopLinkClass(url) {
        if (isBusinessUrl(url)) {
            return 'bg-gradient-to-r from-[#389400] to-[#75C400] text-white px-4 py-3 rounded shadow-md hover:shadow-lg hover:opacity-90 transition whitespace-nowrap';
        }

        if (isTaxUrl(url)) {
            return 'border-2 border-gray-800 px-3 py-2 hover:bg-gray-800 hover:text-white transition';
        }

        return isActiveLink(url)
            ? 'text-brand-primary transition'
            : 'hover:text-brand-primary transition';
    }

    function getMobileLinkClass(url) {
        if (isBusinessUrl(url)) {
            return 'bg-brand-primary text-white text-center py-3 rounded';
        }

        if (isTaxUrl(url)) {
            return 'border-2 border-gray-800 px-3 py-2 hover:bg-gray-800 hover:text-white transition';
        }

        return isActiveLink(url)
            ? 'text-brand-primary transition'
            : 'hover:text-brand-primary transition';
    }

    function renderLink(link, mode) {
        const href = normalizeHref(link.url);
        const className = mode === 'mobile' ? getMobileLinkClass(href) : getDesktopLinkClass(href);
        const target = isExternalUrl(href) ? ' target="_blank" rel="noopener noreferrer"' : '';
        return '<a href="' + escapeHtml(href) + '" class="' + escapeHtml(className) + '"' + target + '>' + escapeHtml(link.label) + '</a>';
    }

    function renderUtilityLink(link) {
        const href = normalizeHref(link.url);
        const openInNewTab = link.newTab || isExternalUrl(href);
        const target = openInNewTab ? ' target="_blank" rel="noopener noreferrer"' : '';
        const icon = link.icon
            ? '<div class="w-4 h-4 rounded-full bg-brand-primary flex items-center justify-center text-white mr-2 text-[10px]"><i class="fas ' + escapeHtml(link.icon) + '"></i></div>'
            : '';

        return '<a href="' + escapeHtml(href) + '" class="flex items-center hover:text-brand-primary transition"' + target + '>' + icon + escapeHtml(link.label) + '</a>';
    }

    function renderLinks(content, mode) {
        const section = Array.isArray(content?.sections) ? content.sections[0] : null;
        const links = Array.isArray(section?.content?.links) ? section.content.links : [];
        if (section && section.enabled === false) {
            return '';
        }

        return links
            .filter((link) => link.visible !== false && (link.label || link.url))
            .map((link) => renderLink(link, mode))
            .join('');
    }

    function renderUtilityLinks(content) {
        const section = Array.isArray(content?.sections) ? content.sections[0] : null;
        const links = Array.isArray(section?.content?.utility_links) ? section.content.utility_links : [];
        if (section && section.enabled === false) {
            return '';
        }

        return links
            .filter((link) => link.visible !== false && (link.label || link.url))
            .map((link) => renderUtilityLink(link))
            .join('');
    }

    async function fetchNavRecord() {
        const response = await fetch(SUPABASE_URL + '/rest/v1/site_content?select=*&page_id=eq.' + encodeURIComponent(NAV_PAGE_ID), {
            method: 'GET',
            headers: {
                apikey: SUPABASE_KEY,
                Authorization: 'Bearer ' + SUPABASE_KEY
            }
        });

        if (!response.ok) {
            throw new Error(await response.text());
        }

        const rows = await response.json();
        return Array.isArray(rows) && rows.length ? rows[0] : null;
    }

    function getResolvedContent(record) {
        if (!record) return null;
        const isPreviewMode = new URLSearchParams(window.location.search).get('mode') === 'preview';
        const rawContent = isPreviewMode
            ? record.draft_content
            : (record.published_content ?? record.live_content);

        if (!rawContent || typeof rawContent !== 'object') {
            return null;
        }

        if (!Array.isArray(rawContent.sections)) {
            return null;
        }

        return normalizeNavContent(rawContent);
    }

    async function applyGlobalNav() {
        const desktopNav = document.querySelector('[data-site-nav-desktop]');
        const mobileNav = document.querySelector('[data-site-nav-mobile]');
        const utilityNav = document.querySelector('[data-site-utility-nav]');
        if (!desktopNav && !mobileNav && !utilityNav) {
            return;
        }

        let content = getDefaultNavContent();
        try {
            const record = await fetchNavRecord();
            const resolvedContent = getResolvedContent(record);
            if (resolvedContent) {
                content = resolvedContent;
            }
        } catch (error) {
            console.error('Failed to load global nav content', error);
        }

        if (desktopNav) {
            desktopNav.innerHTML = renderLinks(content, 'desktop');
        }

        if (mobileNav) {
            mobileNav.innerHTML = renderLinks(content, 'mobile');
        }

        if (utilityNav) {
            utilityNav.innerHTML = renderUtilityLinks(content);
        }
    }

    window.addEventListener('storage', function (event) {
        if (event.key !== 'pyf-site-nav-refresh') {
            return;
        }

        applyGlobalNav();
    });

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', applyGlobalNav);
    } else {
        applyGlobalNav();
    }
})();
