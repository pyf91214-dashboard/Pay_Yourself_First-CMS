html = open('admin.html', 'r', encoding='utf-8').read()

# Find all occurrences of 'Editing:' to see what pages have that header style
import re
matches = [(m.start(), m.group(0)) for m in re.finditer(r'Editing: \w[\w ]+', html)]
print(f"Found {len(matches)} 'Editing:' occurrences:")
for start, match in matches:
    context = html[max(0, start-200):start+300]
    print(f"\n=== {match} ===")
    print(context)
