import re

with open('admin-cms.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add image fields to pageData.packages in script
# Find packages: { ... } and add image: '...' to hero, two_paths, affiliate_program
# Hero
content = re.sub(
    r"(packages: \{\s*hero: \{[^\}]*?btn2_link: '[^']*?')",
    r"\1,\n                          image: 'Plans-overview/Packages_Hero.jpg'",
    content
)

# Two Paths
content = re.sub(
    r"(two_paths: \{[^\}]*?btn2_link: '[^']*?')",
    r"\1,\n                          image: 'Plans-overview/Packages_Two Simple Paths.jpg'",
    content
)

# Affiliate Program
content = re.sub(
    r"(affiliate_program: \{[^\}]*?btn_link: '[^']*?')",
    r"\1,\n                          image: 'Plans-overview/Packages_Affiliate Program.jpg'",
    content
)


# 2. Add UI controls to Packages Editor
# Hero Section Image
hero_ui = r'''                                    <div class="mt-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase mb-1">Hero Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.packages.hero.image || 'Plans-overview/Packages_Hero.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm">
                                                <i class="fas fa-folder-open mr-1"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.packages.hero.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>'''
content = content.replace(
    '                                        <div class="p-3 border rounded bg-gray-50 space-y-2 text-center">\n                                            <label class="block text-xs font-bold text-gray-700 uppercase">Button 2 (Earn Fees)</label>\n                                            <input type="text" x-model="pageData.packages.hero.btn2_text" class="w-full px-2 py-1 text-sm border font-medium border-gray-300 rounded">\n                                            <input type="text" x-model="pageData.packages.hero.btn2_link" class="w-full px-2 py-1 text-xs border border-gray-300 text-gray-500 rounded">\n                                        </div>\n                                    </div>',
    '                                        <div class="p-3 border rounded bg-gray-50 space-y-2 text-center">\n                                            <label class="block text-xs font-bold text-gray-700 uppercase">Button 2 (Earn Fees)</label>\n                                            <input type="text" x-model="pageData.packages.hero.btn2_text" class="w-full px-2 py-1 text-sm border font-medium border-gray-300 rounded">\n                                            <input type="text" x-model="pageData.packages.hero.btn2_link" class="w-full px-2 py-1 text-xs border border-gray-300 text-gray-500 rounded">\n                                        </div>\n                                    </div>\n' + hero_ui
)

# Two Paths Section Image
two_paths_ui = r'''                                    <div class="mt-4 border-t pt-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase mb-1">Section Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.packages.two_paths.image || 'Plans-overview/Packages_Two Simple Paths.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm">
                                                <i class="fas fa-folder-open mr-1"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.packages.two_paths.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>'''
content = content.replace(
    '                                                </div>\n                                            </div>\n                                        </div>\n                                    </div>',
    '                                                </div>\n                                            </div>\n                                        </div>\n                                    </div>\n' + two_paths_ui
)

# Affiliate Program Section Image
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
content = content.replace(
    '                                        <div class="flex space-x-2">\n                                            <input type="text" x-model="pageData.packages.affiliate_program.btn_text" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded font-bold" placeholder="Btn Text">\n                                            <input type="text" x-model="pageData.packages.affiliate_program.btn_link" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded text-gray-500" placeholder="Btn Link">\n                                        </div>',
    '                                        <div class="flex space-x-2">\n                                            <input type="text" x-model="pageData.packages.affiliate_program.btn_text" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded font-bold" placeholder="Btn Text">\n                                            <input type="text" x-model="pageData.packages.affiliate_program.btn_link" class="w-1/2 px-2 py-2 text-sm border border-gray-300 rounded text-gray-500" placeholder="Btn Link">\n                                        </div>\n' + aff_img_ui
)

with open('admin-cms.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("admin-cms.html updated")
