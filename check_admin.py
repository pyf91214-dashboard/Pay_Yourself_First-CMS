html = open('admin.html', 'r', encoding='utf-8').read()
print('saveDraft:', 'async saveDraft(' in html)
print('uploadImageTo:', 'async uploadImageTo(' in html)
print('body uses cmsManager:', 'x-data="cmsManager()"' in html)
