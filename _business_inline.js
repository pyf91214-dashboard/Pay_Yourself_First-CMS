
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ["Roboto Flex", 'sans-serif'],
                    },
                    colors: {
                        'brand-primary': '#389400', 
                        'brand-dark': '#1c1c1c',
                        'footer-bg': '#1f2022',
                    }
                }
            }
        }
    


        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Sticky Header Logic
        let lastScrollTop = 0;
        const header = document.getElementById('main-header');
        window.addEventListener('scroll', function() {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (scrollTop > lastScrollTop && scrollTop > 100) { header.classList.add('header-hidden'); } 
            else { header.classList.remove('header-hidden'); }
            lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
        });

    


        const backToTopBtn = document.getElementById('backToTopBtn');
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);

        // Show/Hide logic based on scroll position
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) { // Show after scrolling down 300px
                backToTopBtn.classList.remove('translate-y-20', 'opacity-0');
            } else {
                backToTopBtn.classList.add('translate-y-20', 'opacity-0');
            }
        });

        // Smooth scroll to top function
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Accordion Logic
        document.querySelectorAll('.faq-btn').forEach(button => {
            button.addEventListener('click', () => {
                const content = button.nextElementSibling;
                content.classList.toggle('hidden');
                button.querySelector('i').classList.toggle('rotate-180');
            });
        });

        const defaultBusinessContent = {
            hero: {
                headline: 'Increase Your Cash Flow. <br> Improve Your Quality of Life. <br> Gain Your Freedom.',
                desc: 'Access tax, legal, business, and financial support in one complete package designed to help everyday people keep more, earn more, and spend less.',
                btn1_text: 'Get Business Support Package',
                btn1_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                btn2_text: '',
                btn2_link: '',
                image: 'Business-Support-Page/IPP_Hero.jpg'
            },
            intro: {
                headline: 'Affordable Access To <span class="text-brand-primary">Tax, Legal, And Business</span> Support In One Package.',
                desc1: 'Most people work hard, but still feel financially squeezed. Business Support Package helps you access tools and services normally out of reach, so you can reduce financial pressure and move forward with more confidence.',
                did_you_know: '',
                desc2: '',
                list_headline: 'If any of these sound familiar',
                list: [
                    'You are tired of paying too much in taxes',
                    'You want access to business deductions and guidance',
                    'You want legal and financial support without piecing everything together yourself',
                    'You want a practical system to strengthen your finances'
                ],
                image: 'Business-Support-Page/IPP_70,000 Pages.jpg'
            },
            ideal_for: {
                headline: '',
                desc: '',
                list_headline: '',
                list: [],
                image: 'Business-Support-Page/IPP_Income Power Pro_1.jpg'
            },
            features: {
                list: [
                    'Tax Guidance',
                    'CPA-Level Support',
                    'Legal Services Access',
                    'Business Training',
                    'Consumer Discount Platform',
                    'Optional Affiliate Enrollment'
                ]
            },
            value_section: {
                headline: 'Business Support<span class="text-brand-primary">Package Value</span>',
                table: [],
                total_value: 'Typical Monthly Market Value: $2,358-$6,299',
                investment: 'Your Monthly Investment: $150',
                bottom_line: 'Potential Annual Tax Savings: $3,000-$10,000',
                disclaimer: ''
            },
            investment_card: {
                headline: 'Value',
                price_title: 'Your Investment: $150/Month',
                includes_title: 'Includes:',
                list: [
                    'Tax guidance',
                    'Legal support',
                    'Business training',
                    'Consumer discount platform'
                ],
                guarantee: 'Protected by our 30-Day Money-Back Guarantee',
                btn_text: 'Get Business Support Package',
                btn_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                image: 'Business-Support-Page/IPP_Value.jpg',
                image_caption: ''
            },
            testimonials: {
                headline: 'Testimonials',
                desc: '',
                video_url: 'https://www.youtube-nocookie.com/embed/tw-MUhF0-g0?si=YXHjdcaqmfZ83-BB&rel=0&controls=0'
            },
            faq: {
                headline: 'Common <span class="text-brand-primary">Questions</span>',
                questions: []
            },
            bottom_cta: {
                headline: 'Take Control Of Your Taxes. <span class="text-brand-primary">Strengthen Your Finances.</span>',
                btn1_text: 'Get Business Support Package',
                btn1_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                btn2_text: 'View Service Packages',
                btn2_link: 'packages.html'
            },
            disclaimer_section: {
                headline: 'Disclaimer',
                blocks: []
            },
            advantages: {
                card1: { title: 'Tax Guidance', desc: 'Support to help you understand deductions, withholding, and better tax positioning.' },
                card2: { title: 'CPA-Level Support', desc: 'Professional support designed to help you keep more of what you earn.' },
                card3: { title: 'Legal Services Access', desc: 'Business and personal legal support through partner services.' }
            }
        };

        function setHtml(id, value) {
            const el = document.getElementById(id);
            if (el && value !== undefined && value !== null && value !== '') el.innerHTML = value;
        }

        function setText(id, value) {
            const el = document.getElementById(id);
            if (el && value !== undefined && value !== null && value !== '') el.textContent = value;
        }

        function setHrefAndText(id, href, text) {
            const el = document.getElementById(id);
            if (!el) return;
            if (href) el.href = href;
            if (text) el.textContent = text;
        }

        function toggleButton(id, href, text) {
            const el = document.getElementById(id);
            if (!el) return;
            if (text) {
                el.classList.remove('hidden');
                if (href) el.href = href;
                el.textContent = text;
            } else {
                el.classList.add('hidden');
            }
        }

        function setSrc(id, src) {
            const el = document.getElementById(id);
            if (el && src) el.src = src;
        }

        function get(obj, path, fallback) {
            let current = obj;
            for (let i = 0; i < path.length; i += 1) {
                if (current == null || typeof current !== 'object' || !(path[i] in current)) {
                    return fallback;
                }
                current = current[path[i]];
            }
            return current == null ? fallback : current;
        }

        function renderIntroList(items) {
            const list = document.getElementById('business-intro-list');
            if (!list || !Array.isArray(items)) return;
            list.innerHTML = items.map((item) => `
                <li class="flex items-start"><i class="fas fa-hand-point-right text-brand-primary mt-1 mr-3 text-lg"></i><span class="text-gray-700 font-medium">${item}</span></li>
            `).join('');
        }

        function renderIdealList(items) {
            const list = document.getElementById('business-ideal-list');
            if (!list || !Array.isArray(items)) return;
            list.innerHTML = items.map((item) => `
                <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary mt-1 mr-3 text-lg"></i><span class="text-gray-700 font-medium">${item}</span></li>
            `).join('');
        }

        function renderFeatures(content) {
            const grid = document.getElementById('business-features-grid');
            if (!grid) return;
            const cards = [
                { title: get(content, ['advantages', 'card1', 'title'], ''), desc: get(content, ['advantages', 'card1', 'desc'], ''), icon: 'fa-receipt' },
                { title: get(content, ['advantages', 'card2', 'title'], ''), desc: get(content, ['advantages', 'card2', 'list'], []).join(' • '), icon: 'fa-calculator' },
                { title: get(content, ['advantages', 'card3', 'title'], ''), desc: get(content, ['advantages', 'card3', 'desc'], ''), icon: 'fa-gavel' },
                ...(get(content, ['features', 'list'], [])).map((item, index) => ({
                    title: item,
                    desc: '',
                    icon: ['fa-briefcase', 'fa-percent', 'fa-network-wired', 'fa-comments-dollar', 'fa-user-shield', 'fa-circle-check'][index % 6]
                }))
            ].filter((card) => card.title);

            grid.innerHTML = cards.slice(0, 9).map((card) => `
                <div class="bg-[#F2FFEB] p-8 rounded-xl text-center hover:shadow-lg transition border border-gray-100 h-full">
                    <div class="w-16 h-16 bg-[#4a8a0a] rounded-full flex items-center justify-center text-white text-2xl mx-auto mb-4"><i class="fas ${card.icon}"></i></div>
                    <h3 class="font-bold text-brand-dark mb-2">${card.title}</h3>
                    <p class="text-xs text-gray-600">${card.desc || ''}</p>
                </div>
            `).join('');
        }

        function renderValueBox(content) {
            const box = document.getElementById('business-value-box');
            if (!box) return;
            box.innerHTML = `
                <div class="space-y-4 max-w-2xl mx-auto text-sm md:text-base font-medium text-gray-700 mb-8">
                    <div class="flex justify-between border-b border-gray-300 pb-2">
                        <span>Total Value:</span>
                        <span class="font-bold text-brand-primary">${get(content, ['value_section', 'total_value'], '')}</span>
                    </div>
                    <div class="flex justify-between border-b border-gray-300 pb-2">
                        <span>Investment:</span>
                        <span class="font-bold text-brand-primary">${get(content, ['value_section', 'investment'], '')}</span>
                    </div>
                    <div class="flex justify-between font-bold text-gray-900 pt-2">
                        <span>Bottom Line:</span>
                        <span class="text-right">${get(content, ['value_section', 'bottom_line'], '')}</span>
                    </div>
                </div>
                <h2 class="text-4xl md:text-6xl font-black text-brand-dark uppercase mb-4">${get(content, ['investment_card', 'price_title'], '')}</h2>
                <h3 class="text-2xl md:text-3xl font-bold text-brand-dark uppercase">${get(content, ['value_section', 'headline'], '')}</h3>
                ${get(content, ['value_section', 'disclaimer'], '') ? `<p class="text-xs text-gray-500 mt-6">${get(content, ['value_section', 'disclaimer'], '')}</p>` : ''}
            `;
        }

        function renderInvestmentSection(content) {
            const heading = document.getElementById('business-investment-headline');
            const grid = document.getElementById('business-investment-grid');
            if (!grid) return;
            if (heading) heading.innerHTML = get(content, ['investment_card', 'headline'], heading.innerHTML);
            grid.innerHTML = `
                <div>
                    <h3 class="font-bold text-brand-dark text-lg mb-4">${get(content, ['investment_card', 'includes_title'], 'Includes:')}</h3>
                    <p class="text-gray-600 text-sm mb-8 leading-relaxed">${get(content, ['testimonials', 'desc'], '')}</p>
                    <ul class="space-y-3 mb-8">
                        ${(get(content, ['investment_card', 'list'], [])).map((item) => `<li class="flex items-center text-sm font-medium text-gray-700"><i class="fas fa-check-square text-brand-primary text-xl mr-3"></i>${item}</li>`).join('')}
                    </ul>
                    <p class="font-bold text-brand-dark text-sm mb-6">${get(content, ['investment_card', 'guarantee'], '')}</p>
                    <a href="${get(content, ['investment_card', 'btn_link'], '#')}" target="_blank" class="bg-[#4a8a0a] hover:bg-[#389400] text-white font-bold py-4 px-8 rounded shadow-lg transition uppercase text-xs tracking-widest inline-block">${get(content, ['investment_card', 'btn_text'], 'Learn More')}</a>
                </div>
                <div class="h-80 md:h-96">
                    <img src="${get(content, ['investment_card', 'image'], 'Business-Support-Page/IPP_Value.jpg')}" alt="Business Support Value" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    ${get(content, ['investment_card', 'image_caption'], '') ? `<p class="text-xs text-gray-500 mt-3 text-center">${get(content, ['investment_card', 'image_caption'], '')}</p>` : ''}
                </div>
            `;
        }

        function attachFaqAccordion() {
            document.querySelectorAll('#business-faq-list .faq-btn').forEach((button) => {
                button.addEventListener('click', () => {
                    const content = button.nextElementSibling;
                    content.classList.toggle('hidden');
                    button.querySelector('i').classList.toggle('rotate-180');
                });
            });
        }

        function renderFaqs(items) {
            const container = document.getElementById('business-faq-list');
            if (!container || !Array.isArray(items) || items.length === 0) return;
            container.innerHTML = items.map((faq) => `
                <div class="border border-gray-200 rounded-xl overflow-hidden bg-[#F2FFEB]">
                    <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-white transition focus:outline-none">
                        <span class="font-bold text-gray-900 text-left pr-4">${faq.q || ''}</span>
                        <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                    </button>
                    <div class="faq-content hidden p-6 border-t border-gray-200 text-gray-600 text-sm leading-relaxed bg-white">${faq.a || ''}</div>
                </div>
            `).join('');
            attachFaqAccordion();
        }

        function renderDisclaimer(blocks) {
            const container = document.getElementById('business-disclaimer-content');
            if (!container || !Array.isArray(blocks) || blocks.length === 0) return;
            container.innerHTML = blocks.map((block) => `
                <div class="mb-6 text-left">
                    ${block.title ? `<h4 class="font-bold text-brand-dark mb-2">${block.title}</h4>` : ''}
                    <p>${block.text || ''}</p>
                </div>
            `).join('');
        }

        function applyBusinessContent(content) {
            setHtml('business-hero-headline', get(content, ['hero', 'headline'], ''));
            setText('business-hero-desc', get(content, ['hero', 'desc'], ''));
            setHrefAndText('business-hero-btn1', get(content, ['hero', 'btn1_link'], ''), get(content, ['hero', 'btn1_text'], ''));
            toggleButton('business-hero-btn2', get(content, ['hero', 'btn2_link'], ''), get(content, ['hero', 'btn2_text'], ''));
            setSrc('business-hero-image', get(content, ['hero', 'image'], ''));

            setHtml('business-intro-headline', get(content, ['intro', 'headline'], ''));
            setText('business-intro-desc1', get(content, ['intro', 'desc1'], ''));
            setHtml('business-intro-did-you-know', get(content, ['intro', 'did_you_know'], ''));
            setText('business-intro-desc2', get(content, ['intro', 'desc2'], ''));
            setText('business-intro-list-headline', get(content, ['intro', 'list_headline'], ''));
            renderIntroList(get(content, ['intro', 'list'], []));
            setHrefAndText('business-intro-btn', get(content, ['hero', 'btn1_link'], ''), get(content, ['hero', 'btn1_text'], ''));
            setSrc('business-intro-image', get(content, ['intro', 'image'], ''));

            setHtml('business-ideal-headline', get(content, ['ideal_for', 'headline'], ''));
            setText('business-ideal-desc', get(content, ['ideal_for', 'desc'], ''));
            setText('business-ideal-list-headline', get(content, ['ideal_for', 'list_headline'], ''));
            renderIdealList(get(content, ['ideal_for', 'list'], []));
            setSrc('business-ideal-image', get(content, ['ideal_for', 'image'], ''));

            setHtml('business-features-headline', get(content, ['value_section', 'headline'], document.getElementById('business-features-headline').innerHTML));
            renderFeatures(content);
            renderValueBox(content);
            setText('business-testimonials-headline', get(content, ['testimonials', 'headline'], ''));
            setText('business-testimonials-desc', get(content, ['testimonials', 'desc'], ''));
            setSrc('business-testimonials-video', get(content, ['testimonials', 'video_url'], ''));
            renderInvestmentSection(content);
            setHtml('business-faq-headline', get(content, ['faq', 'headline'], ''));
            renderFaqs(get(content, ['faq', 'questions'], []));
            setHtml('business-cta-headline', get(content, ['bottom_cta', 'headline'], ''));
            setText('business-cta-desc', get(content, ['value_section', 'bottom_line'], ''));
            setHrefAndText('business-cta-btn1', get(content, ['bottom_cta', 'btn1_link'], ''), get(content, ['bottom_cta', 'btn1_text'], ''));
            toggleButton('business-cta-btn2', get(content, ['bottom_cta', 'btn2_link'], ''), get(content, ['bottom_cta', 'btn2_text'], ''));
            setText('business-disclaimer-headline', get(content, ['disclaimer_section', 'headline'], ''));
            renderDisclaimer(get(content, ['disclaimer_section', 'blocks'], []));
        }

        function mergeContent(loaded) {
            return {
                ...defaultBusinessContent,
                ...loaded,
                hero: { ...defaultBusinessContent.hero, ...(loaded.hero || {}) },
                intro: { ...defaultBusinessContent.intro, ...(loaded.intro || {}) },
                ideal_for: { ...defaultBusinessContent.ideal_for, ...(loaded.ideal_for || {}) },
                features: { ...defaultBusinessContent.features, ...(loaded.features || {}) },
                value_section: { ...defaultBusinessContent.value_section, ...(loaded.value_section || {}) },
                investment_card: { ...defaultBusinessContent.investment_card, ...(loaded.investment_card || {}) },
                faq: { ...defaultBusinessContent.faq, ...(loaded.faq || {}) },
                bottom_cta: { ...defaultBusinessContent.bottom_cta, ...(loaded.bottom_cta || {}) },
                disclaimer_section: { ...defaultBusinessContent.disclaimer_section, ...(loaded.disclaimer_section || {}) },
                testimonials: { ...defaultBusinessContent.testimonials, ...(loaded.testimonials || {}) },
                advantages: {
                    ...defaultBusinessContent.advantages,
                    ...(loaded.advantages || {}),
                    card1: { ...defaultBusinessContent.advantages.card1, ...((loaded.advantages || {}).card1 || {}) },
                    card2: { ...defaultBusinessContent.advantages.card2, ...((loaded.advantages || {}).card2 || {}) },
                    card3: { ...defaultBusinessContent.advantages.card3, ...((loaded.advantages || {}).card3 || {}) }
                }
            };
        }

        async function loadBusinessContent() {
            applyBusinessContent(defaultBusinessContent);
            try {
                const isPreviewMode = new URLSearchParams(window.location.search).get('mode') === 'preview';
                const { data, error } = await supabase.from('site_content').select('*').eq('page_id', 'business').single();
                if (error || !data) return;
                const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                if (!loadedContent) return;
                applyBusinessContent(mergeContent(loadedContent));
            } catch (error) {
                console.error('Failed to load Business Support Package content', error);
            }
        }

        loadBusinessContent();
    