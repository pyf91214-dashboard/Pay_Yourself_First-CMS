(function () {
    const SUPABASE_URL = 'https://nqwggnereuhphwmkqove.supabase.co';
    const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    const FOOTER_PAGE_ID = 'footer';
    const CACHE_KEY_PREFIX = 'pyf-footer-cache';

    function createId(prefix) {
        return prefix + '-' + Math.random().toString(36).slice(2, 10);
    }

    function getDefaultFooterData() {
        return {
            brand_name: 'Pay Yourself First',
            sections: [
                {
                    id: 'find-us',
                    type: 'contact',
                    title: 'Find Us',
                    phone: '+1 (855) 793-2582',
                    email: 'service@payyourselffirst.com'
                },
                {
                    id: 'legal',
                    type: 'links',
                    title: 'Legal',
                    items: [
                        { id: 'terms', text: 'Terms & Conditions', url: 'terms.html', new_tab: true },
                        { id: 'privacy', text: 'Privacy Policy', url: 'privacy.html', new_tab: true },
                        { id: 'cookie', text: 'Cookie Policy', url: 'cookie.html', new_tab: true },
                        { id: 'disclaimer', text: 'Disclaimer', url: 'disclaimer.html', new_tab: true },
                        { id: 'use-policy', text: 'Acceptable Use Policy', url: 'use-policy.html', new_tab: true }
                    ]
                },
                {
                    id: 'quick-links',
                    type: 'links',
                    title: 'Quick Links',
                    items: [
                        { id: 'affiliate', text: 'Become an Affiliate', url: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm', new_tab: true },
                        { id: 'join', text: 'Join Now', url: 'packages.html', new_tab: true },
                        { id: 'contact', text: 'Contact Us', url: 'contact-us.html', new_tab: true }
                    ]
                }
            ],
            social_links: [
                { id: 'facebook', label: 'Facebook', icon: 'fa-facebook-f', url: 'https://www.facebook.com/share/1SgQW8W1qQ/?mibextid=wwXIfr' },
                { id: 'twitter', label: 'Twitter / X', icon: 'fa-twitter', url: 'https://x.com/pyfinc' },
                { id: 'instagram', label: 'Instagram', icon: 'fa-instagram', url: 'https://www.instagram.com/pay_yourself_first_inc' },
                { id: 'linkedin', label: 'LinkedIn', icon: 'fa-linkedin-in', url: 'https://www.linkedin.com/company/pay-yourself-first-inc/about/?viewAsMember=true' }
            ],
            copyright_text: 'Copyright © 2025 - Pay Yourself First. All Rights Reserved.',
            bottom_note: 'Powered By SapphireLead © 2025'
        };
    }

    function clone(value) {
        return JSON.parse(JSON.stringify(value));
    }

    function asText(value, fallback) {
        const result = typeof value === 'string' ? value.trim() : '';
        return result || fallback || '';
    }

    function normalizeLinkItem(item, index) {
        const url = asText(item && (item.url || item.href), '');
        return {
            id: asText(item && item.id, createId('footer-item-' + index)),
            text: asText(item && (item.text || item.label || item.content), ''),
            url,
            new_tab: typeof item?.new_tab === 'boolean' ? item.new_tab : /^https?:\/\//i.test(url)
        };
    }

    function normalizeContactItem(item, index) {
        return {
            id: asText(item && item.id, createId('footer-contact-' + index)),
            phone: asText(item && item.phone, ''),
            email: asText(item && item.email, '')
        };
    }

    function normalizeSection(section, index) {
        const type = section && section.type === 'contact' ? 'contact' : 'links';
        if (type === 'contact') {
            const items = Array.isArray(section && section.items) && section.items.length
                ? section.items.map(normalizeContactItem).filter((item) => item.phone || item.email)
                : [normalizeContactItem({
                    phone: section && section.phone,
                    email: section && section.email
                }, index)].filter((item) => item.phone || item.email);

            return {
                id: asText(section && section.id, createId('footer-section-' + index)),
                type,
                title: asText(section && section.title, 'Find Us'),
                phone: items[0] ? items[0].phone : asText(section && section.phone, ''),
                email: items[0] ? items[0].email : asText(section && section.email, ''),
                items
            };
        }

        const items = Array.isArray(section && section.items)
            ? section.items.map(normalizeLinkItem).filter((item) => item.text || item.url)
            : [];

        return {
            id: asText(section && section.id, createId('footer-section-' + index)),
            type,
            title: asText(section && section.title, 'New Section'),
            items
        };
    }

    function normalizeFooterData(data) {
        const defaults = getDefaultFooterData();
        const source = data && typeof data === 'object' ? data : {};
        const sections = Array.isArray(source.sections) && source.sections.length
            ? source.sections.map(normalizeSection)
            : defaults.sections.map(normalizeSection);
        const socialSource = Array.isArray(source.social_links)
            ? source.social_links
            : Array.isArray(source.social)
                ? source.social
                : Object.entries(source.social_links || source.social || {}).map(([key, url]) => ({
                    id: key,
                    label: key,
                    icon: key === 'linkedin' ? 'fa-linkedin-in' : `fa-${key === 'twitter' ? 'twitter' : key}`,
                    url
                }));
        const socialLinks = (socialSource.length ? socialSource : defaults.social_links)
            .map((item, index) => ({
                id: asText(item && item.id, createId('footer-social-' + index)),
                label: asText(item && item.label, 'Social Link'),
                icon: asText(item && item.icon, 'fa-globe'),
                url: asText(item && item.url, '')
            }))
            .filter((item) => item.url);

        return {
            brand_name: asText(source.brand_name, defaults.brand_name),
            sections,
            social_links: socialLinks,
            copyright_text: asText(source.copyright_text, defaults.copyright_text),
            bottom_note: asText(source.bottom_note || source.powered_by_text, defaults.bottom_note)
        };
    }

    function escapeHtml(value) {
        return String(value || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function buildPhoneHref(phone) {
        const stripped = String(phone || '').replace(/[^\d+]/g, '');
        return stripped ? 'tel:' + stripped : '';
    }

    function buildMailHref(email) {
        const clean = asText(email, '');
        return clean ? 'mailto:' + clean : '';
    }

    function renderContactRow(iconClass, value, href) {
        if (!value) return '';
        const content = href
            ? `<a href="${escapeHtml(href)}" class="text-gray-300 text-sm hover:text-brand-primary transition break-all">${escapeHtml(value)}</a>`
            : `<span class="text-gray-300 text-sm break-all">${escapeHtml(value)}</span>`;

        return `
            <li class="flex items-center">
                <i class="fas ${escapeHtml(iconClass)} text-brand-primary text-xl mr-4 w-6"></i>
                ${content}
            </li>
        `;
    }

    function renderLinks(items) {
        if (!items.length) {
            return '<p class="text-sm text-gray-500">No items added yet.</p>';
        }

        return `
            <ul class="space-y-4 text-sm text-gray-300">
                ${items.map((item) => {
                    const text = escapeHtml(item.text || item.url);
                    if (!item.url) {
                        return `<li><span class="text-gray-300">${text}</span></li>`;
                    }

                    const target = item.new_tab ? ' target="_blank" rel="noopener noreferrer"' : '';
                    return `<li><a href="${escapeHtml(item.url)}" class="hover:text-brand-primary transition break-words"${target}>${text}</a></li>`;
                }).join('')}
            </ul>
        `;
    }

    function renderSection(section) {
        const title = escapeHtml(section.title);
        if (section.type === 'contact') {
            const contactItems = Array.isArray(section.items) && section.items.length
                ? section.items
                : [{ phone: section.phone, email: section.email }];

            return `
                <section class="min-w-0">
                    <h3 class="text-xl font-bold mb-6 pb-2 border-b border-gray-600 inline-block w-full">${title}</h3>
                    <div class="space-y-8">
                        ${contactItems.map((item) => `
                            <ul class="space-y-6">
                                ${renderContactRow('fa-phone-alt', item.phone, buildPhoneHref(item.phone))}
                                ${renderContactRow('fa-envelope', item.email, buildMailHref(item.email))}
                            </ul>
                        `).join('')}
                    </div>
                </section>
            `;
        }

        return `
            <section class="min-w-0">
                <h3 class="text-xl font-bold mb-6 pb-2 border-b border-gray-600 inline-block w-full">${title}</h3>
                ${renderLinks(section.items || [])}
            </section>
        `;
    }

    function renderSocialLinks(socialLinks) {
        const links = (Array.isArray(socialLinks) ? socialLinks : [])
            .filter((item) => item.url)
            .map((item) => `
                <a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer" aria-label="${escapeHtml(item.label)}" title="${escapeHtml(item.label)}" class="w-10 h-10 rounded-full bg-brand-primary hover:bg-white text-brand-dark hover:text-brand-primary flex items-center justify-center transition shadow-lg">
                    <i class="fab ${escapeHtml(item.icon || 'fa-globe')}"></i>
                </a>
            `)
            .join('');

        if (!links) return '';

        return `<div class="flex flex-wrap gap-3 mb-10">${links}</div>`;
    }

    function renderFooterMarkup(content) {
        return `
            <footer class="relative bg-footer-bg text-white pt-16 pb-6 border-t-4 border-brand-primary">
                <div class="absolute inset-0 overflow-hidden opacity-5 pointer-events-none">
                    <img src="Homepage/Footer_general.jpg" alt="" class="w-full h-full object-cover grayscale">
                </div>
                <div class="relative container mx-auto px-4">
                    <div class="grid gap-12 mb-16" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));">
                        ${content.sections.map(renderSection).join('')}
                    </div>
                    ${renderSocialLinks(content.social_links)}
                    <div class="border-t border-gray-700 pt-8 flex flex-col gap-2 md:flex-row md:justify-between md:items-center text-xs text-gray-400">
                        <p>${escapeHtml(content.copyright_text)}</p>
                        ${content.bottom_note ? `<p>${escapeHtml(content.bottom_note)}</p>` : ''}
                    </div>
                </div>
            </footer>
        `;
    }

    function renderLoadingMarkup() {
        return `
            <footer class="relative bg-footer-bg text-white pt-16 pb-6 border-t-4 border-brand-primary overflow-hidden">
                <div class="absolute inset-0 overflow-hidden opacity-5 pointer-events-none">
                    <img src="Homepage/Footer_general.jpg" alt="" class="w-full h-full object-cover grayscale">
                </div>
                <div class="relative container mx-auto px-4 animate-pulse">
                    <div class="grid gap-12 mb-16" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));">
                        ${[1, 2, 3].map(() => `
                            <div>
                                <div class="h-6 w-32 bg-white/10 rounded mb-6"></div>
                                <div class="space-y-4">
                                    <div class="h-4 w-40 bg-white/10 rounded"></div>
                                    <div class="h-4 w-32 bg-white/10 rounded"></div>
                                    <div class="h-4 w-36 bg-white/10 rounded"></div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    <div class="flex gap-3 mb-10">
                        ${[1, 2, 3, 4].map(() => '<div class="w-10 h-10 rounded-full bg-white/10"></div>').join('')}
                    </div>
                    <div class="border-t border-gray-700 pt-8 flex flex-col gap-2 md:flex-row md:justify-between">
                        <div class="h-4 w-72 bg-white/10 rounded"></div>
                        <div class="h-4 w-44 bg-white/10 rounded"></div>
                    </div>
                </div>
            </footer>
        `;
    }

    function injectStyles() {
        if (document.getElementById('pyf-footer-manager-styles')) return;

        const style = document.createElement('style');
        style.id = 'pyf-footer-manager-styles';
        style.textContent = `
            [data-pyf-footer-root] {
                display: block;
                transition: opacity 0.18s ease;
            }
        `;
        document.head.appendChild(style);
    }

    function readCache(cacheKey) {
        try {
            const raw = window.sessionStorage.getItem(cacheKey);
            return raw ? JSON.parse(raw) : null;
        } catch (error) {
            return null;
        }
    }

    function writeCache(cacheKey, payload) {
        try {
            window.sessionStorage.setItem(cacheKey, JSON.stringify(payload));
        } catch (error) {
            // Ignore storage failures.
        }
    }

    async function fetchFooterContent(isPreviewMode) {
        const endpoint = `${SUPABASE_URL}/rest/v1/site_content?select=updated_at,draft_content,live_content&page_id=eq.${FOOTER_PAGE_ID}`;
        const response = await fetch(endpoint, {
            method: 'GET',
            headers: {
                apikey: SUPABASE_KEY,
                Authorization: `Bearer ${SUPABASE_KEY}`
            }
        });

        if (!response.ok) {
            throw new Error('Unable to load footer content.');
        }

        const rows = await response.json();
        const row = Array.isArray(rows) && rows.length ? rows[0] : null;
        const source = isPreviewMode ? row?.draft_content : row?.live_content;

        return {
            content: normalizeFooterData(source),
            updatedAt: row?.updated_at || ''
        };
    }

    function mountMarkup(root, content) {
        root.innerHTML = renderFooterMarkup(content);
        root.style.opacity = '1';
        root.setAttribute('data-footer-ready', 'true');
    }

    async function mountFooter(root) {
        injectStyles();
        root.setAttribute('data-footer-ready', 'false');

        const isPreviewMode = new URLSearchParams(window.location.search).get('mode') === 'preview';
        const cacheKey = `${CACHE_KEY_PREFIX}:${isPreviewMode ? 'preview' : 'live'}`;
        const cached = readCache(cacheKey);

        if (cached && cached.content) {
            mountMarkup(root, normalizeFooterData(cached.content));
        } else {
            root.style.opacity = '1';
            root.innerHTML = renderLoadingMarkup();
        }

        try {
            const latest = await fetchFooterContent(isPreviewMode);
            mountMarkup(root, latest.content);
            writeCache(cacheKey, latest);
        } catch (error) {
            if (!cached || !cached.content) {
                mountMarkup(root, getDefaultFooterData());
            }
            console.error(error);
        }
    }

    function mountAll() {
        document.querySelectorAll('[data-pyf-footer-root]').forEach((root) => {
            mountFooter(root);
        });
    }

    window.PYFFooter = {
        mount: mountFooter,
        mountAll,
        defaults: getDefaultFooterData
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', mountAll, { once: true });
    } else {
        mountAll();
    }
})();
