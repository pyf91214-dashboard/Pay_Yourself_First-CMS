import re

def fix_slashes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find attributes starting with x-text, x-html, :src, :href that have \' inside their double quotes.
    # The simplest way is to find \\' and just replace it with ' everywhere outside of <script> blocks.
    # Wait, inside <script> blocks, \\' is also bad unless it's in a double quoted string but usually we use \'
    # Actually, the string literal in HTML we wrote was literally \' (backslash quote).
    # Since HTML uses " to wrap the attribute, we can just use regular single quotes.
    # So \' should just be ' inside the HTML attributes.
    
    # We will replace all `\'` with `'` in the whole file EXCEPT inside <script>...</script>
    
    parts = re.split(r'(<script.*?>.*?</script>)', html, flags=re.DOTALL | re.IGNORECASE)
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace("\\'", "'")
    
    new_html = "".join(parts)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Fixed quotes in {file_path}")

try:
    fix_slashes('contact-us.html')
except Exception as e:
    print(e)
    
try:
    fix_slashes('admin-cms.html')
except Exception as e:
    print(e)
    
try:
    fix_slashes('admin.html')
except Exception as e:
    print(e)
