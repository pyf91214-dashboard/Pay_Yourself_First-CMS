import re
import os

def find_js_errors(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = re.findall(r'<script.*?>([\s\S]*?)<\/script>', content, re.IGNORECASE)
    for i, script in enumerate(scripts):
        # Look for strings spanning across lines
        # This is a naive check: look for ' (quote) followed by text that doesn't close quote on the same line
        lines = script.split('\n')
        for j, line in enumerate(lines):
            # Check if there's an odd number of single quotes or double quotes on this line
            # (ignoring escaped quotes)
            s_quotes = len(re.findall(r"(?<!\\)'", line))
            d_quotes = len(re.findall(r'(?<!\\)"', line))
            
            # This is very rough, but might catch multi-line strings
            if s_quotes % 2 != 0:
                print(f"File {filename}, Script {i}, Line {j}: Potential unclosed single quote: {line.strip()}")
            if d_quotes % 2 != 0:
                print(f"File {filename}, Script {i}, Line {j}: Potential unclosed double quote: {line.strip()}")

print("Checking admin.html...")
find_js_errors('admin.html')
print("\nChecking contact-us.html...")
find_js_errors('contact-us.html')
print("\nChecking admin-cms.html...")
find_js_errors('admin-cms.html')
