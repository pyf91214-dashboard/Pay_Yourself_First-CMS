import re

def rewrite_about_us():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We will perform exact string replacements where possible, and use minimal regex.

    # 1. Who We Are List
    list1_start = content.find('<ul class="space-y-4 mb-10">')
    list1_end = content.find('</ul>', list1_start) + 5
    if list1_start != -1 and 'Who We Are' in content[:list1_start][-500:]:
        content = content[:list1_start] + """<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                                    <span class="text-gray-700 text-lg leading-relaxed" x-text="item"></span>
                                </li>
                            </template>
                        </ul>""" + content[list1_end:]

    # 2. Origin List
    # We find the next ul after origin
    origin_header_pos = content.find('Our Origin')
    if origin_header_pos != -1:
        list2_start = content.find('<ul class="space-y-4 mb-10">', origin_header_pos)
        list2_end = content.find('</ul>', list2_start) + 5
        if list2_start != -1:
            content = content[:list2_start] + """<ul class="space-y-4 mb-10">
                                <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                                    <li class="flex items-start">
                                        <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                                        <span class="text-gray-700 font-medium" x-html="item"></span>
                                    </li>
                                </template>
                            </ul>""" + content[list2_end:]

    # Who We Serve List
    serve_header = content.find('Who We <span class="text-brand-primary">Serve</span>')
    if serve_header != -1:
        list3_start = content.find('<ul class="space-y-4 mb-12">', serve_header)
        if list3_start != -1:
            list3_end = content.find('</ul>', list3_start) + 5
            content = content[:list3_start] + """<ul class="space-y-4 mb-12">
                            <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>""" + content[list3_end:]
                        
    # What Makes PYF Different List
    diff_header = content.find('What Makes <span class="text-brand-primary">PYF Different</span>')
    if diff_header != -1:
        list4_start = content.find('<ul class="space-y-4 mb-10">', diff_header)
        if list4_start != -1:
            list4_end = content.find('</ul>', list4_start) + 5
            content = content[:list4_start] + """<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>""" + content[list4_end:]
                        
    # Our Pledge List
    pledge_header = content.find('Our <span class="text-brand-primary">Pledge To Help You</span>')
    if pledge_header != -1:
        list5_start = content.find('<ul class="space-y-4 mb-10">', pledge_header)
        if list5_start != -1:
            list5_end = content.find('</ul>', list5_start) + 5
            content = content[:list5_start] + """<ul class="space-y-4 mb-10">
                            <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                                <li class="flex items-start">
                                    <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                                    <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                                </li>
                            </template>
                        </ul>""" + content[list5_end:]
                        
    # NOW WE DO BS4 for the rest (headers, paragraphs, images)
    import bs4
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # Re-apply text bindings safely!
    def safe_set(tag, attrs):
        if tag:
            for k,v in attrs.items(): tag[k] = v

    h1 = soup.find('h1', string=re.compile("Here To Help", re.I))
    if h1: 
        h1['x-html'] = "pageData.about_us.hero.headline"
        h1.string = ''

    p = soup.find('p', string=re.compile("Pay Yourself First was created to make financial stability accessible", re.I))
    if p: 
        p['x-text'] = "pageData.about_us.hero.desc"
        p.string = ''
        
    for h2 in soup.find_all('h2'):
        text = h2.text
        if "Who We Are" in text:
            h2['x-html'] = "pageData.about_us.who_we_are.headline"
            h2.string = ""
        elif "Our Origin" in text:
            h2['x-html'] = "pageData.about_us.origin.headline"
            h2.string = ""
        elif "Our Mission" in text:
            h2['x-html'] = "pageData.about_us.mission.headline"
            h2.string = ""
        elif "Serving Everyday" in text:
            h2['x-html'] = "pageData.about_us.serving.headline"
            h2.string = ""
        elif "system, not a personality" in text:
            h2['x-html'] = "pageData.about_us.system.headline"
            h2.string = ""
        elif "Who We Serve" in text:
            h2['x-html'] = "pageData.about_us.who_we_serve.headline"
            h2.string = ""
        elif "PYF Different" in text:
            h2['x-html'] = "pageData.about_us.different.headline"
            h2.string = ""
        elif "Pledge" in text:
            h2['x-html'] = "pageData.about_us.pledge.headline"
            h2.string = ""
        elif "Start Your PYF Journey" in text:
            h2['x-text'] = "pageData.about_us.journey.headline"
            h2.string = ""

    for p in soup.find_all('p'):
        text = p.text.strip()
        if "Pay Yourself First (PYF) is a financial empowerment company built on a" in text:
            p['x-html'] = "pageData.about_us.who_we_are.desc1"
            p.string = ""
        elif "As the cost of living rises" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc2"
            p.string = ""
        elif "PYF was created to solve these problems by giving" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc3"
            p.string = ""
        elif "Our company is built around a system" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc4"
            p.string = ""
        elif "PYF was built by financial professionals with decades" in text:
            p['x-text'] = "pageData.about_us.origin.desc1"
            p.string = ""
        elif "The team behind PYF recognized a gap:" in text:
            p['x-text'] = "pageData.about_us.origin.desc2"
            p.string = ""
        elif "To help everyday people gain control" in text:
            p['x-text'] = "pageData.about_us.mission.desc"
            p.string = ""
        elif "Financial control comes from mastering" in text:
            p['x-text'] = "pageData.about_us.system.subtitle"
            p.string = ""
        elif "If financial improvement is your goal" in text:
            p['x-text'] = "pageData.about_us.who_we_serve.footer"
            p.string = ""
        elif "Choose the path that fits" in text:
            p['x-text'] = "pageData.about_us.journey.desc"
            p.string = ""
            
    # Bottom headlines
    h3_origin = soup.find('h3', string=re.compile("fill that gap", re.I))
    if h3_origin:
        h3_origin['x-html'] = "pageData.about_us.origin.headline_bottom"
        h3_origin.string = ""
        
    h3_mission = soup.find('h3', string=re.compile("Our mission is simple", re.I))
    if h3_mission:
        h3_mission['x-text'] = "pageData.about_us.mission.subtitle"
        h3_mission.string = ""

    # Journey Buttons
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

    # Finally, write the output
    final_output = str(soup)
    
    # We must format Alpine templates correctly without bs4 encoding
    final_output = final_output.replace('&lt;template', '<template').replace('&lt;/template', '</template')

    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(final_output)

    print("Re-wrote about-us.html completely!")

rewrite_about_us()
