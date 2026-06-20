html = open('admin.html', 'r', encoding='utf-8').read()

# 1. Check Contact Us editor section  
idx = html.find("<!-- Contact Us Editor -->")
if idx != -1:
    print("=== Contact Us Editor section (first 1500 chars) ===")
    print(html[idx:idx+1500])
else:
    # Try finding by x-show
    idx2 = html.find("activePage === 'contact_us'")
    if idx2 != -1:
        print("=== Contact Us section (via x-show) ===")
        print(html[max(0, idx2-100):idx2+1500])
    else:
        print("ERROR: Contact Us section NOT found in admin.html!")

print("\n\n=== saveDraft function ===")
idx3 = html.find("async saveDraft(")
if idx3 != -1:
    print(html[idx3:idx3+600])
else:
    print("saveDraft NOT found!")
    
print("\n\n=== uploadImageTo function ===")
idx4 = html.find("async uploadImageTo(")
if idx4 != -1:
    print(html[idx4:idx4+600])
else:
    print("uploadImageTo NOT found!")
    
print("\n\n=== Global save/publish buttons ===")
idx5 = html.find("Save Draft")
if idx5 != -1:
    print(html[max(0, idx5-200):idx5+200])
