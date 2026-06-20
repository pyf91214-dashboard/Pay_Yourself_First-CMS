import re
import os

def regex_patch():
    # Keep it clean
    os.system('git checkout about-us.html')
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 0. Alpine JS Setup
    content = re.sub(
        r'<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">',
        r'<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>',
        content
    )
    
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
    if "siteData" not in content:
        content = content.replace("</body>", script_block)

    # 1. Hero
    content = re.sub(r'(<h1[^>]*>).*?(Take Control).*?(</h1>)', r'\1\n                    <span x-html="pageData.about_us.hero.headline"></span>\n                \3', content, flags=re.DOTALL)
    content = re.sub(r'(<p[^>]*>).*?(Pay Yourself First was created to make financial stability accessible).*?(</p>)', r'<p class="text-base md:text-xl text-gray-100 mb-10 font-medium leading-relaxed max-w-3xl whitespace-pre-line" x-text="pageData.about_us.hero.desc"></p>', content, flags=re.DOTALL|re.IGNORECASE)
    content = re.sub(r'src="About-us/About Us_Hero\.jpg"', r':src="pageData.about_us.hero.image || \'About-us/About Us_Hero.jpg\'"', content)

    # 2. Who We Are
    content = re.sub(r'(<h2[^>]*>).*?(Who).*?(We Are).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.who_we_are.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?Pay Yourself First \(PYF\) is a financial empowerment.*?<\/p>', r'<p class="text-gray-700 text-lg mb-6 leading-relaxed" x-html="pageData.about_us.who_we_are.desc1"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?As the cost of living rises and financial pressure.*?<\/p>', r'<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.who_we_are.desc2"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?PYF was created to solve these problems by.*?<\/p>', r'<p class="text-gray-700 text-lg mb-6 leading-relaxed" x-text="pageData.about_us.who_we_are.desc3"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?Our company is built around a system.*?<\/p>', r'<p class="text-gray-700 text-lg leading-relaxed" x-text="pageData.about_us.who_we_are.desc4"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<ul class="space-y-4 mb-10">.*?W-2 workers overpaying taxes.*?</ul>', r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                    <span class="text-gray-700 text-lg leading-relaxed" x-html="item"></span>
                                </li>
                            </template>
                        </ul>''', content, flags=re.DOTALL)
    content = re.sub(r'src="About-us/About Us_Who We Are\.jpg"', r':src="pageData.about_us.who_we_are.image || \'About-us/About Us_Who We Are.jpg\'"', content)

    # 3. Origin
    content = re.sub(r'(<h2[^>]*>).*?(Our).*?(Origin).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.origin.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?PYF was built by financial professionals with decades.*?<\/p>', r'<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.origin.desc1"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<ul class="space-y-4 mb-10">.*?People earned money but struggled to keep it.*?</ul>', r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-html="item"></span>
                                </li>
                            </template>
                        </ul>''', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?The team behind PYF recognized a gap.*?<\/p>', r'<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.origin.desc2"></p>', content, flags=re.DOTALL)
    content = re.sub(r'(<h3[^>]*>).*?(fill that gap).*?(</h3>)', r'<h3 class="text-2xl font-extrabold text-brand-dark uppercase" x-html="pageData.about_us.origin.headline_bottom"></h3>', content, flags=re.DOTALL)
    content = re.sub(r'src="About-us/About Us_Our Origin\.jpg"', r':src="pageData.about_us.origin.image || \'About-us/About Us_Our Origin.jpg\'"', content)

    # 4. Mission
    content = re.sub(r'(<h2[^>]*>).*?(Our).*?(Mission).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.mission.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'(<h3[^>]*>.*?)(Our mission is simple)(.*?</h3>)', r'<h3 class="text-2xl font-bold text-gray-800 mb-6 uppercase tracking-wide" x-text="pageData.about_us.mission.subtitle"></h3>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?To help everyday people gain control of their finances.*?<\/p>', r'<p class="text-xl text-gray-600 font-medium leading-relaxed" x-text="pageData.about_us.mission.desc"></p>', content, flags=re.DOTALL)
    content = re.sub(r'src="About-us/About Us_Our Mission\.jpg"', r':src="pageData.about_us.mission.image || \'About-us/About Us_Our Mission.jpg\'"', content)

    # 5. Serving Everyday
    content = re.sub(r'(<h2[^>]*>).*?(Serving Everyday Americans).*?(</h2>)', r'<h2 class="text-3xl md:text-5xl font-extrabold mb-12 uppercase leading-tight" x-html="pageData.about_us.serving.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">.*?</div>.*?</div>', r'''<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">
                        <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                            <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                                <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide" x-text="stat.title"></h4>
                                <p class="text-gray-600 font-medium leading-relaxed" x-text="stat.desc"></p>
                            </div>
                        </template>
                    </div>''', content, flags=re.DOTALL, count=1)
    content = re.sub(r'<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">.*?</div>.*?</div>', r'''<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">
                        <h3 class="text-2xl font-extrabold text-brand-dark mb-6 text-center uppercase">3 Core Principles</h3>
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
                    </div>''', content, flags=re.DOTALL, count=1)
    content = re.sub(r'src="About-us/About Us_Serving Everyday Americans\.jpg"', r':src="pageData.about_us.serving.image || \'About-us/About Us_Serving Everyday Americans.jpg\'"', content)

    # 6. System
    content = re.sub(r'(<h2[^>]*>).*?(A system, not a personality).*?(</h2>)', r'<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-6 leading-tight" x-html="pageData.about_us.system.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?Financial control comes from mastering three critical levers.*?<\/p>', r'<p class="text-xl md:text-2xl text-center text-gray-600 font-medium mb-16 max-w-4xl mx-auto" x-text="pageData.about_us.system.subtitle"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">.*?<!-- Call to Action / Transition -->', r'''<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
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

                                <div x-show="card.quote !== undefined" class="bg-[#f0fdf4] border-l-4 border-brand-primary p-4 rounded-r-lg mt-auto mb-4">
                                    <p class="text-brand-dark italic font-semibold" x-text="card.quote"></p>
                                </div>
                                <div x-show="card.footer !== undefined" class="bg-gray-100 p-4 rounded-lg text-center mt-auto">
                                    <p class="text-gray-800 font-bold text-sm uppercase tracking-wide" x-text="card.footer"></p>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>

                <!-- Call to Action / Transition -->''', content, flags=re.DOTALL, count=1)

    # 7. Who We Serve
    content = re.sub(r'(<h2[^>]*>).*?(Who We).*?(Serve).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-4" x-html="pageData.about_us.who_we_serve.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<ul class="space-y-4 mb-12">.*?W-2 workers navigating tax complexities.*?</ul>', r'''<ul class="space-y-4 mb-12">
                            <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>''', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?If financial improvement is your goal, PYF is designed for you.*?<\/p>', r'<p class="text-xl text-gray-800 font-bold border-l-4 border-brand-primary pl-4 py-2 italic" x-text="pageData.about_us.who_we_serve.footer"></p>', content, flags=re.DOTALL)
    content = re.sub(r'src="About-us/About Us_Who We Serve\.jpg"', r':src="pageData.about_us.who_we_serve.image || \'About-us/About Us_Who We Serve.jpg\'"', content)

    # 8. What Makes PYF Different
    content = re.sub(r'(<h2[^>]*>).*?(What Makes).*?(PYF Different).*?(</h2>)', r'<h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.different.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<ul class="space-y-4 mb-10">.*?Professional-grade tax and legal support.*?</ul>', r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-text="item"></span>
                                </li>
                            </template>
                        </ul>''', content, flags=re.DOTALL, count=1)
    content = re.sub(r'src="About-us/About Us_What Makes PYF Different\.jpg"', r':src="pageData.about_us.different.image || \'About-us/About Us_What Makes PYF Different.jpg\'"', content)

    # 9. Pledge
    content = re.sub(r'(<h2[^>]*>).*?(Our).*?(Pledge To Help You).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.pledge.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<ul class="space-y-4 mb-10">.*?Understand your finances.*?</ul>', r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>''', content, flags=re.DOTALL, count=1)
    content = re.sub(r'src="About-us/About Us_Built For Real Life_Our Commitment\.jpg"', r':src="pageData.about_us.pledge.image || \'About-us/About Us_Built For Real Life_Our Commitment.jpg\'"', content)

    # 10. Journey
    content = re.sub(r'(<h2[^>]*>).*?(Start Your PYF Journey).*?(</h2>)', r'<h2 class="text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-6 drop-shadow-md" x-text="pageData.about_us.journey.headline"></h2>', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>.*?Choose the path that fits your goals today.*?<\/p>', r'<p class="text-lg md:text-2xl text-brand-100 font-medium mb-12 max-w-3xl mx-auto leading-relaxed whitespace-pre-line" x-text="pageData.about_us.journey.desc"></p>', content, flags=re.DOTALL)
    content = re.sub(r'<a href="https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm"[^>]*>.*?BECOME AN AFFILIATE.*?</a>', r'<a :href="pageData.about_us.journey.btn1_link" class="bg-white text-brand-primary font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-50 flex items-center justify-center uppercase tracking-wider"><span x-text="pageData.about_us.journey.btn1_text"></span></a>', content, flags=re.DOTALL)
    content = re.sub(r'<a href="packages.html"[^>]*>.*?View Service Packages.*?</a>', r'<a :href="pageData.about_us.journey.btn2_link" class="bg-brand-dark text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-900 border border-transparent hover:border-gray-700 flex items-center justify-center"><span x-text="pageData.about_us.journey.btn2_text"></span></a>', content, flags=re.DOTALL)

    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

regex_patch()
