import re
import json

def patch_admin():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to insert our new editing blocks into the contact_us section of admin-cms.html
    # First, find the end of the Contact Info section.
    marker = r'<div><label class="text-xs font-bold text-gray-700 uppercase">Mailing Address</label><textarea x-model="pageData.contact_us.info.address" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>\s*</div>\s*</div>'
    
    new_blocks = """
                            <!-- Customer & Affiliate Links -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Helpful Links & Portals
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Customer Portal URL</label><input type="text" x-model="pageData.contact_us.portals.customer" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Affiliate Portal URL</label><input type="text" x-model="pageData.contact_us.portals.affiliate" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                </div>
                            </div>

                            <!-- Service Provider Help -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Service Provider Help
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.contact_us.service_provider.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description Top</label><textarea x-model="pageData.contact_us.service_provider.desc1" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description Middle</label><input type="text" x-model="pageData.contact_us.service_provider.desc2" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    
                                    <div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Bullet Points</label>
                                        <template x-for="(item, index) in pageData.contact_us.service_provider.list" :key="index">
                                            <div class="flex space-x-2 mb-2">
                                                <input type="text" x-model="pageData.contact_us.service_provider.list[index]" class="w-full px-3 py-2 border rounded">
                                                <button @click="pageData.contact_us.service_provider.list.splice(index, 1)" class="text-red-500 px-2"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <button @click="if(!pageData.contact_us.service_provider.list) pageData.contact_us.service_provider.list = []; pageData.contact_us.service_provider.list.push('')" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Detail</button>
                                    </div>
                                    
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description Bottom</label><textarea x-model="pageData.contact_us.service_provider.desc3" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.contact_us.service_provider.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.contact_us.service_provider.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Bottom Notices -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Bottom Text
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Main Footer Text</label><textarea x-model="pageData.contact_us.bottom_text" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                </div>
                            </div>
"""
    match = re.search(marker, content)
    if match:
        content = content[:match.end()] + "\n" + new_blocks + content[match.end():]
        print("Patched admin panels!")

    # Extend json data initialization
    data_match = re.search(r'(contact_us: \{[^}]*hero: \{.*?\},[^}]*info: \{.*?\})(\s*\})', content, re.DOTALL)
    if data_match:
        new_data = """,
                        portals: {
                            customer: 'https://payyourselffirst.benefithub.com/welcome/',
                            affiliate: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login'
                        },
                        service_provider: {
                            headline: 'Need Help With A <span class=\"text-brand-primary\">Service Provider?</span>',
                            desc1: 'Some PYF plans include services delivered by licensed professionals through third-party partner networks.',
                            desc2: 'If you need assistance with:',
                            list: [
                                'Finding a participating provider',
                                'Scheduling an appointment',
                                'Provider-specific questions',
                                'Service quality concerns'
                            ],
                            desc3: 'Please contact us using the form above, and we\\'ll help coordinate with the appropriate provider network.',
                            image: 'Contact-us/Contact Us_Need help with a service provider.jpg'
                        },
                        bottom_text: 'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.'
        """
        content = content[:data_match.end(1)] + new_data + content[data_match.end(1):]
        print("Patched admin data initializations!")
        
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)

def patch_frontend():
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Portals
    customer_pattern = r'<a href="https://payyourselffirst\.benefithub\.com/welcome/".*?Customer Portal Login\s*</a>'
    new_customer = r'<a :href="pageData.contact_us.portals ? pageData.contact_us.portals.customer : \'https://payyourselffirst.benefithub.com/welcome/\'" class="bg-[#66b510] hover:bg-[#4a8a0a] text-white font-bold py-4 px-8 rounded shadow text-sm uppercase text-center transition">Customer Portal Login</a>'
    content = re.sub(customer_pattern, new_customer, content, flags=re.DOTALL)

    affiliate_pattern = r'<a href="https://backoffice\.pyfaffiliates\.com/merchants/login\.php#login\s*"\s*target="_blank".*?Affiliate Portal Login\s*</a>'
    new_affiliate = r'<a :href="pageData.contact_us.portals ? pageData.contact_us.portals.affiliate : \'https://backoffice.pyfaffiliates.com/merchants/login.php#login\'" target="_blank" class="bg-[#66b510] hover:bg-[#4a8a0a] text-white font-bold py-4 px-8 rounded shadow text-sm uppercase text-center transition">Affiliate Portal Login</a>'
    content = re.sub(affiliate_pattern, new_affiliate, content, flags=re.DOTALL)

    # Service Provider Help
    headline_pattern = r'<h2 class="text-3xl font-extrabold text-center text-brand-dark uppercase mb-16">\s*Need Help With A <span class="text-brand-primary">Service Provider\?</span>\s*</h2>'
    new_headline = r'<h2 class="text-3xl font-extrabold text-center text-brand-dark uppercase mb-16" x-html="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.headline : \'Need Help With A <span class=\\\'text-brand-primary\\\'>Service Provider?</span>\'"></h2>'
    content = re.sub(headline_pattern, new_headline, content)

    desc1_pattern = r'<p class="text-gray-700 mb-6 font-medium">\s*Some PYF plans include services delivered by licensed professionals through third-party partner networks\.\s*</p>'
    new_desc1 = r'<p class="text-gray-700 mb-6 font-medium" x-text="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.desc1 : \'Some PYF plans include services delivered by licensed professionals through third-party partner networks.\'"></p>'
    content = re.sub(desc1_pattern, new_desc1, content)
    
    desc2_pattern = r'<p class="text-gray-700 mb-4 font-medium">\s*If you need assistance with:\s*</p>'
    new_desc2 = r'<p class="text-gray-700 mb-4 font-medium" x-text="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.desc2 : \'If you need assistance with:\'"></p>'
    content = re.sub(desc2_pattern, new_desc2, content)

    list_pattern = r'<ul class="space-y-3 mb-8">.*?</ul>'
    new_list = r'''<ul class="space-y-3 mb-8">
                            <template x-for="item in (pageData.contact_us.service_provider ? pageData.contact_us.service_provider.list : ['Finding a participating provider', 'Scheduling an appointment', 'Provider-specific questions', 'Service quality concerns'])">
                                <li class="flex items-center text-gray-900 font-bold">
                                    <i class="fas fa-circle text-[#1c4a00] text-[10px] mr-3"></i> <span x-text="item"></span>
                                </li>
                            </template>
                        </ul>'''
    content = re.sub(list_pattern, new_list, content, flags=re.DOTALL)

    desc3_pattern = r'<p class="text-gray-700 mb-8 font-medium">\s*Please contact us using the form above, and we\'ll help coordinate with the appropriate provider network\.\s*</p>'
    new_desc3 = r'<p class="text-gray-700 mb-8 font-medium" x-text="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.desc3 : \'Please contact us using the form above, and we\\\'ll help coordinate with the appropriate provider network.\'"></p>'
    content = re.sub(desc3_pattern, new_desc3, content)

    image_pattern = r'<img src="Contact-us/Contact Us_Need help with a service provider\.jpg"\s*alt="Service Provider Help"\s*class="rounded-\[2rem\] shadow-xl w-full h-full object-cover">'
    new_image = r'<img :src="pageData.contact_us.service_provider ? pageData.contact_us.service_provider.image : \'Contact-us/Contact Us_Need help with a service provider.jpg\'" alt="Service Provider Help" class="rounded-[2rem] shadow-xl w-full h-full object-cover">'
    content = re.sub(image_pattern, new_image, content)

    # Bottom Text
    bottom_text_pattern = r'<h2 class="text-2xl font-bold text-brand-dark leading-relaxed">\s*We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible\. If you need help, don’t hesitate to reach out\.\s*</h2>'
    new_bottom_text = r'<h2 class="text-2xl font-bold text-brand-dark leading-relaxed" x-text="pageData.contact_us.bottom_text || \'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.\'"></h2>'
    content = re.sub(bottom_text_pattern, new_bottom_text, content)

    # Need to update alpine payload inside contact-us.html as well!
    data_match = re.search(r'(contact_us: \{[^}]*hero: \{.*?\},[^}]*info: \{.*?\})(\s*\})', content, re.DOTALL)
    if data_match:
        new_data = """,
                        portals: {
                            customer: 'https://payyourselffirst.benefithub.com/welcome/',
                            affiliate: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login'
                        },
                        service_provider: {
                            headline: 'Need Help With A <span class=\"text-brand-primary\">Service Provider?</span>',
                            desc1: 'Some PYF plans include services delivered by licensed professionals through third-party partner networks.',
                            desc2: 'If you need assistance with:',
                            list: [
                                'Finding a participating provider',
                                'Scheduling an appointment',
                                'Provider-specific questions',
                                'Service quality concerns'
                            ],
                            desc3: 'Please contact us using the form above, and we\\'ll help coordinate with the appropriate provider network.',
                            image: 'Contact-us/Contact Us_Need help with a service provider.jpg'
                        },
                        bottom_text: 'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.'
        """
        content = content[:data_match.end(1)] + new_data + content[data_match.end(1):]
        print("Patched frontend data initializations!")

    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    patch_admin()
    patch_frontend()
