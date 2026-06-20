import re
html = open('admin-cms.html', 'r', encoding='utf-8').read()
if "activePage === 'contact_us'" in html:
    print("contact_us panel exists in admin-cms.html")
else:
    print("contact_us panel does not exist in admin-cms.html")
