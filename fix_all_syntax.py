import re

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the address block in pageData (single quotes with physical newlines)
    # We look for address: '...' spanning multiple lines
    addr_pattern = r"(address:\s*')([^']*?Pay Yourself First[^']*?)(')"
    def replace_newlines(match):
        return match.group(1) + match.group(2).replace('\n', '\\n') + match.group(3)
    
    content = re.sub(addr_pattern, replace_newlines, content, flags=re.DOTALL)
    
    # Fix the desc block if it has physical newlines
    desc_pattern = r"(desc:\s*')([^']*?Whether you have questions[^']*?)(')"
    content = re.sub(desc_pattern, replace_newlines, content, flags=re.DOTALL)

    # Also check contact_us.hero.desc
    hero_desc_pattern = r"(desc:\s*\")([^\"]*?Whether you have questions[^\"]*?)(\")"
    def replace_newlines_double(match):
        return match.group(1) + match.group(2).replace('\n', '\\n') + match.group(3)
    content = re.sub(hero_desc_pattern, replace_newlines_double, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filename}")

fix_file('admin-cms.html')
fix_file('contact-us.html')
