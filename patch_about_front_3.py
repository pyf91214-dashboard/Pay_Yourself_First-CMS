import re

def patch_frontend_sections_3():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Our Pledge
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6">\s*Our <span class="text-brand-primary">Pledge To Help You</span>\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.about_us.pledge.headline"></h2>',
        content, count=1, flags=re.DOTALL
    )
    
    pledge_list_replacement = """<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium" x-html="item"></span>
                                </li>
                            </template>
                        </ul>"""

    content = re.sub(
        r'<ul class="space-y-4 mb-10">\s*<li class="flex items-start">.*?<\/ul>',
        pledge_list_replacement,
        content, count=1, flags=re.DOTALL
    )

    content = re.sub(
        r'<img src="About-us/About Us_Built For Real Life_Our Commitment\.jpg"',
        r'<img :src="pageData.about_us.pledge.image || \'About-us/About Us_Built For Real Life_Our Commitment.jpg\'"',
        content, count=1
    )

    # 2. Start Your Journey
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-6 drop-shadow-md">\s*Start Your PYF Journey\s*</h2>',
        r'<h2 class="text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-6 drop-shadow-md" x-text="pageData.about_us.journey.headline"></h2>',
        content, count=1, flags=re.DOTALL
    )

    content = re.sub(
        r'<p class="text-lg md:text-2xl text-brand-100 font-medium mb-12 max-w-3xl mx-auto leading-relaxed whitespace-pre-line">\s*Choose the path that fits your goals today\. PYF will support<br class="hidden md:block"> you every step of the way\.\s*</p>',
        r'<p class="text-lg md:text-2xl text-brand-100 font-medium mb-12 max-w-3xl mx-auto leading-relaxed whitespace-pre-line" x-text="pageData.about_us.journey.desc"></p>',
        content, count=1, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<a href="https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm"\s*class="bg-white text-brand-primary font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-50 flex items-center justify-center uppercase tracking-wider">\s*BECOME AN AFFILIATE\s*</a>',
        r'<a :href="pageData.about_us.journey.btn1_link" class="bg-white text-brand-primary font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-50 flex items-center justify-center uppercase tracking-wider" x-text="pageData.about_us.journey.btn1_text"></a>',
        content, count=1, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<a href="packages\.html" class="bg-brand-dark text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-900 border border-transparent hover:border-gray-700 flex items-center justify-center">\s*View Service Packages\s*</a>',
        r'<a :href="pageData.about_us.journey.btn2_link" class="bg-brand-dark text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl hover:bg-gray-900 border border-transparent hover:border-gray-700 flex items-center justify-center" x-text="pageData.about_us.journey.btn2_text"></a>',
        content, count=1, flags=re.DOTALL
    )

    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Patched Pledge and Journey in about-us.html")

patch_frontend_sections_3()
