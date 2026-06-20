import re

def fix_response_time():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Mailing Address text area
    marker = r'<div><label class="text-xs font-bold text-gray-700 uppercase">Mailing Address</label><textarea x-model="pageData\.contact_us\.info\.address" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>'
    
    # Check if we already injected response_time
    if 'pageData.contact_us.info.response_time' not in content:
        new_inputs = """
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Expected Response Time</label><input type="text" x-model="pageData.contact_us.info.response_time" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Support Hours</label><input type="text" x-model="pageData.contact_us.info.support_hours" class="w-full px-3 py-2 border rounded mt-1"></div>
        """
        match = re.search(marker, content)
        if match:
            content = content[:match.end()] + new_inputs + content[match.end():]
            print("Patched admin-cms.html with response time & hours editors!")
            
    # Add to default JSON
    if 'response_time: "1-2 business days"' not in content:
        content = content.replace(
            "address: 'Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only'\n                        },",
            "address: 'Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only',\n                            response_time: '1-2 business days',\n                            support_hours: '9am - 5pm ET'\n                        },"
        )
        print("Patched admin default JSON info block!")

    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the text nodes.
    rt_pattern = r'<p class="text-sm font-bold text-gray-900">\s*Expected response time: 1-2 business days\s*</p>'
    new_rt = r'<p class="text-sm font-bold text-gray-900" x-text="\'Expected response time: \' + (pageData.contact_us.info.response_time || \'1-2 business days\')">Expected response time: 1-2 business days</p>'
    content = re.sub(rt_pattern, new_rt, content)
    
    sh_pattern = r'<p class="text-sm font-bold text-gray-900">\s*Support hours: 9am - 5pm ET\s*</p>'
    new_sh = r'<p class="text-sm font-bold text-gray-900" x-text="\'Support hours: \' + (pageData.contact_us.info.support_hours || \'9am - 5pm ET\')">Support hours: 9am - 5pm ET</p>'
    content = re.sub(sh_pattern, new_sh, content)

    # Add to default script JSON
    if 'response_time: "1-2 business days"' not in content:
        content = content.replace(
            "address: \"Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only\"\n                        },",
            "address: \"Pay Yourself First\\n107 S. West Street, Suite 557\\nAlexandria, VA 22314\\nCorrespondence Only\",\n                            response_time: \"1-2 business days\",\n                            support_hours: \"9am - 5pm ET\"\n                        },"
        )

    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_response_time()
