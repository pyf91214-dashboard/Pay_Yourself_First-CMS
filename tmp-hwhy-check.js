
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        
        document.addEventListener('alpine:init', () => {
            const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
            
            Alpine.data('siteData', () => ({
                pageData: {
                    hero: {
                        headline: 'We Help You Gain Greater Control Of\n<span class="text-[#bbf7d0]">Your Financial Life</span>',
                        desc: 'Most people work hard, pay their bills, and still feel behind.\nPay Yourself First gives you the tools, guidance, and support to earn more, keep more, and spend less \u2014 all with a simple, practical system designed for everyday Americans.',
                        btn1_text: 'See How We Help You Earn More',
                        btn1_link: 'affiliate-plan.html',
                        btn2_text: 'See How We Help You Save More',
                        btn2_link: 'packages.html',
                        buttons: [
                            { text: 'See How We Help You Earn More', link: 'affiliate-plan.html', style: 'primary' },
                            { text: 'See How We Help You Save More', link: 'packages.html', style: 'secondary' }
                        ],
                        image: 'How-we-help-you/How we help you_hero image.jpg'
                    },
                    why_exists: {
                        headline: 'Why <span class="text-brand-primary">PYF Exists</span>',
                        desc1: 'Pay Yourself First was created by a legend in the financial services industry who spent decades helping tens of thousands of people improve their financial lives. He witnessed a pattern across every background:',
                        list: [
                            'People earning good money but saving almost none',
                            'W-2 workers overpaying thousands in taxes without knowing it',
                            '1099 earners struggling with unstable income',
                            'Families living comfortably but headed toward an insecure retirement',
                            'Hard-working individuals with no financial safety net'
                        ],
                        desc2: 'PYF was built to give individuals the financial tools and services that the rich and wealthy have at affordable prices. PYF also provides a pathway for people to strengthen their finances by minimizing their taxes and increasing their income.',
                        image: 'How-we-help-you/Why PYF Exists.jpg'
                    },
                    problems: {
                        headline: 'The <span class="text-brand-primary">Problems</span> Most People Face',
                        block1: {
                            image: 'How-we-help-you/Problems most people face_1.jpg',
                            title: 'Everyday people struggle with challenges that compound over time.',
                            list: ['Insufficient take-home pay', 'High taxes and few tax deductions', 'Rising costs of living', 'Limited access to financial guidance', 'High healthcare and personal expenses', 'Lack of long-term financial stability']
                        },
                        block2: {
                            image: 'How-we-help-you/Problems most people face_2.jpg',
                            title: 'Whether someone earns a salary, runs a small business, works a gig job, or lives on commission, these challenges lead to the same outcomes.',
                            list: ['Stress', 'Debt', 'Lack of savings', 'No margin for emergencies', 'An uncertain future']
                        },
                        cards: [
                            {
                                image: 'How-we-help-you/Problems most people face_1.jpg',
                                title: 'Everyday people struggle with challenges that compound over time.',
                                list: ['Insufficient take-home pay', 'High taxes and few tax deductions', 'Rising costs of living', 'Limited access to financial guidance', 'High healthcare and personal expenses', 'Lack of long-term financial stability']
                            },
                            {
                                image: 'How-we-help-you/Problems most people face_2.jpg',
                                title: 'Whether someone earns a salary, runs a small business, works a gig job, or lives on commission, these challenges lead to the same outcomes.',
                                list: ['Stress', 'Debt', 'Lack of savings', 'No margin for emergencies', 'An uncertain future']
                            }
                        ],
                        footer: 'PYF exists to help you overcome these problems in a simple way that anyone can do.'
                    },
                    mastering: {
                        headline: 'Financial <span class="text-brand-primary"> Control</span> comes from mastering <span class="text-brand-primary"> three things</span>',
                        card1: {
                            title: '1. Earn More',
                            desc: 'PYF offers simple, accessible ways for people to open new income pathways through home-based entrepreneurship — supported by:',
                            list: ['Education', 'Tools', 'Professional Guidance'],
                            image: 'How-we-help-you/Mastering Three Things_Earn More.jpg'
                        },
                        card2: {
                            title: '2. Keep More',
                            desc: 'Most W-2 earners unknowingly overpay their taxes. PYF connects users with licensed tax professionals who help them:',
                            list: ['Adjust withholding correctly', 'Unlock home-based deductions', 'Maximize tax savings', 'Reduce taxes to legal minimum'],
                            quote: '"This single category often creates the biggest transformation for everyday Americans."',
                            image: 'How-we-help-you/Mastering Three Things_Save More.jpg'
                        },
                        card3: {
                            title: '3. Spend Less',
                            desc: 'Access to nationwide savings programs that reduce everyday expenses, including:',
                            list: ['Shopping', 'Dining', 'Vision', 'Dental', 'Travel', 'Telehealth', 'Auto Care', 'Rx Meds'],
                            footer: 'Every dollar saved is a dollar that strengthens long-term stability.',
                            image: 'How-we-help-you/Mastering Three Things_Spend Less.jpg'
                        },
                        cards: [
                            {
                                title: '1. Earn More',
                                desc: 'PYF offers simple, accessible ways for people to open new income pathways through home-based entrepreneurship — supported by:',
                                list: ['Education', 'Tools', 'Professional Guidance'],
                                image: 'How-we-help-you/Mastering Three Things_Earn More.jpg',
                                quote: '',
                                footer: ''
                            },
                            {
                                title: '2. Keep More',
                                desc: 'Most W-2 earners unknowingly overpay their taxes. PYF connects users with licensed tax professionals who help them:',
                                list: ['Adjust withholding correctly', 'Unlock home-based deductions', 'Maximize tax savings', 'Reduce taxes to legal minimum'],
                                image: 'How-we-help-you/Mastering Three Things_Save More.jpg',
                                quote: '"This single category often creates the biggest transformation for everyday Americans."',
                                footer: ''
                            },
                            {
                                title: '3. Spend Less',
                                desc: 'Access to nationwide savings programs that reduce everyday expenses, including:',
                                list: ['Shopping', 'Dining', 'Vision', 'Dental', 'Travel', 'Telehealth', 'Auto Care', 'Rx Meds'],
                                image: 'How-we-help-you/Mastering Three Things_Spend Less.jpg',
                                quote: '',
                                footer: 'Every dollar saved is a dollar that strengthens long-term stability.'
                            }
                        ]
                    },
                    designed_for: {
                        headline: 'PYF Is <span class="text-brand-primary">Designed For</span>',
                        desc: 'PYF serves everyday people from all backgrounds who want practical, real-world financial improvement.',
                        list: ['W-2 workers who want to keep more of their paycheck', '1099 earners who need stability and tax guidance', 'Home-based entrepreneurs growing new income streams', 'Gig workers who want predictable support', 'Families reducing rising household expenses', 'Individuals planning for long-term financial security', 'Anyone who wants a better financial future without complicated requirements.'],
                        footer: 'If you want to build income, reduce expenses, or improve your financial stability, PYF is designed with you in mind.',
                        image: 'How-we-help-you/PYF Is Designed For.jpg'
                    },
                    three_ways: {
                        headline: 'Three Ways PYF <span class="text-brand-primary">Helps You Move Forward</span>',
                        desc: 'You don\'t have to know exactly what you want yet. PYF offers two simple paths, depending on your goals.',
                        card1: {
                            image: 'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg',
                            title: 'Earn Referral Fees',
                            best_for: 'People who want to create additional income and/or having a home-based business',
                            list: ['Recurring Income Opportunity', 'Marketing Resources & Tools', 'Affiliate Training & Support'],
                            footer: 'You have the chance to add a source of income as a side hustle or legitimate business',
                            btn_text: 'Become An Affiliate',
                            btn_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm'
                        },
                        card2: {
                            image: 'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg',
                            title: 'Save Money on Everyday Living',
                            best_for: 'People who simply want to reduce expenses and make life more affordable.',
                            list: ['Shopping and travel savings', 'Wellness and fitness programs', 'Dental, vision, and hearing discounts', 'Telehealth services', 'Personal legal support'],
                            footer: 'If your primary goal is to lower your monthly costs, this path gives you immediate, practical value.',
                            btn_text: 'Choose A Discount Package',
                            btn_link: 'packages.html'
                        },
                        card3: {
                            image: 'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg',
                            title: 'Support For Your Home Based/Small Business',
                            best_for: 'People who want support services for their Home Based/Small Business',
                            list: ['Expert Tax & Accounting Services', 'Expert Business Legal Services', 'Expert Personal Legal Services', 'Business Coaching', 'Home Based/Small Business Education'],
                            footer: 'If your primary goal is to lower your taxes to the legal minimum, increase your revenue, and improve your work/life balance, this path will give you the most value.',
                            note: '*Business coaches have decades of experience in business and a proven track record of success',
                            btn_text: 'Start Your Support Services',
                            btn_link: 'business-support-package.html'
                        },
                        cards: [
                            {
                                image: 'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg',
                                title: 'Earn Referral Fees',
                                best_for: 'People who want to create additional income and/or having a home-based business',
                                list: ['Recurring Income Opportunity', 'Marketing Resources & Tools', 'Affiliate Training & Support'],
                                footer: 'You have the chance to add a source of income as a side hustle or legitimate business',
                                note: '',
                                btn_text: 'Become An Affiliate',
                                btn_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm'
                            },
                            {
                                image: 'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg',
                                title: 'Save Money on Everyday Living',
                                best_for: 'People who simply want to reduce expenses and make life more affordable.',
                                list: ['Shopping and travel savings', 'Wellness and fitness programs', 'Dental, vision, and hearing discounts', 'Telehealth services', 'Personal legal support'],
                                footer: 'If your primary goal is to lower your monthly costs, this path gives you immediate, practical value.',
                                note: '',
                                btn_text: 'Choose A Discount Package',
                                btn_link: 'packages.html'
                            },
                            {
                                image: 'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg',
                                title: 'Support For Your Home Based/Small Business',
                                best_for: 'People who want support services for their Home Based/Small Business',
                                list: ['Expert Tax & Accounting Services', 'Expert Business Legal Services', 'Expert Personal Legal Services', 'Business Coaching', 'Home Based/Small Business Education'],
                                footer: 'If your primary goal is to lower your taxes to the legal minimum, increase your revenue, and improve your work/life balance, this path will give you the most value.',
                                note: '*Business coaches have decades of experience in business and a proven track record of success',
                                btn_text: 'Start Your Support Services',
                                btn_link: 'business-support-package.html'
                            }
                        ]
                    },
                    why_works: {
                        headline: 'Why PYF Works',
                        desc: 'You don\'t have to pick a single path. You are free to choose a combination of any of the three or all three. Everything PYF offers is built to give everyday people an advantage normally reserved for the wealthy and very high-income earners.',
                        list: ['Professional and expert tax and legal support', 'Proven savings programs', 'Entrepreneurial tools and education', 'A clear path toward financial stability', 'A system designed by someone who has guided thousands toward success'],
                        subtitle: 'Most Importantly',
                        subdesc: 'You are not doing this alone.',
                        subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward — whether you want to earn more, keep more, or spend less.',
                        image: 'How-we-help-you/Why PYF Works.jpg'
                    },
                    start_path: {
                        headline: 'Start With The Path That Matches Your Goals',
                        desc: 'You can always change your path as you change your aims. PYF will support you every step of the way',
                        btn1_text: 'Start The Earn Path',
                        btn1_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm',
                        btn2_text: 'Start The Savings Path',
                        btn2_link: 'packages.html',
                        btn3_text: 'Start The Support Path',
                        btn3_link: 'business-support-package.html',
                        buttons: [
                            { text: 'Start The Earn Path', link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm', style: 'primary' },
                            { text: 'Start The Savings Path', link: 'packages.html', style: 'secondary' },
                            { text: 'Start The Support Path', link: 'business-support-package.html', style: 'primary' }
                        ]
                    },
                    sections: [
                        { id: 'hero', type: 'hero', label: 'Hero Banner' },
                        { id: 'why-exists', type: 'why_exists', label: 'Why PYF Exists' },
                        { id: 'problems', type: 'problems', label: 'Problems Most People Face' },
                        { id: 'mastering', type: 'mastering', label: 'Mastering Three Things' },
                        { id: 'designed-for', type: 'designed_for', label: 'Designed For' },
                        { id: 'three-ways', type: 'three_ways', label: 'Three Ways PYF Helps You Move Forward' },
                        { id: 'why-works', type: 'why_works', label: 'Why PYF Works' },
                        { id: 'start-path', type: 'start_path', label: 'Start Path' }
                    ]
                },
                isContentReady: false,
                resolvedImages: {
                    hero: '',
                    whyExists: '',
                    problemsBlock1: '',
                    problemsBlock2: '',
                    masteringCard1: '',
                    masteringCard2: '',
                    masteringCard3: '',
                    designedFor: '',
                    threeWaysCard1: '',
                    threeWaysCard2: '',
                    threeWaysCard3: '',
                    whyWorks: ''
                },
                loadedImages: {
                    hero: false,
                    whyExists: false,
                    problemsBlock1: false,
                    problemsBlock2: false,
                    masteringCard1: false,
                    masteringCard2: false,
                    masteringCard3: false,
                    designedFor: false,
                    threeWaysCard1: false,
                    threeWaysCard2: false,
                    threeWaysCard3: false,
                    whyWorks: false
                },

                getDefaultSections() {
                    return [
                        { id: 'hero', type: 'hero', label: 'Hero Banner' },
                        { id: 'why-exists', type: 'why_exists', label: 'Why PYF Exists' },
                        { id: 'problems', type: 'problems', label: 'Problems Most People Face' },
                        { id: 'mastering', type: 'mastering', label: 'Mastering Three Things' },
                        { id: 'designed-for', type: 'designed_for', label: 'Designed For' },
                        { id: 'three-ways', type: 'three_ways', label: 'Three Ways PYF Helps You Move Forward' },
                        { id: 'why-works', type: 'why_works', label: 'Why PYF Works' },
                        { id: 'start-path', type: 'start_path', label: 'Start Path' }
                    ];
                },

                normalizeSections(sections) {
                    const defaults = this.getDefaultSections();
                    if (!Array.isArray(sections)) return defaults;

                    return sections
                        .map((section, index) => {
                            const type = section?.type || section?.id;
                            const fallback = defaults.find(item => item.type === type || item.id === type);
                            if (!fallback) return null;

                            return {
                                id: section?.id || `${fallback.id}-${index + 1}`,
                                type: fallback.type,
                                label: section?.label || fallback.label
                            };
                        })
                        .filter(Boolean);
                },

                hasSection(type) {
                    return (this.pageData.sections || []).some(section => section.type === type);
                },

                getHeroButtons() {
                    if (Array.isArray(this.pageData.hero?.buttons) && this.pageData.hero.buttons.length) {
                        return this.pageData.hero.buttons.filter(button => button && (button.text || button.link));
                    }

                    return [
                        { text: this.pageData.hero?.btn1_text, link: this.pageData.hero?.btn1_link, style: 'primary' },
                        { text: this.pageData.hero?.btn2_text, link: this.pageData.hero?.btn2_link, style: 'secondary' }
                    ].filter(button => button.text || button.link);
                },

                getHeroButtonClass(button, index) {
                    const style = button?.style || (index === 0 ? 'primary' : 'secondary');
                    const base = 'font-bold py-4 px-8 rounded shadow transition uppercase text-sm tracking-wide w-full sm:w-auto';
                    return style === 'primary'
                        ? `${base} bg-brand-primary text-white hover:bg-[#2d7a00]`
                        : `${base} bg-[#dcfce7] text-brand-primary hover:bg-white`;
                },

                getProblemCards() {
                    if (Array.isArray(this.pageData.problems?.cards) && this.pageData.problems.cards.length) {
                        return this.pageData.problems.cards.filter(card => card && (card.title || (Array.isArray(card.list) && card.list.length)));
                    }

                    return [this.pageData.problems?.block1, this.pageData.problems?.block2].filter(Boolean);
                },

                getProblemCardImage(card, index) {
                    if (card?.image) return card.image;
                    return index % 2 === 0
                        ? 'How-we-help-you/Problems most people face_1.jpg'
                        : 'How-we-help-you/Problems most people face_2.jpg';
                },

                getMasteringCards() {
                    if (Array.isArray(this.pageData.mastering?.cards) && this.pageData.mastering.cards.length) {
                        return this.pageData.mastering.cards.filter(card => card && (card.title || card.desc || (Array.isArray(card.list) && card.list.length)));
                    }

                    return [this.pageData.mastering?.card1, this.pageData.mastering?.card2, this.pageData.mastering?.card3].filter(Boolean);
                },

                getThreeWaysCards() {
                    if (Array.isArray(this.pageData.three_ways?.cards) && this.pageData.three_ways.cards.length) {
                        return this.pageData.three_ways.cards.filter(card => card && (card.title || card.best_for || (Array.isArray(card.list) && card.list.length)));
                    }

                    return [this.pageData.three_ways?.card1, this.pageData.three_ways?.card2, this.pageData.three_ways?.card3].filter(Boolean);
                },

                getThreeWaysCardImage(card, index) {
                    if (card?.image) return card.image;
                    const fallbacks = [
                        'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg',
                        'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg',
                        'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg'
                    ];
                    return fallbacks[index] || fallbacks[fallbacks.length - 1];
                },

                getStartPathButtons() {
                    if (Array.isArray(this.pageData.start_path?.buttons) && this.pageData.start_path.buttons.length) {
                        return this.pageData.start_path.buttons.filter(button => button && (button.text || button.link));
                    }

                    return [
                        { text: this.pageData.start_path?.btn1_text, link: this.pageData.start_path?.btn1_link, style: 'primary' },
                        { text: this.pageData.start_path?.btn2_text, link: this.pageData.start_path?.btn2_link, style: 'secondary' },
                        { text: this.pageData.start_path?.btn3_text, link: this.pageData.start_path?.btn3_link, style: 'primary' }
                    ].filter(button => button.text || button.link);
                },

                getStartPathButtonClass(button, index) {
                    const style = button?.style || (index % 2 === 1 ? 'secondary' : 'primary');
                    return style === 'secondary'
                        ? 'bg-gradient-to-r from-[#bbf7d0] to-[#86efac] text-brand-dark hover:brightness-105'
                        : 'bg-gradient-to-r from-[#389400] to-[#75C400] text-white hover:opacity-95';
                },

                syncSectionLayout() {
                    const root = document.querySelector('[data-hwhy-sections-root]');
                    if (!root) return;

                    const nodesByType = new Map(
                        Array.from(root.querySelectorAll('[data-hwhy-section]')).map(node => [node.dataset.hwhySection, node])
                    );

                    (this.pageData.sections || []).forEach(section => {
                        const node = nodesByType.get(section.type);
                        if (node) root.appendChild(node);
                    });
                },

                getImageTargets(content) {
                    return {
                        hero: content.hero?.image || 'How-we-help-you/How we help you_hero image.jpg',
                        whyExists: content.why_exists?.image || 'How-we-help-you/Why PYF Exists.jpg',
                        problemsBlock1: content.problems?.block1?.image || 'How-we-help-you/Problems most people face_1.jpg',
                        problemsBlock2: content.problems?.block2?.image || 'How-we-help-you/Problems most people face_2.jpg',
                        masteringCard1: content.mastering?.card1?.image || 'How-we-help-you/Mastering Three Things_Earn More.jpg',
                        masteringCard2: content.mastering?.card2?.image || 'How-we-help-you/Mastering Three Things_Save More.jpg',
                        masteringCard3: content.mastering?.card3?.image || 'How-we-help-you/Mastering Three Things_Spend Less.jpg',
                        designedFor: content.designed_for?.image || 'How-we-help-you/PYF Is Designed For.jpg',
                        threeWaysCard1: content.three_ways?.card1?.image || 'How-we-help-you/PYF Helps You Move Foward_Earn Referral Fees.jpg',
                        threeWaysCard2: content.three_ways?.card2?.image || 'How-we-help-you/PYF Helps You Move Foward_save money on everyday living .jpg',
                        threeWaysCard3: content.three_ways?.card3?.image || 'How-we-help-you/PYF Helps You Move Foward_support for you home based business.jpg',
                        whyWorks: content.why_works?.image || 'How-we-help-you/Why PYF Works.jpg'
                    };
                },

                preloadImage(src) {
                    return new Promise((resolve, reject) => {
                        if (!src) {
                            reject(new Error('Missing image source'));
                            return;
                        }

                        const img = new Image();
                        img.onload = () => resolve(src);
                        img.onerror = () => reject(new Error(`Failed to preload image: ${src}`));
                        img.src = src;
                    });
                },

                async resolveImages(content) {
                    const imageTargets = this.getImageTargets(content);

                    await Promise.all(Object.entries(imageTargets).map(async ([key, src]) => {
                        try {
                            const loadedSrc = await this.preloadImage(src);
                            this.resolvedImages[key] = loadedSrc;
                            this.loadedImages[key] = true;
                        } catch (error) {
                            console.error(error);
                        }
                    }));
                },
                
                async init() {
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    let mergedContent = { ...this.pageData };
                    
                    try {
                        let { data, error } = await supabase.from('site_content').select('*').eq('page_id', 'how_we_help_you').single();
                        if (error) throw error;
                        if (data) {
                            const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                            mergedContent = { ...this.pageData, ...(loadedContent || {}) };
                        }
                    } catch (e) {
                        console.error("Failed to load CMS data", e);
                    }

                    mergedContent.sections = this.normalizeSections(mergedContent.sections);
                    this.pageData = mergedContent;
                    this.syncSectionLayout();
                    this.isContentReady = true;
                    await this.resolveImages(mergedContent);
                }
            }));
        });
    
