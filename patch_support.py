import re
import json

def parse_faqs():
    with open('support.html', 'r', encoding='utf-8') as f:
        content = f.read()

    categories = []
    
    parts = re.split(r'<h2 class="[^"]*tracking-wide[^"]*">', content)
    
    for i in range(1, len(parts)):
        part_content = parts[i]
        
        # The title is everything up to </h2>
        title_match = re.search(r'\s*(.*?)\s*</h2>', part_content, flags=re.DOTALL)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        
        questions = []
        
        q_matches = re.finditer(r'<span class="font-bold text-brand-dark text-base md:text-lg">(.*?)</span>.*?<div class="accordion-content">\s*<div class="px-6 pb-6 pt-0 text-gray-600 leading-relaxed">(.*?)</div>\s*</div>', part_content, flags=re.DOTALL)
        
        for q_match in q_matches:
            q = q_match.group(1).strip()
            a = q_match.group(2).strip()
            questions.append({"q": q, "a": a})
            
        categories.append({"title": title, "questions": questions})
        
    return categories

def apply_patch():
    with open('support.html', 'r', encoding='utf-8') as f:
        content = f.read()

    cats = parse_faqs()
    
    support_data = {
        "hero": {
            "headline": "Pay Yourself First Customer and Affiliate FAQ",
            "desc": "This FAQ answers common questions about our services and affiliate program.\nWhether you're considering becoming a customer, an affiliate, or both, \nyou'll find clear explanations to help you understand exactly what PYF offers.",
            "image": "Support-Page/Support Page_Hero.jpg"
        },
        "categories": cats
    }
    
    main_pattern = r'<main class="flex-grow pt-\[110px\] md:pt-\[130px\] px-4 md:px-8 bg-white">(.*?)</main>'
    
    new_main_html = """
        <div class="max-w-4xl mx-auto py-12">
            <template x-for="(cat, catIndex) in pageData.support.categories" :key="catIndex">
                <div class="mb-12">
                    <div class="mb-6 border-b border-brand-green/30 pb-2">
                        <h2 class="text-2xl font-bold text-brand-green uppercase tracking-wide" x-html="cat.title"></h2>
                    </div>
                    
                    <div class="space-y-4">
                        <template x-for="(faq, qIndex) in cat.questions" :key="qIndex">
                            <div class="bg-faq-bg rounded-sm">
                                <button class="accordion-btn w-full px-6 py-5 flex justify-between items-center text-left focus:outline-none" aria-expanded="false" @click="toggleAccordion($event)">
                                    <span class="font-bold text-brand-dark text-base md:text-lg" x-text="faq.q"></span>
                                    <i class="fa-solid fa-chevron-down text-brand-green text-xl accordion-icon flex-shrink-0 ml-4"></i>
                                </button>
                                <div class="accordion-content">
                                    <div class="px-6 pb-6 pt-0 text-gray-600 leading-relaxed" x-html="faq.a"></div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </template>
        </div>"""
    
    content = re.sub(main_pattern, f'<main class="flex-grow pt-[110px] md:pt-[130px] px-4 md:px-8 bg-white">{new_main_html}</main>', content, flags=re.DOTALL)
    
    hero_pattern = r'''<img src="Support-Page/Support Page_Hero\.jpg" 
                 alt="Customer Support Team" 
                 class="absolute inset-0 w-full h-full object-cover">'''
    new_hero = '''<img :src="pageData.support.hero.image || \'Support-Page/Support Page_Hero.jpg\'" 
                 alt="Customer Support Team" 
                 class="absolute inset-0 w-full h-full object-cover">'''
    content = content.replace(hero_pattern, new_hero)
    
    content = re.sub(
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md">\s*Pay Yourself First Customer and Affiliate FAQ\s*</h1>',
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md" x-text="pageData.support.hero.headline"></h1>',
        content, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<p class="text-md md:text-md text-gray-100 font-medium leading-relaxed max-w-6xl">.*?<\/p>',
        r'<p class="text-md md:text-md text-gray-100 font-medium leading-relaxed max-w-6xl whitespace-pre-line" x-text="pageData.support.hero.desc"></p>',
        content, flags=re.DOTALL
    )
    
    head_addition = """
    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

    <!-- Alpine.js for Interactions -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
"""
    content = content.replace('    <style>', head_addition + '    <style>')
    content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="siteData" x-cloak>')
    
    with open('support_data.json', 'w', encoding='utf-8') as f:
        json.dump(support_data, f, indent=4)
        
    with open('support.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_patch()
