import re

with open('admin-cms.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Clean up duplicates that were injected by multiple scripts
# Hero
hero_dup = r'''                                    <div class="mt-2">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.hero.image \|\| 'How-we-help-you/How we help you_hero image.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-\[10px\] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo\(\$event, 'pageData.how_we_help_you.hero.image'\)" accept="image/\*"></label>
                                        </div>
                                    </div>'''
content = re.sub(hero_dup, "", content)

# Why Exists
why_exists_dup = r'''                                    <div class="mt-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.why_exists.image \|\| 'How-we-help-you/Why PYF Exists.jpg'" class="h-16 w-16 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-\[10px\] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo\(\$event, 'pageData.how_we_help_you.why_exists.image'\)" accept="image/\*"></label>
                                        </div>
                                    </div>'''
content = re.sub(why_exists_dup, "", content)

# Problems 1 & 2
prob1_dup = r'''                                            <div class="mt-2 flex items-center space-x-2">
                                                <img :src="pageData.how_we_help_you.problems.block1.image \|\| 'How-we-help-you/Problems most people face_1.jpg'" class="h-10 w-16 object-cover border rounded">
                                                <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-\[10px\] font-bold py-1 px-2 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo\(\$event, 'pageData.how_we_help_you.problems.block1.image'\)" accept="image/\*"></label>
                                            </div>'''
content = re.sub(prob1_dup, "", content)
prob2_dup = r'''                                            <div class="mt-2 flex items-center space-x-2">
                                                <img :src="pageData.how_we_help_you.problems.block2.image \|\| 'How-we-help-you/Problems most people face_2.jpg'" class="h-10 w-16 object-cover border rounded">
                                                <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-\[10px\] font-bold py-1 px-2 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo\(\$event, 'pageData.how_we_help_you.problems.block2.image'\)" accept="image/\*"></label>
                                            </div>'''
content = re.sub(prob2_dup, "", content)

# Why Works
why_works_dup = r'''                                            <div class="mt-4">
                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                                <div class="flex items-center space-x-4">
                                                    <img :src="pageData.how_we_help_you.why_works.image \|\| 'How-we-help-you/Why PYF Works.jpg'" class="h-16 w-32 object-cover border rounded">
                                                    <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-\[10px\] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo\(\$event, 'pageData.how_we_help_you.why_works.image'\)" accept="image/\*"></label>
                                                </div>
                                            </div>'''
content = re.sub(why_works_dup, "", content)

with open('admin-cms.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Duplicates cleaned up")
