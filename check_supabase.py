import urllib.request
import json

url = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content?select=page_id,updated_at&order=updated_at.desc"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M"

req = urllib.request.Request(url, headers={
    "apikey": key,
    "Authorization": f"Bearer {key}"
})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        print("=== Records in site_content table ===")
        for row in data:
            print(f"  page_id: {row['page_id']}, updated_at: {row.get('updated_at', 'N/A')}")
except Exception as e:
    print(f"ERROR: {e}")
