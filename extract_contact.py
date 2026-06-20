import re
html = open('admin-cms.html', 'r', encoding='utf-8').read()
match = re.search(r'(<div\s+x-show="activePage === \'contact_us\'.*?</div>\s*<!--\s*END\s*|\s*<div\s+x-show="activePage === \'(?:business|about_us)\')', html, re.DOTALL)
if match:
    # Just checking a chunk
    print(html[max(0, match.start() - 50):match.end() + 100][:1500])
else:
    print("Could not extract block")

# Let's also check the pageData structure for contact_us
data_match = re.search(r'contact_us:\s*{(.*?)}', html, re.DOTALL)
if data_match:
    print("\n--- pageData.contact_us ---")
    print(data_match.group(0)[:1500])
