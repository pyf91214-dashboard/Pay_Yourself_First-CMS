import re

def apply_patch():
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Supabase & Alpine
    head_addition = """
    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script src="js/supabase-client.js"></script>

    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
"""
    if "https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" not in content:
        content = content.replace('    <style>', head_addition + '    <style>')
        
    if "x-data=\"pageData()\"" not in content:
        content = content.replace('<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen">', '<body class="bg-white text-gray-800 font-sans antialiased flex flex-col min-h-screen" x-data="pageData()" x-cloak>')
    
    # 1. Hero background and texts
    hero_pattern = r'''<img src="Contact-us/Contact Us_Hero\.jpg"\s*alt="Contact Us Team"\s*class="[^"]*">'''
    new_hero = '''<img :src="pageData.contact_us.hero.image || 'Contact-us/Contact Us_Hero.jpg'" 
                 alt="Contact Us Team" 
                 class="absolute inset-0 w-full h-full object-cover">'''
    content = re.sub(hero_pattern, new_hero, content)
    
    content = re.sub(
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md">\s*Get In Touch With Us\s*</h1>',
        r'<h1 class="text-3xl md:text-5xl font-extrabold text-white mb-6 uppercase leading-tight drop-shadow-md" x-html="pageData.contact_us.hero.headline"></h1>',
        content, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<p class="text-base md:text-xl text-gray-100 font-medium leading-relaxed max-w-2xl">.*?<\/p>',
        r'<p class="text-base md:text-xl text-gray-100 font-medium leading-relaxed max-w-2xl whitespace-pre-line" x-html="pageData.contact_us.hero.desc"></p>',
        content, flags=re.DOTALL
    )
    
    # 2. Add the Alpine init block at the end (before </body></html>)
    script_block = """
    <script>
        document.addEventListener('alpine:init', () => {
            Alpine.data('pageData', () => ({
                pageData: {
                    contact_us: {
                        hero: {
                            headline: "Get In Touch With Us",
                            desc: "Whether you have questions about our services, need support, or want to\\nexplore business partnerships, we're here to help.",
                            image: "Contact-us/Contact Us_Hero.jpg"
                        }
                    }
                },
                async init() {
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    
                    try {
                        if (typeof supabase !== 'undefined' && supabase) {
                            let { data, error } = await supabase.from('site_content').select('*').eq('page_id', 'contact_us').single();
                            if (data) {
                                const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                                this.pageData.contact_us = { ...this.pageData.contact_us, ...loadedContent };
                            }
                        }
                    } catch (e) {
                        console.error("Failed to load CMS data", e);
                    }
                }
            }));
        });
    </script>
"""
    if "Alpine.data('pageData'" not in content:
        content = content.replace('</body>\n</html>', script_block + '</body>\n</html>')

    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    apply_patch()
    print("contact-us.html patched successfully.")
