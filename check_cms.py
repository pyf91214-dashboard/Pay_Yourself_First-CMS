html = open('admin.html', 'r', encoding='utf-8').read()
print('CMS Alpine Script embedded:', '<!-- CMS Alpine Script -->' in html)
idx = html.find('x-data="cmsManager"')
print('CMS div with x-data=cmsManager:', idx != -1)
if idx != -1:
    print(html[max(0, idx-60):idx+200])
else:
    # Check if it's with parens
    idx2 = html.find('x-data="cmsManager()"')
    print('CMS div with x-data=cmsManager():', idx2 != -1)
    if idx2 != -1:
        print(html[max(0, idx2-60):idx2+200])
