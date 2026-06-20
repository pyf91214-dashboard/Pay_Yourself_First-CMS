html = open('admin.html', 'r', encoding='utf-8').read()

# Find publishLive function
idx = html.find("async publishLive(")
print("=== publishLive function ===")
print(html[idx:idx+800])

# Find init function
idx2 = html.find("async init()")
print("\n=== init function ===")
print(html[idx2:idx2+800])

# Check contact-us.html
cu = open('contact-us.html', 'r', encoding='utf-8').read()
idx3 = cu.find("async init()")
print("\n=== contact-us.html init ===")
print(cu[idx3:idx3+600])
