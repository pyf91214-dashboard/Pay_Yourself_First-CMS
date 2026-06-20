html = open('admin-cms.html', 'r', encoding='utf-8').read()
idx = html.find('Editing: ')
# Look 3000 chars backwards to find the nearest x-show attribute
context = html[max(0, idx-3000):idx+500]
print(context)
