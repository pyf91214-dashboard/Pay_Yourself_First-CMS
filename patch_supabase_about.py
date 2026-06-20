import json
import urllib.request
import urllib.error
import urllib.parse
from urllib.error import HTTPError

URL = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content?page_id=eq.about_us"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M"

with open('about_data.json', 'r', encoding='utf-8') as f:
    about_data = json.load(f)

req = urllib.request.Request(URL, headers={
    'apikey': KEY,
    'Authorization': f'Bearer {KEY}',
    'Accept': 'application/json'
})

try:
    with urllib.request.urlopen(req) as response:
        rows = json.loads(response.read().decode('utf-8'))
        
        if len(rows) > 0:
            existing = rows[0]
            if "draft_content" in existing and existing["draft_content"]:
                # Preserve their hero modifications if any
                if "hero" in existing["draft_content"]:
                    about_data["hero"] = existing["draft_content"]["hero"]

        payload = {
            "page_id": "about_us",
            "draft_content": about_data,
            "live_content": about_data
        }
        
        if len(rows) > 0:
            # PATCH
            req_update = urllib.request.Request(URL, data=json.dumps(payload).encode('utf-8'), headers={
                'apikey': KEY,
                'Authorization': f'Bearer {KEY}',
                'Content-Type': 'application/json'
            }, method='PATCH')
            with urllib.request.urlopen(req_update) as res:
                print("PATCH complete:", res.status)
        else:
            # POST
            post_url = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content"
            req_update = urllib.request.Request(post_url, data=json.dumps(payload).encode('utf-8'), headers={
                'apikey': KEY,
                'Authorization': f'Bearer {KEY}',
                'Content-Type': 'application/json'
            }, method='POST')
            with urllib.request.urlopen(req_update) as res:
                print("POST complete:", res.status)

except HTTPError as e:
    print("Error:", e.code, e.read().decode())
