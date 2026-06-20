import re

with open('packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update hero image
content = re.sub(
    r'<img src="Plans-overview/Packages_Hero\.jpg"',
    r'<img :src="pageData.packages.hero.image || \'Plans-overview/Packages_Hero.jpg\'"',
    content
)

# 2. Update two paths image
content = re.sub(
    r'<img src="Plans-overview/Packages_Two Simple Paths\.jpg"',
    r'<img :src="pageData.packages.two_paths.image || \'Plans-overview/Packages_Two Simple Paths.jpg\'"',
    content
)

# 3. Update affiliate program image
content = re.sub(
    r'<img src="Plans-overview/Packages_Affiliate Program\.jpg"',
    r'<img :src="pageData.packages.affiliate_program.image || \'Plans-overview/Packages_Affiliate Program.jpg\'"',
    content
)

# 4. Add default image paths to pageData object in script
# Hero
content = content.replace(
    "btn2_link: 'affiliate-plan.html' },",
    "btn2_link: 'affiliate-plan.html', image: 'Plans-overview/Packages_Hero.jpg' },"
)

# Two Paths
content = content.replace(
    "btn2_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm' },",
    "btn2_link: 'https://backoffice.pyfaffiliates.com/affiliates/signup.php#SignupForm', image: 'Plans-overview/Packages_Two Simple Paths.jpg' },"
)

# Affiliate Program
content = content.replace(
    "btn_link: '#' },",
    "btn_link: '#', image: 'Plans-overview/Packages_Affiliate Program.jpg' },"
)

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("packages.html updated")
