html = open('admin.html', 'r', encoding='utf-8').read()

# Find all function definitions inside cmsManager
import re

# Get the cmsManager Alpine data registration block
start = html.find("Alpine.data('cmsManager'")
end = html.find("</script>", start)
block = html[start:end]

# Find all async/function definitions
fns = re.findall(r'async\s+(\w+)\s*\(|(\w+)\s*:\s*(?:async\s*)?\([^)]*\)\s*(?:=>)?\s*\{|(\w+)\s*\(', block[:3000])
print("Functions found in cmsManager:")
funcs = re.findall(r'async\s+(\w+)\s*\(', block)
for f in funcs:
    print(f"  async {f}()")
    
# Also check for previewDraft
print("\npreviewDraft defined:", 'previewDraft' in block)
print("saveDraft defined:", 'saveDraft' in block)
print("publishLive defined:", 'publishLive' in block)
print("uploadImageTo defined:", 'uploadImageTo' in block)
print("init defined:", 'init()' in block or 'async init()' in block)
