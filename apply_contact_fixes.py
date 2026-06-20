import re
import os

def fix_admin():
    file = 'admin-cms.html'
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update JSON Defaults to include bottom_notices, map_image, service_links
    # Find contact_us: { ... bottom_text: ... }
    
    # We will search for bottom_text and append the missing JSON fields right after it
    json_inject = r"""bottom_text: 'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.',
                        bottom_notices: [
                            {icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response'},
                            {icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice'},
                            {icon: 'fa-flag-usa', text: 'Provider Availability Varies By State'}
                        ],
                        map_image: {
                            image: 'Contact-us/Contact Us_Mailing Address.jpg',
                            heading: 'Mailing Address'
                        },
                        service_links: {
                            faq_link: 'support.html', faq_text: 'Support / FAQ Page',
                            package_link: 'packages.html', package_text: 'Package Overview',
                            affiliate_link: 'affiliate-page.html', affiliate_text: 'Affiliate Support Section'
                        },
                        form_action: 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit'"""
    
    html = re.sub(r'bottom_text:\s*\'[^\']*\'', json_inject, html)

    # 2. Add text fields to Service Links UI in admin-cms.html
    old_links = r"""<div><label class="text-xs font-bold text-gray-700 uppercase">Link 1: Support/FAQ</label><input type="text" x-model="pageData\.contact_us\.service_links\.faq_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Link 2: Package Overview</label><input type="text" x-model="pageData\.contact_us\.service_links\.package_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Link 3: Affiliate Support</label><input type="text" x-model="pageData\.contact_us\.service_links\.affiliate_link" class="w-full px-3 py-2 border rounded mt-1"></div>"""
    
    new_links = """
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 1 Text</label><input type="text" x-model="pageData.contact_us.service_links.faq_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 1 URL</label><input type="text" x-model="pageData.contact_us.service_links.faq_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 2 Text</label><input type="text" x-model="pageData.contact_us.service_links.package_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 2 URL</label><input type="text" x-model="pageData.contact_us.service_links.package_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 3 Text</label><input type="text" x-model="pageData.contact_us.service_links.affiliate_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Link 3 URL</label><input type="text" x-model="pageData.contact_us.service_links.affiliate_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>"""
    html = re.sub(old_links, new_links, html)

    # 3. Move Mailing Address textarea to the Mailing Address Map UI
    # remove from Contact Info
    old_address_input = r"""<div><label class="text-xs font-bold text-gray-700 uppercase">Mailing Address</label><textarea x-model="pageData\.contact_us\.info\.address" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>\s*"""
    html = re.sub(old_address_input, "", html)

    # insert into Map UI
    old_map_ui = r"""<label class="text-xs font-bold text-gray-700 uppercase block mb-1">Map Background Image</label>"""
    new_map_ui = """<div><label class="text-xs font-bold text-gray-700 uppercase">Map Heading Text</label><input type="text" x-model="pageData.contact_us.map_image.heading" class="w-full px-3 py-2 border rounded mt-1 mb-4"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Mailing Address Text (Overlay)</label><textarea x-model="pageData.contact_us.info.address" class="w-full px-3 py-2 border rounded mt-1 mb-4" rows="4"></textarea></div>
                                    <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Map Background Image</label>"""
    html = re.sub(old_map_ui, new_map_ui, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed admin-cms.html")

def fix_frontend():
    file = 'contact-us.html'
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update Service Links rendering to use dynamic text and the same structure
    # I'll manually replace the labels
    html = re.sub(
        r'<a :href="pageData\.contact_us\.service_links \? pageData\.contact_us\.service_links\.faq_link : \'[^\']+\'" target="_blank" class="text-\[#3498db\] hover:underline">Support / FAQ Page</a>',
        r'<a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.faq_link : \'support.html\'" target="_blank" class="text-[#3498db] hover:underline" x-text="pageData.contact_us.service_links ? pageData.contact_us.service_links.faq_text : \'Support / FAQ Page\'"></a>',
        html
    )
    
    html = re.sub(
        r'<a :href="pageData\.contact_us\.service_links \? pageData\.contact_us\.service_links\.package_link : \'[^\']+\'" target="_blank" class="text-\[#3498db\] hover:underline">Package Overview</a>',
        r'<a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.package_link : \'packages.html\'" target="_blank" class="text-[#3498db] hover:underline" x-text="pageData.contact_us.service_links ? pageData.contact_us.service_links.package_text : \'Package Overview\'"></a>',
        html
    )

    html = re.sub(
        r'<a :href="pageData\.contact_us\.service_links \? pageData\.contact_us\.service_links\.affiliate_link : \'[^\']+\'" target="_blank" class="text-\[#3498db\] hover:underline">Affiliate Support Section</a>',
        r'<a :href="pageData.contact_us.service_links ? pageData.contact_us.service_links.affiliate_link : \'affiliate-page.html\'" target="_blank" class="text-[#3498db] hover:underline" x-text="pageData.contact_us.service_links ? pageData.contact_us.service_links.affiliate_text : \'Affiliate Support Section\'"></a>',
        html
    )
    
    # 2. Add heading text map
    html = re.sub(
        r'<h2 class="text-3xl font-extrabold uppercase mb-4 tracking-wide">Mailing Address</h2>',
        r'<h2 class="text-3xl font-extrabold uppercase mb-4 tracking-wide" x-text="(pageData.contact_us.map_image && pageData.contact_us.map_image.heading) ? pageData.contact_us.map_image.heading : \'Mailing Address\'"></h2>',
        html
    )

    # 3. Add same defaults to JS in contact-us.html
    json_inject = r"""bottom_text: 'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.',
                        bottom_notices: [
                            {icon: 'fa-user-clock', text: 'Please Allow 1-2 Business Days For A Response'},
                            {icon: 'fa-stop', text: 'PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice'},
                            {icon: 'fa-flag-usa', text: 'Provider Availability Varies By State'}
                        ],
                        map_image: {
                            image: 'Contact-us/Contact Us_Mailing Address.jpg',
                            heading: 'Mailing Address'
                        },
                        service_links: {
                            faq_link: 'support.html', faq_text: 'Support / FAQ Page',
                            package_link: 'packages.html', package_text: 'Package Overview',
                            affiliate_link: 'affiliate-page.html', affiliate_text: 'Affiliate Support Section'
                        },
                        form_action: 'https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit'"""
    html = re.sub(r'bottom_text:\s*\'We’re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don’t hesitate to reach out.\'', json_inject, html)


    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed contact-us.html")

fix_admin()
fix_frontend()
