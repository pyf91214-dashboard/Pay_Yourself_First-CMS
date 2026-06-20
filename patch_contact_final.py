import re

def patch_admin():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_blocks = """
                            <!-- Contact Form Settings -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Contact Us Form
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Form Submission URL (Action)</label><input type="text" x-model="pageData.contact_us.form_action" class="w-full px-3 py-2 border rounded mt-1"></div>
                                </div>
                            </div>
                            
                            <!-- Mailing Address Map Section -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Mailing Address Map
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Map Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.contact_us.map_image.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.contact_us.map_image.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Service Links Additions -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Service Links
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Link 1: Support/FAQ</label><input type="text" x-model="pageData.contact_us.service_links.faq_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Link 2: Package Overview</label><input type="text" x-model="pageData.contact_us.service_links.package_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Link 3: Affiliate Support</label><input type="text" x-model="pageData.contact_us.service_links.affiliate_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                </div>
                            </div>
                            
                            <!-- Bottom Notices List -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center cursor-move">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Bottom Notices (List)
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <template x-for="(notice, index) in pageData.contact_us.bottom_notices" :key="index">
                                        <div class="flex items-center space-x-2 mb-2 p-2 border rounded bg-gray-50">
                                            <input type="text" x-model="notice.icon" class="w-1/4 px-2 py-1 border border-gray-300 rounded text-xs" placeholder="Icon (e.g. fa-user-clock)">
                                            <textarea x-model="notice.text" class="w-3/4 px-2 py-1 border border-gray-300 rounded text-xs" rows="2" placeholder="Notice Text"></textarea>
                                            <button @click="pageData.contact_us.bottom_notices.splice(index, 1)" class="text-red-500 hover:text-red-700 px-1"><i class="fas fa-trash"></i></button>
                                        </div>
                                    </template>
                                    <button @click="if(!pageData.contact_us.bottom_notices) pageData.contact_us.bottom_notices = []; pageData.contact_us.bottom_notices.push({icon: 'fa-check', text: ''})" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Notice</button>
                                </div>
                            </div>
"""
    # Insert new blocks before Bottom Text
    marker_bottom_text = r'<!-- Bottom Notices -->'
    if 'Section: Contact Us Form' not in content:
        content = content.replace(marker_bottom_text, new_blocks + "\n" + marker_bottom_text)
        print("Injected UI sections to admin-cms.html")
    
    # Extend JSON data
    # Let's find bottom_text:
    json_marker = r'bottom_text: \'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible\. If you need help, don’t hesitate to reach out\.\''
    new_json_data = json_marker + """,
                        form_action: 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit',
                        map_image: { image: 'Contact-us/Contact Us_Mailing Address.jpg' },
                        service_links: {
                            faq_link: 'support.html',
                            package_link: 'packages.html',
                            affiliate_link: 'affiliate-page.html'
                        },
                        bottom_notices: [
                            { icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response' },
                            { icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice' },
                            { icon: 'fa-flag-usa', text: 'Provider Availability Varies By State' }
                        ]
    """
    if 'form_action:' not in content:
        content = content.replace(json_marker, new_json_data)
        print("Injected JSON defaults to admin-cms.html")

    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)


def patch_front():
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Form action URL
    form_action = r'action=\'https://forms\.zohopublic\.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/[A-Za-z0-9_-]+/htmlRecords/submit\''
    new_form_action = r':action="pageData.contact_us.form_action || \'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit\'"'
    content = re.sub(form_action, new_form_action, content)

    # 3 Service Links
    link_faq = r'Link to <a href="support\.html"[^>]*>Support / FAQ Page</a>'
    new_link_faq = r'Link to <a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.faq_link : \'support.html\'" target="_blank" class="text-[#3498db] hover:underline">Support / FAQ Page</a>'
    content = re.sub(link_faq, new_link_faq, content)
    
    link_pkg = r'Link to <a href="packages\.html"[^>]*>Package Overview</a>'
    new_link_pkg = r'Link to <a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.package_link : \'packages.html\'" target="_blank" class="text-[#3498db] hover:underline">Package Overview</a>'
    content = re.sub(link_pkg, new_link_pkg, content)
    
    link_aff = r'Link to <a href="affiliate-page\.html"[^>]*>Affiliate Support Section</a>'
    new_link_aff = r'Link to <a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.affiliate_link : \'affiliate-page.html\'" target="_blank" class="text-[#3498db] hover:underline">Affiliate Support Section</a>'
    content = re.sub(link_aff, new_link_aff, content)

    # Map image
    map_img = r'<img src="Contact-us/Contact Us_Mailing Address\.jpg"'
    new_map_img = r'<img :src="(pageData.contact_us.map_image && pageData.contact_us.map_image.image) ? pageData.contact_us.map_image.image : \'Contact-us/Contact Us_Mailing Address.jpg\'"'
    content = re.sub(map_img, new_map_img, content)

    # Bottom notices grid (replace the hardcoded 3 blocks with template loop)
    # The grid contains exactly the 3 items. We replace its inside.
    grid_pattern = r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">\s*<div class="bg-\[\#F2FFEB\].*?</div>\s*</div>'
    new_grid = r'''<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <template x-for="(notice, index) in (pageData.contact_us.bottom_notices || [{icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response'}, {icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice'}, {icon: 'fa-flag-usa', text: 'Provider Availability Varies By State'}])" :key="index">
                        <div class="bg-[#F2FFEB] p-8 rounded-lg flex flex-col items-center text-center h-full">
                            <div class="w-16 h-16 bg-[#1c4a00] rounded-full flex items-center justify-center mb-6 text-white text-2xl">
                                <i class="fas" :class="notice.icon"></i>
                            </div>
                            <p class="text-sm font-bold text-gray-800" x-text="notice.text"></p>
                        </div>
                    </template>
                </div>'''
    content = re.sub(grid_pattern, new_grid, content, flags=re.DOTALL)

    # Extend default JSON script
    json_marker_front = r'bottom_text: "We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible\. If you need help, don’t hesitate to reach out\."'
    new_json_data_front = json_marker_front + """,
                        form_action: "https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit",
                        map_image: { image: "Contact-us/Contact Us_Mailing Address.jpg" },
                        service_links: {
                            faq_link: "support.html",
                            package_link: "packages.html",
                            affiliate_link: "affiliate-page.html"
                        },
                        bottom_notices: [
                            { icon: "fa-user-clock", text: "Please Allow 1-2 Business Days For A Response" },
                            { icon: "fa-stop", text: "PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice" },
                            { icon: "fa-flag-usa", text: "Provider Availability Varies By State" }
                        ]
    """
    if 'form_action:' not in content:
        content = content.replace(json_marker_front, new_json_data_front)
        print("Injected JSON defaults to contact-us.html")

    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    patch_admin()
    patch_front()
