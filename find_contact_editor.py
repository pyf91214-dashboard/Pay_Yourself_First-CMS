html = open('admin-cms.html', 'r', encoding='utf-8').read()
# Find contact_us editor section and print it
idx = html.find("<!-- Contact Us Editor -->")
if idx != -1:
    print(html[idx:idx+5000])
else:
    print("NOT FOUND. Looking for activePage === 'contact_us'...")
    idx2 = html.find("activePage === 'contact_us'")
    if idx2 != -1:
        print(html[max(0, idx2-200):idx2+5000])
    else:
        print("ALSO NOT FOUND")
