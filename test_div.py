import re
with open('admin-cms.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Splitting by main sections
sections = ['home', 'how_we_help_you', 'packages', 'tax', 'support', 'about_us', 'contact_us', 'business']

for i in range(len(sections) - 1):
    sec = sections[i]
    next_sec = sections[i+1]
    
    start_str = f'<div x-show="activePage === \'{sec}\'"'
    end_str = f'<div x-show="activePage === \'{next_sec}\'"'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Could not find {sec} to {next_sec}")
        continue
        
    sec_content = content[start_idx:end_idx]
    
    o = len(re.findall(r'<div\b', sec_content))
    c = len(re.findall(r'</div\b', sec_content))
    diff = o - c
    print(f'Section {sec}: Open={o}, Close={c}, Diff={diff}')

# For the last one:
last_start = content.find(f'<div x-show="activePage === \'business\'"')
last_content = content[last_start:content.find('</div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </main>', last_start)]
o = len(re.findall(r'<div\b', last_content))
c = len(re.findall(r'</div\b', last_content))
print(f'Section business: Open={o}, Close={c}, Diff={o-c}')
