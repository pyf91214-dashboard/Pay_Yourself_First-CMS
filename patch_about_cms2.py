import re

def update_admin_cms():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to insert the Missing sections between 'Our Mission' and 'Who We Serve'
    # Wait, 'Our Mission' and 'Who We Serve' are inside a div `<div class="space-y-6">`
    # Let's find <!-- Who We Serve --> and insert our new blocks right before it.
    
    insert_str = "<!-- Who We Serve -->"
    
    if insert_str not in content:
        print("Could not find insert anchor!")
        return
        
    replacement = """
                                <!-- Serving Everyday Americans -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-chart-line mr-3 text-brand-primary"></i> Serving Everyday Americans</div>
                                    </div>
                                    <div class="p-4 space-y-3">
                                        <input type="text" x-model="pageData.about_us.serving.headline" class="w-full px-3 py-2 border rounded text-sm font-mono text-blue-600" placeholder="Headline (HTML)">
                                        
                                        <div class="bg-gray-50 p-3 rounded border">
                                            <h4 class="font-bold text-xs text-gray-700 uppercase mb-2">Stats</h4>
                                            <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                                                <div class="flex space-x-2 mb-2">
                                                    <input type="text" x-model="stat.title" class="w-1/3 px-2 py-1 text-sm border font-bold rounded" placeholder="Stat Value (e.g. 14+ Years)">
                                                    <input type="text" x-model="stat.desc" class="flex-1 px-2 py-1 text-sm border rounded" placeholder="Stat Description">
                                                </div>
                                            </template>
                                        </div>

                                        <div class="bg-gray-50 p-3 rounded border">
                                            <h4 class="font-bold text-xs text-gray-700 uppercase mb-2">Core Principles</h4>
                                            <template x-for="(prin, idx) in pageData.about_us.serving.principles" :key="idx">
                                                <div class="flex space-x-2 mb-2">
                                                    <input type="text" x-model="prin.icon" class="w-1/3 px-2 py-1 text-xs font-mono border rounded" placeholder="Icon Class (e.g. fas fa-brain)">
                                                    <input type="text" x-model="prin.title" class="flex-1 px-2 py-1 text-sm border rounded font-bold" placeholder="Principle Title">
                                                </div>
                                            </template>
                                        </div>

                                        <div class="flex items-center space-x-4 mt-2">
                                            <img :src="pageData.about_us.serving.image" class="h-16 w-24 object-cover rounded border">
                                            <label class="cursor-pointer text-xs font-bold py-1 px-3 bg-gray-100 hover:bg-gray-200 border rounded">Browse<input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.serving.image')" accept="image/*"></label>
                                        </div>
                                    </div>
                                </div>

                                <!-- System Cards -->
                                <div class="bg-white rounded-xl shadow-soft border border-gray-100 overflow-hidden">
                                    <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between">
                                        <div class="flex items-center text-gray-600 font-bold text-sm"><i class="fas fa-layer-group mr-3 text-brand-primary"></i> The PYF System</div>
                                    </div>
                                    <div class="p-4 space-y-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Headline (HTML)</label><input type="text" x-model="pageData.about_us.system.headline" class="w-full px-3 py-2 border rounded mt-1 font-mono text-sm text-blue-600"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Subtitle</label><input type="text" x-model="pageData.about_us.system.subtitle" class="w-full px-3 py-2 border rounded mt-1 font-bold text-sm"></div>

                                        <div class="space-y-4">
                                            <template x-for="(card, cIdx) in pageData.about_us.system.cards" :key="cIdx">
                                                <div class="border rounded bg-gray-50 p-4">
                                                    <div class="flex justify-between items-center mb-2">
                                                        <input type="text" x-model="card.title" class="font-bold text-lg text-brand-primary w-1/2 px-2 py-1 border rounded" placeholder="Card Title">
                                                        <div class="flex items-center space-x-2">
                                                            <img :src="card.image" class="h-8 w-12 object-cover rounded border">
                                                            <label class="cursor-pointer text-[10px] font-bold py-1 px-2 bg-white border rounded shadow-sm">Browse Image <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.about_us.system.cards['+cIdx+'].image')" accept="image/*"></label>
                                                        </div>
                                                    </div>
                                                    <textarea x-model="card.desc" rows="2" class="w-full px-2 py-1 border rounded text-sm mb-2" placeholder="Description"></textarea>
                                                    
                                                    <div class="border border-gray-200 bg-white p-2 rounded mb-2">
                                                        <div class="flex justify-between items-center mb-1">
                                                            <span class="text-xs font-bold uppercase text-gray-500">Bullets</span>
                                                            <button @click="card.list.push('New Bullet')" class="text-xs bg-gray-200 hover:bg-gray-300 px-2 py-1 rounded font-bold">+ Add</button>
                                                        </div>
                                                        <template x-for="(listItem, lIdx) in card.list" :key="lIdx">
                                                            <div class="flex space-x-1 mb-1">
                                                                <input type="text" x-model="card.list[lIdx]" class="flex-1 text-xs border px-1 py-1 rounded">
                                                                <button @click="card.list.splice(lIdx, 1)" class="text-red-500 text-xs"><i class="fas fa-trash"></i></button>
                                                            </div>
                                                        </template>
                                                    </div>
                                                    
                                                    <div x-show="card.quote !== undefined" class="mt-2">
                                                        <label class="text-[10px] font-bold uppercase text-gray-500">Quote</label>
                                                        <input type="text" x-model="card.quote" class="w-full px-2 py-1 border text-sm text-green-700 italic font-medium rounded">
                                                    </div>
                                                    <div x-show="card.footer !== undefined" class="mt-2">
                                                        <label class="text-[10px] font-bold uppercase text-gray-500">Footer Text</label>
                                                        <input type="text" x-model="card.footer" class="w-full px-2 py-1 border text-sm font-bold text-gray-700 rounded">
                                                    </div>
                                                </div>
                                            </template>
                                        </div>
                                    </div>
                                </div>

                                <!-- Who We Serve -->"""
                                
    content = content.replace(insert_str, replacement)
    
    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated admin-cms.html successfully.")

update_admin_cms()
