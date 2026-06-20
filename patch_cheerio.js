const fs = require('fs');
const cheerio = require('cheerio');

// Load HTML
let html = fs.readFileSync('about-us.html', 'utf8');

// The initialization script
const scriptBlock = `
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
<script>
    const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
    document.addEventListener('alpine:init', () => {
        const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
        Alpine.data('siteData', () => ({
            pageData: {
                about_us: {
                    hero: {}, who_we_are: { list: [] }, origin: { list: [] }, mission: {},
                    serving: { stats: [], principles: [] }, system: { cards: [] },
                    who_we_serve: { list: [] }, different: { list: [] }, pledge: { list: [] }, journey: {}
                }
            },
            async init() {
                try {
                    let { data } = await supabase.from('site_content').select('*').eq('page_id', 'about_us').single();
                    if (data) {
                        const loadedContent = new URLSearchParams(window.location.search).get('mode') === 'preview' ? data.draft_content : data.live_content;
                        if(loadedContent) this.pageData.about_us = { ...this.pageData.about_us, ...loadedContent };
                    }
                } catch (e) { console.error("CMS Load Error", e); }
            }
        }));
    });
</script>
`;

const $ = cheerio.load(html, { decodeEntities: false });

// 1. Setup Body
$('body').attr('x-data', 'siteData').attr('x-cloak', '');
if (!$('script[src*="alpinejs"]').length) {
    $('body').append(scriptBlock);
}

// 2. Headings and Paragraphs
$('h1').each((i, el) => {
    if ($(el).text().includes("Here To Help")) {
        $(el).attr('x-html', 'pageData.about_us.hero.headline').empty();
    }
});

$('p').each((i, el) => {
    let t = $(el).text();
    if (t.includes("Pay Yourself First was created")) {
        $(el).attr('x-text', 'pageData.about_us.hero.desc').empty();
    }
    if (t.includes("Pay Yourself First (PYF) is a financial empowerment")) {
        $(el).attr('x-html', 'pageData.about_us.who_we_are.desc1').empty();
    }
    if (t.includes("As the cost of living rises")) {
        $(el).attr('x-text', 'pageData.about_us.who_we_are.desc2').empty();
    }
    if (t.includes("PYF was created to solve these problems")) {
        $(el).attr('x-text', 'pageData.about_us.who_we_are.desc3').empty();
    }
    if (t.includes("Our company is built around a system")) {
        $(el).attr('x-text', 'pageData.about_us.who_we_are.desc4').empty();
    }
    if (t.includes("PYF was built by financial professionals with decades")) {
        $(el).attr('x-text', 'pageData.about_us.origin.desc1').empty();
    }
    if (t.includes("The team behind PYF recognized a gap")) {
        $(el).attr('x-text', 'pageData.about_us.origin.desc2').empty();
    }
    if (t.includes("To help everyday people gain control")) {
        $(el).attr('x-text', 'pageData.about_us.mission.desc').empty();
    }
    if (t.includes("Financial control comes from mastering three critical levers")) {
        $(el).attr('x-text', 'pageData.about_us.system.subtitle').empty();
    }
    if (t.includes("If financial improvement is your goal")) {
        $(el).attr('x-text', 'pageData.about_us.who_we_serve.footer').empty();
    }
    if (t.includes("Choose the path that fits your goals today")) {
        $(el).attr('x-text', 'pageData.about_us.journey.desc').text('');
    }
});

$('h2').each((i, el) => {
    let t = $(el).text();
    if (t.includes("Who") && t.includes("We Are")) {
        $(el).attr('x-html', 'pageData.about_us.who_we_are.headline').empty();
        // Target Who We Are list
        let ul = $(el).nextAll('ul').first();
        if (ul.length) {
            ul.empty().append(`
                <template x-for="(item, idx) in pageData.about_us.who_we_are.list" :key="idx">
                    <li class="flex items-start">
                        <i class="fas fa-check text-brand-primary mt-1 mr-3 flex-shrink-0"></i>
                        <span class="text-gray-700 text-lg leading-relaxed" x-html="item"></span>
                    </li>
                </template>
            `);
        }
    }
    if (t.includes("Origin")) {
        $(el).attr('x-html', 'pageData.about_us.origin.headline').empty();
        let ul = $(el).nextAll('ul').first();
        if (ul.length) {
            ul.empty().append(`
                <template x-for="(item, idx) in pageData.about_us.origin.list" :key="idx">
                    <li class="flex items-start">
                        <i class="fas fa-exclamation-triangle text-[#C0392B] text-xl mt-1 mr-4 flex-shrink-0"></i>
                        <span class="text-gray-700 font-medium" x-html="item"></span>
                    </li>
                </template>
            `);
        }
    }
    if (t.includes("Mission")) {
        $(el).attr('x-html', 'pageData.about_us.mission.headline').empty();
    }
    if (t.includes("Serving Everyday Americans")) {
        $(el).attr('x-html', 'pageData.about_us.serving.headline').empty();
        let statsContainer = $(el).nextAll('div.flex').first();
        if (statsContainer.length) {
            statsContainer.empty().append(`
                <template x-for="(stat, idx) in pageData.about_us.serving.stats" :key="idx">
                    <div class="px-8 py-10 text-center w-full md:w-1/3 hover:bg-gray-50 transition duration-300">
                        <h4 class="text-3xl font-extrabold text-[#111827] mb-2 uppercase tracking-wide" x-text="stat.title"></h4>
                        <p class="text-gray-600 font-medium leading-relaxed" x-text="stat.desc"></p>
                    </div>
                </template>
            `);
        }
    }
    if (t.includes("A system, not a personality")) {
        $(el).attr('x-html', 'pageData.about_us.system.headline').empty();
    }
    if (t.includes("Who We") && t.includes("Serve")) {
        $(el).attr('x-html', 'pageData.about_us.who_we_serve.headline').empty();
        let ul = $(el).nextAll('ul').first();
        if (ul.length) {
            ul.empty().append(`
                <template x-for="(item, idx) in pageData.about_us.who_we_serve.list" :key="idx">
                    <li class="flex items-start">
                        <i class="fas fa-check-circle text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                        <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                    </li>
                </template>
            `);
        }
    }
    if (t.includes("PYF Different")) {
        $(el).attr('x-html', 'pageData.about_us.different.headline').empty();
        let ul = $(el).nextAll('ul').first();
        if (ul.length) {
            ul.empty().append(`
                <template x-for="(item, idx) in pageData.about_us.different.list" :key="idx">
                    <li class="flex items-start">
                        <i class="fas fa-star text-yellow-500 text-xl mt-1 mr-4 flex-shrink-0"></i>
                        <span class="text-gray-700 font-medium" x-text="item"></span>
                    </li>
                </template>
            `);
        }
    }
    if (t.includes("Pledge")) {
        $(el).attr('x-html', 'pageData.about_us.pledge.headline').empty();
        let ul = $(el).nextAll('ul').first();
        if (ul.length) {
            ul.empty().append(`
                <template x-for="(item, idx) in pageData.about_us.pledge.list" :key="idx">
                    <li class="flex items-start">
                        <i class="fas fa-check-double text-brand-primary text-xl mt-1 mr-4 flex-shrink-0"></i>
                        <span class="text-gray-700 font-medium text-lg" x-text="item"></span>
                    </li>
                </template>
            `);
        }
    }
    if (t.includes("Start Your PYF Journey")) {
        $(el).attr('x-text', 'pageData.about_us.journey.headline').empty();
    }
});

$('h3').each((i, el) => {
    let t = $(el).text();
    if (t.includes("fill that gap")) {
        $(el).attr('x-html', 'pageData.about_us.origin.headline_bottom').empty();
    }
    if (t.includes("Our mission is simple")) {
        $(el).attr('x-text', 'pageData.about_us.mission.subtitle').empty();
    }
    if (t.includes("3 Core Principles")) {
        let grid = $(el).nextAll('div.grid').first();
        if (grid.length) {
            grid.empty().append(`
                <template x-for="(prin, idx) in pageData.about_us.serving.principles" :key="idx">
                    <div class="flex items-center space-x-4 bg-white p-4 rounded shadow-sm border border-gray-100">
                        <div class="h-12 w-12 bg-[#bbf7d0] rounded-full flex items-center justify-center flex-shrink-0">
                            <i :class="prin.icon" class="text-brand-primary text-xl"></i>
                        </div>
                        <h4 class="font-bold text-gray-800 text-lg uppercase" x-text="prin.title"></h4>
                    </div>
                </template>
            `);
        }
    }
});

$('a').each((i, el) => {
    let t = $(el).text().trim().toLowerCase();
    if (t.includes('become an affiliate')) {
        $(el).attr(':href', 'pageData.about_us.journey.btn1_link');
        $(el).attr('x-text', 'pageData.about_us.journey.btn1_text').empty();
    }
    if (t.includes('view service packages')) {
        $(el).attr(':href', 'pageData.about_us.journey.btn2_link');
        $(el).attr('x-text', 'pageData.about_us.journey.btn2_text').empty();
    }
});

$('img').each((i, el) => {
    let src = $(el).attr('src') || '';
    if (src.includes('Hero')) $(el).attr(':src', "pageData.about_us.hero.image || 'About-us/About Us_Hero.jpg'");
    if (src.includes('Who We Are')) $(el).attr(':src', "pageData.about_us.who_we_are.image || 'About-us/About Us_Who We Are.jpg'");
    if (src.includes('Origin')) $(el).attr(':src', "pageData.about_us.origin.image || 'About-us/About Us_Our Origin.jpg'");
    if (src.includes('Mission')) $(el).attr(':src', "pageData.about_us.mission.image || 'About-us/About Us_Our Mission.jpg'");
    if (src.includes('Serving Everyday')) $(el).attr(':src', "pageData.about_us.serving.image || 'About-us/About Us_Serving Everyday Americans.jpg'");
    if (src.includes('Who We Serve')) $(el).attr(':src', "pageData.about_us.who_we_serve.image || 'About-us/About Us_Who We Serve.jpg'");
    if (src.includes('What Makes PYF Different')) $(el).attr(':src', "pageData.about_us.different.image || 'About-us/About Us_What Makes PYF Different.jpg'");
    if (src.includes('Commitment')) $(el).attr(':src', "pageData.about_us.pledge.image || 'About-us/About Us_Built For Real Life_Our Commitment.jpg'");
});

// The System Levers blocks mapping
let cardsGrid = $('div.grid').filter((i, el) => {
    return $(el).parent().html().includes('A system, not a personality');
});

if (cardsGrid.length === 0) {
    // If not found this way, just look for the first grid after the text "Financial control comes"
    $('p').each((i, el) => {
        if ($(el).text().includes("Financial control comes from mastering")) {
            let n = $(el).nextAll('div.grid').first();
            if (n.length) {
                n.empty().append(`
                <template x-for="(card, idx) in pageData.about_us.system.cards" :key="idx">
                    <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-100 flex flex-col transition duration-300 hover:shadow-2xl translate-y-0 hover:-translate-y-2 group">
                        <!-- Card Image overlay context -->
                        <div class="relative h-64 overflow-hidden">
                            <img :src="card.image" :alt="card.title" class="w-full h-full object-cover transition duration-700 group-hover:scale-105">
                            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                            <div class="absolute bottom-0 left-0 w-full p-6">
                                <h3 class="text-3xl font-extrabold text-white uppercase tracking-wider" x-text="card.title"></h3>
                            </div>
                        </div>

                        <div class="p-8 flex-1 flex flex-col">
                            <p class="text-gray-700 text-lg mb-6 leading-relaxed flex-1" x-text="card.desc"></p>
                            
                            <ul class="space-y-3 mb-8">
                                <template x-for="(item, lIdx) in card.list" :key="lIdx">
                                    <li class="flex items-start text-gray-800 font-medium bg-gray-50 rounded-lg p-3 border border-gray-100">
                                        <i class="fas fa-check-circle text-brand-primary text-lg mr-3 mt-0.5"></i>
                                        <span x-text="item"></span>
                                    </li>
                                </template>
                            </ul>

                            <div x-show="card.quote" class="bg-[#f0fdf4] border-l-4 border-brand-primary p-4 rounded-r-lg mt-auto mb-4">
                                <p class="text-brand-dark italic font-semibold" x-text="card.quote"></p>
                            </div>
                            <div x-show="card.footer" class="bg-gray-100 p-4 rounded-lg text-center mt-auto">
                                <p class="text-gray-800 font-bold text-sm uppercase tracking-wide" x-text="card.footer"></p>
                            </div>
                        </div>
                    </div>
                </template>
                `);
            }
        }
    });
}

// Ensure Alpine templates aren't escaped by Cheerio
let output = $.html();
// Sometimes Cheerio might encode <template>, but usually it works fine with decodeEntities: false
fs.writeFileSync('about-us-cheerio.html', output);
console.log('Processed DOM via cheerio!');
