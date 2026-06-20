Deploy this function to Supabase so the CMS can securely send admin invitation emails.

Recommended function name:
`admin-invite`

Expected behavior:
- verifies the caller is an authenticated approved admin
- inserts a pending `admin_users` row when needed
- sends a Supabase Auth invite email to the target address
- keeps existing auth and CMS flows intact

Browser caller:
- `js/admin-settings.js`

Required redirect URL:
- add your live invite page to Supabase Auth redirect URLs
- example: `https://pyf-dashboard-with-my-mail-myb.vercel.app/admin-accept-invite.html`
