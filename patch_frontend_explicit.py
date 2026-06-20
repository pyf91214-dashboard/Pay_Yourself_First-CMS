import os

def string_replace_frontend():
    os.system('git checkout about-us.html')

    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Body script injection
    content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>')
    
    script_block = """
<!-- Supabase and AlpineJS scripts for CMS Dynamic Content -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
<script>
    const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    document.addEventListener('alpine:init', () => {
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
        Alpine.data('siteData', () => ({
            pageData: {
                about_us: {
                    hero: {}, who_we_are: { list: [] }, origin: { list: [] }, mission: {},
                    serving: { stats: [], principles: [] }, system: { cards: [] },
                    who_we_serve: { list: [] }, different: { list: [] }, pledge: { list: [] }, journey: {}
                }
            },
            async init() {
                try {
                    let { data } = await supabase.from('site_content').select('*').eq('page_id', 'about_us').single();
                    if (data) {
                        const loadedContent = new URLSearchParams(window.location.search).get('mode') === 'preview' ? data.draft_content : data.live_content;
                        if(loadedContent) this.pageData.about_us = { ...this.pageData.about_us, ...loadedContent };
                    }
                } catch (e) { console.error("CMS Load Error", e); }
            }
        }));
    });
</script>
</body>"""
    content = content.replace('</body>', script_block)

    # 1. Hero Group
    content = content.replace(
        '<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md">\n                    We\'re Here To Help <span class="text-[#bbf7d0]">Everyday People</span><br>\n                    Take Control Of Their Financial Future\n                </h1>',
        '<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md" x-html="pageData.about_us.hero.headline"></h1>'
    )
    content = content.replace(
        '<p class="text-base md:text-xl text-gray-100 mb-10 font-medium leading-relaxed max-w-3xl whitespace-pre-line">\n                    Pay Yourself First was created to make financial stability accessible to everyone, not just the wealthy or very high-income earners. Our system gives people access to the tools, guidance, and support to earn more, keep more, and spend less through practical, real-world solutions.\n                </p>',
        '<p class="text-base md:text-xl text-gray-100 mb-10 font-medium leading-relaxed max-w-3xl whitespace-pre-line" x-text="pageData.about_us.hero.desc"></p>'
    )
    content = content.replace('src="About-us/About Us_Hero.jpg"', ':src="pageData.about_us.hero.image || \'About-us/About Us_Hero.jpg\'"')

    # 2. Who We Are
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\n                    Who <span class="text-brand-primary">We Are</span>\n                </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.who_we_are.headline"></h2>'
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg mb-6 leading-relaxed">\n                            Pay Yourself First (PYF) is a financial empowerment company built on a simple belief: <span class="font-bold text-brand-primary">You deserve a clear, practical way to improve your finances.</span>\n                        </p>',
        '<p class="text-gray-700 text-lg mb-6 leading-relaxed" x-html="pageData.about_us.who_we_are.desc1"></p>'
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed">\n                            As the cost of living rises and financial pressure grows, too many people feel stuck.\n                        </p>',
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.who_we_are.desc2"></p>'
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg mb-6 leading-relaxed">\n                            PYF was created to solve these problems by giving you access to the tools, education, and professional support they need to gain financial control.\n                        </p>',
        '<p class="text-gray-700 text-lg mb-6 leading-relaxed" x-text="pageData.about_us.who_we_are.desc3"></p>'
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg leading-relaxed">\n                            Our company is built around a system. One designed to help people break negative financial cycles, build financial stability, and move forward with clarity and confidence.\n                        </p>',
        '<p class="text-gray-700 text-lg leading-relaxed" x-text="pageData.about_us.who_we_are.desc4"></p>'
    )
    content = content.replace(
        '''<ul class="space-y-4 mb-10">
                            <li class="flex items-start">
                                <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                <span class="text-gray-700 text-lg leading-relaxed">W-2 workers overpaying taxes without realizing it</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                <span class="text-gray-700 text-lg leading-relaxed">1099 earners facing unstable income</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                <span class="text-gray-700 text-lg leading-relaxed">Families spending more but saving less</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                <span class="text-gray-700 text-lg leading-relaxed">Individuals working hard but falling behind financially.</span>
                            </li>
                        </ul>''',
        '''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                    <span class="text-gray-700 text-lg leading-relaxed" x-html="item"></span>
                                </li>
                            </template>
                        </ul>'''
    )
    content = content.replace('src="About-us/About Us_Who We Are.jpg"', ':src="pageData.about_us.who_we_are.image || \'About-us/About Us_Who We Are.jpg\'"')

    # 3. Origin Group
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\n                    Our <span class="text-brand-primary">Origin</span>\n                </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.origin.headline"></h2>'
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed">\n                            PYF was built by financial professionals with decades of experience guiding real people—just like you—toward better financial outcomes. Through this work, a consistent pattern emerged:\n                        </p>',
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.origin.desc1"></p>'
    )
    content = content.replace(
        '''<ul class="space-y-4 mb-10">
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">People earned money but struggled to keep it</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Tax rules were confusing and costly</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Financial tools used by the wealthy were out of reach for most</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Independent earners lacked support systems</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Many families headed toward an uncertain financial future</span>
                            </li>
                        </ul>''',
        '''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-html="item"></span>
                                </li>
                            </template>
                        </ul>'''
    )
    content = content.replace(
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed">\n                            The team behind PYF recognized a gap: people needed a system — not just products, tips, or one-time fixes, but a comprehensive approach that helped them improve their financial lives year after year.\n                        </p>',
        '<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.origin.desc2"></p>'
    )
    content = content.replace(
        '<h3 class="text-2xl font-extrabold text-brand-dark uppercase">\n                            PYF was created to <span class="text-brand-primary">fill that gap.</span>\n                        </h3>',
        '<h3 class="text-2xl font-extrabold text-brand-dark uppercase" x-html="pageData.about_us.origin.headline_bottom"></h3>'
    )
    content = content.replace('src="About-us/About Us_Our Origin.jpg"', ':src="pageData.about_us.origin.image || \'About-us/About Us_Our Origin.jpg\'"')

    # 4. Mission Group
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6">\n                            Our <span class="text-brand-primary">Mission</span>\n                        </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.mission.headline"></h2>'
    )
    content = content.replace(
        '<h3 class="text-2xl font-bold text-gray-800 mb-6 uppercase tracking-wide">Our mission is simple</h3>',
        '<h3 class="text-2xl font-bold text-gray-800 mb-6 uppercase tracking-wide" x-text="pageData.about_us.mission.subtitle"></h3>'
    )
    content = content.replace(
        '<p class="text-xl text-gray-600 font-medium leading-relaxed">\n                            To help everyday people gain control of their finances by giving them access to tools, education, and expert support normally out of reach to them.\n                        </p>',
        '<p class="text-xl text-gray-600 font-medium leading-relaxed" x-text="pageData.about_us.mission.desc"></p>'
    )
    content = content.replace('src="About-us/About Us_Our Mission.jpg"', ':src="pageData.about_us.mission.image || \'About-us/About Us_Our Mission.jpg\'"')

    # 5. Serving Everyday Americans
    content = content.replace(
        '<h2 class="text-3xl md:text-5xl font-extrabold mb-12 uppercase leading-tight">\n                    Serving Everyday Americans For Over A <span class="text-brand-primary">Decade</span>\n                </h2>',
        '<h2 class="text-3xl md:text-5xl font-extrabold mb-12 uppercase leading-tight" x-html="pageData.about_us.serving.headline"></h2>'
    )
    content = content.replace(
        '''<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">
                        <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                            <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide">14+ Years</h4>
                            <p class="text-gray-600 font-medium leading-relaxed">In business supporting individuals and families.</p>
                        </div>
                        <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                            <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide">46 States</h4>
                            <p class="text-gray-600 font-medium leading-relaxed">Nationwide coverage and accessibility.</p>
                        </div>
                        <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                            <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide">Thousands</h4>
                            <p class="text-gray-600 font-medium leading-relaxed">Of users building better financial futures.</p>
                        </div>
                    </div>''',
        '''<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">
                        <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                            <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                                <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide" x-text="stat.title"></h4>
                                <p class="text-gray-600 font-medium leading-relaxed" x-text="stat.desc"></p>
                            </div>
                        </template>
                    </div>'''
    )
    content = content.replace(
        '''<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">
                        <h3 class="text-2xl font-extrabold text-brand-dark mb-6 text-center uppercase">3 Core Principles</h3>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                                <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-file-invoice-dollar text-brand-primary text-xl"></i>
                                </div>
                                <h4 class="font-bold text-gray-800 text-lg uppercase">Taxpayer Awareness</h4>
                            </div>
                            <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                                <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-chart-line text-brand-primary text-xl"></i>
                                </div>
                                <h4 class="font-bold text-gray-800 text-lg uppercase">Financial Literacy</h4>
                            </div>
                            <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                                <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-briefcase text-brand-primary text-xl"></i>
                                </div>
                                <h4 class="font-bold text-gray-800 text-lg uppercase">Entrepreneurship</h4>
                            </div>
                        </div>
                    </div>''',
        '''<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">
                        <h3 class="text-2xl font-extrabold text-brand-dark mb-6 text-center uppercase" x-text="pageData.about_us.serving.principles_title || '3 Core Principles'"></h3>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <template x-for="(prin, idx) in pageData.about_us.serving.principles" :key="idx">
                                <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                                    <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                                        <i :class="prin.icon" class="text-brand-primary text-xl"></i>
                                    </div>
                                    <h4 class="font-bold text-gray-800 text-lg uppercase" x-text="prin.title"></h4>
                                </div>
                            </template>
                        </div>
                    </div>'''
    )
    content = content.replace('src="About-us/About Us_Serving Everyday Americans.jpg"', ':src="pageData.about_us.serving.image || \'About-us/About Us_Serving Everyday Americans.jpg\'"')

    # 6. PYF System 
    content = content.replace(
        '<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-6 leading-tight">\n                    A system, not a personality. <br> <span class="text-brand-primary">PYF is designed </span> to work regardless of who <span class="text-brand-primary">uses </span> it\n                </h2>',
        '<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-6 leading-tight" x-html="pageData.about_us.system.headline"></h2>'
    )
    content = content.replace(
        '<p class="text-xl md:text-2xl text-center text-gray-600 font-medium mb-16 max-w-4xl mx-auto">\n                    Financial control comes from mastering three critical levers:\n                </p>',
        '<p class="text-xl md:text-2xl text-center text-gray-600 font-medium mb-16 max-w-4xl mx-auto" x-text="pageData.about_us.system.subtitle"></p>'
    )
    
    # Very large block for the system cards! We use split instead of replace because of spaces
    sys_start = content.find('<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">')
    if sys_start != -1:
        sys_end = content.find('<!-- Call to Action / Transition -->', sys_start)
        if sys_end != -1:
            content = content[:sys_start] + '''<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
                    <template x-for="(card, idx) in pageData.about_us.system.cards" :key="idx">
                        <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-100 flex flex-col transition duration-300 hover:shadow-2xl translate-y-0 hover:-translate-y-2 group">
                            
                            <!-- Card Image overlay context -->
                            <div class="relative h-64 overflow-hidden">
                                <img :src="card.image" :alt="card.title" class="w-full h-full object-cover transition duration-700 group-hover:scale-105">
                                <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                                <div class="absolute bottom-0 left-0 w-full p-6">
                                    <h3 class="text-3xl font-extrabold text-white uppercase tracking-wider" x-text="card.title"></h3>
                                </div>
                            </div>

                            <div class="p-8 flex-1 flex flex-col">
                                <p class="text-gray-700 text-lg mb-6 leading-relaxed flex-1" x-text="card.desc"></p>
                                
                                <ul class="space-y-3 mb-8">
                                    <template x-for="(item, lIdx) in card.list" :key="lIdx">
                                        <li class="flex items-start text-gray-800 font-medium bg-gray-50 rounded-lg p-3 border border-gray-100">
                                            <i class="fas fa-check-circle text-brand-primary text-lg mr-3 mt-0.5"></i>
                                            <span x-text="item"></span>
                                        </li>
                                    </template>
                                </ul>

                                <div x-show="card.quote" class="bg-[#f0fdf4] border-l-4 border-brand-primary p-4 rounded-r-lg mt-auto mb-4">
                                    <p class="text-brand-dark italic font-semibold" x-text="card.quote"></p>
                                </div>
                                <div x-show="card.footer" class="bg-gray-100 p-4 rounded-lg text-center mt-auto">
                                    <p class="text-gray-800 font-bold text-sm uppercase tracking-wide" x-text="card.footer"></p>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>\n\n                ''' + content[sys_end:]

    # 7. Who We Serve
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-4">\n                            Who We <span class="text-brand-primary">Serve</span>\n                        </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-4" x-html="pageData.about_us.who_we_serve.headline"></h2>'
    )
    content = content.replace(
        '''<ul class="space-y-4 mb-12">
                            <li class="flex items-start">
                                <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">W-2 workers navigating tax complexities</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Gig workers seeking predictable support</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Families lowering household expenses</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Individuals planning for long-term security</span>
                            </li>
                        </ul>''',
        '''<ul class="space-y-4 mb-12">
                            <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>'''
    )
    content = content.replace(
        '<p class="text-xl text-gray-800 font-bold border-l-4 border-brand-primary pl-4 py-2 italic">\n                            If financial improvement is your goal, PYF is designed for you.\n                        </p>',
        '<p class="text-xl text-gray-800 font-bold border-l-4 border-brand-primary pl-4 py-2 italic" x-text="pageData.about_us.who_we_serve.footer"></p>'
    )
    content = content.replace('src="About-us/About Us_Who We Serve.jpg"', ':src="pageData.about_us.who_we_serve.image || \'About-us/About Us_Who We Serve.jpg\'"')

    # 8. What Makes PYF Different
    content = content.replace(
        '<h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark uppercase mb-6">\n                            What Makes <span class="text-brand-primary">PYF Different</span>\n                        </h2>',
        '<h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.different.headline"></h2>'
    )
    content = content.replace(
        '''<ul class="space-y-4 mb-10">
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Professional-grade tax and legal support for everyday people</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Real savings programs that reduce real expenses</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Entrepreneurial tools and education resources that are simple to use</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">A system, not a personality. PYF is designed to work regardless of who leads it</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">A clear, step-by-step path toward financial clarity for those who want it</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium">Support year-round, not just during tax season</span>
                            </li>
                        </ul>''',
        '''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>'''
    )
    content = content.replace('src="About-us/About Us_What Makes PYF Different.jpg"', ':src="pageData.about_us.different.image || \'About-us/About Us_What Makes PYF Different.jpg\'"')

    # 9. Pledge
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6">\n                            Our <span class="text-brand-primary">Pledge To Help You</span>\n                        </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.pledge.headline"></h2>'
    )
    content = content.replace(
        '''<ul class="space-y-4 mb-10">
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Understand your finances</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Reduce unnecessary expenses</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Legally minimize your tax burden</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Increase your income opportunities</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Gain a clearer path toward long-term stability</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                <span class="text-gray-700 font-medium text-lg">Access professional guidance</span>
                            </li>
                        </ul>''',
        '''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>'''
    )
    content = content.replace('src="About-us/About Us_Built For Real Life_Our Commitment.jpg"', ':src="pageData.about_us.pledge.image || \'About-us/About Us_Built For Real Life_Our Commitment.jpg\'"')

    # 10. Journey
    content = content.replace(
        '<h2 class="text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-6 drop-shadow-md">\n                Start Your PYF Journey\n            </h2>',
        '<h2 class="text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-6 drop-shadow-md" x-text="pageData.about_us.journey.headline"></h2>'
    )
    content = content.replace(
        '<p class="text-lg md:text-2xl text-brand-100 font-medium mb-12 max-w-3xl mx-auto leading-relaxed whitespace-pre-line">\n                Choose the path that fits your goals today. PYF will support<br class="hidden md:block"> you every step of the way.\n            </p>',
        '<p class="text-lg md:text-2xl text-brand-100 font-medium mb-12 max-w-3xl mx-auto leading-relaxed whitespace-pre-line" x-text="pageData.about_us.journey.desc"></p>'
    )
    content = content.replace(
        '<a href="https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm"\n                   class="bg-white text-brand-primary font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-50 flex items-center justify-center uppercase tracking-wider">\n                    BECOME AN AFFILIATE\n                </a>',
        '<a :href="pageData.about_us.journey.btn1_link"\n                   class="bg-white text-brand-primary font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-50 flex items-center justify-center uppercase tracking-wider" x-text="pageData.about_us.journey.btn1_text">\n                </a>'
    )
    content = content.replace(
        '<a href="packages.html" class="bg-brand-dark text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-900 border border-transparent hover:border-gray-700 flex items-center justify-center">\n                    View Service Packages\n                </a>',
        '<a :href="pageData.about_us.journey.btn2_link" class="bg-brand-dark text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-900 border border-transparent hover:border-gray-700 flex items-center justify-center" x-text="pageData.about_us.journey.btn2_text">\n                </a>'
    )

    with open('about-us.html', 'w', encoding='utf-8') as f:
         f.write(content)

string_replace_frontend()
