import urllib.request
import json

url = "https://nqwggnereuhphwmkqove.supabase.co/rest/v1/site_content"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M"

# Correct Contact Us content (clean defaults, no test data)
correct_content = {
    "hero": {
        "headline": "Get In Touch With Us",
        "desc": "Whether you have questions about our services, need support, or want to\nexplore business partnerships, we're here to help.",
        "image": "Contact-us/Contact Us_Hero.jpg"
    },
    "info": {
        "email": "service@payyourselffirst.com",
        "phone": "1-800-123-4567",
        "address": "Pay Yourself First\n107 S. West Street, Suite 557\nAlexandria, VA 22314\nCorrespondence Only",
        "response_time": "1-2 Business Days",
        "support_hours": "Mon-Fri, 9 AM - 5 PM EST"
    },
    "portals": {
        "customer": "https://payyourselffirst.benefithub.com/welcome/",
        "affiliate": "https://backoffice.pyfaffiliates.com/merchants/login.php#login"
    },
    "service_provider": {
        "headline": "Need Help With A <span class=\"text-brand-primary\">Service Provider?</span>",
        "desc1": "Some PYF plans include services delivered by licensed professionals through third-party partner networks.",
        "desc2": "If you need assistance with:",
        "list": [
            "Finding a participating provider",
            "Scheduling an appointment",
            "Provider-specific questions",
            "Service quality concerns"
        ],
        "desc3": "Please contact us using the form above, and we'll help coordinate with the appropriate provider network.",
        "image": "Contact-us/Contact Us_Need help with a service provider.jpg"
    },
    "bottom_text": "We\u2019re committed to making your experience with Pay Yourself First as smooth and supportive as possible. If you need help, don\u2019t hesitate to reach out.",
    "bottom_notices": [
        {"icon": "fa-user-clock", "text": "Please Allow 1-2 Business Days For A Response"},
        {"icon": "fa-stop", "text": "PYF Cannot and Does Not Provide Tax, Legal, or Medical Advice"},
        {"icon": "fa-flag-usa", "text": "Provider Availability Varies By State"}
    ],
    "map_image": {
        "image": "Contact-us/Contact Us_Mailing Address.jpg",
        "heading": "Mailing Address"
    },
    "service_links": {
        "faq_link": "support.html", "faq_text": "Support / FAQ Page",
        "package_link": "packages.html", "package_text": "Package Overview",
        "affiliate_link": "affiliate-page.html", "affiliate_text": "Affiliate Support Section"
    },
    "form_action": "https://forms.zohopublic.com/payyourselffirst1/form/PYFMainSiteContactUs/formperma/c6Fb3hI5V4Qrp9CMD5OPrutVAxOgF5v8wy10YwxFd8A/htmlRecords/submit"
}

payload = json.dumps({
    "page_id": "contact_us",
    "draft_content": correct_content,
    "live_content": correct_content
}).encode('utf-8')

req = urllib.request.Request(
    url + "?on_conflict=page_id",
    data=payload,
    method="POST",
    headers={
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates"
    }
)

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        print("Contact Us data reset to clean defaults successfully!")
except urllib.error.HTTPError as e:
    print(f"ERROR {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"ERROR: {e}")
