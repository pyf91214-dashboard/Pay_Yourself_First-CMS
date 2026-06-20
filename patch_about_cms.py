import re

def update_admin_cms():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The existing block is very simple
    # We will search for <div x-show="activePage === 'about_us'" x-cloak>
    # And replace until <!-- Contact Us Editor -->
    
    start_str = "<!-- About Us Editor -->"
    end_str = "<!-- Contact Us Editor -->"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find about_us block in admin-cms.html")
        return
        
    replacement = """<!-- About Us Editor -->
                        <div x-show="activePage === 'about_us'" x-cloak>
                            <div class="flex justify-between items-center mb-8 bg-white p-4 rounded-xl shadow-sm border border-gray-100">
                                <div>
                                    <h2 class="text-2xl font-extrabold text-gray-800 tracking-tight">About Us Editor</h2>
                                    <p class="text-sm text-gray-500 mt-1 font-medium">Manage the complete About Us page content.</p>
                                </div>
                                <div class="flex space-x-3">
                                    <button @click="saveDraft()" class="bg-white border-2 border-brand-primary text-brand-primary hover:bg-brand-50 font-bold py-2 px-6 rounded-lg shadow-sm transition flex items-center">
                                        <i class="fas fa-save mr-2"></i> Save Draft
                                    </button>
                                </div>
                            </div>
                            
                            <!-- Hero Section -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-image mr-3 text-brand-primary"></i> Hero Section
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline (HTML)</label><input type="text" x-model="pageData.about_us.hero.headline" class="w-full px-3 py-2 border rounded mt-1 text-sm font-mono text-blue-600"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description</label><textarea x-model="pageData.about_us.hero.desc" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    
                                    <div class="flex items-center space-x-4">
                                        <img :src="pageData.about_us.hero.image || 'About-us/About Us_Hero.jpg'" class="h-20 w-32 object-cover rounded border">
                                        <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                            <i class="fas fa-folder-open mr-2"></i> Browse
                                            <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.hero.image')" accept="image/*">
                                        </label>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Who We Are -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-users mr-3 text-brand-primary"></i> Who We Are
                                    </div>
                                    <button @click="pageData.about_us.who_we_are.list.push('New item')" class="text-xs bg-brand-primary text-white rounded px-3 py-1 font-bold">+ Add Bullet</button>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline (HTML)</label><input type="text" x-model="pageData.about_us.who_we_are.headline" class="w-full px-3 py-2 border rounded mt-1 font-mono text-sm text-blue-600"></div>
                                    <textarea x-model="pageData.about_us.who_we_are.desc1" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 1"></textarea>
                                    <textarea x-model="pageData.about_us.who_we_are.desc2" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 2"></textarea>
                                    
                                    <div class="bg-gray-50 p-4 rounded border">
                                        <h4 class="font-bold text-sm text-gray-700 mb-2">Bullet Points</h4>
                                        <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                                            <div class="flex space-x-2 mb-2">
                                                <input type="text" x-model="pageData.about_us.who_we_are.list[idx]" class="flex-1 px-2 py-1 text-sm border rounded">
                                                <button @click="pageData.about_us.who_we_are.list.splice(idx, 1)" class="text-red-500"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                    </div>
                                    
                                    <textarea x-model="pageData.about_us.who_we_are.desc3" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 3"></textarea>
                                    <textarea x-model="pageData.about_us.who_we_are.desc4" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 4"></textarea>

                                    <div class="flex items-center space-x-4">
                                        <img :src="pageData.about_us.who_we_are.image" class="h-20 w-32 object-cover rounded border">
                                        <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                            <i class="fas fa-folder-open mr-2"></i> Browse
                                            <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.who_we_are.image')" accept="image/*">
                                        </label>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Our Origin -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-seedling mr-3 text-brand-primary"></i> Our Origin
                                    </div>
                                    <button @click="pageData.about_us.origin.list.push('New item')" class="text-xs bg-brand-primary text-white rounded px-3 py-1 font-bold">+ Add Bullet</button>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline (HTML)</label><input type="text" x-model="pageData.about_us.origin.headline" class="w-full px-3 py-2 border rounded mt-1 font-mono text-sm text-blue-600"></div>
                                    <textarea x-model="pageData.about_us.origin.desc1" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 1"></textarea>
                                    
                                    <div class="bg-gray-50 p-4 rounded border">
                                        <h4 class="font-bold text-sm text-gray-700 mb-2">Bullet Points</h4>
                                        <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                                            <div class="flex space-x-2 mb-2">
                                                <input type="text" x-model="pageData.about_us.origin.list[idx]" class="flex-1 px-2 py-1 text-sm border rounded">
                                                <button @click="pageData.about_us.origin.list.splice(idx, 1)" class="text-red-500"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                    </div>
                                    
                                    <textarea x-model="pageData.about_us.origin.desc2" class="w-full px-3 py-2 border rounded mt-1" rows="2" placeholder="Description 2"></textarea>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Bottom Headline (HTML)</label><input type="text" x-model="pageData.about_us.origin.headline_bottom" class="w-full px-3 py-2 border rounded mt-1 font-mono text-sm text-blue-600"></div>

                                    <div class="flex items-center space-x-4">
                                        <img :src="pageData.about_us.origin.image" class="h-20 w-32 object-cover rounded border">
                                        <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                            <i class="fas fa-folder-open mr-2"></i> Browse
                                            <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.origin.image')" accept="image/*">
                                        </label>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Our Mission & Who We Serve & What Makes Us Different -->
                            <div class="space-y-6">
                                <!-- Mission -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-bullseye mr-3 text-brand-primary"></i> Our Mission</div>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.mission.headline" class="w-full px-3 py-2 border rounded text-sm font-mono text-blue-600" placeholder="Headline (HTML)">
                                        <input type="text" x-model="pageData.about_us.mission.subtitle" class="w-full px-3 py-2 border rounded text-sm font-bold" placeholder="Subtitle">
                                        <textarea x-model="pageData.about_us.mission.desc" class="w-full px-3 py-2 border rounded text-sm" rows="3" placeholder="Description"></textarea>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.about_us.mission.image" class="h-16 w-16 object-cover rounded border">
                                            <label class="cursor-pointer text-xs font-bold py-1 px-3 bg-gray-100 hover:bg-gray-200 border rounded">Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.mission.image')" accept="image/*"></label>
                                        </div>
                                    </div>
                                </div>

                                <!-- Who We Serve -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-hand-holding-heart mr-3 text-brand-primary"></i> Who We Serve</div>
                                        <button @click="pageData.about_us.who_we_serve.list.push('New item')" class="text-xs bg-brand-primary text-white rounded px-2 py-1">+ Add</button>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.who_we_serve.headline" class="w-full px-3 py-2 border rounded text-sm font-mono text-blue-600">
                                        <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                                            <div class="flex space-x-2"><input type="text" x-model="pageData.about_us.who_we_serve.list[idx]" class="flex-1 px-2 py-1 text-sm border rounded"><button @click="pageData.about_us.who_we_serve.list.splice(idx, 1)" class="text-red-500"><i class="fas fa-trash"></i></button></div>
                                        </template>
                                        <input type="text" x-model="pageData.about_us.who_we_serve.footer" class="w-full px-3 py-2 border rounded text-sm font-bold" placeholder="Footer Text">
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.about_us.who_we_serve.image" class="h-16 w-16 object-cover rounded border">
                                            <label class="cursor-pointer text-xs font-bold py-1 px-3 bg-gray-100 border rounded">Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.who_we_serve.image')" accept="image/*"></label>
                                        </div>
                                    </div>
                                </div>

                                <!-- Different -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-star mr-3 text-brand-primary"></i> What Makes PYF Different</div>
                                        <button @click="pageData.about_us.different.list.push('New item')" class="text-xs bg-brand-primary text-white rounded px-2 py-1">+ Add</button>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.different.headline" class="w-full px-3 py-2 border rounded text-sm font-mono text-blue-600">
                                        <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                                            <div class="flex space-x-2"><input type="text" x-model="pageData.about_us.different.list[idx]" class="flex-1 px-2 py-1 text-sm border rounded"><button @click="pageData.about_us.different.list.splice(idx, 1)" class="text-red-500"><i class="fas fa-trash"></i></button></div>
                                        </template>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.about_us.different.image" class="h-16 w-24 object-cover rounded border">
                                            <label class="cursor-pointer text-xs font-bold py-1 px-3 bg-gray-100 border rounded">Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.different.image')" accept="image/*"></label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                        
                        <!-- Contact Us Editor -->"""
                        
    new_content = content[:start_idx] + replacement + content[end_idx + len(end_str):]
    
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Updated admin-cms.html successfully.")

update_admin_cms()
