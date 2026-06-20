import re
import json

def patch_frontend():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('about_data.json', 'r', encoding='utf-8') as f:
        about_data = f.read()
        
    # Replace body
    content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>')
    
    # Hero Section
    content = re.sub(
        r'<img src="About-us/About Us_Hero\.jpg"',
        r'<img :src="pageData.about_us.hero.image || \'About-us/About Us_Hero.jpg\'"',
        content
    )
    content = re.sub(
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md">.*?</h1>',
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md" x-html="pageData.about_us.hero.headline"></h1>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<p class="text-base md:text-xl text-gray-100 mb-10 font-medium leading-relaxed max-w-3xl">.*?</p>',
        r'<p class="text-base md:text-xl text-gray-100 mb-10 font-medium leading-relaxed max-w-3xl whitespace-pre-line" x-text="pageData.about_us.hero.desc"></p>',
        content, flags=re.DOTALL
    )
    
    # Who We Are
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*Who <span class="text-brand-primary">We Are</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.who_we_are.headline"></h2>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<p class="text-gray-700 text-lg mb-6 leading-relaxed">\s*Pay Yourself First \(PYF\) is a financial.*?<\/p>',
        r'<p class="text-gray-700 text-lg mb-6 leading-relaxed" x-html="pageData.about_us.who_we_are.desc1"></p>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<p class="text-gray-700 text-lg mb-8 leading-relaxed">\s*As the cost of living rises.*?<\/p>',
        r'<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.who_we_are.desc2"></p>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<ul class="space-y-4 mb-10">\s*<li class="flex items-start">.*?<\/ul>',
        r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-html="item"></span>
                                </li>
                            </template>
                        </ul>''',
        content, flags=re.DOTALL
    )
    content = re.sub(r'<img src="About-us/About Us_Who We Are\.jpg"', r'<img :src="pageData.about_us.who_we_are.image || \'About-us/About Us_Who We Are.jpg\'"', content)
    
    # Origin
    content = re.sub(r'<img src="About-us/About Us_Our Origin\.jpg"', r'<img :src="pageData.about_us.origin.image || \'About-us/About Us_Our Origin.jpg\'"', content)
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*Our <span class="text-brand-primary">Origin</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.about_us.origin.headline"></h2>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<p class="text-gray-700 text-lg mb-8 leading-relaxed">\s*PYF was built by financial professionals.*?<\/p>',
        r'<p class="text-gray-700 text-lg mb-8 leading-relaxed" x-text="pageData.about_us.origin.desc1"></p>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<ul class="space-y-4 mb-10">\s*<li class="flex items-start">.*?<\/ul>',
        r'''<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-html="item"></span>
                                </li>
                            </template>
                        </ul>''',
        content, count=1, flags=re.DOTALL
    )
    content = re.sub(
        r'<h3 class="text-2xl font-extrabold text-brand-dark uppercase">\s*PYF was created to <span class="text-brand-primary">fill that gap\.</span>\s*</h3>',
        r'<h3 class="text-2xl font-extrabold text-brand-dark uppercase" x-html="pageData.about_us.origin.headline_bottom"></h3>',
        content, flags=re.DOTALL
    )
    
    # Mission
    content = re.sub(r'<img src="About-us/About Us_Our Mission\.jpg"', r'<img :src="pageData.about_us.mission.image || \'About-us/About Us_Our Mission.jpg\'"', content)
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6">\s*Our <span class="text-brand-primary">Mission</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.mission.headline"></h2>',
        content, flags=re.DOTALL
    )
    
    # Serving 
    content = re.sub(r'<img src="About-us/About Us_Serving Everyday Americans\.jpg"', r'<img :src="pageData.about_us.serving.image || \'About-us/About Us_Serving Everyday Americans.jpg\'"', content)
    
    # Who We Serve
    content = re.sub(r'<img src="About-us/About Us_Who We Serve\.jpg"', r'<img :src="pageData.about_us.who_we_serve.image || \'About-us/About Us_Who We Serve.jpg\'"', content)
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-4">\s*Who We <span class="text-brand-primary">Serve</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-4" x-html="pageData.about_us.who_we_serve.headline"></h2>',
        content, flags=re.DOTALL
    )
    
    # Diff
    content = re.sub(r'<img src="About-us/About Us_What Makes PYF Different\.jpg"', r'<img :src="pageData.about_us.different.image || \'About-us/About Us_What Makes PYF Different.jpg\'"', content)
    content = re.sub(
        r'<h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark uppercase mb-6">\s*What Makes <span class="text-brand-primary">PYF Different</span>\s*</h2>',
        r'<h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.different.headline"></h2>',
        content, flags=re.DOTALL
    )

    # Need to append the Alpine script at the end
    script_block = f"""
    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <script>
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        
        document.addEventListener('alpine:init', () => {{
            const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
            
            Alpine.data('siteData', () => ({{
                pageData: {{
                    about_us: {about_data}
                }},
                
                async init() {{
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    
                    try {{
                        let {{ data, error }} = await supabase.from('site_content').select('*').eq('page_id', 'about_us').single();
                        if (data) {{
                            const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                            this.pageData.about_us = {{ ...this.pageData.about_us, ...loadedContent }};
                        }}
                    }} catch (e) {{
                        console.error("Failed to load CMS data", e);
                    }}
                }}
            }}));
        }});
    </script>
</body>"""

    content = content.replace("</body>", script_block)
    
    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Patched about-us.html")

patch_frontend()
