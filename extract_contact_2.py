import re
html = open('admin-cms.html', 'r', encoding='utf-8').read()
match = re.search(r'(<div\s+x-show="activePage === \'contact_us\'" x-cloak>.*?</form>\s*</div>\s*</div>)', html, re.DOTALL)
if not match:
    match = re.search(r'(<div\s+x-show="activePage === \'contact_us\'" x-cloak>.*?(?:<!-- START OF|</div>\s*</div>\s*<!--))', html, re.DOTALL)
if match:
    print(match.group(1)[:1000])
else:
    print("contact_us html block not found")

# full pageData.contact_us
data_match = re.search(r'contact_us:\s*{(.+?)}', html, re.DOTALL)
if data_match:
    print("\n--- pageData.contact_us ---")
    print(data_match.group(0)[:1500])
