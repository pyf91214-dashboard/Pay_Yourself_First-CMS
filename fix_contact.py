import re

def fix():
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix bindings backslashes
    content = content.replace(r"\'", "'")
    
    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix()
