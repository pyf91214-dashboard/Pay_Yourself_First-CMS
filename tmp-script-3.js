
    const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    
    document.addEventListener('alpine:init', () => {
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
        
        Alpine.data('cmsManager', () => ({
            activePage: 'home',
            sidebarOpen: false,
            cmsSidebarOpen: false,
            isLoading: true,
            isSaving: false,
            isUploadingImage: false,
            selectedHomeSectionToAdd: '',
            selectedHowWeHelpYouSectionToAdd: '',
            pageData: {
                home: {
                    hero_title: 'An Empowered Lifestyle Starts With Putting Money Back In Your Pocket',
                    hero_subtitle: 'PYF is a lifestyle empowerment company dedicated to educating, equipping, and empowering families and individuals with practical strategies, systems, and tools for financial independence.',
                    hero_image: 'Homepage/Website Home Hero Image.jpg',
                    pillars: [
                        { title: "Save Money", desc: "Access millions of discounts on products and services you already buy.", icon: "fa-piggy-bank", color: "blue-500" },
                        { title: "Reduce Taxes", desc: "Leverage business deductions to keep more of what you earnâ€”with professional CPA level support.", icon: "fa-file-invoice-dollar", color: "brand-primary" },
                        { title: "Build Income", desc: "As an affiliate you can create a residual revenue stream on your own schedule, independent of an employer. It is free and optional to be a PYF affiliate. There are no upfront or ongoing qualifications to be an affiliate.", icon: "fa-chart-line", color: "green-500" }
                    ],
                    tax_systems: {
                        headline: 'There Are <span class="text-brand-primary">Two</span> Tax Systems. Which One Are <span class="text-brand-primary">You</span> In?',
                        desc: 'Many work hard yet still fall behind financially. With rising costs and stagnant wages, the financial squeeze is real. The solution? Most overlook the legitimate, government-approved tax deductions that can dramatically improve your finances.',
                        perks_headline: 'If any of these perks sound attractive, you\'re not alone:',
                        perks_list: [
                            'Imagine keeping $3,000-$10,000 more annually by accessing tax deductions',
                            'Building income through our affiliate program',
                            'Envision having professional support without the professional price tag'
                        ],
                        image: 'Homepage/Two Tax Systems.jpg'
                    },
                    peace_of_mind: {
                        headline: 'Lower <span class="text-brand-primary">Taxes</span>, Higher <span class="text-brand-primary">Cash</span> Flow, And Increased <span class="text-brand-primary">Financial Peace Of Mind.</span>',
                        desc: 'Business Support Package combines tax support, legal services, entrepreneurship training, and moreâ€”in one comprehensive plan.',
                        advantages_headline: 'Key Advantages',
                        advantages_list: [
                            'Leverage business tax deductions. Including expenses you currently have.',
                            'Get tax, legal, and business guidance when you need it.',
                            'Educational resources and support tools for entrepreneurs.'
                        ],
                        image: 'Homepage/Financial Peace of Mind.jpg'
                    },
                    support_features: [
                         { title: "Tax Support", desc: "Guidance from experienced tax professionals", icon: "fa-file-invoice-dollar" },
                         { title: "Legal Support", desc: "Help with business and personal legal matters", icon: "fa-scale-balanced" },
                         { title: "Business Support", desc: "Tools, training, and coaching for growth", icon: "fa-users" },
                         { title: "Discount Platform", desc: "Savings on everyday essentials", icon: "fa-percent" }
                    ],
                    history: {
                        headline: "Serving People Since 2011",
                        desc: "For over a decade, Pay Yourself First has helped W-2 employees, independent contractors, and entrepreneurs legally reduce their tax liability, cut expenses, and build an additional income stream.",
                        guarantee: "All backed by our 30-Day Money-Back Guarantee."
                    },
                    testimonials: {
                        headline: "Real People. Real Results.",
                        items: [
                            { quote: "Pay Yourself First shifted my mindset from a consumer to a CEO. A person who owns their own business.", author_initials: "DT", author_name: "D. Thomas" },
                            { quote: "I've saved much more money using Pay Yourself First than what I pay for the subscription.", author_initials: "CW", author_name: "C. Wheeler" },
                            { quote: "Pay Yourself First changed my position from owing taxes every year to getting a larger refund. In the short-term I can instantly posture myself into a better tax outcome this year. I can instantly use business owner deductions for my own personal tax account this year.", author_initials: "MM", author_name: "M. Moore" }
                        ]
                    },
                    packages_intro: {
                        headline: 'Save Money. Make Money. Or Both.<br><span class="text-brand-primary">Which Package Is Right For You?</span>',
                        desc: 'Business Support Package is our most popular package because it combines tax savings guidance, entrepreneurship training and support, discounts, and professional support in one comprehensive system. But we also offer alternative Packages based on your specific goals.',
                        affiliate_text: 'It is free to become a PYF Affiliate. There is no cost and no upfront or ongoing requirements or qualifications. As a PYF affiliate you can receive referral fees when you share PYF products with others. If a product is paid on a one-time basis you will be paid a one-time referral fee. If a product is paid on a monthly basis you will be paid a monthly referral fee. You can become a PYF affiliate without purchasing a PYF product or in combination with any PYF product.',
                        affiliate_img: 'Homepage/Affiliate Program.jpg'
                    },
                    bottom_cta: {
                        headline: 'Don\'t Overpay Your Taxes. Keep <span class="text-brand-primary">More</span> Of Your <span class="text-brand-primary">Earnings</span>. <br> Save More <span class="text-brand-primary">Money</span>.',
                        desc: 'Get the PYF Business Support Package and start keeping more of what you earn while building additional income if you choose to.',
                        btn_text: 'Get Business Support Package',
                        btn_link: 'business-support-package.html',
                        features: [
                            { icon: 'fa-check-circle', text: '30-Day Money-Back Guarantee' },
                            { icon: 'fa-user-tie', text: 'Professional CPA Support Included' },
                            { icon: 'fa-file-contract', text: 'No Long Term Contract' }
                        ]
                    },
                    service_packages: [
                        { title: 'Business Support Package', desc: 'The ultimate package for tax savings, business growth, and financial independence. Includes all features.', btn_text: 'Get Business Support Package', btn_link: 'business-support-package.html' },
                        { title: 'Doctor Power', desc: 'Convenient telehealth and wellness savings for families. Access doctors 24/7 without high costs.', btn_text: 'Get Doctor Power', btn_link: 'doctor-power.html' },
                        { title: 'Dental Power', desc: 'Lower dental, vision, and hearing care costs. Keep your family\'s smile bright for less.', btn_text: 'Get Dental Power', btn_link: 'dental-power.html' },
                        { title: 'Purchase Power', desc: 'Save money on shopping, dining, entertainment, and more. Everyday discounts that add up fast.', btn_text: 'Get Purchase Power', btn_link: 'purchase-power.html' }
                    ],
                    sections: [
                        { id: 'hero', type: 'hero', label: 'Hero Banner' },
                        { id: 'pillars', type: 'pillars', label: 'The Three Pillars' },
                        { id: 'tax-systems', type: 'tax_systems', label: 'Tax Systems' },
                        { id: 'peace-of-mind', type: 'peace_of_mind', label: 'Peace Of Mind' },
                        { id: 'support-features', type: 'support_features', label: 'Support Features' },
                        { id: 'history', type: 'history', label: 'History' },
                        { id: 'testimonials', type: 'testimonials', label: 'Testimonials' },
                        { id: 'packages-intro', type: 'packages_intro', label: 'Packages Intro' },
                        { id: 'bottom-cta', type: 'bottom_cta', label: 'Bottom CTA' }
                    ]
                },
                footer: {
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
                },
                how_we_help_you: {
                    hero: {
                        headline: 'We Help You Gain Greater Control Of\n<span class="text-[#bbf7d0]">Your Financial Life</span>',
                        desc: 'Most people work hard, pay their bills, and still feel behind. <br class="hidden md:block">\nPay Yourself First gives you the tools, guidance, and support to earn more, keep more, and spend less â€” all with a simple, practical system designed for everyday Americans.',
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
                            desc: 'PYF offers simple, accessible ways for people to open new income pathways through home-based entrepreneurship â€” supported by:',
                            list: [{ icon: 'graduation-cap', text: 'Education' }, { icon: 'wrench', text: 'Tools' }, { icon: 'users', text: 'Professional Guidance' }],
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
                        }
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
                            btn_text: 'Start Your Support Services',
                            btn_link: 'business-support-package.html'
                        }
                    },
                    why_works: {
                        headline: 'Why PYF Works',
                        desc: 'You don\'t have to pick a single path. You are free to choose a combination of any of the three or all three. Everything PYF offers is built to give everyday people an advantage normally reserved for the wealthy and very high-income earners.',
                        list: ['Professional and expert tax and legal support', 'Proven savings programs', 'Entrepreneurial tools and education', 'A clear path toward financial stability', 'A system designed by someone who has guided thousands toward success'],
                        subtitle: 'Most Importantly',
                        subdesc: 'You are not doing this alone.',
                        subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward â€” whether you want to earn more, keep more, or spend less.'
                    },
                    start_path: {
                        headline: 'Start With The Path That Matches Your Goals',
                        desc: 'You can always change your path as you change your aims. PYF will support you every step of the way',
                        btn1_text: 'Start The Earn Path',
                        btn1_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm',
                        btn2_text: 'Start The Savings Path',
                        btn2_link: 'packages.html',
                        btn3_text: 'Start The Support Path',
                        btn3_link: 'business-support-package.html'
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
                packages: {
                    hero: {
                        headline: 'Choose The Path That Fits Your Goals',
                        desc: 'You can save money, or you can receive referral fees, or you can do both â€” the choice is yours.',
                        btn1_text: 'I Want to Save Money',
                        btn1_link: '#service-packages',
                        btn2_text: 'I Want to Receive Referral Fees',
                        btn2_link: 'affiliate-plan.html',
                          image: 'Plans-overview/Packages_Hero.jpg'
                    },
                    two_paths: {
                        headline: 'Two Simple <span class="text-brand-primary">Paths</span>',
                        desc: 'Not sure where to start?<br>Choose the path that matches your priorities:',
                        path1_title: 'Path 1 â€” Save Money',
                        path1_desc: 'Pick one of our service plans. No affiliate enrollment required.',
                        path2_title: 'Path 2 â€” Earn Referral Fees',
                        path2_desc: 'Become an Affiliate and receive referral fees by sharing PYF with others.',
                        footer: 'You may choose either path individually or combine them at any time.',
                        btn1_text: 'View Service Packages',
                        btn1_link: 'packages.html',
                        btn2_text: 'Become An Affiliate',
                        btn2_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm',
                          image: 'Plans-overview/Packages_Two Simple Paths.jpg'
                    },
                    affiliate_program: {
                        headline: 'Affiliate <span class="text-brand-primary">Program</span>',
                        subtitle: 'Affiliate Program - <span class="text-brand-primary">$0/Month</span>',
                        desc: 'Become a PYF Affiliate at no cost. Receive referral fees when people you refer purchase PYF service packages.',
                        benefits_title: 'Key Benefits',
                        benefits_list: [
                            'Free to join',
                            'No purchase required',
                            'No monthly fees',
                            'No production requirements',
                            'Receive referral fees',
                            'Add any PYF service packages at any time'
                        ],
                        btn_text: 'Become An Affiliate',
                        btn_link: '#',
                          image: 'Plans-overview/Packages_Affiliate Program.jpg'
                    },
                    service_packages: {
                        headline: 'Service <span class="text-brand-primary">Packages</span>',
                        desc: 'These are consumer service packages. They do not require affiliate enrollment.',
                        packages: [
                            {
                                id: 'business',
                                title: 'Business Support Package',
                                badge: 'Most Popular',
                                price: '$149.99/MONTH',
                                desc: 'Our premium support package gives you the expert tax, legal, and business support you need to operate a business if you choose to, reduce your taxes to the legal minimum, and improve your financial position.',
                                best_for: 'People who are interested in tax deductions, business support services, entrepreneurship education, and financial literacy.',
                                includes_title: 'Includes Everything In Other Plans Plus:',
                                includes_list1: ['Tax-deduction support', 'CPA support', 'Personal & business legal'],
                                includes_list2: ['Business training & tools', 'Purchase Power', 'Add Dental/Doctor anytime'],
                                btn_text: 'View Business Support Package',
                                btn_link: 'business-support-package.html'
                            },
                            {
                                id: 'doctor',
                                title: 'Doctor Power',
                                badge: '',
                                price: '$24.95/mo',
                                desc: 'Telemedicine, wellness, fitness, personal legal support.',
                                best_for: 'Families seeking convenience & wellness.',
                                includes_title: 'Includes',
                                includes_list1: ['24/7 doctor access', 'Wellness programs', 'Family legal support', 'Dental Power', 'Purchase Power'],
                                includes_list2: [],
                                btn_text: 'View Details',
                                btn_link: 'doctor-power.html'
                            },
                            {
                                id: 'dental',
                                title: 'Dental Power',
                                badge: '',
                                price: '$16.95/mo',
                                desc: 'Save on dental, vision, hearing, and prescriptions.',
                                best_for: 'Significant dental & health savings.',
                                includes_title: 'Includes',
                                includes_list1: ['20%â€“60% dental savings', 'Vision program', 'Hearing program', 'Prescription savings', 'Purchase Power'],
                                includes_list2: [],
                                btn_text: 'View Details',
                                btn_link: 'dental-power.html'
                            },
                            {
                                id: 'purchase',
                                title: 'Purchase Power',
                                badge: '',
                                price: '$9.95/mo',
                                desc: 'Save on dining, groceries, shopping, travel, etc.',
                                best_for: 'Instant/flexible everyday savings.',
                                includes_title: 'Includes',
                                includes_list1: ['Dining & grocery', 'Retail & shopping', 'Travel savings', 'Automotive', 'Household savings'],
                                includes_list2: [],
                                btn_text: 'View Details',
                                btn_link: 'purchase-power.html'
                            }
                        ]
                    },
                    comparison_table: {
                        headline: 'Compare <span class="text-brand-primary">All Packages</span>',
                        rows: [
                            { feature: 'Monthly Subscription', affiliate: '$0', purchase_power: '$9.95', dental_power: '$16.95', doctor_power: '$24.95', business_support: '$149.99' },
                            { feature: 'Purchase Power Discounts', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-check text-gray-800"></i>', dental_power: 'Included', doctor_power: 'Included', business_support: 'Included' },
                            { feature: 'Dental Savings', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: 'Included', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Vision Savings', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: 'Included', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Hearing Savings', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: 'Included', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Prescription Savings', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: 'Included', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Telemedicine', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Wellness & Fitness', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: 'Included', business_support: 'Optional Add-On' },
                            { feature: 'Legal Support', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: 'Personal Legal Support', business_support: 'Personal & Business Legal Support' },
                            { feature: 'Tax-Deduction Support', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: '<i class="fas fa-times text-red-500"></i>', business_support: 'Included' },
                            { feature: 'Business Tools', affiliate: '<i class="fas fa-times text-red-500"></i>', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: '<i class="fas fa-times text-red-500"></i>', business_support: 'Included' },
                            { feature: 'Referral Earnings', affiliate: 'Yes', purchase_power: '<i class="fas fa-times text-red-500"></i>', dental_power: '<i class="fas fa-times text-red-500"></i>', doctor_power: '<i class="fas fa-times text-red-500"></i>', business_support: '<i class="fas fa-times text-red-500"></i>' },
                            { feature: 'Add-On Friendly', affiliate: '<i class="fas fa-check text-gray-800"></i>', purchase_power: '<i class="fas fa-check text-gray-800"></i>', dental_power: '<i class="fas fa-check text-gray-800"></i>', doctor_power: '<i class="fas fa-check text-gray-800"></i>', business_support: '<i class="fas fa-check text-gray-800"></i>' }
                        ]
                    },
                    faq: {
                        headline: 'Frequently Asked <span class="text-brand-primary">Questions</span>',
                        questions: [
                            { q: 'Do I need to be an affiliate to purchase a service plan?', a: 'No. All service plans can be purchased individually. Affiliate enrollment is completely optional.' },
                            { q: 'Is Business Support Package an affiliate plan?', a: 'No. Business Support Package is a service plan.' },
                            { q: 'Can affiliates earn from service plan referrals?', a: 'Yes.' },
                            { q: 'Can I change plans later?', a: 'Yes. All plans are month-to-month and can be modified or combined anytime.' },
                            { q: 'Do all plans include Purchase Power?', a: 'All service plans except the Affiliate Program include Purchase Power.' }
                        ]
                    },
                    cta: {
                        headline: 'Ready to Move Forward?',
                        desc: 'Start saving, start earning referral fees, or both. Choose the path that matches your goals',
                        btn1_text: 'BECOME AN AFFILIATE',
                        btn1_link: '#',
                        btn2_text: 'View Service Packages',
                        btn2_link: '#service-packages'
                    }
                },
                tax: {
                    hero: {
                        headline: 'Access To Expert Tax Preparation <br> And Advice For Just $49',
                        desc: 'Service provided by a national Professional Tax Firm with 30 years of experience and CPAs on staff.<br> Federal and State filing included. Professional Tax Advice all season long.',
                        bg_image: 'Tax-season-discount/Tax Season Discount_Hero.jpg',
                        btn_text: 'Start My Access',
                        btn_link: 'https://buy.stripe.com/3cIfZa2kiex9gyg4lOcIE02'
                    },
                    includes: {
                        headline: 'Your <span class="bg-brand-primary text-white px-2 py-1 rounded mx-1">$49</span> Tax Season Discount Package <span class="text-brand-primary">Includes</span>',
                        items: [
                            { icon: 'user-tie', title: 'Professional Tax Preparation', desc: 'Service provided by a professional tax firm with 30 years of experience advising over 1 million taxpayers' },
                            { icon: 'file-contract', title: 'Federal and State Filing', desc: 'Preparation and E-Filing for both returns' },
                            { icon: 'calendar-alt', title: 'Schedule C or E Filing', desc: 'Flat $60 for Schedule C or E (Personal or LLC)' },
                            { icon: 'user-check', title: 'Professional Tax Advice', desc: 'Access to human experts throughout tax season' },
                            { icon: 'comments', title: 'Review of Prior Year Returns', desc: 'Provided by expert and experienced tax professionals' },
                            { icon: 'folder-open', title: 'Second Opinion Available', desc: 'Independent review from tax professionals' },
                            { icon: 'shield-alt', title: '$1,000,000 Liability Protection', desc: 'Tax services backed by a professional liability insurance policy.' },
                            { icon: 'balance-scale', title: 'Tax Attorney Consultation', desc: 'Access to attorney consultation for business matters' },
                            { icon: 'gavel', title: 'Business Legal Services', desc: 'Access to ongoing discounted legal support through our partners' }
                        ]
                    },
                    pricing: {
                        regular_prep: '$ 279',
                        regular_advice: '$ 119',
                        total_value: '$ 398',
                        your_price: '$49',
                        you_save: '$349'
                    },
                    done_for_you: {
                        headline: 'Affordable Tax Preparation And Advice From A Human <span class="text-brand-primary">Expert</span>, Not Just Software.',
                        desc: 'Get your max refund and file your taxes with confidence. No need to try and save money on tax preparation using "Do It Yourself" software. Have your taxes prepared and filed by using a professional firm at a very affordable price.',
                        image: 'Tax-season-discount/Tax Season Discount_Affordable Tax Preparation.jpg',
                        sub_headline: 'If any of these sound familiar',
                        list: [
                            "You're tired of overpaying for tax preparation",
                            "You're not confident about the credentials of your tax preparer",
                            "You're frustrated and unconfident about preparing your taxes yourself",
                            "You want professional help without spending hundreds of dollars",
                            "You need reliable tax advice throughout the season, not just at filing time"
                        ],
                        footer_box: 'This Package is for you!',
                        limited_offer: 'Limited Time Offer | Purchase Period: December 1, 2025 â€“ March 31, 2026',
                        btn_text: 'Start My Access',
                        btn_link: 'https://buy.stripe.com/3cIfZa2kiex9gyg4lOcIE02'
                    },
                    savings_table: {
                        headline: 'See How Much You <span class="text-brand-primary">Save With PYF</span>',
                        desc: 'Professional tax services for individuals and businesses at affordable prices.',
                        rows: [
                            { return_type: 'Simple 1040', diy: '$50-$100', chain: '$200-$300', cpa: '$220-$300', pyf: '$49', save: '$151-$251' },
                            { return_type: '1040 + Itemized', diy: '$100-$150', chain: '$300-$400', cpa: '$323-$400', pyf: '$49', save: '$274-$351' },
                            { return_type: '1040 + Schedule C/E', diy: '$150-$200', chain: '$400-$600', cpa: '$400-$600', pyf: '$109', save: '$291-$491' },
                            { return_type: 'C Corporation', diy: 'N/A*', chain: '$800-$2,000', cpa: '$913-$2,500', pyf: '$395', save: '$518-$2,105' },
                            { return_type: 'S Corporation', diy: 'N/A*', chain: '$800-$2,000', cpa: '$800-$2,000', pyf: '$395', save: '$405-$1,605' }
                        ],
                        footer: '*Corporate returns too complex for DIY software'
                    },
                    features: {
                        headline: 'Done For You. NOT Do-It-Yourself.',
                        image: 'Tax-season-discount/Tax Season Discount_Done For You.jpg',
                        list: [
                            'Credential Tax Experts',
                            'CPA\'s on staff',
                            '100% U.S Based',
                            '$1m Liability Insurance',
                            'Unlimited Sessions',
                            'Jan 1 - Apr 30 2026'
                        ],
                        mid_cta: {
                            desc: 'Whether you\'re filing as an individual or running a business, professional tax preparation shouldn\'t break the bank. Most Americans pay $220 - $400+ for basic returns, and business owners pay $800-$2,500 for corporate filings. With PYF Tax Season Discount, you get the same professional CPA expertise, unlimited advice, and $1M liability insuranceâ€”for a fraction of the cost.',
                            btn_text: 'Start My Access',
                            btn_link: 'https://buy.stripe.com/3cIfZa2kiex9gyg4lOcIE02'
                        }
                    },
                    timeline: {
                        headline: 'Serving People <span class="text-brand-primary">Since 2011</span>',
                        desc: 'Pay Yourself First connects you with a national professional tax firm that has served over 1 million taxpayers since 1995. With 30 years of experience, CPAs on staff, and a $1 million professional liability insurance policy backing all advice, you get the expertise and protection you deserveâ€”at a price that actually makes sense. Services are provided by independent third-party professionals.',
                        image: 'Tax-season-discount/Tax Season Discount_Serving People Since 2011.jpg',
                        second_headline: 'Program <span class="text-brand-primary">Details & Timeline</span>',
                        col1_title: 'Program Dates',
                        col1_desc: '<p><span class="font-bold">Purchase Period:</span> December 1, 2025 â€“ March 31, 2026</p><p><span class="font-bold">Service Active:</span> January 1 â€“ April 30, 2026</p><p><span class="font-bold">Documentation Deadline:</span> March 31, 2026</p>',
                        col2_title: 'Pricing',
                        col2_price: '$49',
                        col2_subline: '(Regular price $99)',
                        col2_desc: '<p>Schedule C/E: + $60 if needed</p><p>Corporate filings: $395 per return</p>',
                        col3_title: 'What\'s Next',
                        col3_desc: 'Sign up today and lock in your rate. We\'ll connect you with your tax professionals when you\'re ready to file.'
                    },
                    faq: {
                        headline: 'Common Questions About <span class="text-brand-primary">Tax Season Discount</span>',
                        questions: [
                            { q: 'What is the service period for this Package?', a: 'The service is active from January 1 â€“ April 30, 2026. You can purchase the Package from December 1, 2025 through March 31, 2026 to lock in your $49 rate.' },
                            { q: 'What\'s included in the $49?', a: 'Access to federal and state tax preparation and filing, plus unlimited tax advice from professionals throughout the tax season.' },
                            { q: 'What if I have Schedule C or E?', a: 'Schedule C or E filing is available for a flat $60 fee (Personal or LLC) in addition to the $49 base price. These are the most common schedules. Other schedules are included at no extra cost or are deeply discounted.' },
                            { q: 'What if I have a C Corporation or an S Corporation?', a: 'The fee for corporate filings is $395 per return.' },
                            { q: 'Is there a guarantee?', a: 'All tax advice and preparation provided is backed by a $1,000,000 professional liability insurance policy for your protection.' },
                            { q: 'Do I need to be a PYF affiliate to purchase this?', a: 'No. This service is available to anyone. Affiliate enrollment is completely optional and free.' },
                            { q: 'Can I add affiliate enrollment later?', a: 'Yes. You can become an affiliate at any timeâ€”during your initial purchase or after.' },
                            { q: 'What do affiliates earn?', a: 'Affiliates may receive referral fees when others purchase PYF products through their referral. Referral fee details are described in the affiliate materials you receive after enrollment.' },
                            { q: 'Are earnings guaranteed?', a: 'No. Referral fees depend solely on your personal activity and results vary.' }
                        ]
                    },
                    affiliate_cta: {
                        headline: 'Become A <span class="text-brand-primary">PYF Affiliate</span>',
                        sub_headline: 'Earn $5 Per Tax Season Discount Referral',
                        desc: 'It is free to become a PYF Affiliate. There is no cost and no upfront or ongoing requirements or qualifications. As a PYF affiliate you can receive referral fees when you share PYF products with others.',
                        list_title: 'Affiliate Pay',
                        list: [
                            '$5 per Tax Season Discount referral.',
                            'Up to $50 monthly for other products.',
                            'Earn by referring other PYF products.',
                            'No cost.'
                        ],
                        footer_text: 'You do not need to purchase a PYF product to become a PYF Affiliate.',
                        btn_text: 'Become an Affiliate',
                        btn_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm',
                        image: 'Tax-season-discount/Tax Season Discount_Become An Affiliate.jpg'
                    },
                    bottom_cta: {
                        headline: 'Don\'t Miss This <span class="text-brand-primary">Limited Time Offer</span>',
                        desc: 'Get professional tax preparation from a national tax firm for just $49. This package is only available during the 2026 tax season (January 1 â€“ April 30).',
                        btn_text: 'Start My Access',
                        btn_link: 'https://buy.stripe.com/3cIfZa2kiex9gyg4lOcIE02',
                        features: [
                            'Serviced by a professional tax firm',
                            '$1M Liability Insurance',
                            '30 Years Experience',
                            'Federal & State Filing Included'
                        ]
                    }
                },
                support: {
                    hero: {
                        headline: 'Pay Yourself First Customer and Affiliate FAQ',
                        desc: "This FAQ answers common questions about our services and affiliate program.\nWhether you're considering becoming a customer, an affiliate, or both, \nyou'll find clear explanations to help you understand exactly what PYF offers.",
                        image: 'Support-Page/Support Page_Hero.jpg'
                    },
                    categories: [
                        {
                            title: 'General Questions',
                            questions: [
                                { q: 'What is Pay Yourself First?', a: 'Pay Yourself First (PYF) is a financial empowerment company that helps you earn more, keep more, and spend less. We offer discount programs, health and wellness services, and an affiliate program that allows you to earn referral fees by sharing PYF products with others.' }
                            ]
                        }
                    ]
                },
                about_us: {
    "hero": {
        "headline": "We're Here To Help <span class=\"text-[#bbf7d0]\">Everyday People</span><br>\n                    Take Control Of Their Financial Future",
        "desc": "Pay Yourself First was created to make financial stability accessible to everyone, not just the wealthy or very high-income earners. Our system gives people access to the tools, guidance, and support to earn more, keep more, and spend less through practical, real-world solutions.",
        "btn1_text": "How We Help You",
        "btn1_link": "how-we-help-you.html",
        "btn2_text": "View Our Packages",
        "btn2_link": "packages.html",
        "image": "About-us/About Us_Hero.jpg"
    },
    "who_we_are": {
        "headline": "Who <span class=\"text-brand-primary\">We Are</span>",
        "desc1": "Pay Yourself First (PYF) is a financial empowerment company built on a simple belief: <span class=\"font-bold text-brand-primary\">You deserve a clear, practical way to improve your finances.</span>",
        "desc2": "As the cost of living rises and financial pressure grows, too many people feel stuck.",
        "list": [
            "W-2 workers overpaying taxes without realizing it",
            "1099 earners facing unstable income",
            "Families spending more but saving less",
            "Individuals working hard but falling behind financially."
        ],
        "desc3": "PYF was created to solve these problems by giving you access to the tools, education, and professional support they need to gain financial control.",
        "desc4": "Our company is built around a system. One designed to help people break\nnegative financial cycles, build financial stability, and move forward with clarity\nand confidence.",
        "image": "About-us/About Us_Who We Are.jpg"
    },
    "origin": {
        "headline": "Our <span class=\"text-brand-primary\">Origin</span>",
        "desc1": "PYF was built by financial professionals with decades of experience guiding real people\u2014just like you\u2014toward better financial outcomes. Through this work, a consistent pattern emerged:",
        "list": [
            "People earned money but struggled to keep it",
            "Tax rules were confusing and costly",
            "Financial tools used by the wealthy were out of reach for most",
            "Independent earners lacked support systems",
            "Many families headed toward an uncertain financial future"
        ],
        "desc2": "The team behind PYF recognized a gap: people needed a system \u2014 not just products, tips, or one-time fixes, but a comprehensive approach that helped them improve their financial lives year after year.",
        "headline_bottom": "PYF was created to <span class=\"text-brand-primary\">fill that gap.</span>",
        "image": "About-us/About Us_Our Origin.jpg"
    },
    "mission": {
        "headline": "Our <span class=\"text-brand-primary\">Mission</span>",
        "subtitle": "Our mission is simple",
        "desc": "To help everyday people gain control of their finances by giving them access to tools, education, and expert support normally out of reach to them.",
        "image": "About-us/About Us_Our Mission.jpg"
    },
    "serving": {
        "headline": "Serving Everyday Americans For Over A <span class=\"text-brand-primary\">Decade</span>",
        "stats": [
            {
                "title": "14+ Years",
                "desc": "In business supporting individuals and families."
            },
            {
                "title": "46 States",
                "desc": "Nationwide coverage and accessibility."
            },
            {
                "title": "Thousands",
                "desc": "Of users building better financial futures."
            }
        ],
        "principles": [
            {
                "icon": "fas fa-brain",
                "title": "Taxpayer Awareness"
            },
            {
                "icon": "fas fa-book-reader",
                "title": "Financial Literacy"
            },
            {
                "icon": "fas fa-city",
                "title": "Entrepreneurship"
            }
        ],
        "image": "About-us/About Us_Serving Everyday Americans.jpg"
    },
    "system": {
        "headline": "A system, not a personality. <br> <span class=\"text-brand-primary\">PYF is designed </span> to work regardless of who <span class=\"text-brand-primary\">uses </span> it",
        "subtitle": "Financial control comes from mastering three critical levers:",
        "cards": [
            {
                "id": "1",
                "title": "1. Earn More",
                "desc": "PYF offers simple, accessible ways for people to open new income pathways through home-based entrepreneurship \u2014 supported by:",
                "list": [
                    "Education",
                    "Tools",
                    "Professional Guidance"
                ],
                "image": "About-us/About Us_Built For Real Life_Earn More.jpg"
            },
            {
                "id": "2",
                "title": "2. Keep More",
                "desc": "Most W-2 earners unknowingly overpay their taxes. PYF connects users with licensed tax professionals who help them:",
                "list": [
                    "Adjust withholding correctly",
                    "Unlock home-based deductions",
                    "Maximize tax savings",
                    "Reduce taxes to legal minimum"
                ],
                "image": "About-us/About Us_Built For Real Life_Keep More.jpg",
                "quote": "\"This single category often creates the biggest transformation for everyday Americans.\""
            },
            {
                "id": "3",
                "title": "3. Spend Less",
                "desc": "Access to nationwide savings programs that reduce everyday expenses, including:",
                "list": [
                    "Shopping",
                    "Dining",
                    "Vision",
                    "Dental",
                    "Travel",
                    "Telehealth",
                    "Auto Care",
                    "Rx Meds"
                ],
                "footer": "Every dollar saved is a dollar that strengthens long-term stability.",
                "image": "About-us/About Us_Built For Real Life_Spend Less.jpg"
            }
        ]
    },
    "who_we_serve": {
        "headline": "Who We <span class=\"text-brand-primary\">Serve</span>",
        "subtitle": "PYF is built for real people with real financial goals.",
        "list": [
            "W-2 workers who want to keep more of what they earn",
            "1099 earners who need stability and tax guidance",
            "Home-based entrepreneurs building supplemental income",
            "Gig workers seeking predictable support",
            "Families lowering household expenses",
            "Individuals planning for long-term security"
        ],
        "footer": "If financial improvement is your goal, PYF is designed for you.",
        "image": "About-us/About Us_Who We Serve.jpg"
    },
    "different": {
        "headline": "What Makes <span class=\"text-brand-primary\">PYF Different</span>",
        "list": [
            "Professional-grade tax and legal support for everyday people",
            "Real savings programs that reduce real expenses",
            "Entrepreneurial tools and education resources that are simple to use",
            "A system, not a personality. PYF is designed to work regardless of who leads it",
            "A clear, step-by-step path toward financial clarity for those who want it",
            "Support year-round, not just during tax season"
        ],
        "image": "About-us/About Us_What Makes PYF Different.jpg"
    },
    "pledge": {
        "headline": "Our <span class=\"text-brand-primary\">Pledge To Help You</span>",
        "list": [
            "Understand your finances",
            "Reduce unnecessary expenses",
            "Legally minimize your tax burden",
            "Increase your income opportunities",
            "Gain a clearer path toward long-term stability",
            "Access professional guidance"
        ],
        "image": "About-us/About Us_Built For Real Life_Our Commitment.jpg"
    },
    "journey": {
        "headline": "Start Your PYF Journey",
        "desc": "Choose the path that fits your goals today. PYF will support\nyou every step of the way.",
        "btn1_text": "BECOME AN AFFILIATE",
        "btn1_link": "https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm",
        "btn2_text": "View Service Packages",
        "btn2_link": "packages.html"
    }
},
                contact_us: {
                    hero: {
                        headline: 'Get In Touch With Us',
                        desc: "Whether you have questions about our services, need support, or want to explore business partnerships, we're here to help.",
                        image: 'Contact-us/Contact Us_Hero.jpg'
                    },
                    form: {
                        heading: 'Contact <span class="text-brand-primary">Us</span>',
                        name_label: 'Name',
                        first_name_placeholder: 'First Name',
                        last_name_placeholder: 'Last Name',
                        email_label: 'Email',
                        email_placeholder: 'Enter your email address',
                        phone_label: 'Phone',
                        phone_placeholder: 'Phone Number',
                        reason_label: 'Reason For Contact',
                        reason_placeholder: '-Select-',
                        reason_options: [
                            'Billing Question',
                            'Technical Question',
                            'Product Question',
                            'Affiliate Question',
                            'Referral Fee Question',
                            'Business Inquiry',
                            'General Inquiry'
                        ],
                        message_label: 'Message Box',
                        message_placeholder: 'How can we help you?',
                        hear_about_label: 'How Did You Hear About Us?',
                        hear_about_placeholder: '-Select-',
                        hear_about_options: [
                            'Friend/Family',
                            'Pay Yourself First Affiliate',
                            'Online Ad',
                            'Social Media',
                            'Search Engine',
                            'Flyer'
                        ],
                        consent_label: 'Please Check',
                        consent_text: 'I consent to receive responses to my inquiry via email and, if I provided my phone number, by phone. I can opt out of promotional communications at any time.',
                        submit_text: 'Submit Message'
                    },
                    info: {
                        email: 'service@payyourselffirst.com',
                        phone: '1-800-123-4567',
                        address: 'Pay Yourself First\n107 S. West Street, Suite 557\nAlexandria, VA 22314\nCorrespondence Only',
                        response_time: '1-2 business days',
                        support_hours: '9am - 5pm ET'
                    },
                    portals: {
                        customer: 'https://payyourselffirst.benefithub.com/welcome/',
                        affiliate: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login'
                    },
                    support_section: {
                        heading: 'PYF <span class="text-brand-primary">Support</span> Email',
                        email_label: 'Email address:',
                        response_label: 'Expected response time:',
                        hours_label: 'Support hours:',
                        email_icon: 'fa-at',
                        response_icon: 'fa-clock',
                        hours_icon: 'fa-business-time',
                        customer_portal_text: 'Customer Portal Login',
                        affiliate_portal_text: 'Affiliate Portal Login'
                    },
                    service_provider: {
                        headline: 'Need Help With A <span class="text-brand-primary">Service Provider?</span>',
                        desc1: 'Some PYF plans include services delivered by licensed professionals through third-party partner networks.',
                        desc2: 'If you need assistance with:',
                        list: [
                            'Finding a participating provider',
                            'Scheduling an appointment',
                            'Provider-specific questions',
                            'Service quality concerns'
                        ],
                        desc3: "Please contact us using the form above, and we'll help coordinate with the appropriate provider network.",
                        image: 'Contact-us/Contact Us_Need help with a service provider.jpg',
                        cta_text: 'Go To Form',
                        cta_link: '#form'
                    },
                    bottom_text: 'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.',
                    bottom_notices: [
                        {icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response'},
                        {icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice'},
                        {icon: 'fa-flag-usa', text: 'Provider Availability Varies By State'}
                    ],
                    map_image: {
                        image: 'Contact-us/Contact Us_Mailing Address.jpg',
                        heading: 'Mailing Address'
                    },
                    service_links: {
                        heading: 'Helpful <span class="text-brand-primary">Service Links</span>',
                        link_prefix: 'Link to',
                        faq_icon: 'fa-globe',
                        faq_link: 'support.html', faq_text: 'Support / FAQ Page',
                        package_icon: 'fa-globe',
                        package_link: 'packages.html', package_text: 'Package Overview',
                        affiliate_icon: 'fa-globe',
                        affiliate_link: 'affiliate-page.html', affiliate_text: 'Affiliate Support Section'
                    },
                    form_action: 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit'
                },
                                business: {
                    hero: {
                        headline: 'Increase Your Cash Flow. <br> Improve Your Quality of Life. <br> Gain Your Freedom.',
                        desc: 'Join those who\'ve discovered how to access legitimate tax deductions and expert professional support to improve their financial life without quitting their day job.',
                        btn1_text: 'Get Business Support Package',
                        btn1_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                        btn2_text: 'Watch This Video',
                        btn2_link: '#',
                        image: 'Business-Support-Page/IPP_Hero.jpg'
                    },
                    intro: {
                        headline: 'Most People Don\'t Understand Enough About Business Tax Deductions. Even those who own businesses. Why would they? The United States tax code is over 70,000 pages long!',
                        desc1: 'Business owners have access to over 400 tax deductions that W-2 employees rarely use. Not because the system is unfair—but because most people simply don\'t know these deductions exist, whether they qualify, or how to document them properly.',
                        did_you_know: 'Did you know? <span class="text-gray-700 font-medium">W-2 employees can take advantage of these deductions as well.</span>',
                        desc2: 'The tax code rewards business activity. When you understand how the rules work, you can legally reduce your tax burden and bring more money back into your household.',
                        list_headline: 'If any of these sound familiar, you\'re not alone.',
                        list: [
                            'Are taxes taking too much of your income?',
                            'Are rising prices creating stress and financial pressure?',
                            'Are stagnant wages making it hard to get ahead?'
                        ],
                        image: 'Business-Support-Page/IPP_70,000 Pages.jpg'
                    },
                    ideal_for: {
                        headline: 'Business <span class="text-brand-primary">Support</span> Package',
                        desc: 'Business Support Package is available to anyone and is especially beneficial to business owners or those who are considering operating a business. IPP gives you the expert tax, legal, and business support you need to reduce your taxes to the legal minimum, and improve your financial position.',
                        list_headline: 'Business Support Package is ideal for:',
                        list: [
                            'Individuals who want expert tax and financial support',
                            'People who want to stop overpaying taxes',
                            'Business owners who want guidance on deductions',
                            'Business owners who want expert tax, legal, and business support'
                        ],
                        image: 'Business-Support-Page/IPP_Income Power Pro_1.jpg'
                    },
                    features: {
                        list: [
                            'Access to 400+ legitimate tax deductions (where applicable)',
                            'Expert and professional guidance from licensed tax and legal professionals',
                            'Professional CPA support included',
                            'Millions of products and services at discounted prices',
                            'Build monthly recurring referral income (As a PYF Affiliate)',
                            'Education and tools to help you organize and manage your financial life'
                        ],
                        image: 'Business-Support-Page/IPP_Income Power Pro_2.jpg'
                    },
                    advantages: {
                        headline: 'Core <span class="text-brand-primary">Advantages</span>',
                        card1: {
                            image: 'Business-Support-Page/IPP_Core Advantages_Tax Support.jpg',
                            title: 'Tax Support You Can Use Right Away',
                            desc: 'Put more money back into your pocket with professional guidance.',
                            list: [
                                'Learn which deductions apply',
                                'Reduce taxable income legally',
                                'Receive guidance on proper documentation',
                                'Adjust W-2 withholdings when appropriate'
                            ],
                            footer: '*Tax savings vary based on individual circumstances.'
                        },
                        card2: {
                            image: 'Business-Support-Page/IPP_Core Advantages_Business Education.jpg',
                            title: 'Business Education & Financial Literacy',
                            list: [
                                'Financial Planning For Entrepreneurs',
                                'Discounted Business Support Services',
                                'Multi-Millionaire Business Success Coach',
                                'Access to wealth-building strategies'
                            ]
                        },
                        card3: {
                            image: 'Business-Support-Page/IPP_Core Advantages_PYF Support System.jpg',
                            title: 'PYF SUPPORT SYSTEM',
                            desc: 'What\'s Included with Business Support Package:',
                            list: [
                                'Expert Business Guidance',
                                'Expert Tax Support',
                                'Personal Legal Support',
                                'Business Legal Support',
                                'Home Based/Small Business Education'
                            ]
                        }
                    },
                    value_section: {
                        headline: 'Business Support<span class="text-brand-primary">Package Value</span>',
                        table: [
                            { service: 'Tax Savings (Typical Range)', market: '$250 – $833', included: 'Savings Potential*' },
                            { service: 'Consumer Discount Savings', market: '$50 – $208', included: 'Included Savings Potential*' },
                            { service: 'Business Training & Coaching', market: '$1,500 – $4,500', included: 'Included' },
                            { service: 'CPA Support', market: '$239', included: 'Included' },
                            { service: 'Business Legal Services', market: '$169', included: 'Included' },
                            { service: 'Discount Platform Access', market: '$50', included: 'Included' },
                            { service: 'Community Access', market: '$100 – $300', included: 'Included' }
                        ],
                        total_value: 'Total Monthly Market Value + Savings: $2,358–$6,299 per month',
                        investment: 'Your Investment: $150 per month',
                        bottom_line: 'Bottom line: You\'re accessing over $6,000 per month in combined market value and potential savings for $150/month—a powerful value proposition backed by professional support.',
                        disclaimer: '*Savings vary based on individual spending habits, use of the platform, and legitimate qualification for deductible expenses.',
                        image: 'Business-Support-Page/IPP_Income Power Pro Value.jpg'
                    },
                    testimonials: {
                        headline: 'Testimonials',
                        desc: 'Since 2011 Pay Yourself First has helped W-2 employees, independent contractors, and entrepreneurs legally reduce tax liability and build compliant home-based businesses. Our affiliates range from teachers and government employees to corporate professionals — all learning to leverage the tax code the way business owners do.',
                        video_url: 'https://www.youtube-nocookie.com/embed/tw-MUhF0-g0?si=YXHjdcaqmfZ83-BB&amp;rel=0&controls=0'
                    },
                    investment_card: {
                        headline: 'Value',
                        price_title: 'Your Investment: $150/Month<br><span class="text-xs md:text-sm font-bold text-gray-600">(Tax-Deductible For Business Owners)</span>',
                        includes_title: 'Includes:',
                        list: [
                            'Tax guidance',
                            'Legal support',
                            'Business training',
                            'Consumer discount platform',
                            'Entrepreneurship resources',
                            'Community support',
                            'Optional affiliate enrollment at no additional cost'
                        ],
                        guarantee: 'Protected by our 30-Day Money-Back Guarantee',
                        btn_text: 'Get Business Support Package',
                        btn_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                        image: 'Business-Support-Page/IPP_Value.jpg',
                        image_caption: 'That’s $5 per day to unlock $3,000-$10,000 annually in potential tax savings.'
                    },
                    faq: {
                        headline: 'Common <span class="text-brand-primary">Questions</span>',
                        questions: [
                            { q: 'Can I use Business Support Package without starting a business?', a: 'Yes. Many services apply whether or not you operate a business. However, certain tax benefits require legitimate business activity. You should consult a tax professional for guidance specific to your situation.' },
                            { q: 'Do I need to enroll as an affiliate?', a: 'No. You may purchase Business Support Package standalone with no affiliate enrollment.' },
                            { q: 'Does enrolling as an affiliate cost anything?', a: 'No. Affiliate enrollment is optional. If you choose to enroll, it is provided at no additional cost.' },
                            { q: 'What do affiliates earn?', a: 'Affiliates may receive referral fees when others purchase PYF products through their referral. Referral fee details are described in the affiliate materials you receive after enrollment.' },
                            { q: 'Are earnings guaranteed?', a: 'No. Referral fees depend solely on your personal activity and results vary.' },
                            { q: 'Is Business Support Package a business opportunity?', a: 'No. Business Support Package is a service product. Affiliate enrollment is optional and provided for customers who choose to share PYF services.' },
                            { q: 'What\'s the difference between a standalone Affiliate and an IPP member who enrolls as an affiliate?', a: 'Both have access to the same affiliate program and can receive the same referral fees. However, Business Support Package members who are also affiliates have access to professional tax support, legal services, business training, and a discount platform—tools that help them build an affiliate business more effectively.' }
                        ]
                    },
                    bottom_cta: {
                        headline: 'Take Control of Your Taxes. Strengthen Your Finances. Move Forward with Confidence.',
                        btn1_text: 'BECOME AN AFFILIATE',
                        btn1_link: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login',
                        btn2_text: 'View Service Packages',
                        btn2_link: 'packages.html'
                    },
                    disclaimer_section: {
                        headline: 'Disclaimer',
                        blocks: [
                            { title: 'Service Provider Disclosure', text: 'Pay Yourself First (PYF) is the administrator of the Income Power Pro program. PYF does not directly provide tax, legal, financial, or discount services. All services included with Income Power Pro are delivered by independent third-party providers. Access to these services is subject to the terms, conditions, and availability of each provider.' },
                            { title: 'Earnings Disclaimer', text: 'Referral fee earnings are not guaranteed and vary based on individual effort and market conditions. Past results do not guarantee future performance.' }
                        ]
                    }
                }
            },

            normalizeContactUsData(contactData = {}) {
                const defaultReasonOptions = [
                    'Billing Question',
                    'Technical Question',
                    'Product Question',
                    'Affiliate Question',
                    'Referral Fee Question',
                    'Business Inquiry',
                    'General Inquiry'
                ];
                const defaultHearAboutOptions = [
                    'Friend/Family',
                    'Pay Yourself First Affiliate',
                    'Online Ad',
                    'Social Media',
                    'Search Engine',
                    'Flyer'
                ];
                const defaultServiceProviderList = [
                    'Finding a participating provider',
                    'Scheduling an appointment',
                    'Provider-specific questions',
                    'Service quality concerns'
                ];
                const defaultBottomNotices = [
                    { icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response' },
                    { icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice' },
                    { icon: 'fa-flag-usa', text: 'Provider Availability Varies By State' }
                ];

                const normalized = {
                    ...contactData,
                    hero: {
                        headline: 'Get In Touch With Us',
                        desc: "Whether you have questions about our services, need support, or want to explore business partnerships, we're here to help.",
                        image: 'Contact-us/Contact Us_Hero.jpg',
                        ...(contactData.hero || {})
                    },
                    form: {
                        heading: 'Contact <span class="text-brand-primary">Us</span>',
                        name_label: 'Name',
                        first_name_placeholder: 'First Name',
                        last_name_placeholder: 'Last Name',
                        email_label: 'Email',
                        email_placeholder: 'Enter your email address',
                        phone_label: 'Phone',
                        phone_placeholder: 'Phone Number',
                        reason_label: 'Reason For Contact',
                        reason_placeholder: '-Select-',
                        reason_options: defaultReasonOptions,
                        message_label: 'Message Box',
                        message_placeholder: 'How can we help you?',
                        hear_about_label: 'How Did You Hear About Us?',
                        hear_about_placeholder: '-Select-',
                        hear_about_options: defaultHearAboutOptions,
                        consent_label: 'Please Check',
                        consent_text: 'I consent to receive responses to my inquiry via email and, if I provided my phone number, by phone. I can opt out of promotional communications at any time.',
                        submit_text: 'Submit Message',
                        ...(contactData.form || {})
                    },
                    info: {
                        email: 'service@payyourselffirst.com',
                        phone: '1-800-123-4567',
                        address: 'Pay Yourself First\n107 S. West Street, Suite 557\nAlexandria, VA 22314\nCorrespondence Only',
                        response_time: '1-2 business days',
                        support_hours: '9am - 5pm ET',
                        ...(contactData.info || {})
                    },
                    portals: {
                        customer: 'https://payyourselffirst.benefithub.com/welcome/',
                        affiliate: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login',
                        ...(contactData.portals || {})
                    },
                    support_section: {
                        heading: 'PYF <span class="text-brand-primary">Support</span> Email',
                        email_label: 'Email address:',
                        response_label: 'Expected response time:',
                        hours_label: 'Support hours:',
                        email_icon: 'fa-at',
                        response_icon: 'fa-clock',
                        hours_icon: 'fa-business-time',
                        customer_portal_text: 'Customer Portal Login',
                        affiliate_portal_text: 'Affiliate Portal Login',
                        ...(contactData.support_section || {})
                    },
                    service_provider: {
                        headline: 'Need Help With A <span class="text-brand-primary">Service Provider?</span>',
                        desc1: 'Some PYF plans include services delivered by licensed professionals through third-party partner networks.',
                        desc2: 'If you need assistance with:',
                        list: defaultServiceProviderList,
                        desc3: "Please contact us using the form above, and we'll help coordinate with the appropriate provider network.",
                        image: 'Contact-us/Contact Us_Need help with a service provider.jpg',
                        cta_text: 'Go To Form',
                        cta_link: '#form',
                        ...(contactData.service_provider || {})
                    },
                    map_image: {
                        image: 'Contact-us/Contact Us_Mailing Address.jpg',
                        heading: 'Mailing Address',
                        ...(contactData.map_image || {})
                    },
                    service_links: {
                        heading: 'Helpful <span class="text-brand-primary">Service Links</span>',
                        link_prefix: 'Link to',
                        faq_icon: 'fa-globe',
                        faq_link: 'support.html',
                        faq_text: 'Support / FAQ Page',
                        package_icon: 'fa-globe',
                        package_link: 'packages.html',
                        package_text: 'Package Overview',
                        affiliate_icon: 'fa-globe',
                        affiliate_link: 'affiliate-page.html',
                        affiliate_text: 'Affiliate Support Section',
                        ...(contactData.service_links || {})
                    }
                };

                normalized.form.reason_options = Array.isArray(normalized.form.reason_options) && normalized.form.reason_options.length
                    ? normalized.form.reason_options
                    : [...defaultReasonOptions];
                normalized.form.hear_about_options = Array.isArray(normalized.form.hear_about_options) && normalized.form.hear_about_options.length
                    ? normalized.form.hear_about_options
                    : [...defaultHearAboutOptions];
                normalized.service_provider.list = Array.isArray(normalized.service_provider.list) && normalized.service_provider.list.length
                    ? normalized.service_provider.list
                    : [...defaultServiceProviderList];
                normalized.bottom_notices = Array.isArray(contactData.bottom_notices) && contactData.bottom_notices.length
                    ? contactData.bottom_notices
                    : defaultBottomNotices.map(notice => ({ ...notice }));
                normalized.bottom_text = contactData.bottom_text || 'Weâ€™re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, donâ€™t hesitate to reach out.';
                normalized.form_action = contactData.form_action || 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit';

                return normalized;
            },

            getPagePayload(pageId) {
                let source = this.pageData[pageId];
                if (window.Alpine && typeof window.Alpine.raw === 'function') {
                    source = window.Alpine.raw(source);
                }

                if (pageId === 'home') {
                    return this.normalizeHomeData(JSON.parse(JSON.stringify(source || {})));
                }

                if (pageId === 'how_we_help_you') {
                    return this.normalizeHowWeHelpYouData(JSON.parse(JSON.stringify(source || {})));
                }

                if (pageId === 'footer') {
                    return this.normalizeFooterData(JSON.parse(JSON.stringify(source || {})));
                }

                if (pageId === 'contact_us') {
                    return this.normalizeContactUsData(JSON.parse(JSON.stringify(source || {})));
                }

                return JSON.parse(JSON.stringify(source || {}));
            },

            getDefaultHomeSections() {
                return [
                    { id: 'hero', type: 'hero', label: 'Hero Banner' },
                    { id: 'pillars', type: 'pillars', label: 'The Three Pillars' },
                    { id: 'tax-systems', type: 'tax_systems', label: 'Tax Systems' },
                    { id: 'peace-of-mind', type: 'peace_of_mind', label: 'Peace Of Mind' },
                    { id: 'support-features', type: 'support_features', label: 'Support Features' },
                    { id: 'history', type: 'history', label: 'History' },
                    { id: 'testimonials', type: 'testimonials', label: 'Testimonials' },
                    { id: 'packages-intro', type: 'packages_intro', label: 'Packages Intro' },
                    { id: 'bottom-cta', type: 'bottom_cta', label: 'Bottom CTA' }
                ];
            },

            normalizeHomeSections(sections) {
                const defaults = this.getDefaultHomeSections();
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

            normalizeHomeData(homeData = {}) {
                return {
                    ...this.pageData.home,
                    ...homeData,
                    sections: this.normalizeHomeSections(homeData.sections ?? this.pageData.home.sections)
                };
            },

            hasHomeSection(type) {
                return (this.pageData.home.sections || []).some(section => section.type === type);
            },

            getAvailableHomeSections() {
                const existingTypes = new Set((this.pageData.home.sections || []).map(section => section.type));
                return this.getDefaultHomeSections().filter(section => !existingTypes.has(section.type));
            },

            addHomeSection(type) {
                const defaults = this.getDefaultHomeSections();
                const existingTypes = new Set((this.pageData.home.sections || []).map(section => section.type));
                if (existingTypes.has(type)) return;

                const section = defaults.find(item => item.type === type);
                if (!section) return;

                if (!Array.isArray(this.pageData.home.sections)) {
                    this.pageData.home.sections = [];
                }

                this.pageData.home.sections.push({ ...section });
                this.selectedHomeSectionToAdd = '';
            },

            moveHomeSection(index, direction) {
                const nextIndex = index + direction;
                if (!Array.isArray(this.pageData.home.sections)) return;
                if (nextIndex < 0 || nextIndex >= this.pageData.home.sections.length) return;

                const [section] = this.pageData.home.sections.splice(index, 1);
                this.pageData.home.sections.splice(nextIndex, 0, section);
            },

            removeHomeSection(type) {
                if (!Array.isArray(this.pageData.home.sections)) return;
                this.pageData.home.sections = this.pageData.home.sections.filter(section => section.type !== type);
            },

            getDefaultHowWeHelpYouSections() {
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

            normalizeHowWeHelpYouSections(sections) {
                const defaults = this.getDefaultHowWeHelpYouSections();
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

            normalizeHowWeHelpYouData(pageData = {}) {
                const base = this.pageData.how_we_help_you;
                const heroSource = { ...(base.hero || {}), ...(pageData.hero || {}) };
                const problemsSource = { ...(base.problems || {}), ...(pageData.problems || {}) };
                const heroButtons = Array.isArray(heroSource.buttons) && heroSource.buttons.length
                    ? heroSource.buttons
                    : [
                        { text: heroSource.btn1_text || '', link: heroSource.btn1_link || '', style: 'primary' },
                        { text: heroSource.btn2_text || '', link: heroSource.btn2_link || '', style: 'secondary' }
                    ].filter(button => button.text || button.link);
                const problemCards = Array.isArray(problemsSource.cards) && problemsSource.cards.length
                    ? problemsSource.cards
                    : [problemsSource.block1, problemsSource.block2].filter(Boolean);

                return {
                    ...base,
                    ...pageData,
                    hero: {
                        ...(base.hero || {}),
                        ...(pageData.hero || {}),
                        buttons: heroButtons.map((button, index) => ({
                            text: button?.text || `Button ${index + 1}`,
                            link: button?.link || '#',
                            style: button?.style === 'primary' ? 'primary' : 'secondary'
                        })),
                        btn1_text: heroButtons[0]?.text || '',
                        btn1_link: heroButtons[0]?.link || '',
                        btn2_text: heroButtons[1]?.text || '',
                        btn2_link: heroButtons[1]?.link || ''
                    },
                    problems: {
                        ...(base.problems || {}),
                        ...(pageData.problems || {}),
                        cards: problemCards.map((card, index) => ({
                            image: card?.image || '',
                            title: card?.title || `Problem Card ${index + 1}`,
                            list: Array.isArray(card?.list) ? card.list : []
                        })),
                        block1: problemCards[0] || (base.problems || {}).block1 || { image: '', title: '', list: [] },
                        block2: problemCards[1] || (base.problems || {}).block2 || { image: '', title: '', list: [] }
                    },
                    sections: this.normalizeHowWeHelpYouSections(pageData.sections ?? this.pageData.how_we_help_you.sections)
                };
            },

            hasHowWeHelpYouSection(type) {
                return (this.pageData.how_we_help_you.sections || []).some(section => section.type === type);
            },

            getAvailableHowWeHelpYouSections() {
                const existingTypes = new Set((this.pageData.how_we_help_you.sections || []).map(section => section.type));
                return this.getDefaultHowWeHelpYouSections().filter(section => !existingTypes.has(section.type));
            },

            addHowWeHelpYouSection(type) {
                const section = this.getDefaultHowWeHelpYouSections().find(item => item.type === type);
                if (!section || this.hasHowWeHelpYouSection(type)) return;
                if (!Array.isArray(this.pageData.how_we_help_you.sections)) {
                    this.pageData.how_we_help_you.sections = [];
                }
                this.pageData.how_we_help_you.sections.push({ ...section });
                this.selectedHowWeHelpYouSectionToAdd = '';
            },

            moveHowWeHelpYouSection(index, direction) {
                const nextIndex = index + direction;
                if (!Array.isArray(this.pageData.how_we_help_you.sections)) return;
                if (nextIndex < 0 || nextIndex >= this.pageData.how_we_help_you.sections.length) return;
                const [section] = this.pageData.how_we_help_you.sections.splice(index, 1);
                this.pageData.how_we_help_you.sections.splice(nextIndex, 0, section);
            },

            removeHowWeHelpYouSection(type) {
                if (!Array.isArray(this.pageData.how_we_help_you.sections)) return;
                this.pageData.how_we_help_you.sections = this.pageData.how_we_help_you.sections.filter(section => section.type !== type);
            },

            createFooterItem() {
                return {
                    id: `footer-item-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
                    text: '',
                    url: '',
                    new_tab: false
                };
            },

            createFooterSocialLink() {
                return {
                    id: `footer-social-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
                    label: 'New Social',
                    icon: 'fa-globe',
                    url: ''
                };
            },

            createFooterSection(type = 'links') {
                if (type === 'contact') {
                    return {
                        id: `footer-section-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
                        type: 'contact',
                        title: 'Find Us',
                        phone: '',
                        email: ''
                    };
                }

                return {
                    id: `footer-section-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
                    type: 'links',
                    title: 'New Section',
                    items: [this.createFooterItem()]
                };
            },

            normalizeFooterData(footerData = {}) {
                const defaults = {
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

                const rawSocialLinks = Array.isArray(footerData.social_links)
                    ? footerData.social_links
                    : Object.entries((footerData && footerData.social_links) || {}).map(([key, url]) => ({
                        id: key,
                        label: key,
                        icon: key === 'linkedin' ? 'fa-linkedin-in' : `fa-${key === 'twitter' ? 'twitter' : key}`,
                        url
                    }));

                const merged = {
                    ...defaults,
                    ...footerData,
                    social_links: (rawSocialLinks.length ? rawSocialLinks : defaults.social_links).map((social, index) => ({
                        id: social.id || `footer-social-${index}`,
                        label: social.label || 'Social Link',
                        icon: social.icon || 'fa-globe',
                        url: social.url || ''
                    }))
                };

                const sections = Array.isArray(footerData.sections) && footerData.sections.length
                    ? footerData.sections
                    : defaults.sections;

                merged.sections = sections.map((section, index) => {
                    if (section.type === 'contact') {
                        return {
                            id: section.id || `footer-contact-${index}`,
                            type: 'contact',
                            title: section.title || 'Find Us',
                            phone: section.phone || '',
                            email: section.email || ''
                        };
                    }

                    const items = Array.isArray(section.items) && section.items.length
                        ? section.items.map((item, itemIndex) => ({
                            id: item.id || `footer-item-${index}-${itemIndex}`,
                            text: item.text || '',
                            url: item.url || '',
                            new_tab: !!item.new_tab
                        }))
                        : [this.createFooterItem()];

                    return {
                        id: section.id || `footer-links-${index}`,
                        type: 'links',
                        title: section.title || 'New Section',
                        items
                    };
                });

                return merged;
            },

            addFooterSection(type = 'links') {
                if (!Array.isArray(this.pageData.footer.sections)) {
                    this.pageData.footer.sections = [];
                }
                this.pageData.footer.sections.push(this.createFooterSection(type));
            },

            addFooterItem(section) {
                if (!Array.isArray(section.items)) {
                    section.items = [];
                }
                section.items.push(this.createFooterItem());
            },

            addFooterSocialLink() {
                if (!Array.isArray(this.pageData.footer.social_links)) {
                    this.pageData.footer.social_links = [];
                }
                this.pageData.footer.social_links.push(this.createFooterSocialLink());
            },

            updateFooterSectionType(section) {
                if (section.type === 'contact') {
                    section.title = section.title || 'Find Us';
                    section.phone = section.phone || '';
                    section.email = section.email || '';
                    delete section.items;
                    return;
                }

                section.title = section.title || 'New Section';
                if (!Array.isArray(section.items) || !section.items.length) {
                    section.items = [this.createFooterItem()];
                }
            },

            setContactPathValue(target, path, value) {
                const parts = path.split('.');
                let current = target;
                for (let i = 0; i < parts.length - 1; i++) {
                    const part = parts[i];
                    if (!current[part] || typeof current[part] !== 'object' || Array.isArray(current[part])) {
                        current[part] = {};
                    }
                    current = current[part];
                }
                current[parts[parts.length - 1]] = value;
            },

            syncContactUsEditorFromDom() {
                const editor = this.$refs.contactEditor;
                if (!editor) return;

                const nextState = this.getPagePayload('contact_us');
                const fields = Array.from(editor.querySelectorAll('[data-sync-path]'));
                const groupedArrays = {};

                fields.forEach((field) => {
                    const path = field.getAttribute('data-sync-path');
                    const value = field.value;

                    if (path.includes('[]')) {
                        if (!groupedArrays[path]) groupedArrays[path] = [];
                        groupedArrays[path].push(value);
                        return;
                    }

                    this.setContactPathValue(nextState, path, value);
                });

                Object.entries(groupedArrays).forEach(([path, values]) => {
                    if (path === 'bottom_notices[].icon' || path === 'bottom_notices[].text') return;
                    this.setContactPathValue(nextState, path.replace('[]', ''), values);
                });

                const bottomNoticeIcons = groupedArrays['bottom_notices[].icon'] || [];
                const bottomNoticeTexts = groupedArrays['bottom_notices[].text'] || [];
                if (bottomNoticeIcons.length || bottomNoticeTexts.length) {
                    nextState.bottom_notices = bottomNoticeIcons.map((icon, index) => ({
                        icon,
                        text: bottomNoticeTexts[index] || ''
                    }));
                }

                this.pageData.contact_us = this.normalizeContactUsData(nextState);
            },

            async upsertContactUsContent(payload, includeLive = false) {
                const body = {
                    page_id: 'contact_us',
                    draft_content: payload,
                    updated_at: new Date().toISOString()
                };

                if (includeLive) {
                    body.live_content = payload;
                }

                const response = await fetch(`${supabaseUrl}/rest/v1/site_content?on_conflict=page_id`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'apikey': supabaseKey,
                        'Authorization': `Bearer ${supabaseKey}`,
                        'Prefer': 'resolution=merge-duplicates,return=representation'
                    },
                    body: JSON.stringify(body)
                });

                if (!response.ok) {
                    throw new Error(await response.text());
                }

                return response.json();
            },

            async fetchContactUsContent() {
                const response = await fetch(`${supabaseUrl}/rest/v1/site_content?select=page_id,draft_content,live_content&page_id=eq.contact_us`, {
                    method: 'GET',
                    headers: {
                        'apikey': supabaseKey,
                        'Authorization': `Bearer ${supabaseKey}`
                    }
                });

                if (!response.ok) {
                    throw new Error(await response.text());
                }

                const rows = await response.json();
                return rows && rows.length ? rows[0] : null;
            },
            
            async init() {
                try {
                    this.pageData.home = this.normalizeHomeData(this.pageData.home);
                    this.pageData.how_we_help_you = this.normalizeHowWeHelpYouData(this.pageData.how_we_help_you);
                    this.pageData.footer = this.normalizeFooterData(this.pageData.footer);
                    this.pageData.contact_us = this.normalizeContactUsData(this.pageData.contact_us);

                    // Fetch all page records
                    let { data, error } = await supabase.from('site_content').select('*');
                    if (data && data.length > 0) {
                        data.forEach(record => {
                            if (record.page_id && record.draft_content) {
                                // Provide backwards compatibility for existing default records
                                if (this.pageData[record.page_id]) {
                                    if (record.page_id === 'home') {
                                        this.pageData.home = this.normalizeHomeData({
                                            ...this.pageData.home,
                                            ...record.draft_content
                                        });
                                    } else if (record.page_id === 'how_we_help_you') {
                                        this.pageData.how_we_help_you = this.normalizeHowWeHelpYouData({
                                            ...this.pageData.how_we_help_you,
                                            ...record.draft_content
                                        });
                                    } else if (record.page_id === 'footer') {
                                        this.pageData.footer = this.normalizeFooterData({
                                            ...this.pageData.footer,
                                            ...record.draft_content,
                                            sections: Array.isArray(record.draft_content.sections) ? record.draft_content.sections : this.pageData.footer.sections,
                                            social_links: Array.isArray((record.draft_content || {}).social_links)
                                                ? record.draft_content.social_links
                                                : ((record.draft_content || {}).social_links || this.pageData.footer.social_links)
                                        });
                                    } else if (record.page_id === 'contact_us') {
                                        this.pageData.contact_us = this.normalizeContactUsData({
                                            ...this.pageData.contact_us,
                                            ...record.draft_content
                                        });
                                    } else {
                                        // Deep merge objects to prevent losing nested properties
                                        Object.keys(record.draft_content).forEach(key => {
                                            if (typeof record.draft_content[key] === 'object' && !Array.isArray(record.draft_content[key]) && this.pageData[record.page_id][key]) {
                                                this.pageData[record.page_id][key] = { ...this.pageData[record.page_id][key], ...record.draft_content[key] };
                                            } else {
                                                this.pageData[record.page_id][key] = record.draft_content[key];
                                            }
                                        });
                                    }
                                }
                            }
                        });
                    }
                } catch (e) {
                    console.error("Failed to load initial CMS data", e);
                } finally {
                    this.isLoading = false;
                }
            },
            
            async saveDraft(showToast = true) {
                this.isSaving = true;
                try {
                    if (this.activePage === 'contact_us') {
                        this.syncContactUsEditorFromDom();
                        const payload = this.getPagePayload('contact_us');
                        this.pageData.contact_us = this.normalizeContactUsData(payload);
                        await this.upsertContactUsContent(payload, false);
                        const saved = await this.fetchContactUsContent();
                        const savedHeadline = saved?.draft_content?.hero?.headline || '(missing)';
                        if (savedHeadline !== payload.hero.headline) {
                            throw new Error(`Draft verify failed. Sent "${payload.hero.headline}" but stored "${savedHeadline}".`);
                        }
                    } else {
                        const payload = this.getPagePayload(this.activePage);
                        const { error } = await supabase.from('site_content')
                            .upsert({ page_id: this.activePage, draft_content: payload, updated_at: new Date().toISOString() }, { onConflict: 'page_id' });
                        if (error) throw error;
                    }
                    if (showToast) alert('Draft saved successfully!');
                } catch (e) {
                    console.error(e);
                    alert(`Error saving draft: ${e.message || e}`);
                } finally {
                    this.isSaving = false;
                }
            },
            
            async publishLive() {
                if(!confirm("Are you sure you want to publish these changes to the live site?")) return;
                this.isSaving = true;
                try {
                    if (this.activePage === 'contact_us') {
                        this.syncContactUsEditorFromDom();
                        const payload = this.getPagePayload('contact_us');
                        this.pageData.contact_us = this.normalizeContactUsData(payload);
                        await this.upsertContactUsContent(payload, true);
                        const saved = await this.fetchContactUsContent();
                        const savedHeadline = saved?.live_content?.hero?.headline || '(missing)';
                        if (savedHeadline !== payload.hero.headline) {
                            throw new Error(`Publish verify failed. Sent "${payload.hero.headline}" but live stored "${savedHeadline}".`);
                        }
                        alert(`Changes pushed to live site successfully!\nVerified live hero headline: ${savedHeadline}`);
                    } else {
                        // Make sure draft is saved first
                        await this.saveDraft(false);
                        const payload = this.getPagePayload(this.activePage);
                        const { error } = await supabase.from('site_content')
                            .upsert({ page_id: this.activePage, draft_content: payload, live_content: payload, updated_at: new Date().toISOString() }, { onConflict: 'page_id' });
                        if (error) throw error;
                        alert('Changes pushed to live site successfully!');
                    }
                } catch (e) {
                    console.error(e);
                    alert(`Error publishing: ${e.message || e}`);
                } finally {
                    this.isSaving = false;
                }
            },
            
            previewDraft() {
                // Ensure draft is saved before previewing
                this.saveDraft(false).then(() => {
                    const url = this.activePage === 'home' || this.activePage === 'footer'
                        ? 'index.html?mode=preview'
                        : `${this.activePage.replaceAll('_', '-')}.html?mode=preview`;
                    window.open(url, '_blank');
                });
            },
            
            async uploadImageTo(event, targetPath) {
                const file = event.target.files[0];
                if (!file) return;
                
                this.isUploadingImage = true;
                try {
                    const fileExt = file.name.split('.').pop();
                    const fileName = Math.random().toString(36).substring(2, 15) + '.' + fileExt;
                    
                    let folder = 'general';
                    if (targetPath.startsWith('pageData.')) {
                        folder = targetPath.split('.')[1];
                    }
                    const filePath = folder + '/' + fileName;

                    let { error: uploadError } = await supabase.storage.from('cms_images').upload(filePath, file);
                    if (uploadError) throw uploadError;
                    
                    const { data } = supabase.storage.from('cms_images').getPublicUrl(filePath);
                    
                    let cleanPath = targetPath.replace(/\[/g, ".").replace(/\]/g, "").replace(/'|"/g, "");
                    const parts = cleanPath.split('.');
                    let obj = this;
                    for (let i = 0; i < parts.length - 1; i++) {
                        if (!obj[parts[i]]) obj[parts[i]] = {};
                        obj = obj[parts[i]];
                    }
                    obj[parts[parts.length - 1]] = data.publicUrl;
                    
                    this.pageData = JSON.parse(JSON.stringify(this.pageData));
                    await this.saveDraft(false);
                } catch (e) {
                    console.error("Image upload failed", e);
                    alert("Failed to upload image. Make sure bucket permissions are set.");
                } finally {
                    this.isUploadingImage = false;
                    event.target.value = '';
                }
            }
        }));
    });

