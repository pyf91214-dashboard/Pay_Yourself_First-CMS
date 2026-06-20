import re
with open('admin-cms.html', 'r', encoding='utf-8') as f:
    content = f.read()

s = content.find("activePage === 'home'")
e = content.find("activePage === 'how_we_help_you'")
sec = content[s:e]

# Let's count divs line by line
lines = sec.split('\n')
depth = 0
for i, line in enumerate(lines):
    op = len(re.findall(r'<div\b', line))
    cl = len(re.findall(r'</div\b', line))
    depth += (op - cl)
    if depth < 0:
        print(f"Extra closing div on relative line {i}: {line}")
        depth = 0 # reset to keep tracing

print("Done")
