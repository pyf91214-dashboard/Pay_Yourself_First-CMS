import re

def patch_admin_js():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('about_data.json', 'r', encoding='utf-8') as f:
        about_data_str = f.read()
        
    pattern = r'about_us:\s*\{.*?\},\s*contact_us:'
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if not match:
        print("Could not find about_us: { ... } in JS")
        return
        
    replacement = f"about_us: {about_data_str},\n                  contact_us:"
    
    new_content = content[:match.start()] + replacement + content[match.end():]
    
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Patched script object in admin-cms.html")

patch_admin_js()
