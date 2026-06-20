import re
import sys

file_path = r"d:\Sapphire Leads\Pay Yourself First Website\Pyf-dashboard with my Mail\admin-cms.html"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace the business schema
schema_new = """                business: {
                    hero: {
                        headline: 'Increase Your Cash Flow. <br> Improve Your Quality of Life. <br> Gain Your Freedom.',
                        desc: 'Join those who\\'ve discovered how to access legitimate tax deductions and expert professional support to improve their financial life without quitting their day job.',
                        btn1_text: 'Get Business Support Package',
                        btn1_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                        btn2_text: 'Watch This Video',
                        btn2_link: '#',
                        image: 'Business-Support-Page/IPP_Hero.jpg'
                    },
                    intro: {
                        headline: 'Most People Don\\'t Understand Enough About Business Tax Deductions. Even those who own businesses. Why would they? The United States tax code is over 70,000 pages long!',
                        desc1: 'Business owners have access to over 400 tax deductions that W-2 employees rarely use. Not because the system is unfair—but because most people simply don\\'t know these deductions exist, whether they qualify, or how to document them properly.',
                        did_you_know: 'Did you know? <span class="text-gray-700 font-medium">W-2 employees can take advantage of these deductions as well.</span>',
                        desc2: 'The tax code rewards business activity. When you understand how the rules work, you can legally reduce your tax burden and bring more money back into your household.',
                        list_headline: 'If any of these sound familiar, you\\'re not alone.',
                        list: [
                            'Are taxes taking too much of your income?',
                            'Are rising prices creating stress and financial pressure?',
                            'Are stagnant wages making it hard to get ahead?'
                        ],
                        image: 'Business-Support-Page/IPP_70,000 Pages.jpg'
                    },
                    ideal_for: {
                        headline: 'Business <span class="text-brand-primary">Support</span> Package',
                        desc: 'Business Support Package is available to anyone and is especially beneficial to business owners or those who are considering operating a business. IPP gives you the expert tax, legal, and business support you need to reduce your taxes to the legal minimum, and improve your financial position.',
                        list_headline: 'Business Support Package is ideal for:',
                        list: [
                            'Individuals who want expert tax and financial support',
                            'People who want to stop overpaying taxes',
                            'Business owners who want guidance on deductions',
                            'Business owners who want expert tax, legal, and business support'
                        ],
                        image: 'Business-Support-Page/IPP_Income Power Pro_1.jpg'
                    },
                    features: {
                        list: [
                            'Access to 400+ legitimate tax deductions (where applicable)',
                            'Expert and professional guidance from licensed tax and legal professionals',
                            'Professional CPA support included',
                            'Millions of products and services at discounted prices',
                            'Build monthly recurring referral income (As a PYF Affiliate)',
                            'Education and tools to help you organize and manage your financial life'
                        ],
                        image: 'Business-Support-Page/IPP_Income Power Pro_2.jpg'
                    },
                    advantages: {
                        headline: 'Core <span class="text-brand-primary">Advantages</span>',
                        card1: {
                            image: 'Business-Support-Page/IPP_Core Advantages_Tax Support.jpg',
                            title: 'Tax Support You Can Use Right Away',
                            desc: 'Put more money back into your pocket with professional guidance.',
                            list: [
                                'Learn which deductions apply',
                                'Reduce taxable income legally',
                                'Receive guidance on proper documentation',
                                'Adjust W-2 withholdings when appropriate'
                            ],
                            footer: '*Tax savings vary based on individual circumstances.'
                        },
                        card2: {
                            image: 'Business-Support-Page/IPP_Core Advantages_Business Education.jpg',
                            title: 'Business Education & Financial Literacy',
                            list: [
                                'Financial Planning For Entrepreneurs',
                                'Discounted Business Support Services',
                                'Multi-Millionaire Business Success Coach',
                                'Access to wealth-building strategies'
                            ]
                        },
                        card3: {
                            image: 'Business-Support-Page/IPP_Core Advantages_PYF Support System.jpg',
                            title: 'PYF SUPPORT SYSTEM',
                            desc: 'What\\'s Included with Business Support Package:',
                            list: [
                                'Expert Business Guidance',
                                'Expert Tax Support',
                                'Personal Legal Support',
                                'Business Legal Support',
                                'Home Based/Small Business Education'
                            ]
                        }
                    },
                    value_section: {
                        headline: 'Business Support<span class="text-brand-primary">Package Value</span>',
                        table: [
                            { service: 'Tax Savings (Typical Range)', market: '$250 – $833', included: 'Savings Potential*' },
                            { service: 'Consumer Discount Savings', market: '$50 – $208', included: 'Included Savings Potential*' },
                            { service: 'Business Training & Coaching', market: '$1,500 – $4,500', included: 'Included' },
                            { service: 'CPA Support', market: '$239', included: 'Included' },
                            { service: 'Business Legal Services', market: '$169', included: 'Included' },
                            { service: 'Discount Platform Access', market: '$50', included: 'Included' },
                            { service: 'Community Access', market: '$100 – $300', included: 'Included' }
                        ],
                        total_value: 'Total Monthly Market Value + Savings: $2,358–$6,299 per month',
                        investment: 'Your Investment: $150 per month',
                        bottom_line: 'Bottom line: You\\'re accessing over $6,000 per month in combined market value and potential savings for $150/month—a powerful value proposition backed by professional support.',
                        disclaimer: '*Savings vary based on individual spending habits, use of the platform, and legitimate qualification for deductible expenses.',
                        image: 'Business-Support-Page/IPP_Income Power Pro Value.jpg'
                    },
                    testimonials: {
                        headline: 'Testimonials',
                        desc: 'Since 2011 Pay Yourself First has helped W-2 employees, independent contractors, and entrepreneurs legally reduce tax liability and build compliant home-based businesses. Our affiliates range from teachers and government employees to corporate professionals — all learning to leverage the tax code the way business owners do.',
                        video_url: 'https://www.youtube-nocookie.com/embed/tw-MUhF0-g0?si=YXHjdcaqmfZ83-BB&amp;rel=0&controls=0'
                    },
                    investment_card: {
                        headline: 'Value',
                        price_title: 'Your Investment: $150/Month<br><span class="text-xs md:text-sm font-bold text-gray-600">(Tax-Deductible For Business Owners)</span>',
                        includes_title: 'Includes:',
                        list: [
                            'Tax guidance',
                            'Legal support',
                            'Business training',
                            'Consumer discount platform',
                            'Entrepreneurship resources',
                            'Community support',
                            'Optional affiliate enrollment at no additional cost'
                        ],
                        guarantee: 'Protected by our 30-Day Money-Back Guarantee',
                        btn_text: 'Get Business Support Package',
                        btn_link: 'https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03',
                        image: 'Business-Support-Page/IPP_Value.jpg',
                        image_caption: 'That’s $5 per day to unlock $3,000-$10,000 annually in potential tax savings.'
                    },
                    faq: {
                        headline: 'Common <span class="text-brand-primary">Questions</span>',
                        questions: [
                            { q: 'Can I use Business Support Package without starting a business?', a: 'Yes. Many services apply whether or not you operate a business. However, certain tax benefits require legitimate business activity. You should consult a tax professional for guidance specific to your situation.' },
                            { q: 'Do I need to enroll as an affiliate?', a: 'No. You may purchase Business Support Package standalone with no affiliate enrollment.' },
                            { q: 'Does enrolling as an affiliate cost anything?', a: 'No. Affiliate enrollment is optional. If you choose to enroll, it is provided at no additional cost.' },
                            { q: 'What do affiliates earn?', a: 'Affiliates may receive referral fees when others purchase PYF products through their referral. Referral fee details are described in the affiliate materials you receive after enrollment.' },
                            { q: 'Are earnings guaranteed?', a: 'No. Referral fees depend solely on your personal activity and results vary.' },
                            { q: 'Is Business Support Package a business opportunity?', a: 'No. Business Support Package is a service product. Affiliate enrollment is optional and provided for customers who choose to share PYF services.' },
                            { q: 'What\\'s the difference between a standalone Affiliate and an IPP member who enrolls as an affiliate?', a: 'Both have access to the same affiliate program and can receive the same referral fees. However, Business Support Package members who are also affiliates have access to professional tax support, legal services, business training, and a discount platform—tools that help them build an affiliate business more effectively.' }
                        ]
                    },
                    bottom_cta: {
                        headline: 'Take Control of Your Taxes. Strengthen Your Finances. Move Forward with Confidence.',
                        btn1_text: 'BECOME AN AFFILIATE',
                        btn1_link: 'https://backoffice.pyfaffiliates.com/merchants/login.php#login',
                        btn2_text: 'View Service Packages',
                        btn2_link: 'packages.html'
                    },
                    disclaimer_section: {
                        headline: 'Disclaimer',
                        blocks: [
                            { title: 'Service Provider Disclosure', text: 'Pay Yourself First (PYF) is the administrator of the Income Power Pro program. PYF does not directly provide tax, legal, financial, or discount services. All services included with Income Power Pro are delivered by independent third-party providers. Access to these services is subject to the terms, conditions, and availability of each provider.' },
                            { title: 'Earnings Disclaimer', text: 'Referral fee earnings are not guaranteed and vary based on individual effort and market conditions. Past results do not guarantee future performance.' }
                        ]
                    }
                }"""

pattern_schema = re.compile(r'business:\s*\{\s*hero:.*?items:\s*\[.*?\]\s*\}\s*\}', re.DOTALL)
if not pattern_schema.search(text):
    print("Could not find business schema to replace")
    sys.exit(1)
text = pattern_schema.sub(schema_new, text)

# 2. Replace the UI Block
ui_new = """                        <!-- Business Editor -->
                        <div x-show="activePage === 'business'" x-cloak>
                            <div class="flex justify-between items-center mb-8 bg-white p-4 rounded-xl shadow-sm border border-gray-100">
                                <div>
                                    <h2 class="text-2xl font-extrabold text-gray-800 tracking-tight">Business Pkg Editor</h2>
                                    <p class="text-sm text-gray-500 mt-1 font-medium">Manage the Business Support Package page.</p>
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
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Hero
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><textarea x-model="pageData.business.hero.headline" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description</label><textarea x-model="pageData.business.hero.desc" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 1 Text</label><input type="text" x-model="pageData.business.hero.btn1_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 1 URL</label><input type="text" x-model="pageData.business.hero.btn1_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 2 Text</label><input type="text" x-model="pageData.business.hero.btn2_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 2 URL</label><input type="text" x-model="pageData.business.hero.btn2_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                    <div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Background Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.business.hero.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.hero.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Intro / Tax Deductions -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Tax Deductions Info
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><textarea x-model="pageData.business.intro.headline" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description 1</label><textarea x-model="pageData.business.intro.desc1" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">"Did you know?" Text</label><input type="text" x-model="pageData.business.intro.did_you_know" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description 2</label><textarea x-model="pageData.business.intro.desc2" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                    <div class="mt-4 border-t pt-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">List Headline</label><input type="text" x-model="pageData.business.intro.list_headline" class="w-full px-3 py-2 border rounded mt-1 mb-2"></div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Familiar Points List</label>
                                        <template x-for="(item, index) in pageData.business.intro.list" :key="index">
                                            <div class="flex space-x-2 mb-2">
                                                <input type="text" x-model="pageData.business.intro.list[index]" class="w-full px-3 py-2 border rounded">
                                                <button @click="pageData.business.intro.list.splice(index, 1)" class="text-red-500 hover:text-red-700 px-2 border rounded"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <button @click="pageData.business.intro.list.push('')" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Point</button>
                                    </div>
                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.business.intro.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.intro.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Ideal For -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: "Ideal For" Overview
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.ideal_for.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description</label><textarea x-model="pageData.business.ideal_for.desc" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    <div class="mt-4 border-t pt-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">List Headline</label><input type="text" x-model="pageData.business.ideal_for.list_headline" class="w-full px-3 py-2 border rounded mt-1 mb-2"></div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Target Types List</label>
                                        <template x-for="(item, index) in pageData.business.ideal_for.list" :key="index">
                                            <div class="flex space-x-2 mb-2">
                                                <input type="text" x-model="pageData.business.ideal_for.list[index]" class="w-full px-3 py-2 border rounded">
                                                <button @click="pageData.business.ideal_for.list.splice(index, 1)" class="text-red-500 hover:text-red-700 px-2 border rounded"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <button @click="pageData.business.ideal_for.list.push('')" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Target Type</button>
                                    </div>
                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.business.ideal_for.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.ideal_for.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Features List (Checkmarks) -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Access & Features List
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Features List</label>
                                    <template x-for="(item, index) in pageData.business.features.list" :key="index">
                                        <div class="flex space-x-2 mb-2">
                                            <input type="text" x-model="pageData.business.features.list[index]" class="w-full px-3 py-2 border rounded">
                                            <button @click="pageData.business.features.list.splice(index, 1)" class="text-red-500 hover:text-red-700 px-2 border rounded"><i class="fas fa-trash"></i></button>
                                        </div>
                                    </template>
                                    <button @click="pageData.business.features.list.push('')" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Feature</button>
                                    
                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Image</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.business.features.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.features.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Core Advantages -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Core Advantages Cards
                                    </div>
                                </div>
                                <div class="p-6 space-y-6">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Main Headline</label><input type="text" x-model="pageData.business.advantages.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    
                                    <!-- Card 1 -->
                                    <div class="border p-4 rounded bg-gray-50">
                                        <h4 class="font-bold text-gray-800 mb-4 border-b pb-2">Card 1: Tax Support</h4>
                                        <div class="space-y-4">
                                            <div class="flex items-center space-x-4 mb-2">
                                                <img :src="pageData.business.advantages.card1.image" class="h-16 w-24 object-cover rounded border">
                                                <label class="cursor-pointer bg-white text-gray-700 font-bold py-1 px-3 border rounded">Browse <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.advantages.card1.image')" accept="image/*"></label>
                                            </div>
                                            <div><label class="text-xs font-bold text-gray-700">Title</label><input type="text" x-model="pageData.business.advantages.card1.title" class="w-full px-3 py-2 border rounded"></div>
                                            <div><label class="text-xs font-bold text-gray-700">Description</label><textarea x-model="pageData.business.advantages.card1.desc" class="w-full px-3 py-2 border rounded" rows="2"></textarea></div>
                                            <div>
                                                <label class="text-xs font-bold text-gray-700">Bullet Points</label>
                                                <template x-for="(item, i) in pageData.business.advantages.card1.list" :key="i">
                                                    <div class="flex space-x-2 mt-1">
                                                        <input type="text" x-model="pageData.business.advantages.card1.list[i]" class="w-full px-2 py-1 border rounded text-sm">
                                                        <button @click="pageData.business.advantages.card1.list.splice(i, 1)" class="text-red-500 hover:text-red-700 px-1"><i class="fas fa-trash"></i></button>
                                                    </div>
                                                </template>
                                                <button @click="pageData.business.advantages.card1.list.push('')" class="text-xs text-brand-primary mt-1">+ Add Point</button>
                                            </div>
                                            <div><label class="text-xs font-bold text-gray-700">Footer Text</label><input type="text" x-model="pageData.business.advantages.card1.footer" class="w-full px-3 py-2 border rounded"></div>
                                        </div>
                                    </div>
                                    
                                    <!-- Card 2 -->
                                    <div class="border p-4 rounded bg-gray-50">
                                        <h4 class="font-bold text-gray-800 mb-4 border-b pb-2">Card 2: Business Education</h4>
                                        <div class="space-y-4">
                                            <div class="flex items-center space-x-4 mb-2">
                                                <img :src="pageData.business.advantages.card2.image" class="h-16 w-24 object-cover rounded border">
                                                <label class="cursor-pointer bg-white text-gray-700 font-bold py-1 px-3 border rounded">Browse <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.advantages.card2.image')" accept="image/*"></label>
                                            </div>
                                            <div><label class="text-xs font-bold text-gray-700">Title</label><input type="text" x-model="pageData.business.advantages.card2.title" class="w-full px-3 py-2 border rounded"></div>
                                            <div>
                                                <label class="text-xs font-bold text-gray-700">Bullet Points</label>
                                                <template x-for="(item, i) in pageData.business.advantages.card2.list" :key="i">
                                                    <div class="flex space-x-2 mt-1">
                                                        <input type="text" x-model="pageData.business.advantages.card2.list[i]" class="w-full px-2 py-1 border rounded text-sm">
                                                        <button @click="pageData.business.advantages.card2.list.splice(i, 1)" class="text-red-500 hover:text-red-700 px-1"><i class="fas fa-trash"></i></button>
                                                    </div>
                                                </template>
                                                <button @click="pageData.business.advantages.card2.list.push('')" class="text-xs text-brand-primary mt-1">+ Add Point</button>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Card 3 -->
                                    <div class="border p-4 rounded bg-gray-50">
                                        <h4 class="font-bold text-gray-800 mb-4 border-b pb-2">Card 3: Support System</h4>
                                        <div class="space-y-4">
                                            <div class="flex items-center space-x-4 mb-2">
                                                <img :src="pageData.business.advantages.card3.image" class="h-16 w-24 object-cover rounded border">
                                                <label class="cursor-pointer bg-white text-gray-700 font-bold py-1 px-3 border rounded">Browse <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.advantages.card3.image')" accept="image/*"></label>
                                            </div>
                                            <div><label class="text-xs font-bold text-gray-700">Title</label><input type="text" x-model="pageData.business.advantages.card3.title" class="w-full px-3 py-2 border rounded"></div>
                                            <div><label class="text-xs font-bold text-gray-700">Description</label><input type="text" x-model="pageData.business.advantages.card3.desc" class="w-full px-3 py-2 border rounded"></div>
                                            <div>
                                                <label class="text-xs font-bold text-gray-700">Bullet Points</label>
                                                <template x-for="(item, i) in pageData.business.advantages.card3.list" :key="i">
                                                    <div class="flex space-x-2 mt-1">
                                                        <input type="text" x-model="pageData.business.advantages.card3.list[i]" class="w-full px-2 py-1 border rounded text-sm">
                                                        <button @click="pageData.business.advantages.card3.list.splice(i, 1)" class="text-red-500 hover:text-red-700 px-1"><i class="fas fa-trash"></i></button>
                                                    </div>
                                                </template>
                                                <button @click="pageData.business.advantages.card3.list.push('')" class="text-xs text-brand-primary mt-1">+ Add Point</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Value Table Section -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Value Table
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.value_section.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    
                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Table Rows</label>
                                        <div class="bg-gray-100 p-2 rounded text-xs font-bold flex">
                                            <div class="w-1/3">Service / Benefit</div>
                                            <div class="w-1/3">Typical Monthly Market</div>
                                            <div class="w-1/3">Included with PYF</div>
                                            <div class="w-8"></div>
                                        </div>
                                        <template x-for="(row, i) in pageData.business.value_section.table" :key="i">
                                            <div class="flex space-x-2 mt-2">
                                                <input type="text" x-model="row.service" class="w-1/3 px-2 py-1 flex-1 border rounded text-xs">
                                                <input type="text" x-model="row.market" class="w-1/3 px-2 py-1 flex-1 border rounded text-xs">
                                                <input type="text" x-model="row.included" class="w-1/3 px-2 py-1 flex-1 border rounded text-xs">
                                                <button @click="pageData.business.value_section.table.splice(i, 1)" class="text-red-500 hover:text-red-700 px-2 rounded border"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <button @click="pageData.business.value_section.table.push({service:'', market:'', included:''})" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-2">Add Table Row</button>
                                    </div>

                                    <div class="mt-4 border-t pt-4 space-y-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Total Value Subtext</label><input type="text" x-model="pageData.business.value_section.total_value" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Investment Highlight</label><input type="text" x-model="pageData.business.value_section.investment" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Bottom Line Description</label><textarea x-model="pageData.business.value_section.bottom_line" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Disclaimer / Footnote</label><input type="text" x-model="pageData.business.value_section.disclaimer" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>

                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Image Beside Table</label>
                                        <div class="flex items-center space-x-4">
                                            <img :src="pageData.business.value_section.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.value_section.image')" accept="image/*">
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Testimonials -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Video Testimonials
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.testimonials.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Description</label><textarea x-model="pageData.business.testimonials.desc" class="w-full px-3 py-2 border rounded mt-1" rows="3"></textarea></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">YouTube Video Embed URL</label><input type="text" x-model="pageData.business.testimonials.video_url" class="w-full px-3 py-2 border rounded mt-1" placeholder="https://www.youtube.com/embed/..."></div>
                                </div>
                            </div>

                            <!-- Investment Card -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Investment Summary Card
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.investment_card.headline" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Price Headline</label><input type="text" x-model="pageData.business.investment_card.price_title" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    
                                    <div class="mt-4 border-t pt-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">List Headline</label><input type="text" x-model="pageData.business.investment_card.includes_title" class="w-full px-3 py-2 border rounded mt-1 mb-2"></div>
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-2">Included List Points</label>
                                        <template x-for="(item, index) in pageData.business.investment_card.list" :key="index">
                                            <div class="flex space-x-2 mt-1">
                                                <input type="text" x-model="pageData.business.investment_card.list[index]" class="w-full px-2 py-1 border rounded text-sm">
                                                <button @click="pageData.business.investment_card.list.splice(index, 1)" class="text-red-500 hover:text-red-700 px-2 rounded border"><i class="fas fa-trash"></i></button>
                                            </div>
                                        </template>
                                        <button @click="pageData.business.investment_card.list.push('')" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-2">Add Point</button>
                                    </div>
                                    
                                    <div class="mt-4 border-t pt-4 space-y-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Guarantee Text</label><input type="text" x-model="pageData.business.investment_card.guarantee" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div class="grid grid-cols-2 gap-4">
                                            <div><label class="text-xs font-bold text-gray-700 uppercase">Button Text</label><input type="text" x-model="pageData.business.investment_card.btn_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                            <div><label class="text-xs font-bold text-gray-700 uppercase">Button URL</label><input type="text" x-model="pageData.business.investment_card.btn_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        </div>
                                    </div>

                                    <div class="mt-4 border-t pt-4">
                                        <label class="text-xs font-bold text-gray-700 uppercase block mb-1">Image</label>
                                        <div class="flex items-center space-x-4 mb-2">
                                            <img :src="pageData.business.investment_card.image" class="h-20 w-32 object-cover rounded border">
                                            <label class="cursor-pointer bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold py-2 px-4 rounded transition border">
                                                <i class="fas fa-folder-open mr-2"></i> Browse
                                                <input type="file" class="hidden" @change="uploadImageTo($event, 'pageData.business.investment_card.image')" accept="image/*">
                                            </label>
                                        </div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Image Caption (Highlights)</label><input type="text" x-model="pageData.business.investment_card.image_caption" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                </div>
                            </div>

                            <!-- FAQ Section -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: FAQ
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.faq.headline" class="w-full px-3 py-2 border rounded mt-1 mb-4"></div>
                                    
                                    <template x-for="(faq, i) in pageData.business.faq.questions" :key="i">
                                        <div class="border bg-gray-50 p-4 rounded mb-4 relative">
                                            <button @click="pageData.business.faq.questions.splice(i, 1)" class="absolute top-2 right-2 text-red-500 hover:text-red-700"><i class="fas fa-times"></i></button>
                                            <div class="mb-2">
                                                <label class="text-xs font-bold text-gray-700">Question</label>
                                                <input type="text" x-model="faq.q" class="w-full px-3 py-2 border rounded text-sm bg-white">
                                            </div>
                                            <div>
                                                <label class="text-xs font-bold text-gray-700">Answer</label>
                                                <textarea x-model="faq.a" class="w-full px-3 py-2 border rounded text-sm bg-white" rows="2"></textarea>
                                            </div>
                                        </div>
                                    </template>
                                    <button @click="pageData.business.faq.questions.push({q: '', a: ''})" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Question</button>
                                </div>
                            </div>

                            <!-- Bottom CTA -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Bottom CTA
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><textarea x-model="pageData.business.bottom_cta.headline" class="w-full px-3 py-2 border rounded mt-1" rows="2"></textarea></div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 1 Text</label><input type="text" x-model="pageData.business.bottom_cta.btn1_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 1 URL</label><input type="text" x-model="pageData.business.bottom_cta.btn1_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-4">
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 2 Text</label><input type="text" x-model="pageData.business.bottom_cta.btn2_text" class="w-full px-3 py-2 border rounded mt-1"></div>
                                        <div><label class="text-xs font-bold text-gray-700 uppercase">Button 2 URL</label><input type="text" x-model="pageData.business.bottom_cta.btn2_link" class="w-full px-3 py-2 border rounded mt-1"></div>
                                    </div>
                                </div>
                            </div>

                            <!-- Disclaimer -->
                            <div class="bg-white rounded-xl shadow-soft border border-gray-100 mb-6 overflow-hidden">
                                <div class="bg-gray-50 px-4 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div class="flex items-center text-gray-600 font-bold text-sm">
                                        <i class="fas fa-grip-vertical mr-3 text-gray-400"></i> Section: Disclaimer
                                    </div>
                                </div>
                                <div class="p-6 space-y-4">
                                    <div><label class="text-xs font-bold text-gray-700 uppercase">Headline</label><input type="text" x-model="pageData.business.disclaimer_section.headline" class="w-full px-3 py-2 border rounded mt-1 mb-4"></div>
                                    
                                    <template x-for="(block, i) in pageData.business.disclaimer_section.blocks" :key="i">
                                        <div class="border bg-gray-50 p-4 rounded mb-4 relative">
                                            <button @click="pageData.business.disclaimer_section.blocks.splice(i, 1)" class="absolute top-2 right-2 text-red-500 hover:text-red-700"><i class="fas fa-times"></i></button>
                                            <div class="mb-2">
                                                <label class="text-xs font-bold text-gray-700">Block Title</label>
                                                <input type="text" x-model="block.title" class="w-full px-3 py-2 border rounded text-sm bg-white">
                                            </div>
                                            <div>
                                                <label class="text-xs font-bold text-gray-700">Content Text</label>
                                                <textarea x-model="block.text" class="w-full px-3 py-2 border rounded text-sm bg-white" rows="2"></textarea>
                                            </div>
                                        </div>
                                    </template>
                                    <button @click="pageData.business.disclaimer_section.blocks.push({title: '', text: ''})" class="text-xs font-bold text-brand-primary border border-brand-primary px-3 py-1 rounded mt-1">Add Block</button>
                                </div>
                            </div>
                        </div>"""

pattern_ui = re.compile(r'<!-- Business Editor -->\s*<div x-show="activePage === \'business\'" x-cloak>.*?</div>\s*</div>\s*</div>\s*</main>', re.DOTALL)
if not pattern_ui.search(text):
    print("Could not find business UI to replace")
    sys.exit(1)
    
text = pattern_ui.sub(ui_new + '\n                    </div>\n                </div>\n        </main>', text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("done")
