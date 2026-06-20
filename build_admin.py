import os
import re

base_dir = r"d:\Sapphire Leads\Pay Yourself First Website\Pyf-dashboard with my Mail"

files = {
    'dashboard': os.path.join(base_dir, 'admin-dashboard.html'),
    'customers': os.path.join(base_dir, 'admin-customers.html'),
    'affiliates': os.path.join(base_dir, 'admin-affiliates.html'),
    'cms': os.path.join(base_dir, 'admin-cms.html')
}

contents = {}
for k, v in files.items():
    with open(v, 'r', encoding='utf-8') as f:
        contents[k] = f.read()

sections = {}
for k, html in contents.items():
    m2 = re.search(r'(<header.*?</main>)', html, re.DOTALL)
    if m2:
        sections[k] = m2.group(1)

chart_script_match = re.search(r'(<!-- Chart Configuration Script -->.*?</script>)', contents['dashboard'], re.DOTALL)
if chart_script_match:
    chart_script = chart_script_match.group(1)
else:
    chart_script = ''

add_customer_modal_match = re.search(r'(<!-- Add Customer Modal \(Alpine.js\) -->.*?)</body>', contents['customers'], re.DOTALL)
if add_customer_modal_match:
    add_customer_modal = add_customer_modal_match.group(1)
else:
    add_customer_modal = ''

payout_modal_match = re.search(r'(<!-- Payout Modal \(Alpine.js\) -->.*?)</body>', contents['affiliates'], re.DOTALL)
if payout_modal_match:
    payout_modal = payout_modal_match.group(1)
else:
    payout_modal = ''

cms_script_match = re.search(r'(<!-- CMS Alpine Script -->.*?</script>)', contents['cms'], re.DOTALL)
if cms_script_match:
    cms_script = cms_script_match.group(1)
else:
    cms_script = ''

transactions_html = """
        <!-- Header -->
        <header class="flex items-center px-6 py-4 bg-white border-b border-gray-100 z-10 shadow-sm">
            <div class="flex items-center">
                <button @click="sidebarOpen = true" class="text-gray-500 focus:outline-none lg:hidden mr-4">
                    <i class="fas fa-bars text-xl"></i>
                </button>
                <div class="hidden sm:block text-sm font-medium text-gray-500">
                    <span class="text-gray-400">Pages</span> / <span class="text-gray-900 font-bold ml-1">Transactions</span>
                </div>
            </div>
            
            <div class="flex items-center space-x-5">
                <button class="relative p-2 text-gray-400 hover:text-brand-700 transition focus:outline-none">
                    <i class="fas fa-bell text-xl"></i>
                </button>
                
                <div x-data="{ dropdownOpen: false }" class="relative">
                    <button @click="dropdownOpen = !dropdownOpen" class="flex items-center focus:outline-none relative z-10 transition border-2 border-transparent hover:border-brand-700 rounded-full">
                        <img class="object-cover w-9 h-9 rounded-full" src="https://ui-avatars.com/api/?name=Admin+User&background=389400&color=fff" alt="Admin avatar">
                    </button>
                    <!-- Dropdown Menu -->
                    <div x-show="dropdownOpen" @click.away="dropdownOpen = false" class="absolute right-0 z-20 w-48 py-2 mt-2 bg-white rounded-xl shadow-xl border border-gray-100" style="display: none;">
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-brand-50 hover:text-brand-700">Profile</a>
                        <hr class="my-2 border-gray-100">
                        <a href="#" class="block px-4 py-2 text-sm text-red-600 hover:bg-red-50">Log Out</a>
                    </div>
                </div>
            </div>
        </header>

        <main class="flex-1 overflow-x-hidden overflow-y-auto bg-[#fafafa] p-6 lg:p-8">
            <div class="mb-8">
                <h1 class="text-2xl font-extrabold text-gray-900 tracking-tight">Transactions</h1>
                <p class="text-sm text-gray-500 mt-1">View all payment history and receipts.</p>
            </div>
            <div class="bg-white rounded-2xl p-12 shadow-soft border border-gray-100 text-center">
                <i class="fas fa-file-invoice-dollar text-6xl text-gray-200 mb-4"></i>
                <h3 class="text-xl font-bold text-gray-700">Detailed Transactions View</h3>
                <p class="text-gray-500 mt-2">This section is currently under development.</p>
            </div>
        </main>
"""

sections['transactions'] = transactions_html

with open(os.path.join(base_dir, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="en" class="antialiased h-full bg-gray-50">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PYF Admin Hub</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <!-- Supabase JS -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

    <!-- Alpine.js for Interactions -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#f0fdf4',
                            100: '#dcfce7',
                            500: '#22c55e',
                            600: '#16a34a',
                            700: '#389400',
                            800: '#166534',
                            900: '#1c1c1c',
                        }
                    },
                    boxShadow: {
                        'soft': '0 4px 20px -2px rgba(0, 0, 0, 0.05)',
                        'glow': '0 0 20px rgba(56, 148, 0, 0.15)',
                    }
                }
            }
        }
    </script>
    <style>
        [x-cloak] { display: none !important; }
    </style>
</head>
<body class="h-full flex overflow-hidden text-gray-800" x-data="{ currentTab: 'dashboard', sidebarOpen: false, addCustomerModal: false, payoutModal: false }">

    <!-- Mobile sidebar backdrop -->
    <div x-show="sidebarOpen" x-cloak class="fixed inset-0 z-20 transition-opacity bg-gray-900 bg-opacity-50 lg:hidden" @click="sidebarOpen = false"></div>

    <!-- Sidebar -->
    <aside :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full'" class="fixed inset-y-0 left-0 z-30 w-64 overflow-y-auto transition duration-300 transform bg-brand-900 lg:translate-x-0 lg:static lg:inset-auto flex flex-col border-r border-gray-800" style="z-index: 50;">
        
        <div class="flex items-center justify-center h-20 bg-brand-900 border-b border-gray-800/50">
            <div class="flex items-center text-white font-extrabold text-xl tracking-tight">
                <i class="fas fa-shield-halved text-brand-700 text-2xl mr-3"></i>
                PYF <span class="text-brand-700 ml-1">ADMIN</span>
            </div>
        </div>

        <nav class="mt-6 flex-1 px-4 space-y-2">
            <a @click.prevent="currentTab = 'dashboard'; sidebarOpen = false" :class="currentTab === 'dashboard' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-chart-pie w-6"></i>
                <span class="mx-3">Dashboard</span>
            </a>
            
            <a @click.prevent="currentTab = 'customers'; sidebarOpen = false" :class="currentTab === 'customers' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-users w-6"></i>
                <span class="mx-3">Customers</span>
            </a>

            <a @click.prevent="currentTab = 'affiliates'; sidebarOpen = false" :class="currentTab === 'affiliates' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-network-wired w-6"></i>
                <span class="mx-3">Affiliates</span>
            </a>

            <a @click.prevent="currentTab = 'transactions'; sidebarOpen = false" :class="currentTab === 'transactions' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-file-invoice-dollar w-6"></i>
                <span class="mx-3">Transactions</span>
            </a>
            
            <a @click.prevent="currentTab = 'cms'; sidebarOpen = false" :class="currentTab === 'cms' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-pen-nib w-6"></i>
                <span class="mx-3">CMS & Content</span>
            </a>
        </nav>

        <div class="p-4 border-t border-gray-800/50">
            <a @click.prevent="currentTab = 'settings'; sidebarOpen = false" :class="currentTab === 'settings' ? 'text-white bg-brand-700/20 text-brand-500 font-semibold' : 'text-gray-400 hover:text-white hover:bg-gray-800 font-medium'" class="flex items-center px-4 py-3 rounded-xl transition cursor-pointer">
                <i class="fas fa-cog w-6"></i>
                <span class="mx-3">Settings</span>
            </a>
        </div>
    </aside>

''')
    
    for view in ['dashboard', 'customers', 'affiliates', 'transactions', 'cms']:
        x_data_attr = ' x-data="cmsManager"' if view == 'cms' else ''
        f.write(f'    <div class="flex-1 flex flex-col overflow-hidden relative" x-show="currentTab === \'{view}\'"{x_data_attr} x-cloak>\n')
        f.write(sections.get(view, ''))
        f.write('\n    </div>\n')

    f.write('''
    <!-- SETTINGS VIEW -->
    <div class="flex-1 flex flex-col overflow-hidden relative" x-show="currentTab === 'settings'" x-cloak>
        <header class="flex items-center px-6 py-4 bg-white border-b border-gray-100 z-10 shadow-sm">
            <div class="flex items-center">
                <button @click="sidebarOpen = true" class="text-gray-500 focus:outline-none lg:hidden mr-4">
                    <i class="fas fa-bars text-xl"></i>
                </button>
                <div class="hidden sm:block text-sm font-medium text-gray-500">
                    <span class="text-gray-400">Pages</span> / <span class="text-gray-900 font-bold ml-1">Settings</span>
                </div>
            </div>
        </header>

        <main class="flex-1 overflow-x-hidden overflow-y-auto bg-[#fafafa] p-6 lg:p-8">
            <div class="mb-8">
                <h1 class="text-2xl font-extrabold text-gray-900 tracking-tight">Settings</h1>
                <p class="text-sm text-gray-500 mt-1">Manage platform options.</p>
            </div>
            <div class="bg-white rounded-2xl p-12 shadow-soft border border-gray-100 text-center">
                <i class="fas fa-cog text-6xl text-gray-200 mb-4"></i>
                <h3 class="text-xl font-bold text-gray-700">Platform Settings</h3>
                <p class="text-gray-500 mt-2">This section is currently under development.</p>
            </div>
        </main>
    </div>
''')

    if add_customer_modal:
        f.write(add_customer_modal + '\n')
    if payout_modal:
        f.write(payout_modal + '\n')
    if chart_script:
        f.write(chart_script + '\n')
    if cms_script:
        f.write(cms_script + '\n')
    
    f.write('</body>\n</html>\n')

print("Merge completed successfully.")
