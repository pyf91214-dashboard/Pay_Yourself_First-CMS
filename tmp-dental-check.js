        const supabaseUrl = 'https://bjnofwcdplatjoflbnag.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJqbm9md2NkcGxhdGpvZmxibmFnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2OTQwNjQsImV4cCI6MjA2OTI3MDA2NH0.nLQGwbJw0n4dZZ1_JxO9v6wN77k8On7U5f2J0iY2lQ';
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);

        document.addEventListener('alpine:init', () => {
            Alpine.data('dentalPowerPage', () => ({
                isContentReady: false,
                pageData: { sections: [] },
                expandedCards: {},
                openFaqs: {},

                getDefaultPageData() {
                    return {
                        sections: [
                            {
                                id: 'dental-hero',
                                type: 'hero',
                                enabled: true,
                                order: 1,
                                content: {
                                    headline: 'Dental, Vision, and Hearing Savings For Your Household',
                                    desc: 'Dental savings, vision care discounts, hearing services, and prescription savings.',
                                    price_text: 'PRICE: $16.95/month',
                                    image: 'Dental-power-page/Dental Power_Hero.jpg',
                                    buttons: [{ text: 'Get Dental Power', link: 'https://buy.stripe.com/8x25kwgb80Gjgyg3hKcIE05' }]
                                }
                            },
                            {
                                id: 'dental-benefits',
                                type: 'benefits',
                                enabled: true,
                                order: 2,
                                content: {
                                    headline: 'Essential Savings For <span class="text-brand-primary">Dental, Vision, Hearing & Prescriptions</span>',
                                    desc: 'A dental and health savings package, combining dental network access, vision care, hearing services, and prescription discounts.',
                                    cards: [
                                        {
                                            title: 'Dental Network Savings',
                                            image: 'Dental-power-page/Dental Network Savings_DentalPower_card.jpg',
                                            intro: 'Pay Yourself First offers our dental plan through Careington International Corporation. They have one of the most recognized professional dental networks in the nation and boasts a provider network of over 70,000 dental access points.',
                                            paragraphs: ['As a member, you can take advantage of savings offered by an industry leader in discount dental care.'],
                                            highlight_title: 'What\'s included:',
                                            highlight_items: [
                                                'Save 20% to 60% on most dental procedures including routine oral exams, unlimited cleanings, and major work such as dentures, root canals, and crowns.',
                                                '20% savings on orthodontics including braces and retainers for children and adults',
                                                '20% reduction on specialist normal fees including Endodontics, Oral Surgery, Pediatric Dentistry, Periodontics, and Prosthodontics where available',
                                                'Cosmetic dentistry such as bonding and veneers also included',
                                                'All dentists must meet highly selective credentialing standards based on education, background, license standing and other requirements.',
                                                'You may visit any participating dentist on the plan and change providers at any time.'
                                            ],
                                            bullets: [],
                                            notes: []
                                        },
                                        {
                                            title: 'Vision Program',
                                            image: 'Dental-power-page/Vision Program_DentalPower_card.jpg',
                                            intro: 'VSP Vision Savings Pass is a discount vision program that offers savings on eye care and eyewear. With the best choices in eyewear, VSP makes it easy to find the perfect frame.',
                                            paragraphs: [],
                                            highlight_title: 'What\'s included:',
                                            highlight_items: [
                                                'Access to discounts through a trusted, private-practice VSP doctor',
                                                'One rate of $50 for eye exams',
                                                '15% savings on contact lens exams',
                                                'Special pricing on complete pairs of glasses and sunglasses',
                                                'Unlimited use on materials throughout the year',
                                                'Exclusive Member Extras and special offers'
                                            ],
                                            bullets: [],
                                            notes: [
                                                '*Brands subject to change',
                                                '**This cost is only available with the purchase of a complete pair of prescription glasses; otherwise you will receive 20% off an eye exam only.',
                                                '***Applies only to contact lens exam, not materials. You are responsible for 100% of the contact lens material cost. This plan is not insurance. Not available in WA.'
                                            ]
                                        },
                                        {
                                            title: 'Hearing Program',
                                            image: 'Dental-power-page/Hearing Program_DentalPower_card.jpg',
                                            intro: 'We are pleased to provide a hearing care discount plan that makes hearing-aid services accessible, as well as affordable. HearPO is one of the largest providers of hearing health care benefits in the United States.',
                                            paragraphs: [],
                                            highlight_title: 'Key Features of Our HearPO:',
                                            highlight_items: [
                                                '30% discount on diagnostic services, including hearing exams',
                                                'Lowest Price Guarantee*',
                                                'Financing options with up to 12-months no interest',
                                                '60 day no risk trial period',
                                                '1 year follow-up care',
                                                '3 year warranty on most hearing aids',
                                                '1 year of free batteries (80 cell per hearing aid)',
                                                'Discounts on batteries mailed directly to your home',
                                                'Over a 90% customer satisfaction for over a decade'
                                            ],
                                            bullets: [],
                                            notes: [
                                                '*Competitor coupon required for verification of price and model. Limited to manufacturers offered through the HearPO program. Local provider quotes only will be matched.',
                                                '**Some exclusions apply. Limited to one time claim for loss and damage.'
                                            ]
                                        },
                                        {
                                            title: 'Prescription Discount Program',
                                            image: 'Dental-power-page/Prescription Discount Program_DentalPower_card.jpg',
                                            intro: 'Members are entitled to prescription savings offered by MedImpact. Discounts are available at over 53,000 participating pharmacies nationwide.',
                                            paragraphs: [
                                                'Members can save even more on maintenance medications through the convenient and money-saving mail service. MedVantix members receive savings on 90 day supplies of medications when ordered online, by phone or through the mail with our mail-order pharmacy!',
                                                'Our card is accepted in over 53,000 pharmacies nationwide including CVS Pharmacy, Walgreens, Walmart Pharmacy, Target, Rite Aid, Safeway, Kroger Pharmacy, Publix Pharmacy, Sam\'s Club Pharmacy, Costco Pharmacy, and many more.',
                                                'For prescription drug pricing or to locate a participating pharmacy, please call toll free (855) PYF-CLUB.'
                                            ],
                                            highlight_title: '',
                                            highlight_items: [],
                                            bullets: [],
                                            notes: []
                                        }
                                    ]
                                }
                            },
                            {
                                id: 'dental-pricing',
                                type: 'pricing',
                                enabled: true,
                                order: 3,
                                content: {
                                    headline: 'A Comprehensive Package For Just <span class="text-brand-primary">$16.95/mo</span>',
                                    plan_name: 'Dental Power',
                                    price: '$16.95/Month',
                                    includes_title: 'Includes',
                                    includes: ['Dental network access (70,000+ providers)', 'Vision savings program', 'Hearing care discounts', 'Prescription drug savings (53,000+ pharmacies)', 'Nationwide provider networks', 'Purchase Power retail discounts'],
                                    button_text: 'Get Dental Power',
                                    button_link: 'https://buy.stripe.com/8x25kwgb80Gjgyg3hKcIE05',
                                    image: 'Dental-power-page/Dental Power_Comprehensive Package.jpg',
                                    note: 'Dental Power includes Purchase Power at no additional cost.'
                                }
                            },
                            {
                                id: 'dental-faq',
                                type: 'faq',
                                enabled: true,
                                order: 4,
                                content: {
                                    headline: 'Common <span class="text-brand-primary">Questions</span>',
                                    questions: [
                                        { q: 'Is PYF Dental Power an insurance plan?', a: 'No, PYF Dental Power is a discount plan. It provides predetermined discounts on dental, vision, hearing, and prescription medicine services.' },
                                        { q: 'Can my whole family use it?', a: 'Yes. The Dental Power plan can be used by your entire household.' },
                                        { q: 'Can I use this plan if I already have dental insurance?', a: 'Yes, this plan would not conflict with your dental insurance. It would be an added complement.' },
                                        { q: 'Can I get Dental Power without joining as an affiliate?', a: 'Yes.' },
                                        { q: 'What does "affiliate enrollment" mean?', a: 'PYF affiliate program is free and allows you to receive referral fees when you refer others to PYF products. You can enroll as an affiliate with any PYF product at no additional cost, or enroll as an affiliate with no product purchase required. <a href="affiliate-page.html" class="text-brand-primary underline">Learn more</a>' },
                                        { q: 'Can I use Dental Power with my current dentist?', a: 'You can use the plan with any provider in the Dental Power network. Check the provider directory to see if your dentist participates.' },
                                        { q: 'Are there any waiting periods or annual limits?', a: 'No. There are no waiting periods, no annual limits, and no pre-approvals required.' }
                                    ]
                                }
                            },
                            {
                                id: 'dental-cta',
                                type: 'bottom_cta',
                                enabled: true,
                                order: 5,
                                content: {
                                    headline: 'Ready To Get <span class="text-brand-primary">Dental Power?</span>',
                                    button_text: 'Get Dental Power',
                                    button_link: 'https://buy.stripe.com/8x25kwgb80Gjgyg3hKcIE05',
                                    badges: ['30-Day Money-Back Guarantee', 'No Long-Term Contract', 'Providing service since 2011']
                                }
                            },
                            {
                                id: 'dental-disclaimer',
                                type: 'disclaimer_section',
                                enabled: true,
                                order: 6,
                                content: {
                                    headline: 'Disclaimer',
                                    body: '<p><strong>Disclosures: THIS PLAN IS NOT INSURANCE. THIS IS NOT A MEDICARE PRESCRIPTION DRUG PLAN.*</strong> This plan does not meet the minimum creditable coverage requirements under M.G.L. c. 111M and 956 CMR 5.00. The plan provides discounts at certain health care providers for medical services. The range of discounts will vary depending on the type of provider and service. The plan does not make payments directly to the providers of medical services. Plan members are obligated to pay for all health care services but will receive a discount from those health care providers who have contracted with the discount medical plan organization. You may access a list of participating health care providers at this website. Upon request the plan will make available a written list of participating health care providers. You have the right to cancel within the first 30 days after receipt of membership materials and receive a full refund, less a nominal processing fee (nominal fee for MD residents is $5). Discount Medical Plan</p><p><strong>Organization and administrator:</strong> Careington International Corporation, 7400 Gaylord Parkway, Frisco, TX 75034; phone 800-441-0380. The program and its administrators have no liability for providing or guaranteeing service by providers or the quality of service rendered by providers. This program is not available in Montana and Vermont. This plan is not currently available in Washington. *Medicare statement applies to MD residents when pharmacy discounts are part of program</p>'
                                }
                            }
                        ]
                    };
                },

                normalizeSection(section = {}, fallback = {}, index = 0) {
                    return {
                        id: section.id || fallback.id || `dental-section-${index + 1}`,
                        type: section.type || fallback.type || `section-${index + 1}`,
                        enabled: typeof section.enabled === 'boolean' ? section.enabled : (typeof fallback.enabled === 'boolean' ? fallback.enabled : true),
                        order: Number(section.order ?? fallback.order ?? index + 1),
                        content: JSON.parse(JSON.stringify(section.content || fallback.content || {}))
                    };
                },

                hydratePageData(content = {}) {
                    const defaults = this.getDefaultPageData();
                    const defaultSections = defaults.sections || [];
                    const incomingSections = Array.isArray(content.sections) ? content.sections : [];
                    const sections = incomingSections.length
                        ? incomingSections.map((section, index) => {
                            const fallback = defaultSections.find((item) => item.type === section.type) || {};
                            return this.normalizeSection(section, fallback, index);
                        })
                        : defaultSections.map((section, index) => this.normalizeSection(section, section, index));

                    return { sections };
                },

                hasSection(type) {
                    return (this.pageData.sections || []).some((section) => section.type === type && section.enabled !== false);
                },

                getSection(type) {
                    return (this.pageData.sections || []).find((section) => section.type === type) || null;
                },

                getSectionContent(type) {
                    return this.getSection(type)?.content || {};
                },

                hasExpandableContent(card = {}) {
                    return Boolean(
                        (Array.isArray(card.paragraphs) && card.paragraphs.length) ||
                        (Array.isArray(card.highlight_items) && card.highlight_items.length) ||
                        (Array.isArray(card.bullets) && card.bullets.length) ||
                        (Array.isArray(card.notes) && card.notes.length) ||
                        card.highlight_title
                    );
                },

                toggleCard(index) {
                    this.expandedCards[index] = !this.expandedCards[index];
                },

                toggleFaq(index) {
                    this.openFaqs[index] = !this.openFaqs[index];
                },

                syncSectionLayout() {
                    const root = document.querySelector('[data-dental-sections-root]');
                    if (!root) return;

                    const nodesByType = new Map(
                        Array.from(root.querySelectorAll('[data-dental-section]')).map((node) => [node.dataset.dentalSection, node])
                    );

                    (this.pageData.sections || [])
                        .sort((a, b) => a.order - b.order)
                        .forEach((section) => {
                            const node = nodesByType.get(section.type);
                            if (node) root.appendChild(node);
                        });
                },

                async init() {
                    const mode = new URLSearchParams(window.location.search).get('mode');
                    this.pageData = this.hydratePageData(this.getDefaultPageData());
                    this.isContentReady = true;

                    try {
                        const { data, error } = await supabase
                            .from('site_content')
                            .select('*')
                            .eq('page_id', 'dental-power')
                            .single();

                        if (error || !data) {
                            console.error('Dental Power CMS load failed', error);
                            await this.$nextTick();
                            this.syncSectionLayout();
                            return;
                        }

                        const content = mode === 'preview'
                            ? data.draft_content
                            : (data.published_content ?? data.live_content);

                        if (!content) {
                            console.error('Dental Power CMS content missing for mode', mode);
                            await this.$nextTick();
                            this.syncSectionLayout();
                            return;
                        }

                        this.pageData = JSON.parse(JSON.stringify(content));
                        this.pageData = this.hydratePageData(this.pageData);

                        console.log('Dental page_id:', 'dental-power');
                        console.log('Fetched:', data);
                        console.log('Final pageData:', this.pageData);

                        await this.$nextTick();
                        this.syncSectionLayout();
                        this.isContentReady = true;
                    } catch (error) {
                        console.error('Dental Power CMS load failed', error);
                        await this.$nextTick();
                        this.syncSectionLayout();
                    }
                }
            }));
        });

        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if (menuBtn && mobileMenu) {
            menuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
        }

        let lastScrollTop = 0;
        const header = document.getElementById('main-header');
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (header) {
                if (scrollTop > lastScrollTop && scrollTop > 100) {
                    header.classList.add('header-hidden');
                } else {
                    header.classList.remove('header-hidden');
                }
            }
            lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
        });

        const backToTopBtn = document.getElementById('backToTopBtn');
        window.addEventListener('scroll', () => {
            if (!backToTopBtn) return;
            if (window.scrollY > 300) {
                backToTopBtn.classList.remove('translate-y-20', 'opacity-0');
            } else {
                backToTopBtn.classList.add('translate-y-20', 'opacity-0');
            }
        });

        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
