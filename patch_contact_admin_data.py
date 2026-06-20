import re

def fix_admin_defaults():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the contact_us default json block in admin-cms.html
    # We will replace it fully up to the `info: { ... }` block
    
    old_contact_block = r'''contact_us:\s*\{\s*hero:\s*\{\s*headline:\s*\'Contact Us\',\s*desc:\s*\'We are here to help and answer any questions you might have\.\',\s*image:\s*\'Contact-Us/Hero\.jpg\'\s*\},.*?info:\s*\{\s*email:\s*\'support@payyourselffirst\.com\',\s*phone:\s*'1-800-123-4567',\s*address:\s*'123 Main St, City, ST 12345'\s*\}'''

    new_contact_block = """contact_us: {
                    hero: {
                        headline: 'Get In Touch With Us',
                        desc: 'Whether you have questions about our services, need support, or want to\\nexplore business partnerships, we\\'re here to help.',
                        image: 'Contact-us/Contact Us_Hero.jpg'
                    },
                    info: {
                        email: 'service@payyourselffirst.com',
                        phone: '1-800-123-4567',
                        address: 'Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only'
                    }"""
    
    content = re.sub(old_contact_block, new_contact_block, content, flags=re.DOTALL)

    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
if __name__ == '__main__':
    fix_admin_defaults()
