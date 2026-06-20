import re
html = open('admin-cms.html', 'r', encoding='utf-8').read()
match = re.search(r'(<div\s+x-show="activePage === \'contact_us\'" x-cloak>.*?</form>\s*</div>\s*</div>)', html, re.DOTALL)
if match:
    # Print the entire structure inside the form
    print(match.group(1))
else:
    match2 = re.search(r'(<div\s+x-show="activePage === \'contact_us\'" x-cloak>.*?)(?:<!-- START OF|<div class="text-center mt-8">)', html, re.DOTALL)
    if match2:
        print(match2.group(1))
