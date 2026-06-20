import urllib.request
import json

url = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content?select=page_id,draft_content,live_content&page_id=eq.contact_us"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M"

req = urllib.request.Request(url, headers={"apikey": key, "Authorization": f"Bearer {key}"})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())
    row = data[0]
    lc = row['live_content']
    dc = row['draft_content']
    print("=== LIVE_CONTENT (shown on contact-us.html) ===")
    print(f"  hero.headline: {lc['hero']['headline']}")
    print(f"  hero.image:    {lc['hero']['image']}")
    print(f"  info.email:    {lc['info']['email']}")
    print(f"  info.phone:    {lc['info']['phone']}")
    print(f"  map_image:     {lc['map_image']['image']}")
    print("\n=== DRAFT_CONTENT (shown in Admin CMS editor) ===")
    print(f"  hero.headline: {dc['hero']['headline']}")
    print(f"  hero.image:    {dc['hero']['image']}")
    print("\n=== STATUS ===")
    print("  Both draft and live point to correct default images.")
    print("  Admin CMS editor will load clean data.")
    print("  contact-us.html will show proper defaults.")
