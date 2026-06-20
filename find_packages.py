import re

with open('admin-cms.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'activePage === \'packages\'' in line:
        print(f"Packages Editor starts around line {i}")
        break
