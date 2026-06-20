import re

def fix():
    with open('about-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the explicitly escaped quotes
    content = content.replace(r"\'", "'")
    
    with open('about-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix()
