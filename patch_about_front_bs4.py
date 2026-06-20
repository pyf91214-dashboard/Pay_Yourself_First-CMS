import bs4
import re

def patch_frontend_bs4():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')

    # Hero
    h1 = soup.find('h1', string=re.compile("Here To Help", re.I))
    if h1: h1['x-html'] = "pageData.about_us.hero.headline"
    
    p = soup.find('p', string=re.compile("Pay Yourself First was created to make financial stability accessible", re.I))
    if p: p['x-text'] = "pageData.about_us.hero.desc"
    
    img_hero = soup.find('img', src=re.compile('Hero\.jpg', re.I))
    if img_hero: img_hero[':src'] = "pageData.about_us.hero.image || 'About-us/About Us_Hero.jpg'"
    
    # Who We Are
    h2_who = soup.find('h2', string=re.compile("Who", re.I)) # Actually string match fails if there's span
    # We can search by containing text
    for h2 in soup.find_all('h2'):
        if "Who" in h2.text and "We Are" in h2.text:
            h2['x-html'] = "pageData.about_us.who_we_are.headline"
            h2.clear()
        if "Our" in h2.text and "Origin" in h2.text:
            h2['x-html'] = "pageData.about_us.origin.headline"
            h2.clear()
        if "Our" in h2.text and "Mission" in h2.text:
            h2['x-html'] = "pageData.about_us.mission.headline"
            h2.clear()
        if "Serving" in h2.text and "Everyday" in h2.text:
            h2['x-html'] = "pageData.about_us.serving.headline"
            h2.clear()
        if "A system" in h2.text and "personality" in h2.text:
            h2['x-html'] = "pageData.about_us.system.headline"
            h2.clear()
        if "Who We" in h2.text and "Serve" in h2.text:
            # Need to avoid "Who We Are", "Serving..."
            if "Serve" in h2.text and "We" in h2.text and "Who" in h2.text:
                h2['x-html'] = "pageData.about_us.who_we_serve.headline"
                h2.clear()
        if "PYF Different" in h2.text:
            h2['x-html'] = "pageData.about_us.different.headline"
            h2.clear()
        if "Pledge" in h2.text:
            h2['x-html'] = "pageData.about_us.pledge.headline"
            h2.clear()
        if "Start Your PYF Journey" in h2.text:
            h2['x-text'] = "pageData.about_us.journey.headline"
            h2.clear()

    # Images
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if "Who We Are" in src: img[':src'] = "pageData.about_us.who_we_are.image || 'About-us/About Us_Who We Are.jpg'"
        elif "Origin" in src: img[':src'] = "pageData.about_us.origin.image || 'About-us/About Us_Our Origin.jpg'"
        elif "Mission" in src: img[':src'] = "pageData.about_us.mission.image || 'About-us/About Us_Our Mission.jpg'"
        elif "Serving" in src: img[':src'] = "pageData.about_us.serving.image || 'About-us/About Us_Serving Everyday Americans.jpg'"
        elif "Who We Serve" in src: img[':src'] = "pageData.about_us.who_we_serve.image || 'About-us/About Us_Who We Serve.jpg'"
        elif "Different" in src: img[':src'] = "pageData.about_us.different.image || 'About-us/About Us_What Makes PYF Different.jpg'"
        elif "Our Commitment" in src: img[':src'] = "pageData.about_us.pledge.image || 'About-us/About Us_Built For Real Life_Our Commitment.jpg'"

    # Paragraphs map
    for p in soup.find_all('p'):
        text = p.text.strip()
        if "Pay Yourself First (PYF) is a financial empowerment company built on a" in text:
            p['x-html'] = "pageData.about_us.who_we_are.desc1"
            p.string = ""
        elif "As the cost of living rises" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc2"
            p.string = ""
        elif "PYF was created to solve these problems by" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc3"
            p.string = ""
        elif "Our company is built around a system" in text:
            p['x-text'] = "pageData.about_us.who_we_are.desc4"
            p.string = ""
        elif "PYF was built by financial professionals with decades" in text:
            p['x-text'] = "pageData.about_us.origin.desc1"
            p.string = ""
        elif "The team behind PYF recognized a gap" in text:
            p['x-text'] = "pageData.about_us.origin.desc2"
            p.string = ""
        elif "To help everyday people gain control" in text:
            p['x-text'] = "pageData.about_us.mission.desc"
            p.string = ""
        elif "Financial control comes from mastering three critical levers" in text:
            p['x-text'] = "pageData.about_us.system.subtitle"
            p.string = ""
        elif "If financial improvement is your goal" in text:
            p['x-text'] = "pageData.about_us.who_we_serve.footer"
            p.string = ""
        elif "Choose the path that fits your goals today" in text:
            p['x-text'] = "pageData.about_us.journey.desc"
            p.string = ""

    # Origin bottom headline
    h3_origin = soup.find('h3', string=re.compile("fill that gap"))
    if h3_origin: 
        h3_origin['x-html'] = "pageData.about_us.origin.headline_bottom"
        h3_origin.clear()

    # Mission subtitle
    h3_mission = soup.find('h3', string=re.compile("Our mission is simple"))
    if h3_mission:
        h3_mission['x-text'] = "pageData.about_us.mission.subtitle"
        h3_mission.string = ""

    # Journey buttons
    for a in soup.find_all('a'):
        text = a.text.strip()
        if "BECOME AN AFFILIATE" in text:
            a[':href'] = "pageData.about_us.journey.btn1_link"
            a['x-text'] = "pageData.about_us.journey.btn1_text"
            a.string = ""
        elif "View Service Packages" in text:
            a[':href'] = "pageData.about_us.journey.btn2_link"
            a['x-text'] = "pageData.about_us.journey.btn2_text"
            a.string = ""

    with open('about-us-patched.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Parsed and updated basic bindings")

patch_frontend_bs4()
