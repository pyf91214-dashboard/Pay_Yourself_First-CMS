import re
import sys

file_path = r"d:\Sapphire Leads\Pay Yourself First Website\Pyf-dashboard with my Mail\business-support-package.html"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Tax Deductions Intro Section
intro_target = """                    <div>
                        <h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark mb-6 leading-tight">
                            Most People Don't Understand Enough About Business Tax Deductions. Even those who own businesses. Why would they? The United States tax code is over 70,000 pages long!
                        </h2>
                        <p class="text-gray-700 mb-6 leading-relaxed">
                            Business owners have access to over 400 tax deductions that W-2 employees rarely use. Not because the system is unfair—but because most people simply don't know these deductions exist, whether they qualify, or how to document them properly.
                        </p>
                        <p class="text-brand-primary font-bold text-lg mb-8">
                            Did you know? <span class="text-gray-700 font-medium">W-2 employees can take advantage of these deductions as well.</span>
                        </p>
                        <p class="text-gray-700 mb-6 leading-relaxed">
                            The tax code rewards business activity. When you understand how the rules work, you can legally reduce your tax burden and bring more money back into your household.
                        </p>
                        
                        <h3 class="text-xl font-bold text-brand-dark mb-6">If any of these sound familiar, you're not alone.</h3>
                        <ul class="space-y-3">
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] mt-1 mr-3"></i>
                                <span class="text-gray-700 font-medium">Are taxes taking too much of your income?</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] mt-1 mr-3"></i>
                                <span class="text-gray-700 font-medium">Are rising prices creating stress and financial pressure?</span>
                            </li>
                            <li class="flex items-start">
                                <i class="fas fa-exclamation-triangle text-[#C0392B] mt-1 mr-3"></i>
                                <span class="text-gray-700 font-medium">Are stagnant wages making it hard to get ahead?</span>
                            </li>
                        </ul>
                    </div>
                    <div class="h-full min-h-[500px]">
                        <img src="Business-Support-Page/IPP_70,000 Pages.jpg" alt="Consulting discussion" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>"""

intro_new = """                    <div>
                        <h2 class="text-2xl md:text-3xl font-extrabold text-brand-dark mb-6 leading-tight" x-text="pageData.business.intro.headline">
                        </h2>
                        <p class="text-gray-700 mb-6 leading-relaxed" x-text="pageData.business.intro.desc1">
                        </p>
                        <p class="text-brand-primary font-bold text-lg mb-8" x-html="pageData.business.intro.did_you_know">
                        </p>
                        <p class="text-gray-700 mb-6 leading-relaxed" x-text="pageData.business.intro.desc2">
                        </p>
                        
                        <h3 class="text-xl font-bold text-brand-dark mb-6" x-text="pageData.business.intro.list_headline"></h3>
                        <ul class="space-y-3">
                            <template x-for="(item, i) in pageData.business.intro.list" :key="i">
                                <li class="flex items-start">
                                    <i class="fas fa-exclamation-triangle text-[#C0392B] mt-1 mr-3"></i>
                                    <span class="text-gray-700 font-medium" x-text="item"></span>
                                </li>
                            </template>
                        </ul>
                    </div>
                    <div class="h-full min-h-[500px]">
                        <img :src="pageData.business.intro.image" alt="Consulting discussion" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>"""
text = text.replace(intro_target, intro_new)


# 2. Ideal For
ideal_target = """                    <div class="h-[400px]">
                        <img src="Business-Support-Page/IPP_Income Power Pro_1.jpg" alt="Cash in pocket" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                    <div>
                        <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-6">
                            Business <span class="text-brand-primary">Support</span> Package
                        </h2>
                        <p class="text-gray-700 mb-8 leading-relaxed">
                            Business Support Package is available to anyone and is especially beneficial to business owners or those who are considering operating a business. IPP gives you the expert tax, legal, and business support you need to reduce your taxes to the legal minimum, and improve your financial position.
                        </p>
                        <h4 class="text-lg font-bold text-brand-dark mb-4">Business Support Package is ideal for:</h4>
                        <ul class="space-y-4">
                            <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i> <span class="text-gray-700">Individuals who want expert tax and financial support</span></li>
                            <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i> <span class="text-gray-700">People who want to stop overpaying taxes</span></li>
                            <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i> <span class="text-gray-700">Business owners who want guidance on deductions</span></li>
                            <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i> <span class="text-gray-700">Business owners who want expert tax, legal, and business support</span></li>
                        </ul>
                    </div>"""

ideal_new = """                    <div class="h-[400px]">
                        <img :src="pageData.business.ideal_for.image" alt="Cash in pocket" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                    <div>
                        <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-6" x-html="pageData.business.ideal_for.headline">
                        </h2>
                        <p class="text-gray-700 mb-8 leading-relaxed" x-text="pageData.business.ideal_for.desc">
                        </p>
                        <h4 class="text-lg font-bold text-brand-dark mb-4" x-text="pageData.business.ideal_for.list_headline"></h4>
                        <ul class="space-y-4">
                            <template x-for="(item, i) in pageData.business.ideal_for.list" :key="i">
                                <li class="flex items-start"><i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i> <span class="text-gray-700" x-text="item"></span></li>
                            </template>
                        </ul>
                    </div>"""
text = text.replace(ideal_target, ideal_new)

# 3. Features
features_target = """                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                    <div>
                        <ul class="space-y-5">
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Access to 400+ legitimate tax deductions (where applicable)</span></li>
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Expert and professional guidance from licensed tax and legal professionals</span></li>
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Professional CPA support included</span></li>
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Millions of products and services at discounted prices</span></li>
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Build monthly recurring referral income (As a PYF Affiliate)</span></li>
                            <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800">Education and tools to help you organize and manage your financial life</span></li>
                        </ul>
                    </div>
                    <div class="h-[400px]">
                        <img src="Business-Support-Page/IPP_Income Power Pro_2.jpg" alt="Consultation" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                </div>"""

features_new = """                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                    <div>
                        <ul class="space-y-5">
                            <template x-for="(item, i) in pageData.business.features.list" :key="i">
                                <li class="flex items-center"><div class="w-8 h-8 rounded-full bg-brand-primary text-white flex items-center justify-center mr-4 shrink-0"><i class="fas fa-check"></i></div> <span class="font-bold text-gray-800" x-text="item"></span></li>
                            </template>
                        </ul>
                    </div>
                    <div class="h-[400px]">
                        <img :src="pageData.business.features.image" alt="Consultation" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                </div>"""
text = text.replace(features_target, features_new)

# 4. Advantages
advantages_target = """        <section class="py-16 md:py-24 bg-white">
            <div class="container mx-auto px-4 text-center">
                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-16">
                    Core <span class="text-brand-primary">Advantages</span>
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto">
                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img src="Business-Support-Page/IPP_Core Advantages_Tax Support.jpg" alt="Tax Support" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-primary mb-4">Tax Support You Can Use Right Away</h3>
                            <p class="text-sm text-gray-600 mb-6">Put more money back into your pocket with professional guidance.</p>
                            <ul class="space-y-3 text-sm text-gray-700">
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Learn which deductions apply</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Reduce taxable income legally</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Receive guidance on proper documentation</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Adjust W-2 withholdings when appropriate</li>
                            </ul>
                            <p class="text-[10px] text-gray-400 italic mt-6">*Tax savings vary based on individual circumstances.</p>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img src="Business-Support-Page/IPP_Core Advantages_Business Education.jpg" alt="Business Education" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-primary mb-4">Business Education & Financial Literacy</h3>
                            <ul class="space-y-3 text-sm text-gray-700 mt-6">
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Financial Planning For Entrepreneurs</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Discounted Business Support Services</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Multi-Millionaire Business Success Coach</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Access to wealth-building strategies</li>
                            </ul>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img src="Business-Support-Page/IPP_Core Advantages_PYF Support System.jpg" alt="Support System" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-dark mb-2">PYF SUPPORT SYSTEM</h3>
                            <p class="text-xs font-bold text-brand-primary mb-6">What's Included with Business Support Package:</p>
                            <ul class="space-y-3 text-sm text-gray-700">
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Expert Business Guidance</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Expert Tax Support</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Personal Legal Support</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Business Legal Support</li>
                                <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> Home Based/Small Business Education</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

advantages_new = """        <section class="py-16 md:py-24 bg-white">
            <div class="container mx-auto px-4 text-center">
                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-16" x-html="pageData.business.advantages.headline">
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto">
                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img :src="pageData.business.advantages.card1.image" alt="Tax Support" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-primary mb-4" x-text="pageData.business.advantages.card1.title"></h3>
                            <p class="text-sm text-gray-600 mb-6" x-text="pageData.business.advantages.card1.desc"></p>
                            <ul class="space-y-3 text-sm text-gray-700">
                                <template x-for="(item, i) in pageData.business.advantages.card1.list" :key="i">
                                    <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> <span x-text="item"></span></li>
                                </template>
                            </ul>
                            <p class="text-[10px] text-gray-400 italic mt-6" x-text="pageData.business.advantages.card1.footer"></p>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img :src="pageData.business.advantages.card2.image" alt="Business Education" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-primary mb-4" x-text="pageData.business.advantages.card2.title"></h3>
                            <ul class="space-y-3 text-sm text-gray-700 mt-6">
                                <template x-for="(item, i) in pageData.business.advantages.card2.list" :key="i">
                                    <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> <span x-text="item"></span></li>
                                </template>
                            </ul>
                        </div>
                    </div>

                    <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100 flex flex-col">
                        <img :src="pageData.business.advantages.card3.image" alt="Support System" class="h-48 w-full object-cover">
                        <div class="p-8 text-left flex-grow">
                            <h3 class="text-lg font-bold text-brand-dark mb-2" x-text="pageData.business.advantages.card3.title"></h3>
                            <p class="text-xs font-bold text-brand-primary mb-6" x-text="pageData.business.advantages.card3.desc"></p>
                            <ul class="space-y-3 text-sm text-gray-700">
                                <template x-for="(item, i) in pageData.business.advantages.card3.list" :key="i">
                                    <li class="flex items-start"><i class="fas fa-check-square text-brand-primary mt-1 mr-2"></i> <span x-text="item"></span></li>
                                </template>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
text = text.replace(advantages_target, advantages_new)

# 5. Value Section
value_target = """                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-12">
                    Business Support<span class="text-brand-primary">Package Value</span>
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                    <div>
                        <div class="overflow-hidden rounded-lg shadow-lg border border-gray-200 bg-white mb-8">
                            <table class="w-full text-left text-sm">
                                <thead class="bg-[#0f766e] text-white">
                                    <tr>
                                        <th class="p-4 font-bold">Service / Benefit</th>
                                        <th class="p-4 font-bold">Typical Monthly Market</th>
                                        <th class="p-4 font-bold">Included with PYF</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-gray-100">
                                    <tr><td class="p-4">Tax Savings (Typical Range)</td><td class="p-4 text-gray-600">$250 – $833</td><td class="p-4 font-bold text-brand-primary">Savings Potential*</td></tr>
                                    <tr class="bg-gray-50"><td class="p-4">Consumer Discount Savings</td><td class="p-4 text-gray-600">$50 – $208</td><td class="p-4 font-bold text-brand-primary">Included Savings Potential*</td></tr>
                                    <tr><td class="p-4">Business Training & Coaching</td><td class="p-4 text-gray-600">$1,500 – $4,500</td><td class="p-4 font-bold">Included</td></tr>
                                    <tr class="bg-gray-50"><td class="p-4">CPA Support</td><td class="p-4 text-gray-600">$239</td><td class="p-4 font-bold">Included</td></tr>
                                    <tr><td class="p-4">Business Legal Services</td><td class="p-4 text-gray-600">$169</td><td class="p-4 font-bold">Included</td></tr>
                                    <tr class="bg-gray-50"><td class="p-4">Discount Platform Access</td><td class="p-4 text-gray-600">$50</td><td class="p-4 font-bold">Included</td></tr>
                                    <tr><td class="p-4">Community Access</td><td class="p-4 text-gray-600">$100 – $300</td><td class="p-4 font-bold">Included</td></tr>
                                </tbody>
                            </table>
                        </div>

                        <p class="text-brand-primary font-bold text-lg mb-2">Total Monthly Market Value + Savings: $2,358–$6,299 per month</p>
                        <p class="text-brand-dark font-black text-xl mb-6">Your Investment: $150 per month</p>
                        
                        <p class="text-gray-700 text-sm leading-relaxed mb-6 font-medium">
                            Bottom line: You're accessing over $6,000 per month in combined market value and potential savings for $150/month—a powerful value proposition backed by professional support.
                        </p>
                        <p class="text-gray-500 text-xs italic">
                            *Savings vary based on individual spending habits, use of the platform, and legitimate qualification for deductible expenses.
                        </p>
                    </div>

                    <div class="h-full min-h-[500px]">
                        <img src="Business-Support-Page/IPP_Income Power Pro Value.jpg" alt="Value Discussion" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                </div>"""

value_new = """                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-12" x-html="pageData.business.value_section.headline">
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                    <div>
                        <div class="overflow-hidden rounded-lg shadow-lg border border-gray-200 bg-white mb-8">
                            <table class="w-full text-left text-sm">
                                <thead class="bg-[#0f766e] text-white">
                                    <tr>
                                        <th class="p-4 font-bold">Service / Benefit</th>
                                        <th class="p-4 font-bold">Typical Monthly Market</th>
                                        <th class="p-4 font-bold">Included with PYF</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-gray-100">
                                    <template x-for="(row, i) in pageData.business.value_section.table" :key="i">
                                        <tr :class="{'bg-gray-50': i % 2 !== 0}">
                                            <td class="p-4" x-text="row.service"></td>
                                            <td class="p-4 text-gray-600" x-text="row.market"></td>
                                            <td class="p-4 font-bold text-brand-primary" :class="{'text-gray-800': row.included === 'Included'}" x-text="row.included"></td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>

                        <p class="text-brand-primary font-bold text-lg mb-2" x-text="pageData.business.value_section.total_value"></p>
                        <p class="text-brand-dark font-black text-xl mb-6" x-text="pageData.business.value_section.investment"></p>
                        
                        <p class="text-gray-700 text-sm leading-relaxed mb-6 font-medium" x-text="pageData.business.value_section.bottom_line">
                        </p>
                        <p class="text-gray-500 text-xs italic" x-text="pageData.business.value_section.disclaimer">
                        </p>
                    </div>

                    <div class="h-full min-h-[500px]">
                        <img :src="pageData.business.value_section.image" alt="Value Discussion" class="rounded-[2rem] shadow-xl w-full h-full object-cover">
                    </div>
                </div>"""
text = text.replace(value_target, value_new)

# 6. Testimonials
test_target = """            <div class="max-w-5xl mx-auto text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-extrabold uppercase mb-6 text-brand-dark tracking-wide">
                    Testimonials
                </h2>
                <p class="text-base md:text-lg text-gray-600 leading-relaxed">
                    Since 2011 Pay Yourself First has helped W-2 employees, independent contractors, and entrepreneurs legally reduce tax liability and build compliant home-based businesses. Our affiliates range from teachers and government employees to corporate professionals — all learning to leverage the tax code the way business owners do.
                </p>
            </div>

            <div class="relative max-w-4xl mx-auto rounded-2xl overflow-hidden shadow-[0_8px_30px_rgba(0,0,0,0.12)] bg-black aspect-video">
                
                <iframe 
                    class="absolute inset-0 w-full h-full"
                    src="https://www.youtube-nocookie.com/embed/tw-MUhF0-g0?si=YXHjdcaqmfZ83-BB&amp;rel=0&controls=0" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                </iframe>

            </div>"""

test_new = """            <div class="max-w-5xl mx-auto text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-extrabold uppercase mb-6 text-brand-dark tracking-wide" x-text="pageData.business.testimonials.headline">
                </h2>
                <p class="text-base md:text-lg text-gray-600 leading-relaxed" x-text="pageData.business.testimonials.desc">
                </p>
            </div>

            <div class="relative max-w-4xl mx-auto rounded-2xl overflow-hidden shadow-[0_8px_30px_rgba(0,0,0,0.12)] bg-black aspect-video">
                
                <iframe 
                    class="absolute inset-0 w-full h-full"
                    :src="pageData.business.testimonials.video_url" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                </iframe>

            </div>"""
text = text.replace(test_target, test_new)

# 7. Investment Card
inv_target = """                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-16 text-center">
                    Value
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
                    
                    <div class="bg-white rounded-xl shadow-2xl border border-gray-100 overflow-hidden">
                        <div class="bg-[#E0FFCC] p-6 text-center border-b border-[#bbf7d0] mr-8 ml-8 mt-8 rounded-md">
                            <h3 class="text-brand-dark font-black uppercase text-sm md:text-2xl leading-snug">
                                Your Investment: $150/Month<br>
                                <span class="text-xs md:text-sm font-bold text-gray-600">(Tax-Deductible For Business Owners)</span>
                            </h3>
                        </div>

                        <div class="p-8">
                            <h4 class="font-bold text-gray-900 text-sm mb-6 uppercase">Includes:</h4>
                            <ul class="space-y-4 mb-8">
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Tax guidance</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Legal support</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Business training</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Consumer discount platform</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Entrepreneurship resources</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Community support</span>
                                </li>
                                <li class="flex items-center">
                                    <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                    <span class="text-gray-700 font-bold text-sm">Optional affiliate enrollment at no additional cost</span>
                                </li>
                            </ul>

                            <p class="text-md font-bold text-gray-900 mb-6">
                                Protected by our 30-Day Money-Back Guarantee
                            </p>

                            <a href="https://buy.stripe.com/8x2aEQe300Gjgyg19CcIE03" target="_blank" class="block w-full bg-[#4a8a0a] hover:bg-[#389400] text-white font-bold py-4 rounded shadow transition text-center text-sm uppercase tracking-wide">
                                Get Business Support Package
                            </a>
                        </div>
                    </div>

                    <div>
                        <div class="rounded-xl overflow-hidden shadow-lg mb-6 h-[400px]">
                            <img src="Business-Support-Page/IPP_Value.jpg" 
                                 alt="Handshake Deal" 
                                 class="w-full h-full object-cover">
                        </div>
                        
                        <div class="bg-[#dcfce7] p-4 rounded-lg text-center border border-[#bbf7d0]">
                            <p class="text-xs md:text-xs font-bold text-gray-800">
                                That’s $5 per day to unlock $3,000-$10,000 annually in potential tax savings.
                            </p>
                        </div>
                    </div>

                </div>"""

inv_new = """                <h2 class="text-3xl font-extrabold text-brand-dark uppercase mb-16 text-center" x-text="pageData.business.investment_card.headline">
                </h2>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
                    
                    <div class="bg-white rounded-xl shadow-2xl border border-gray-100 overflow-hidden">
                        <div class="bg-[#E0FFCC] p-6 text-center border-b border-[#bbf7d0] mr-8 ml-8 mt-8 rounded-md">
                            <h3 class="text-brand-dark font-black uppercase text-sm md:text-2xl leading-snug" x-html="pageData.business.investment_card.price_title">
                            </h3>
                        </div>

                        <div class="p-8">
                            <h4 class="font-bold text-gray-900 text-sm mb-6 uppercase" x-text="pageData.business.investment_card.includes_title"></h4>
                            <ul class="space-y-4 mb-8">
                                <template x-for="(item, i) in pageData.business.investment_card.list" :key="i">
                                    <li class="flex items-center">
                                        <i class="fas fa-check-circle text-brand-primary text-xl mr-3"></i>
                                        <span class="text-gray-700 font-bold text-sm" x-text="item"></span>
                                    </li>
                                </template>
                            </ul>

                            <p class="text-md font-bold text-gray-900 mb-6" x-text="pageData.business.investment_card.guarantee">
                            </p>

                            <a :href="pageData.business.investment_card.btn_link" target="_blank" class="block w-full bg-[#4a8a0a] hover:bg-[#389400] text-white font-bold py-4 rounded shadow transition text-center text-sm uppercase tracking-wide" x-text="pageData.business.investment_card.btn_text">
                            </a>
                        </div>
                    </div>

                    <div>
                        <div class="rounded-xl overflow-hidden shadow-lg mb-6 h-[400px]">
                            <img :src="pageData.business.investment_card.image" 
                                 alt="Handshake Deal" 
                                 class="w-full h-full object-cover">
                        </div>
                        
                        <div class="bg-[#dcfce7] p-4 rounded-lg text-center border border-[#bbf7d0]">
                            <p class="text-xs md:text-xs font-bold text-gray-800" x-text="pageData.business.investment_card.image_caption">
                            </p>
                        </div>
                    </div>

                </div>"""
text = text.replace(inv_target, inv_new)

# 8. FAQ
faq_target = """                <h2 class="text-3xl font-extrabold text-center text-brand-dark uppercase mb-12">
                    Common <span class="text-brand-primary">Questions</span>
                </h2>

                <div class="space-y-4">
                    
                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">Can I use Business Support Package without starting a business?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            Yes. Many services apply whether or not you operate a business. However, certain tax benefits require legitimate business activity. You should consult a tax professional for guidance specific to your situation.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">Do I need to enroll as an affiliate?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            No. You may purchase Business Support Package standalone with no affiliate enrollment.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">Does enrolling as an affiliate cost anything?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            No. Affiliate enrollment is optional. If you choose to enroll, it is provided at no additional cost.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">What do affiliates earn?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            Affiliates may receive referral fees when others purchase PYF products through their referral. Referral fee details are described in the affiliate materials you receive after enrollment.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">Are earnings guaranteed?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            No. Referral fees depend solely on your personal activity and results vary.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">Is Business Support Package a business opportunity?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            No. Business Support Package is a service product. Affiliate enrollment is optional and provided for customers who choose to share PYF services.
                        </div>
                    </div>

                    <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
                        <button class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                            <span class="font-bold text-gray-900 text-left pr-4">What's the difference between a standalone Affiliate and an IPP member who enrolls as an affiliate?</span>
                            <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content hidden p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed">
                            Both have access to the same affiliate program and can receive the same referral fees. However, Business Support Package members who are also affiliates have access to professional tax support, legal services, business training, and a discount platform—tools that help them build an affiliate business more effectively.
                        </div>
                    </div>

                </div>"""

faq_new = """                <h2 class="text-3xl font-extrabold text-center text-brand-dark uppercase mb-12" x-html="pageData.business.faq.headline">
                </h2>

                <div class="space-y-4">
                    <template x-for="(faq, i) in pageData.business.faq.questions" :key="i">
                        <div class="border border-gray-200 rounded-lg overflow-hidden bg-white" x-data="{ open: false }">
                            <button @click="open = !open" class="faq-btn w-full flex justify-between items-center p-6 hover:bg-gray-50 transition focus:outline-none">
                                <span class="font-bold text-gray-900 text-left pr-4" x-text="faq.q"></span>
                                <i class="fas fa-chevron-down text-brand-primary transform transition-transform duration-300" :class="{'rotate-180': open}"></i>
                            </button>
                            <div x-show="open" class="faq-content p-6 border-t border-gray-100 text-gray-600 text-sm leading-relaxed" x-text="faq.a" x-transition>
                            </div>
                        </div>
                    </template>
                </div>"""
text = text.replace(faq_target, faq_new)

# 9. Bottom CTA
cta_target = """                <h2 class="text-2xl md:text-2xl font-extrabold text-brand-dark uppercase mb-8">
                    Take Control of Your Taxes. Strengthen Your Finances. Move Forward with Confidence.
              
                    </h2>
                
              

                <div class="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-6">
                    
                    <a href="https://backoffice.pyfaffiliates.com/merchants/login.php#login
" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide">
                       BECOME AN AFFILIATE
                    </a>



                    <a href="packages.html" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide">
                       View Service Packages
                    </a>

                </div>"""

cta_new = """                <h2 class="text-2xl md:text-2xl font-extrabold text-brand-dark uppercase mb-8" x-text="pageData.business.bottom_cta.headline">
                </h2>

                <div class="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-6">
                    <a :href="pageData.business.bottom_cta.btn1_link" target="_blank" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide" x-text="pageData.business.bottom_cta.btn1_text">
                    </a>

                    <a :href="pageData.business.bottom_cta.btn2_link" class="w-full md:w-auto bg-gradient-to-r from-[#389400] to-[#75C400] text-white font-bold py-4 px-8 rounded shadow hover:shadow-lg hover:opacity-95 transition uppercase text-sm tracking-wide" x-text="pageData.business.bottom_cta.btn2_text">
                    </a>
                </div>"""
text = text.replace(cta_target, cta_new)

# 10. Disclaimer
disc_target = """                <h3 class="text-2xl font-bold text-brand-dark uppercase mb-8 pb-4 border-b border-gray-200 inline-block px-12">
                    Disclaimer
                </h3>

                <div class="space-y-6 text-sm text-gray-500 leading-relaxed max-w-5xl mx-auto">
                    <div>
                        <strong class="text-brand-dark block mb-1">Service Provider Disclosure</strong>
                        <p>Pay Yourself First (PYF) is the administrator of the Income Power Pro program. PYF does not directly provide tax, legal, financial, or discount services. All services included with Income Power Pro are delivered by independent third-party providers. Access to these services is subject to the terms, conditions, and availability of each provider.</p>
                    </div>

                    <div>
                        <strong class="text-brand-dark block mb-1">Earnings Disclaimer</strong>
                        <p>Referral fee earnings are not guaranteed and vary based on individual effort and market conditions. Past results do not guarantee future performance.</p>
                    </div>
                </div>"""

disc_new = """                <h3 class="text-2xl font-bold text-brand-dark uppercase mb-8 pb-4 border-b border-gray-200 inline-block px-12" x-text="pageData.business.disclaimer_section.headline">
                </h3>

                <div class="space-y-6 text-sm text-gray-500 leading-relaxed max-w-5xl mx-auto">
                    <template x-for="(block, i) in pageData.business.disclaimer_section.blocks" :key="i">
                        <div>
                            <strong class="text-brand-dark block mb-1" x-text="block.title"></strong>
                            <p x-text="block.text"></p>
                        </div>
                    </template>
                </div>"""
text = text.replace(disc_target, disc_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("done")
