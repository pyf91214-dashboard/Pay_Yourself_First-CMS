import re

def fix_cms_xdata():
    file = 'admin-cms.html'
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # STEP 1: Change <body x-data="{ sidebarOpen: false }"> to <body x-data="cmsManager()">
    old_body = '<body class="h-full flex overflow-hidden text-gray-800" x-data="{ sidebarOpen: false }">'
    new_body = '<body class="h-full flex overflow-hidden text-gray-800" x-data="cmsManager()">'
    
    if old_body not in html:
        print(f"ERROR: Could not find old body tag! Skipping body change.")
    else:
        html = html.replace(old_body, new_body, 1)
        print("Fixed body x-data.")

    # STEP 2: Add sidebarOpen: false to the cmsManager Alpine component init object
    # Find the cmsManager definition and add sidebarOpen to the top
    old_cmsmanager_top = """Alpine.data('cmsManager', () => ({
            activePage: 'home',
            cmsSidebarOpen: false,"""
    new_cmsmanager_top = """Alpine.data('cmsManager', () => ({
            activePage: 'home',
            sidebarOpen: false,
            cmsSidebarOpen: false,"""
    
    if old_cmsmanager_top not in html:
        print("ERROR: Could not find old cmsManager init! Checking if sidebarOpen already there...")
        if "sidebarOpen: false," in html:
            print("sidebarOpen already present in cmsManager. OK.")
        else:
            print("Could not find a suitable location to add sidebarOpen!")
    else:
        html = html.replace(old_cmsmanager_top, new_cmsmanager_top, 1)
        print("Added sidebarOpen to cmsManager.")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Done: {file}")

fix_cms_xdata()
