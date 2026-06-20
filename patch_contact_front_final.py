import re

def patch_contact_frontend():
    file = 'contact-us.html'
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Info phone
    # Search for Phone Number
    # <p class="text-gray-800 text-lg">1-800-123-4567</p>
    html = re.sub(
        r'<p class="text-gray-800 text-lg">1-800-123-4567</p>',
        r'<p class="text-gray-800 text-lg" x-text="pageData.contact_us.info ? pageData.contact_us.info.phone : \'1-800-123-4567\'"></p>',
        html
    )

    # 2. Service Provider Help headline/desc/list bindings
    # Headline
    html = re.sub(
        r'<h3 class="text-3xl font-extrabold text-brand-dark mb-6">Need Help With A <span class="text-brand-primary">Service Provider\?</span></h3>',
        r'<h3 class="text-3xl font-extrabold text-brand-dark mb-6" x-html="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.headline : \'Need Help With A <span class=\\\'text-brand-primary\\\'>Service Provider?</span>\'"></h3>',
        html
    )
    
    # Desc1
    html = re.sub(
        r'<p class="text-gray-700 text-lg mb-4 leading-relaxed">Some PYF plans include services delivered by licensed professionals through third-party partner networks\.</p>',
        r'<p class="text-gray-700 text-lg mb-4 leading-relaxed" x-text="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.desc1 : \'Some PYF plans include services delivered by licensed professionals through third-party partner networks.\'"></p>',
        html
    )
    
    # Desc2
    html = re.sub(
        r'<p class="text-gray-700 text-lg mb-4 font-semibold">If you need assistance with:</p>',
        r'<p class="text-gray-700 text-lg mb-4 font-semibold" x-text="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.desc2 : \'If you need assistance with:\'"></p>',
        html
    )
    
    # List - Replace the whole ul block
    old_list = r"""<ul class="list-disc list-inside text-gray-700 text-lg mb-8 space-y-2 ml-4">
                            <li>Finding a participating provider</li>
                            <li>Scheduling an appointment</li>
                            <li>Provider-specific questions</li>
                            <li>Service quality concerns</li>
                        </ul>"""
    new_list = """<ul class="list-disc list-inside text-gray-700 text-lg mb-8 space-y-2 ml-4">
                            <template x-for="(item, index) in (pageData.contact_us.service_provider ? pageData.contact_us.service_provider.list : ['Finding a participating provider', 'Scheduling an appointment', 'Provider-specific questions', 'Service quality concerns'])" :key="index">
                                <li x-text="item"></li>
                            </template>
                        </ul>"""
    if old_list in html:
        html = html.replace(old_list, new_list)
    elif "pageData.contact_us.service_provider.list" not in html:
        html = re.sub(r'<ul class="list-disc list-inside.*?</ul>', new_list, html, flags=re.DOTALL)

    # 3. bottom notices is already bound via `template x-for` 
    # Checked earlier: <template x-for="(notice, index) in (pageData.contact_us.bottom_notices || [{icon:...

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed contact-us.html")

patch_contact_frontend()
