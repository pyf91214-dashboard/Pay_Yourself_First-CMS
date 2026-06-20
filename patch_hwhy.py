import re

def process_file():
    with open('how-we-help-you.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Scripts block
    head_insertion = """    <script src="https://cdn.pagesense.io/js/payyourselffirst/c2e5673c7d15457d8a0925080101f545.js"></script>

    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

    <!-- Alpine.js for Interactions -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>"""
    content = content.replace("""    <script src="https://cdn.pagesense.io/js/payyourselffirst/c2e5673c7d15457d8a0925080101f545.js"></script>""", head_insertion)

    # 2. Add x-data to body
    content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>')

    # 3. Add Supabase logic at end
    bottom_script = """        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    </script>

    <!-- Supabase Dynamic Data Script -->
    <script>
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        
        document.addEventListener('alpine:init', () => {
            const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
            
            Alpine.data('siteData', () => ({
                pageData: {
                    hero: {
                        headline: 'We Help You Gain Greater Control Of\\n<span class="text-[#bbf7d0]">Your Financial Life</span>',
                        desc: 'Most people work hard, pay their bills, and still feel behind.\\nPay Yourself First gives you the tools, guidance, and support to earn more, keep more, and spend less \\u2014 all with a simple, practical system designed for everyday Americans.',
                        btn1_text: 'See How We Help You Earn More',
                        btn1_link: 'affiliate-plan.html',
                        btn2_text: 'See How We Help You Save More',
                        btn2_link: 'packages.html'
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
                        desc: 'You don\\'t have to know exactly what you want yet. PYF offers two simple paths, depending on your goals.',
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
                        desc: 'You don\\'t have to pick a single path. You are free to choose a combination of any of the three or all three. Everything PYF offers is built to give everyday people an advantage normally reserved for the wealthy and very high-income earners.',
                        list: ['Professional and expert tax and legal support', 'Proven savings programs', 'Entrepreneurial tools and education', 'A clear path toward financial stability', 'A system designed by someone who has guided thousands toward success'],
                        subtitle: 'Most Importantly',
                        subdesc: 'You are not doing this alone.',
                        subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward — whether you want to earn more, keep more, or spend less.'
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
                
                async init() {
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    
                    try {
                        let { data, error } = await supabase.from('site_content').select('*').eq('page_id', 'how_we_help_you').single();
                        if (data) {
                            const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                            // Clean up empty arrays to avoid wiping defaults
                            if (loadedContent) {
                                if (loadedContent.why_exists && !loadedContent.why_exists.list?.length) delete loadedContent.why_exists.list;
                                if (loadedContent.designed_for && !loadedContent.designed_for.list?.length) delete loadedContent.designed_for.list;
                                if (loadedContent.problems?.block1 && !loadedContent.problems.block1.list?.length) delete loadedContent.problems.block1.list;
                                if (loadedContent.why_works && !loadedContent.why_works.list?.length) delete loadedContent.why_works.list;
                            }
                            this.pageData = { ...this.pageData, ...loadedContent };
                        }
                    } catch (e) {
                        console.error("Failed to load CMS data", e);
                    }
                }
            }));
        });
    </script>
</body>
</html>"""
    content = content.replace("""        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    </script>
</body>
</html>""", bottom_script)

    # Hero bindings
    content = re.sub(
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md max-w-5xl">.*?</h1>',
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md max-w-5xl" x-html="pageData.hero.headline"></h1>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<p class="text-base md:text-xl text-gray-100 mb-10 max-w-4xl font-normal leading-relaxed">.*?</p>',
        r'<p class="text-base md:text-xl text-gray-100 mb-10 max-w-4xl font-normal leading-relaxed" x-html="pageData.hero.desc"></p>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<a href="affiliate-plan.html"([^>]*)>\s*See How We Help You Earn More\s*</a>',
        r'<a :href="pageData.hero.btn1_link" \1 x-text="pageData.hero.btn1_text"></a>',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a href="packages.html"([^>]*)>\s*See How We Help You Save More\s*</a>',
        r'<a :href="pageData.hero.btn2_link" \1 x-text="pageData.hero.btn2_text"></a>',
        content, flags=re.IGNORECASE
    )

    # Why PYF Exists bindings
    content = re.sub(
        r'<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*Why <span class="text-brand-primary">PYF Exists</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.why_exists.headline"></h2>',
        content
    )
    content = re.sub(
        r'<p class="text-gray-700 text-base md:text-lg mb-8 leading-relaxed font-medium">.*?<\/p>',
        r'<p class="text-gray-700 text-base md:text-lg mb-8 leading-relaxed font-medium" x-text="pageData.why_exists.desc1"></p>',
        content, count=1, flags=re.DOTALL
    )
    # The list for Why PYF Exists
    list_str = """                        <ul class="space-y-6 mb-10">
                            <template x-for="(item, index) in pageData.why_exists.list" :key="index">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#068277] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-600 font-bold" x-text="item"></span>
                                </li>
                            </template>
                        </ul>"""
    content = re.sub(r'<ul class="space-y-6 mb-10">.*?</ul>', list_str, content, count=1, flags=re.DOTALL)
    content = re.sub(
        r'<p class="text-gray-700 text-base md:text-lg leading-relaxed font-medium">\s*PYF was built to give individuals.*?<\/p>',
        r'<p class="text-gray-700 text-base md:text-lg leading-relaxed font-medium" x-text="pageData.why_exists.desc2"></p>',
        content, count=1, flags=re.DOTALL
    )

    # The Problems Most People Face
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*The <span class="text-brand-primary">Problems</span> Most People Face\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.problems.headline"></h2>',
        content
    )
    # Block 1
    content = re.sub(
        r'<h3 class="text-xl md:text-2xl font-bold text-gray-900 mb-6 leading-tight">\s*Everyday people struggle with challenges that compound over time.\s*</h3>',
        r'<h3 class="text-xl md:text-2xl font-bold text-gray-900 mb-6 leading-tight" x-text="pageData.problems.block1.title"></h3>',
        content
    )
    list1_str = """                                <ul class="space-y-4">
                                    <template x-for="(item, index) in pageData.problems.block1.list" :key="index">
                                        <li class="flex items-start">
                                            <i class="fas fa-exclamation-triangle text-[#068277] mt-1 mr-3 flex-shrink-0"></i>
                                            <span class="text-gray-700 font-medium text-sm md:text-base" x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>"""
    content = re.sub(r'<ul class="space-y-4">.*?</ul>', list1_str, content, count=1, flags=re.DOTALL)
    
    # Block 2
    content = re.sub(
        r'<h3 class="text-xl md:text-2xl font-bold text-gray-900 mb-6 leading-tight">\s*Whether someone earns a salary, runs a small business, works a gig job, or lives on commission, these challenges lead to the same outcomes.\s*</h3>',
        r'<h3 class="text-xl md:text-2xl font-bold text-gray-900 mb-6 leading-tight" x-text="pageData.problems.block2.title"></h3>',
        content
    )
    list2_str = """                                <ul class="space-y-4">
                                    <template x-for="(item, index) in pageData.problems.block2.list" :key="index">
                                        <li class="flex items-start">
                                            <i class="fas fa-exclamation-triangle text-[#068277] mt-1 mr-3 flex-shrink-0"></i>
                                            <span class="text-gray-700 font-medium text-sm md:text-base" x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>"""
    content = re.sub(r'<ul class="space-y-4">.*?</ul>', list2_str, content, count=1, flags=re.DOTALL)
    
    content = re.sub(
        r'<p class="text-lg md:text-xl font-bold text-brand-dark">\s*PYF exists to help you overcome these problems in a simple way that anyone can do.\s*</p>',
        r'<p class="text-lg md:text-xl font-bold text-brand-dark" x-text="pageData.problems.footer"></p>',
        content
    )

    # Mastering Three Things
    content = re.sub(
        r'<h1 class="text-3xl md:text-5xl font-extrabold uppercase leading-relaxed">\s*Financial.*?</h1>',
        r'<h1 class="text-3xl md:text-5xl font-extrabold uppercase leading-relaxed" x-html="pageData.mastering.headline"></h1>',
        content, flags=re.DOTALL
    )
    content = re.sub(r'<h2 class="text-2xl font-bold text-green-900">1\. Earn More</h2>', r'<h2 class="text-2xl font-bold text-green-900" x-text="pageData.mastering.card1.title"></h2>', content)
    content = re.sub(r'<p class="text-green-950 text-lg leading-relaxed font-medium">\s*PYF offers simple, accessible ways.*?<\/p>', r'<p class="text-green-950 text-lg leading-relaxed font-medium" x-text="pageData.mastering.card1.desc"></p>', content, flags=re.DOTALL)
    
    card1_list = """                        <ul class="mt-6 space-y-3">
                            <template x-for="(item, index) in pageData.mastering.card1.list" :key="index">
                                <li class="flex items-center text-green-900 font-semibold bg-white/40 p-3 rounded-lg">
                                    <i data-lucide="check-circle" class="w-5 h-5 mr-3 text-green-700"></i> <span x-text="item"></span>
                                </li>
                            </template>
                        </ul>"""
    content = re.sub(r'<ul class="mt-6 space-y-3">.*?</ul>', card1_list, content, count=1, flags=re.DOTALL)

    content = re.sub(r'<h2 class="text-2xl font-bold text-green-900">2\. Keep More</h2>', r'<h2 class="text-2xl font-bold text-green-900" x-text="pageData.mastering.card2.title"></h2>', content)
    content = re.sub(r'<p class="text-green-950 mb-4 text-sm font-medium">\s*Most W-2 earners unknowingly overpay their taxes.*?</p>', r'<p class="text-green-950 mb-4 text-sm font-medium" x-text="pageData.mastering.card2.desc"></p>', content, flags=re.DOTALL)

    card2_list_content = """                        <ul class="space-y-2 mb-4">
                            <template x-for="(item, index) in pageData.mastering.card2.list" :key="index">
                                <li class="flex items-start text-green-900 text-sm">
                                    <i data-lucide="check-circle-2" class="w-4 h-4 mr-2 mt-0.5 text-green-700 shrink-0"></i> 
                                    <span x-text="item"></span>
                                </li>
                            </template>
                        </ul>"""
    content = re.sub(r'<ul class="space-y-2 mb-4">.*?</ul>', card2_list_content, content, count=1, flags=re.DOTALL)
    content = re.sub(
        r'<p class="text-xs text-green-900 font-bold italic">\s*"This single category often creates the biggest transformation for everyday Americans."\s*</p>',
        r'<p class="text-xs text-green-900 font-bold italic" x-text="pageData.mastering.card2.quote"></p>',
        content, flags=re.DOTALL
    )

    content = re.sub(r'<h2 class="text-2xl font-bold text-green-900">3\. Spend Less</h2>', r'<h2 class="text-2xl font-bold text-green-900" x-text="pageData.mastering.card3.title"></h2>', content)
    content = re.sub(r'<p class="text-green-950 mb-4 text-sm font-medium">\s*Access to nationwide savings programs that reduce everyday expenses, including:\s*</p>', r'<p class="text-green-950 mb-4 text-sm font-medium" x-text="pageData.mastering.card3.desc"></p>', content, flags=re.DOTALL)
    
    card3_grid = """                        <div class="grid grid-cols-2 gap-3 mb-6">
                            <template x-for="(item, index) in pageData.mastering.card3.list" :key="index">
                                <div class="bg-white/50 rounded-lg p-2 text-center text-sm font-semibold text-green-900 shadow-sm" x-text="item"></div>
                            </template>
                        </div>"""
    content = re.sub(r'<div class="grid grid-cols-2 gap-3 mb-6">.*?</div>', card3_grid, content, count=1, flags=re.DOTALL)
    content = re.sub(
        r'<p class="text-green-900 font-bold text-center text-sm border-t border-green-800/10 pt-4">\s*Every dollar saved is a dollar that strengthens long-term stability.\s*</p>',
        r'<p class="text-green-900 font-bold text-center text-sm border-t border-green-800/10 pt-4" x-text="pageData.mastering.card3.footer"></p>',
        content, flags=re.DOTALL
    )

    # Designed For
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*PYF Is <span class="text-brand-primary">Designed For</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.designed_for.headline"></h2>',
        content
    )
    content = re.sub(
        r'<p class="text-gray-700 text-base md:text-lg mb-8 leading-relaxed font-medium">\s*PYF serves everyday people from all backgrounds who want practical, real-world financial improvement.\s*</p>',
        r'<p class="text-gray-700 text-base md:text-lg mb-8 leading-relaxed font-medium" x-text="pageData.designed_for.desc"></p>',
        content
    )
    list_designed = """                        <ul class="space-y-4 mb-10">
                            <template x-for="(item, index) in pageData.designed_for.list" :key="index">
                                <li class="flex items-start">
                                    <div class="flex-shrink-0 w-6 h-6 rounded-full bg-brand-primary flex items-center justify-center text-white text-xs mt-1 mr-4 shadow-sm">
                                        <i class="fas fa-dollar-sign"></i>
                                    </div>
                                    <span class="text-gray-700 font-medium" x-text="item"></span>
                                </li>
                            </template>
                        </ul>"""
    content = re.sub(r'<ul class="space-y-4 mb-10">.*?</ul>', list_designed, content, count=1, flags=re.DOTALL)
    content = re.sub(
        r'<p class="text-gray-700 text-base md:text-lg leading-relaxed font-medium border-l-4 border-brand-primary pl-6">\s*If you want to build income, reduce expenses, or improve your financial stability, PYF is designed with you in mind.\s*</p>',
        r'<p class="text-gray-700 text-base md:text-lg leading-relaxed font-medium border-l-4 border-brand-primary pl-6" x-text="pageData.designed_for.footer"></p>',
        content
    )

    # Three Ways
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6 leading-tight">\s*Three Ways PYF <span class="text-brand-primary">Helps You Move Forward</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6 leading-tight" x-html="pageData.three_ways.headline"></h2>',
        content
    )
    content = re.sub(
        r'<p class="text-gray-600 text-sm md:text-base">\s*You don\'t have to know exactly what you want yet. PYF offers two simple paths, depending on your goals.\s*</p>',
        r'<p class="text-gray-600 text-sm md:text-base" x-text="pageData.three_ways.desc"></p>',
        content
    )
    content = re.sub(r'<h3 class="text-2xl font-bold text-gray-900 mb-2">Earn Referral Fees</h3>', r'<h3 class="text-2xl font-bold text-gray-900 mb-2" x-text="pageData.three_ways.card1.title"></h3>', content)
    content = re.sub(r'<p class="text-gray-700 text-sm mt-1">People who want to create additional income and/or having a home-based business</p>', r'<p class="text-gray-700 text-sm mt-1" x-text="pageData.three_ways.card1.best_for"></p>', content)
    content = re.sub(r'<ul class="space-y-3 mb-8">\s*<li class="flex items-center">\s*<i class="fas fa-check-circle text-brand-primary mr-3"></i>\s*<span class="text-gray-600 text-sm">Recurring Income Opportunity</span>\s*</li>\s*<li class="flex items-center">\s*<i class="fas fa-check-circle text-brand-primary mr-3"></i>\s*<span class="text-gray-600 text-sm">Marketing Resources & Tools</span>\s*</li>\s*<li class="flex items-center">\s*<i class="fas fa-check-circle text-brand-primary mr-3"></i>\s*<span class="text-gray-600 text-sm">Affiliate Training & Support</span>\s*</li>\s*</ul>', r"""                                <ul class="space-y-3 mb-8">
                                    <template x-for="(item, index) in pageData.three_ways.card1.list" :key="index">
                                        <li class="flex items-center">
                                            <i class="fas fa-check-circle text-brand-primary mr-3"></i>
                                            <span class="text-gray-600 text-sm" x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>""", content)
    content = re.sub(r'<p class="text-gray-600 text-xs italic mb-8 border-l-2 border-brand-primary pl-4">\s*You have the chance to add a source of income as a side hustle or legitimate business\s*</p>', r'<p class="text-gray-600 text-xs italic mb-8 border-l-2 border-brand-primary pl-4" x-text="pageData.three_ways.card1.footer"></p>', content)
    content = re.sub(r'<a href="https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm"([^>]*)>\s*Become An Affiliate\s*</a>', r'<a :href="pageData.three_ways.card1.btn_link" \1 x-text="pageData.three_ways.card1.btn_text"></a>', content, flags=re.IGNORECASE)

    content = re.sub(r'<h3 class="text-2xl font-bold text-gray-900 mb-2">Save Money on Everyday Living</h3>', r'<h3 class="text-2xl font-bold text-gray-900 mb-2" x-text="pageData.three_ways.card2.title"></h3>', content)
    content = re.sub(r'<p class="text-gray-700 text-sm mt-1">People who simply want to reduce expenses and make life more affordable.</p>', r'<p class="text-gray-700 text-sm mt-1" x-text="pageData.three_ways.card2.best_for"></p>', content)
    content = re.sub(r'<ul class="space-y-3 mb-8">\s*<li class="flex items-center">\s*<i class="fas fa-check-circle text-brand-primary mr-3"></i>\s*<span class="text-gray-600 text-sm">Shopping and travel savings</span>\s*</li>.*?</ul>', r"""                                <ul class="space-y-3 mb-8">
                                    <template x-for="(item, index) in pageData.three_ways.card2.list" :key="index">
                                        <li class="flex items-center">
                                            <i class="fas fa-check-circle text-brand-primary mr-3"></i>
                                            <span class="text-gray-600 text-sm" x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>""", content, flags=re.DOTALL)
    content = re.sub(r'<p class="text-gray-600 text-xs italic mb-8 border-l-2 border-brand-primary pl-4">\s*If your primary goal is to lower your monthly costs, this path gives you immediate, practical value.\s*</p>', r'<p class="text-gray-600 text-xs italic mb-8 border-l-2 border-brand-primary pl-4" x-text="pageData.three_ways.card2.footer"></p>', content)
    content = re.sub(r'<a href="packages.html"([^>]*)>\s*Choose A Discount Package\s*</a>', r'<a :href="pageData.three_ways.card2.btn_link" \1 x-text="pageData.three_ways.card2.btn_text"></a>', content, flags=re.IGNORECASE)

    content = re.sub(r'<h3 class="text-2xl font-bold text-gray-900 mb-2">Support For Your Home Based/Small Business</h3>', r'<h3 class="text-2xl font-bold text-gray-900 mb-2" x-text="pageData.three_ways.card3.title"></h3>', content)
    content = re.sub(r'<p class="text-gray-700 text-sm mt-1">People who want support services for their Home Based/Small Business</p>', r'<p class="text-gray-700 text-sm mt-1" x-text="pageData.three_ways.card3.best_for"></p>', content)
    content = re.sub(r'<ul class="space-y-3 mb-8">\s*<li class="flex items-center">\s*<i class="fas fa-check-circle text-brand-primary mr-3"></i>\s*<span class="text-gray-600 text-sm">Expert Tax & Accounting Services</span>\s*</li>.*?</ul>', r"""                                <ul class="space-y-3 mb-8">
                                    <template x-for="(item, index) in pageData.three_ways.card3.list" :key="index">
                                        <li class="flex items-center">
                                            <i class="fas fa-check-circle text-brand-primary mr-3"></i>
                                            <span class="text-gray-600 text-sm" x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>""", content, flags=re.DOTALL)
    content = re.sub(r'<p class="text-gray-600 text-xs italic mb-4 border-l-2 border-brand-primary pl-4">\s*If your primary goal is to lower your taxes to the legal minimum, increase your revenue, and improve your work/life balance, this path will give you the most value.\s*</p>', r'<p class="text-gray-600 text-xs italic mb-4 border-l-2 border-brand-primary pl-4" x-text="pageData.three_ways.card3.footer"></p>', content)
    content = re.sub(r'<a href="business-support-package.html"([^>]*)>\s*Start Your Support Services\s*</a>', r'<a :href="pageData.three_ways.card3.btn_link" \1 x-text="pageData.three_ways.card3.btn_text"></a>', content, flags=re.IGNORECASE)

    # Why PYF Works
    content = re.sub(
        r'<h2 class="text-3xl md:text-5xl font-extrabold uppercase mb-6">\s*Why PYF Works\s*</h2>',
        r'<h2 class="text-3xl md:text-5xl font-extrabold uppercase mb-6" x-text="pageData.why_works.headline"></h2>',
        content
    )
    content = re.sub(
        r'<p class="text-lg md:text-xl font-medium leading-relaxed opacity-95">\s*You don\'t have to pick a single path.*?<\/p>',
        r'<p class="text-lg md:text-xl font-medium leading-relaxed opacity-95" x-text="pageData.why_works.desc"></p>',
        content, flags=re.DOTALL
    )
    lists_works = """                        <ul class="space-y-4">
                            <template x-for="(item, index) in pageData.why_works.list" :key="index">
                                <li class="flex items-start">
                                    <i class="fas fa-check-square text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-bold" x-text="item"></span>
                                </li>
                            </template>
                        </ul>"""
    content = re.sub(r'<ul class="space-y-4">\s*<li class="flex items-start">\s*<i class="fas fa-check-square text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>\s*<span class="text-gray-700 font-bold">Professional and expert tax and legal support</span>\s*</li>.*?</ul>', lists_works, content, flags=re.DOTALL)
    content = re.sub(r'<h3 class="text-2xl font-bold text-brand-primary mb-6">Most Importantly</h3>', r'<h3 class="text-2xl font-bold text-brand-primary mb-6" x-text="pageData.why_works.subtitle"></h3>', content)
    content = re.sub(r'<p class="text-gray-900 font-bold text-lg mb-6">\s*You are not doing this alone.\s*</p>', r'<p class="text-gray-900 font-bold text-lg mb-6" x-text="pageData.why_works.subdesc"></p>', content)
    content = re.sub(r'<p class="text-gray-700 font-medium text-lg leading-relaxed">\s*PYF is built to give people real support.*?<\/p>', r'<p class="text-gray-700 font-medium text-lg leading-relaxed" x-text="pageData.why_works.subdesc2"></p>', content, flags=re.DOTALL)

    # Start Path
    content = re.sub(
        r'<h2 class="text-2xl md:text-4xl font-extrabold text-brand-dark uppercase mb-8">\s*Start With The Path That Matches Your Goals\s*</h2>',
        r'<h2 class="text-2xl md:text-4xl font-extrabold text-brand-dark uppercase mb-8" x-text="pageData.start_path.headline"></h2>',
        content
    )
    content = re.sub(
        r'<p class="text-brand-dark font-bold text-lg md:text-xl mb-12">\s*You can always change your path as you change your aims\. PYF will support you every step of the way\s*</p>',
        r'<p class="text-brand-dark font-bold text-lg md:text-xl mb-12" x-text="pageData.start_path.desc"></p>',
        content
    )
    content = re.sub(
        r'<a href="https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm\s*" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-\[#389400\] to-\[#75C400\] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide">\s*Start The Earn Path\s*</a>',
        r'<a :href="pageData.start_path.btn1_link" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide" x-text="pageData.start_path.btn1_text"></a>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<a href="packages.html" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-\[#bbf7d0\] to-\[#86efac\] text-brand-dark font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:brightness-105 transition uppercase text-sm tracking-wide">\s*Start The Savings Path\s*</a>',
        r'<a :href="pageData.start_path.btn2_link" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#bbf7d0] to-[#86efac] text-brand-dark font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:brightness-105 transition uppercase text-sm tracking-wide" x-text="pageData.start_path.btn2_text"></a>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<a href="business-support-package.html" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-\[#389400\] to-\[#75C400\] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide">\s*Start The Support Path\s*</a>',
        r'<a :href="pageData.start_path.btn3_link" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide" x-text="pageData.start_path.btn3_text"></a>',
        content, flags=re.DOTALL
    )

    with open('how-we-help-you.html', 'w', encoding='utf-8') as f:
        f.write(content)

process_file()
