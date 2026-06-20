import urllib.request
import json

url = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content?select=page_id,draft_content,live_content&page_id=eq.contact_us"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M"

req = urllib.request.Request(url, headers={
    "apikey": key,
    "Authorization": f"Bearer {key}"
})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        if data:
            row = data[0]
            print(f"page_id: {row['page_id']}")
            print(f"draft_content is null: {row['draft_content'] is None}")
            print(f"live_content is null: {row['live_content'] is None}")
            if row['draft_content']:
                dc = row['draft_content']
                print(f"\ndraft_content keys: {list(dc.keys()) if isinstance(dc, dict) else 'NOT A DICT'}")
                if isinstance(dc, dict) and 'hero' in dc:
                    print(f"hero.headline: {dc['hero'].get('headline')}")
            if row['live_content']:
                lc = row['live_content']
                print(f"\nlive_content keys: {list(lc.keys()) if isinstance(lc, dict) else 'NOT A DICT'}")
        else:
            print("No contact_us record found!")
except Exception as e:
    print(f"ERROR: {e}")
