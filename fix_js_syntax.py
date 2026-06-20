import re

def fix():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the problematic contact_us block with the physical newline
    # Replace physical newline with literal string '\n'
    # And make sure single quotes inside don't break string.
    
    # Let's just fix the exact string:
    bad_str = "desc: 'Whether you have questions about our services, need support, or want to\nexplore business partnerships, we\\'re here to help.'"
    good_str = "desc: 'Whether you have questions about our services, need support, or want to\\nexplore business partnerships, we\\'re here to help.'"
    
    content = content.replace(bad_str, good_str)
    
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed admin-cms.html.")

if __name__ == '__main__':
    fix()
