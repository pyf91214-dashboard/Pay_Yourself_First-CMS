html = open('admin.html', 'r', encoding='utf-8').read()

# 1. Find where the CMS Alpine Script starts and ends 
idx_start = html.find('<!-- CMS Alpine Script -->')
idx_end = html.find('</script>', idx_start) + len('</script>')
print('CMS Alpine Script span:', idx_start, '-', idx_end)
print(html[idx_start:idx_start+500])
