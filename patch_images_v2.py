import re

with open('how-we-help-you.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix hero image
content = re.sub(
    r'<img src="How-we-help-you/How we help you_hero image\.jpg"',
    r'<img :src="pageData.hero.image || \'How-we-help-you/How we help you_hero image.jpg\'"',
    content
)

# 2. Fix why exists image
content = re.sub(
    r'<img src="How-we-help-you/Why PYF Exists\.jpg"',
    r'<img :src="pageData.why_exists.image || \'How-we-help-you/Why PYF Exists.jpg\'"',
    content
)

# 3. Fix problems 1 image
content = re.sub(
    r'<img src="How-we-help-you/Problems most people face_1\.jpg"',
    r'<img :src="pageData.problems.block1.image || \'How-we-help-you/Problems most people face_1.jpg\'"',
    content
)

# 4. Fix problems 2 image  
content = re.sub(
    r'<img src="How-we-help-you/Problems most people face_2\.jpg"',
    r'<img :src="pageData.problems.block2.image || \'How-we-help-you/Problems most people face_2.jpg\'"',
    content
)

# 5. Fix why works image
content = re.sub(
    r'<img src="How-we-help-you/Why PYF Works\.jpg"',
    r'<img :src="pageData.why_works.image || \'How-we-help-you/Why PYF Works.jpg\'"',
    content
)

# Clean up dual image if exists
content = content.replace(
"""                        btn2_link: 'packages.html',
                        image: 'How-we-help-you/How we help you_hero image.jpg',
                        image: 'How-we-help-you/How we help you_hero image.jpg'
                    },""",
"""                        btn2_link: 'packages.html',
                        image: 'How-we-help-you/How we help you_hero image.jpg'
                    },"""
)

if "'How-we-help-you/Why PYF Works.jpg'" not in content:
    content = re.sub(
        r"(subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward — whether you want to earn more, keep more, or spend less.')\n\s*},",
        r"\1,\n                        image: 'How-we-help-you/Why PYF Works.jpg'\n                    },",
        content
    )

with open('how-we-help-you.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("regex replace complete")
