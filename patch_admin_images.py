import re

with open('admin-cms.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero
hero_pattern = r'(\<input type="text" x-model="pageData\.how_we_help_you\.hero\.btn2_link" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm"\>\n\s*\</div\>\n\s*\</div\>)'
hero_replacement = r'''\1
                                    <div class="mb-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.hero.image || 'How-we-help-you/How we help you_hero image.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.hero.image')" accept="image/*"></label>
                                        </div>
                                    </div>'''
content = re.sub(hero_pattern, hero_replacement, content)

# 2. Why Exists
why_exists_pattern = r'(\<textarea rows="3" x-model="pageData\.how_we_help_you\.why_exists\.desc2" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm text-gray-700"\>\</textarea\>\n\s*\</div\>)'
why_exists_replacement = r'''\1
                                    <div class="mb-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Main Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.why_exists.image || 'How-we-help-you/Why PYF Exists.jpg'" class="h-16 w-16 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.why_exists.image')" accept="image/*"></label>
                                        </div>
                                    </div>'''
content = re.sub(why_exists_pattern, why_exists_replacement, content)

# 3. Problems 1 & 2
prob1_pattern = r'(\<input type="text" x-model="pageData\.how_we_help_you\.problems\.block1\.list\[index\]" class="w-full px-2 py-1 text-xs border border-gray-300 rounded mb-1"\>\n\s*\</template\>)'
prob1_replacement = r'''\1
                                            <div class="mt-4">
                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Image</label>
                                                <div class="flex items-center space-x-4">
                                                    <img :src="pageData.how_we_help_you.problems.block1.image || 'How-we-help-you/Problems most people face_1.jpg'" class="h-16 w-16 object-cover border rounded">
                                                    <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.problems.block1.image')" accept="image/*"></label>
                                                </div>
                                            </div>'''
content = re.sub(prob1_pattern, prob1_replacement, content)

prob2_pattern = r'(\<input type="text" x-model="pageData\.how_we_help_you\.problems\.block2\.list\[index\]" class="w-full px-2 py-1 text-xs border border-gray-300 rounded mb-1"\>\n\s*\</template\>)'
prob2_replacement = r'''\1
                                            <div class="mt-4">
                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Image</label>
                                                <div class="flex items-center space-x-4">
                                                    <img :src="pageData.how_we_help_you.problems.block2.image || 'How-we-help-you/Problems most people face_2.jpg'" class="h-16 w-16 object-cover border rounded">
                                                    <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.problems.block2.image')" accept="image/*"></label>
                                                </div>
                                            </div>'''
content = re.sub(prob2_pattern, prob2_replacement, content)

# 4. Why Works
why_works_pattern = r'(\<textarea rows="4" :value="pageData\.how_we_help_you\.why_works\.list\.join\(\'\\n\'\)" @input="pageData\.how_we_help_you\.why_works\.list = \$event\.target\.value\.split\(\'\\n\'\)" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm text-gray-900"\>\</textarea\>\n\s*\</div\>)'
why_works_replacement = r'''\1
                                            <div class="mt-4">
                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                                <div class="flex items-center space-x-4">
                                                    <img :src="pageData.how_we_help_you.why_works.image || 'How-we-help-you/Why PYF Works.jpg'" class="h-16 w-32 object-cover border rounded">
                                                    <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded shadow-sm"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.why_works.image')" accept="image/*"></label>
                                                </div>
                                            </div>'''
content = re.sub(why_works_pattern, why_works_replacement, content)

with open('admin-cms.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied to admin-cms.html successfully.")
