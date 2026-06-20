html = open('admin.html', 'r', encoding='utf-8').read()

# Find all occurrences of 'Editing: How We Help You' and surrounding context
import re
matches = [(m.start(), m.group()) for m in re.finditer(r'Editing: How We Help You', html)]
print(f"Found {len(matches)} occurrences of 'Editing: How We Help You'")
for start, _ in matches:
    print('---')
    print(html[max(0, start-300):start+200])

# Find all occurrences of 'Editing: Contact Us' too
matches2 = [(m.start(), m.group()) for m in re.finditer(r'Editing: Contact Us', html)]
print(f"\nFound {len(matches2)} occurrences of 'Editing: Contact Us'")
