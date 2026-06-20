
    const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    
    document.addEventListener('alpine:init', () => {
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
        
        Alpine.data('cmsManager', () => ({
            activePage: 'home',
            cmsSidebarOpen: false,
            isLoading: true,
            isSaving: false,
            isUploadingImage: false,
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
                    ]
                },
                how_we_help_you: {
                    hero: {
                        headline: 'We Help You Gain Greater Control Of\n<span class="text-[#bbf7d0]">Your Financial Life</span>',
                        desc: 'Most people work hard, pay their bills, and still feel behind. <br class="hidden md:block">\nPay Yourself First gives you the tools, guidance, and support to earn more, keep more, and spend less â€” all with a simple, practical system designed for everyday Americans.',
                        btn1_text: 'See How We Help You Earn More',
                        btn1_link: 'affiliate-plan.html',
                        btn2_text: 'See How We Help You Save More',
                        btn2_link: 'packages.html',
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
                    }
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
                        desc: 'Whether you have questions about our services, need support, or want to\nexplore business partnerships, we\'re here to help.',
                        image: 'Contact-us/Contact Us_Hero.jpg'
                    },
                    info: {
                        email: 'service@payyourselffirst.com',
                        phone: '1-800-123-4567',
                        address: 'Pay Yourself First\n107 S. West Street, Suite 557\nAlexandria, VA 22314\nCorrespondence Only'
                    },
                        portals: {
                            customer: 'https://payyourselffirst.benefithub.com/welcome/',
                            affiliate: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login'
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
                            desc3: 'Please contact us using the form above, and we\'ll help coordinate with the appropriate provider network.',
                            image: 'Contact-us/Contact Us_Need help with a service provider.jpg'
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
                            faq_link: 'support.html', faq_text: 'Support / FAQ Page',
                            package_link: 'packages.html', package_text: 'Package Overview',
                            affiliate_link: 'affiliate-page.html', affiliate_text: 'Affiliate Support Section'
                        },
                        form_action: 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit'
        
                },
                business: {
                    hero: {
                        headline: 'Business Support Package',
                        desc: 'Our most comprehensive package for business owners.',
                        image: 'Business/Hero.jpg',
                        btn_text: 'Get Started',
                        btn_link: '#'
                    },
                    features: {
                        headline: 'What is included',
                        items: [
                            { title: 'Tax Support', desc: 'Expert tax guidance.' }
                        ]
                    }
                }
            },
            
            async init() {
                try {
                    // Fetch all page records
                    let { data, error } = await supabase.from('site_content').select('*');
                    if (data && data.length > 0) {
                        data.forEach(record => {
                            if (record.page_id && record.draft_content) {
                                // Provide backwards compatibility for existing default records
                                if (this.pageData[record.page_id]) {
                                    // Prevent empty arrays erasing defaults in Home
                                    if(record.page_id === 'home') {
                                        if (record.draft_content.pillars && record.draft_content.pillars.length === 0) delete record.draft_content.pillars;
                                        if (record.draft_content.support_features && record.draft_content.support_features.length === 0) delete record.draft_content.support_features;
                                        if (record.draft_content.service_packages && record.draft_content.service_packages.length === 0) delete record.draft_content.service_packages;
                                        if (record.draft_content.bottom_cta && record.draft_content.bottom_cta.features && record.draft_content.bottom_cta.features.length === 0) delete record.draft_content.bottom_cta.features;
                                    }
                                    
                                    this.pageData[record.page_id] = { ...this.pageData[record.page_id], ...record.draft_content };
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
                    const { error } = await supabase.from('site_content')
                        .upsert({ page_id: this.activePage, draft_content: this.pageData[this.activePage], updated_at: new Date() }, { onConflict: 'page_id' });
                    if (error) throw error;
                    if (showToast) alert('Draft saved successfully!');
                } catch (e) {
                    console.error(e);
                    alert("Error saving draft!");
                } finally {
                    this.isSaving = false;
                }
            },
            
            async publishLive() {
                if(!confirm("Are you sure you want to publish these changes to the live site?")) return;
                this.isSaving = true;
                try {
                    // Make sure draft is saved first
                    await this.saveDraft(false);
                    const { error } = await supabase.from('site_content')
                        .upsert({ page_id: this.activePage, draft_content: this.pageData[this.activePage], live_content: this.pageData[this.activePage], updated_at: new Date() }, { onConflict: 'page_id' });
                    if (error) throw error;
                    alert('Changes pushed to live site successfully!');
                } catch (e) {
                    console.error(e);
                    alert("Error publishing!");
                } finally {
                    this.isSaving = false;
                }
            },
            
            previewDraft() {
                // Ensure draft is saved before previewing
                this.saveDraft(false).then(() => {
                    const url = this.activePage === 'home' ? 'index.html?mode=preview' : `${this.activePage.replaceAll('_', '-')}.html?mode=preview`;
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
            }
        }));
    });
