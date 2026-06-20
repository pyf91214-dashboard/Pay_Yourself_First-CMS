import re

def patch_frontend_sections():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to map Serving Everyday Americans and System Levers!
    
    # 1. Serving Everyday Americans
    content = re.sub(
        r'<h2 class="text-3xl md:text-5xl font-extrabold mb-12 uppercase leading-tight">\s*Serving Everyday Americans For Over A <span class="text-brand-primary">Decade</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-5xl font-extrabold mb-12 uppercase leading-tight" x-html="pageData.about_us.serving.headline"></h2>',
        content, count=1, flags=re.DOTALL
    )
    
    # Replace the 3 stats
    # They are in a flex flex-col md:flex-row shadow-lg
    stats_replacement = """<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">
                            <!-- Alpine JS Loop for Stats -->
                            <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                                <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                                    <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide" x-text="stat.title"></h4>
                                    <p class="text-gray-600 font-medium leading-relaxed" x-text="stat.desc"></p>
                                </div>
                            </template>
                        </div>"""
    
    content = re.sub(
        r'<div class="flex flex-col md:flex-row justify-center items-center bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden divide-y md:divide-y-0 md:divide-x divide-gray-200">.*?</div>\s*</div>',
        stats_replacement + '\n                    </div>',
        content, count=1, flags=re.DOTALL
    )
    
    # Replace the 3 Core Principles
    principles_replacement = """<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">
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
                        </div>"""
                        
    content = re.sub(
        r'<div class="mt-12 bg-gray-50 rounded-xl p-8 border border-gray-200 shadow-inner">.*?</div>\s*</div>',
        principles_replacement + '\n                    </div>',
        content, count=1, flags=re.DOTALL
    )
    
    # 2. System Levers
    content = re.sub(
        r'<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-6 leading-tight">\s*A system, not a personality\. <br> <span class="text-brand-primary">PYF is designed <\/span> to work regardless of who <span class="text-brand-primary">uses <\/span> it\s*</h2>',
        r'<h2 class="text-3xl md:text-5xl font-extrabold text-center text-brand-dark uppercase mb-6 leading-tight" x-html="pageData.about_us.system.headline"></h2>',
        content, count=1, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<p class="text-xl md:text-2xl text-center text-gray-600 font-medium mb-16 max-w-4xl mx-auto">\s*Financial control comes from mastering three critical levers:\s*<\/p>',
        r'<p class="text-xl md:text-2xl text-center text-gray-600 font-medium mb-16 max-w-4xl mx-auto" x-text="pageData.about_us.system.subtitle"></p>',
        content, count=1, flags=re.DOTALL
    )
    
    # Replace the Cards
    cards_replacement = """<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
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
                </div>"""
                
    content = re.sub(
        r'<div class="grid grid-cols-1 lg:grid-cols-3 gap-10">.*?<!-- Call to Action \/ Transition -->',
        cards_replacement + '\n\n                <!-- Call to Action / Transition -->',
        content, count=1, flags=re.DOTALL
    )

    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Patched missing sections in about-us.html")

patch_frontend_sections()
