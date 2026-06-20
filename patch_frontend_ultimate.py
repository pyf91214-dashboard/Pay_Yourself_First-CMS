import re
import os

def final_patch():
    # 1. Restore from Git
    os.system('git checkout about-us.html')
    
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Body tag
    content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>')
    
    # 2. Alpine Script
    script_block = """
    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <script>
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        
        document.addEventListener('alpine:init', () => {
            const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
            
            Alpine.data('siteData', () => ({
                pageData: {
                    about_us: {
                        hero: {},
                        who_we_are: { list: [] },
                        origin: { list: [] },
                        mission: {},
                        serving: { stats: [], principles: [] },
                        system: { cards: [] },
                        who_we_serve: { list: [] },
                        different: { list: [] },
                        pledge: { list: [] },
                        journey: {}
                    }
                },
                
                async init() {
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    try {
                        let { data, error } = await supabase.from('site_content').select('*').eq('page_id', 'about_us').single();
                        if (data) {
                            const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                            this.pageData.about_us = { ...this.pageData.about_us, ...loadedContent };
                        }
                    } catch (e) { console.error("Failed to load CMS data", e); }
                }
            }));
        });
    </script>
</body>"""
    if "siteData" not in content:
        content = content.replace("</body>", script_block)

    # We use BS4 to safely replace all text and img tags
    import bs4
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # Hero
    h1 = soup.find('h1')
    if h1: h1['x-html'] = "pageData.about_us.hero.headline"; h1.string = ''
    hero_p = soup.find('p', string=re.compile("Pay Yourself First was created"))
    if hero_p: hero_p['x-text'] = "pageData.about_us.hero.desc"; hero_p.string = ''
    h_img = soup.find('img', src=re.compile('Hero\.jpg'))
    if h_img: h_img[':src'] = "pageData.about_us.hero.image || 'About-us/About Us_Hero.jpg'"

    # Replace lists by mapping them specifically
    # Find the ul following 'Who We Are'
    who_we_are_h2 = soup.find(string=re.compile("Who"))
    if who_we_are_h2:
        parent_h2 = who_we_are_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.who_we_are.headline"; parent_h2.clear()
            ul = parent_h2.find_next_sibling('ul')
            if ul:
                # Wrap children in template
                ul.clear()
                ul.append(bs4.BeautifulSoup('''<template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx"><li class="flex items-start"><i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i><span class="text-gray-700 text-lg leading-relaxed" x-text="item"></span></li></template>''', 'html.parser'))
            
            p1 = parent_h2.find_next_sibling('p')
            if p1: p1['x-html'] = "pageData.about_us.who_we_are.desc1"; p1.string = ''
            p2 = p1.find_next_sibling('p') if p1 else None
            if p2: p2['x-text'] = "pageData.about_us.who_we_are.desc2"; p2.string = ''
            p3 = ul.find_next_sibling('p') if ul else None
            if p3: p3['x-text'] = "pageData.about_us.who_we_are.desc3"; p3.string = ''
            p4 = p3.find_next_sibling('p') if p3 else None
            if p4: p4['x-text'] = "pageData.about_us.who_we_are.desc4"; p4.string = ''
    who_img = soup.find('img', src=re.compile('Who We Are\.jpg'))
    if who_img: who_img[':src'] = "pageData.about_us.who_we_are.image || 'About-us/About Us_Who We Are.jpg'"

    # Origin
    origin_h2 = soup.find(string=re.compile("Origin"))
    if origin_h2:
        parent_h2 = origin_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.origin.headline"; parent_h2.clear()
            p1 = parent_h2.find_next_sibling('p')
            if p1: p1['x-text'] = "pageData.about_us.origin.desc1"; p1.string = ''
            ul = parent_h2.find_next_sibling('ul')
            if ul:
                ul.clear()
                ul.append(bs4.BeautifulSoup('''<template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx"><li class="flex items-start"><i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i><span class="text-gray-700 font-medium" x-html="item"></span></li></template>''', 'html.parser'))
            p2 = ul.find_next_sibling('p') if ul else None
            if p2: p2['x-text'] = "pageData.about_us.origin.desc2"; p2.string = ''
            h3 = p2.find_next_sibling('h3') if p2 else None
            if h3: h3['x-html'] = "pageData.about_us.origin.headline_bottom"; h3.clear()
    orig_img = soup.find('img', src=re.compile('Our Origin\.jpg'))
    if orig_img: orig_img[':src'] = "pageData.about_us.origin.image || 'About-us/About Us_Our Origin.jpg'"

    # Mission
    m_h2 = soup.find('h2', string=re.compile("Mission"))
    if not m_h2: m_h2 = soup.find(string=re.compile("Mission")).find_parent('h2') if soup.find(string=re.compile("Mission")) else None
    if m_h2:
        m_h2['x-html'] = "pageData.about_us.mission.headline"; m_h2.clear()
        m_h3 = m_h2.find_next_sibling('h3')
        if m_h3: m_h3['x-text'] = "pageData.about_us.mission.subtitle"; m_h3.string = ''
        m_p = m_h2.find_next_sibling('p')
        if m_p: m_p['x-text'] = "pageData.about_us.mission.desc"; m_p.string = ''
    m_img = soup.find('img', src=re.compile('Our Mission\.jpg'))
    if m_img: m_img[':src'] = "pageData.about_us.mission.image || 'About-us/About Us_Our Mission.jpg'"

    # Serving Everyday Americans
    serv_h2 = soup.find(string=re.compile("Serving Everyday", re.I))
    if serv_h2:
        parent_h2 = serv_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.serving.headline"; parent_h2.clear()
            # Replace inner stats div
            inner_stats = parent_h2.find_next_sibling('div').find('div', class_=re.compile("divide-y"))
            if inner_stats:
                inner_stats.clear()
                inner_stats.append(bs4.BeautifulSoup('''
                    <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                        <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                            <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide" x-text="stat.title"></h4>
                            <p class="text-gray-600 font-medium leading-relaxed" x-text="stat.desc"></p>
                        </div>
                    </template>
                ''', 'html.parser'))
            
            prin = soup.find('h3', string=re.compile("3 Core Principles", re.I))
            if prin:
                prin_grid = prin.find_next_sibling('div')
                if prin_grid:
                    prin_grid.clear()
                    prin_grid.append(bs4.BeautifulSoup('''
                        <template x-for="(prin, idx) in pageData.about_us.serving.principles" :key="idx">
                            <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                                <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                                    <i :class="prin.icon" class="text-brand-primary text-xl"></i>
                                </div>
                                <h4 class="font-bold text-gray-800 text-lg uppercase" x-text="prin.title"></h4>
                            </div>
                        </template>
                    ''', 'html.parser'))
    s_img = soup.find('img', src=re.compile('Serving Everyday Americans\.jpg'))
    if s_img: s_img[':src'] = "pageData.about_us.serving.image || 'About-us/About Us_Serving Everyday Americans.jpg'"

    # System
    sys_h2 = soup.find(string=re.compile("system, not a personality", re.I))
    if sys_h2:
        parent_h2 = sys_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.system.headline"; parent_h2.clear()
            sys_p = parent_h2.find_next_sibling('p')
            if sys_p: sys_p['x-text'] = "pageData.about_us.system.subtitle"; sys_p.string = ''
            
            cards = sys_p.find_next_sibling('div')
            if cards:
                cards.clear()
                cards.append(bs4.BeautifulSoup('''
                <template x-for="(card, idx) in pageData.about_us.system.cards" :key="idx">
                    <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-100 flex flex-col transition duration-300 hover:shadow-2xl translate-y-0 hover:-translate-y-2 group">
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
                ''', 'html.parser'))

    # Who We Serve
    serve_h2 = soup.find(string=re.compile("Who We Serve", re.I))
    if not serve_h2: serve_h2 = soup.find(string=re.compile("Serve", re.I)).find_parent('h2') if soup.find(string=re.compile("Serve", re.I)) else None
    if serve_h2:
        if serve_h2.name != 'h2': serve_h2 = serve_h2.find_parent('h2')
        if serve_h2:
            serve_h2['x-html'] = "pageData.about_us.who_we_serve.headline"; serve_h2.clear()
            s_ul = serve_h2.find_next_sibling('ul')
            if s_ul:
                s_ul.clear()
                s_ul.append(bs4.BeautifulSoup('''
                    <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                        <li class="flex items-start">
                            <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                            <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                        </li>
                    </template>
                ''', 'html.parser'))
            s_p = s_ul.find_next_sibling('p') if s_ul else None
            if s_p: s_p['x-text'] = "pageData.about_us.who_we_serve.footer"; s_p.string = ''
    sws_img = soup.find('img', src=re.compile('Who We Serve\.jpg'))
    if sws_img: sws_img[':src'] = "pageData.about_us.who_we_serve.image || 'About-us/About Us_Who We Serve.jpg'"

    # Different
    diff_h2 = soup.find(string=re.compile("PYF Different", re.I))
    if diff_h2:
        parent_h2 = diff_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.different.headline"; parent_h2.clear()
            d_ul = parent_h2.find_next_sibling('ul')
            if d_ul:
                d_ul.clear()
                d_ul.append(bs4.BeautifulSoup('''
                    <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                        <li class="flex items-start">
                            <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                            <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                        </li>
                    </template>
                ''', 'html.parser'))
    diff_img = soup.find('img', src=re.compile('What Makes PYF Different\.jpg'))
    if diff_img: diff_img[':src'] = "pageData.about_us.different.image || 'About-us/About Us_What Makes PYF Different.jpg'"

    # Pledge
    p_h2 = soup.find(string=re.compile("Pledge To Help You", re.I))
    if p_h2:
        parent_h2 = p_h2.find_parent('h2')
        if parent_h2:
            parent_h2['x-html'] = "pageData.about_us.pledge.headline"; parent_h2.clear()
            p_ul = parent_h2.find_next_sibling('ul')
            if p_ul:
                p_ul.clear()
                p_ul.append(bs4.BeautifulSoup('''
                    <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                        <li class="flex items-start">
                            <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                            <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                        </li>
                    </template>
                ''', 'html.parser'))
    pledge_img = soup.find('img', src=re.compile('Our Commitment\.jpg'))
    if pledge_img: pledge_img[':src'] = "pageData.about_us.pledge.image || 'About-us/About Us_Built For Real Life_Our Commitment.jpg'"

    # Journey
    j_h2 = soup.find('h2', string=re.compile("Start Your PYF Journey", re.I))
    if j_h2: j_h2['x-text'] = "pageData.about_us.journey.headline"; j_h2.string = ''
    j_p = soup.find('p', string=re.compile("Choose the path that fits", re.I))
    if j_p: j_p['x-text'] = "pageData.about_us.journey.desc"; j_p.string = ''
    for a in soup.find_all('a'):
        t = a.text.strip().upper()
        if "BECOME AN AFFILIATE" in t:
            a[':href'] = "pageData.about_us.journey.btn1_link"
            a['x-text'] = "pageData.about_us.journey.btn1_text"
            a.string = ""
        elif "VIEW SERVICE PACKAGES" in t:
            a[':href'] = "pageData.about_us.journey.btn2_link"
            a['x-text'] = "pageData.about_us.journey.btn2_text"
            a.string = ""

    final_output = str(soup)
    # Fix Alpine formatting issues created by bs4
    final_output = final_output.replace('&lt;template', '<template').replace('&lt;/template', '</template').replace('</template&gt;', '</template>')

    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(final_output)

    print("Fully mapped all DOM elements successfully!")

final_patch()
