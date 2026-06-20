import re

def patch_how_we_help_you():
    with open('how-we-help-you.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hero Image
    content = content.replace(
        '<img src="How-we-help-you/How we help you_hero image.jpg"',
        '<img :src="pageData.hero.image || \'How-we-help-you/How we help you_hero image.jpg\'"'
    )

    # 2. Why PYF Exists Image
    content = content.replace(
        '<img src="How-we-help-you/Why PYF Exists.jpg"',
        '<img :src="pageData.why_exists.image || \'How-we-help-you/Why PYF Exists.jpg\'"'
    )

    # 3. Problems 1 Image
    content = content.replace(
        '<img src="How-we-help-you/Problems most people face_1.jpg"',
        '<img :src="pageData.problems.block1.image || \'How-we-help-you/Problems most people face_1.jpg\'"'
    )
    
    # 4. Problems 2 Image
    content = content.replace(
        '<img src="How-we-help-you/Problems most people face_2.jpg"',
        '<img :src="pageData.problems.block2.image || \'How-we-help-you/Problems most people face_2.jpg\'"'
    )

    # 5. Why PYF Works Image
    content = content.replace(
        '<img src="How-we-help-you/Why PYF Works.jpg"',
        '<img :src="pageData.why_works.image || \'How-we-help-you/Why PYF Works.jpg\'"'
    )

    # Now add default values into siteData
    if "image: 'How-we-help-you/How we help you_hero image.jpg'" not in content:
        content = content.replace(
            "btn2_link: 'packages.html'\n                    },",
            "btn2_link: 'packages.html',\n                        image: 'How-we-help-you/How we help you_hero image.jpg'\n                    },"
        )
    if "image: 'How-we-help-you/Why PYF Works.jpg'" not in content:
        content = content.replace(
            "subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward \u2014 whether you want to earn more, keep more, or spend less.'\n                    },",
            "subdesc2: 'PYF is built to give people real support, real clarity, and a real path forward \u2014 whether you want to earn more, keep more, or spend less.',\n                        image: 'How-we-help-you/Why PYF Works.jpg'\n                    },"
        )

    with open('how-we-help-you.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched how-we-help-you.html")

def patch_admin_cms():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hero Banner Image Admin
    hero_snippet = """                                        <div>
                                            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Button 2 Link</label>
                                            <input type="text" x-model="pageData.how_we_help_you.hero.btn2_link" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm">
                                        </div>
                                    </div>"""
    hero_image_html = """                                    <div class="mt-2">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.hero.image || 'How-we-help-you/How we help you_hero image.jpg'" class="h-16 w-32 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.hero.image')" accept="image/*"></label>
                                        </div>
                                    </div>"""
    
    if "pageData.how_we_help_you.hero.image" not in content:
        content = content.replace(hero_snippet, hero_snippet + "\n" + hero_image_html)


    # 2. Why Exists Image Admin
    why_exists_snippet = """                                    <div class="mb-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Description Paragraph 2</label>
                                        <textarea rows="3" x-model="pageData.how_we_help_you.why_exists.desc2" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm text-gray-700"></textarea>
                                    </div>"""
    why_exists_image_html = """                                    <div class="mt-4">
                                        <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.how_we_help_you.why_exists.image || 'How-we-help-you/Why PYF Exists.jpg'" class="h-16 w-16 object-cover border rounded">
                                            <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.why_exists.image')" accept="image/*"></label>
                                        </div>
                                    </div>"""
    if 'pageData.how_we_help_you.why_exists.image" class="h-16' not in content: # it might already exist but let's check
        content = content.replace(why_exists_snippet, why_exists_snippet + "\n" + why_exists_image_html)

    # 3. Problems Block 1 & 2 Admin
    prob1_snippet = """                                            <template x-for="(item, index) in pageData.how_we_help_you.problems.block1.list" :key="index">
                                                <input type="text" x-model="pageData.how_we_help_you.problems.block1.list[index]" class="w-full px-2 py-1 text-xs border border-gray-300 rounded mb-1">
                                            </template>"""
    prob1_img_html = """                                            <div class="mt-2 flex items-center space-x-2">
                                                <img :src="pageData.how_we_help_you.problems.block1.image || 'How-we-help-you/Problems most people face_1.jpg'" class="h-10 w-16 object-cover border rounded">
                                                <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-1 px-2 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.problems.block1.image')" accept="image/*"></label>
                                            </div>"""
    if "pageData.how_we_help_you.problems.block1.image" not in content:
        content = content.replace(prob1_snippet, prob1_snippet + "\n" + prob1_img_html)

    prob2_snippet = """                                            <template x-for="(item, index) in pageData.how_we_help_you.problems.block2.list" :key="index">
                                                <input type="text" x-model="pageData.how_we_help_you.problems.block2.list[index]" class="w-full px-2 py-1 text-xs border border-gray-300 rounded mb-1">
                                            </template>"""
    prob2_img_html = """                                            <div class="mt-2 flex items-center space-x-2">
                                                <img :src="pageData.how_we_help_you.problems.block2.image || 'How-we-help-you/Problems most people face_2.jpg'" class="h-10 w-16 object-cover border rounded">
                                                <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-1 px-2 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.problems.block2.image')" accept="image/*"></label>
                                            </div>"""
    if "pageData.how_we_help_you.problems.block2.image" not in content:
        content = content.replace(prob2_snippet, prob2_snippet + "\n" + prob2_img_html)


    # 4. Why Works Background Image Admin
    why_works_snippet = """                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">List Items (new line sep)</label>
                                                <textarea rows="4" :value="pageData.how_we_help_you.why_works.list.join('\\n')" @input="pageData.how_we_help_you.why_works.list = $event.target.value.split('\\n')" class="w-full px-3 py-2 border border-gray-300 rounded focus:border-brand-700 text-sm text-gray-900"></textarea>
                                            </div>"""
    why_works_img_html = """                                            <div class="mt-4">
                                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wide mb-1">Background Image</label>
                                                <div class="flex items-center space-x-4">
                                                    <img :src="pageData.how_we_help_you.why_works.image || 'How-we-help-you/Why PYF Works.jpg'" class="h-16 w-32 object-cover border rounded">
                                                    <label class="cursor-pointer bg-white hover:bg-gray-100 border text-gray-700 text-[10px] font-bold py-2 px-3 rounded"><i class="fas fa-folder-open mr-1"></i> Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.how_we_help_you.why_works.image')" accept="image/*"></label>
                                                </div>
                                            </div>"""
    if "pageData.how_we_help_you.why_works.image" not in content:
        content = content.replace(why_works_snippet, why_works_snippet + "\n" + why_works_img_html)

    # Note: the admin default structure initialized in `build_admin.py` or `admin.html` might also need defaults but if we set default images with `||` in `img :src` it won't break if not present initially.
    # We will just ensure our `how-we-help-you.html` and `admin-cms.html` changes are perfect here.

    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched admin-cms.html")


if __name__ == '__main__':
    patch_how_we_help_you()
    patch_admin_cms()
