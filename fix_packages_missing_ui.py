import re

# 1. Fix admin-cms.html UI for Affiliate Program
with open('admin-cms.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

aff_img_ui = r'''                                    <div class="mt-4 pt-4 border-t">
                                        <label class="block text-xs font-bold text-gray-700 uppercase mb-1">Affiliate Program Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.packages.affiliate_program.image || 'Plans-overview/Packages_Affiliate Program.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm">
                                                <i class="fas fa-folder-open mr-1"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.packages.affiliate_program.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>'''

# Look for the last div in the affiliate_program block before it closes.
# It currently ends with the buttons flex container.
if aff_img_ui not in admin_content:
    admin_content = admin_content.replace(
        '                                        <input type="text" x-model="pageData.packages.affiliate_program.btn_link" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded text-gray-500" placeholder="Btn Link">\n                                    </div>',
        '                                        <input type="text" x-model="pageData.packages.affiliate_program.btn_link" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded text-gray-500" placeholder="Btn Link">\n                                    </div>\n' + aff_img_ui
    )

with open('admin-cms.html', 'w', encoding='utf-8') as f:
    f.write(admin_content)

# 2. Fix packages.html syntax error
with open('packages.html', 'r', encoding='utf-8') as f:
    pkg_content = f.read()

pkg_content = pkg_content.replace(r"\'Plans-overview/Packages_Hero.jpg\'", "'Plans-overview/Packages_Hero.jpg'")
pkg_content = pkg_content.replace(r"\'Plans-overview/Packages_Two Simple Paths.jpg\'", "'Plans-overview/Packages_Two Simple Paths.jpg'")
pkg_content = pkg_content.replace(r"\'Plans-overview/Packages_Affiliate Program.jpg\'", "'Plans-overview/Packages_Affiliate Program.jpg'")

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(pkg_content)

print("Fixes applied.")
