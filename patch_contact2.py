import re

def apply_patch():
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Email
    content = re.sub(
        r'Email address:\s*<a href="mailto:[^"]*" class="hover:text-brand-primary">[^<]*</a>',
        r'Email address: <a :href="\'mailto:\' + (pageData.contact_us.info ? pageData.contact_us.info.email : \'service@payyourselffirst.com\')" class="hover:text-brand-primary" x-text="pageData.contact_us.info ? pageData.contact_us.info.email : \'service@payyourselffirst.com\'">service@payyourselffirst.com</a>',
        content
    )
    
    # Address
    addr_pattern = r'<p class="text-lg font-medium leading-relaxed">\s*Pay Yourself First<br>\s*107 S\. West Street, Suite 557<br>\s*Alexandria, VA 22314<br>\s*Correspondence Only\s*</p>'
    new_addr = r'<p class="text-lg font-medium leading-relaxed whitespace-pre-line" x-html="pageData.contact_us.info ? pageData.contact_us.info.address : \'Pay Yourself First<br>107 S. West Street, Suite 557<br>Alexandria, VA 22314<br>Correspondence Only\'"></p>'
    content = re.sub(addr_pattern, new_addr, content)

    # Let's also update the Alpine init to include the info default values so it renders properly when loaded or if previewed
    info_block = """                        info: {
                            email: "service@payyourselffirst.com",
                            phone: "1-800-123-4567",
                            address: "Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only"
                        }"""
    if "info: {" not in content:
        content = content.replace('image: "Contact-us/Contact Us_Hero.jpg"\n                        }', 'image: "Contact-us/Contact Us_Hero.jpg"\n                        },\n' + info_block)
        
    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    apply_patch()
    print("contact-us.html info block patched successfully.")
