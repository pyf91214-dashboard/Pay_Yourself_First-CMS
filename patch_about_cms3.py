import re

def update_admin_cms():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The section "What Makes PYF Different" ends at a specific block. We will just insert before <!-- Contact Us Editor -->
    
    insert_str = "<!-- Contact Us Editor -->"
    
    if insert_str not in content:
        print("Could not find insert anchor!")
        return
        
    replacement = """
                                <!-- Our Pledge -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden mt-6">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-handshake mr-3 text-brand-primary"></i> Our Pledge To Help You</div>
                                        <button @click="pageData.about_us.pledge.list.push('New item')" class="text-xs bg-brand-primary text-white rounded px-2 py-1">+ Add</button>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.pledge.headline" class="w-full px-3 py-2 border rounded text-sm font-mono text-blue-600" placeholder="Headline (HTML)">
                                        <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                                            <div class="flex space-x-2">
                                                <input type="text" x-model="pageData.about_us.pledge.list[idx]" class="flex-1 px-2 py-1 text-sm border rounded">
                                                <button @click="pageData.about_us.pledge.list.splice(idx, 1)" class="text-red-500"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.about_us.pledge.image" class="h-16 w-24 object-cover rounded border">
                                            <label class="cursor-pointer text-xs font-bold py-1 px-3 bg-gray-100 border rounded">Browse Image<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.pledge.image')" accept="image/*"></label>
                                        </div>
                                    </div>
                                </div>

                                <!-- PYF Journey CTA -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden mt-6">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-rocket mr-3 text-brand-primary"></i> Start Your PYF Journey (CTA)</div>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.journey.headline" class="w-full px-3 py-2 border rounded text-sm font-bold" placeholder="Headline">
                                        <textarea x-model="pageData.about_us.journey.desc" rows="2" class="w-full px-3 py-2 border rounded text-sm" placeholder="Description"></textarea>
                                        
                                        <div class="flex space-x-4 mt-2">
                                            <div class="flex-1 border p-3 rounded bg-gray-50">
                                                <label class="text-xs font-bold uppercase text-gray-500">Button 1</label>
                                                <input type="text" x-model="pageData.about_us.journey.btn1_text" class="w-full px-2 py-1 border rounded text-sm mt-1" placeholder="Text">
                                                <input type="text" x-model="pageData.about_us.journey.btn1_link" class="w-full px-2 py-1 border rounded text-sm mt-1" placeholder="Link">
                                            </div>
                                            <div class="flex-1 border p-3 rounded bg-gray-50">
                                                <label class="text-xs font-bold uppercase text-gray-500">Button 2</label>
                                                <input type="text" x-model="pageData.about_us.journey.btn2_text" class="w-full px-2 py-1 border rounded text-sm mt-1" placeholder="Text">
                                                <input type="text" x-model="pageData.about_us.journey.btn2_link" class="w-full px-2 py-1 border rounded text-sm mt-1" placeholder="Link">
                                            </div>
                                        </div>
                                    </div>
                                </div>

                        </div>
                        
                        <!-- Contact Us Editor -->"""
                                
    content = content.replace("</div>\n                        \n                        <!-- Contact Us Editor -->", replacement)
    
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated admin-cms.html for Pledge and Journey successfully.")

update_admin_cms()
