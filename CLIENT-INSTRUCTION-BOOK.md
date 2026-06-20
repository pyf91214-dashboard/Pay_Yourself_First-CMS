# Pay Yourself First Website

## Client Instruction Book

This guide explains how to use the Pay Yourself First website, admin area, and CMS without needing to touch the code.

---

## 1. What This Project Is

This project is a website with:

- Public website pages your visitors see
- An admin dashboard for managing content
- A CMS for editing page text, buttons, images, navigation, and footer content
- Supabase in the background for content storage and admin login

In normal use, you should only need:

- The live website
- The admin login page
- Your approved admin email and password

You should not need to edit code files unless you hire a developer.

---

## 2. Main Website Pages

These are the main public pages currently included:

- Home
- How We Help You
- Packages
- Tax Season Discount
- Support
- About Us
- Contact Us
- Business Support Package
- Dental Power
- Doctor Power
- Purchase Power
- Affiliate Plan
- Legal pages:
  - Terms
  - Privacy
  - Cookie
  - Disclaimer
  - Acceptable Use Policy

---

## 3. The Pages You Will Actually Use

### Public site

Your visitors use the public `.html` pages such as:

- `index.html`
- `about-us.html`
- `contact-us.html`
- `packages.html`
- `support.html`

### Admin area

You and your team mainly use:

- `admin-login.html`
- `admin.html`
- `admin-reset.html`
- `admin-accept-invite.html`

The main working dashboard is:

- `admin.html`

---

## 4. Login and Admin Access

### First-time setup for a new admin

New admins must be approved first before they can use the CMS.

Typical process:

1. A super admin adds the new admin email inside the admin dashboard.
2. The approved person goes to `admin-login.html`.
3. They create their password or use the invite/reset flow if provided.
4. After login, they can access `admin.html`.

### Important note

Only approved admin emails can use the CMS. If someone has a password but is not approved in the system, they will not be allowed into the dashboard.

---

## 5. Roles and Permissions

There are two main working roles in the current setup:

- `admin`
- `super_admin`

### Admin

An approved admin can generally:

- Log in
- Access the CMS
- Review content
- Use editing tools already allowed in the dashboard

### Super Admin

A super admin can also:

- Add new admins
- Remove admins
- Change admin roles
- Review admin activity logs

### Permanent protected admin

The project includes a protected permanent admin email:

- `info@payyourselffirst.com`

That account is intentionally protected in the system and should not be removed or downgraded.

---

## 6. How To Use the CMS

After logging in to `admin.html`, you will see the admin hub.

### Main sections inside the admin hub

- `CMS & Content`
- `Page Builder`
- `Settings`

For most daily work, use:

- `CMS & Content`
- `Settings`

### What you can edit

Depending on the page, the CMS allows editing things like:

- Headlines
- Paragraph text
- Buttons
- Links
- Cards and lists
- Images
- Footer content
- Navigation bar links

### Basic editing workflow

1. Log in to `admin.html`
2. Open the page you want to edit
3. Change the text, buttons, or images
4. Save the draft if needed
5. Preview the draft
6. Publish when you are happy

---

## 7. Draft vs Publish

This site uses two content states:

- Draft
- Live / Published

### Draft

Draft is your working version. Visitors do not see it yet.

Use draft when:

- You are still making changes
- You want to review before going live
- You want internal approval first

### Publish

Publish sends the approved version live to the website.

Use publish only when:

- The content has been checked
- Links are correct
- Images are correct
- You are ready for visitors to see the update

---

## 8. How To Preview Changes

The CMS supports preview mode.

Typical preview flow:

1. Make your changes
2. Save the draft
3. Use the preview button
4. Review the page in a new tab
5. Publish if correct

### Best practice before publishing

Always check:

- Spelling
- Button links
- Image placement
- Mobile layout
- That the right page was edited

---

## 9. Editing Images

The CMS supports uploading images to the project storage.

### Recommended image workflow

1. Prepare the image before upload
2. Keep the file size reasonable
3. Use clear file names if possible
4. Upload in the correct page section
5. Preview before publishing

### Image tips

- Use web-friendly image sizes
- Avoid extremely large files unless necessary
- Check that important parts of the image are not cropped on mobile

---

## 10. Navigation and Footer

The website uses shared global content for:

- Main navigation bar
- Footer

This means one update can affect multiple pages.

### Navigation bar

If you edit the navigation bar, review:

- Home
- About Us
- Contact Us
- Packages
- Support
- Tax Season Discount
- Business Support Package

### Footer

If you edit the footer, review:

- Legal links
- Contact details
- Social links
- Copyright text

Because shared content appears across multiple pages, always spot-check more than one page after updating it.

---

## 11. Admin Settings

Inside the settings area, a super admin can manage admin users.

### Common admin tasks

- Add a new admin email
- Remove an admin
- Change an admin role
- Review audit logs

### Before removing an admin

Confirm:

- They no longer need access
- They are not the current user performing the action
- They are not the protected permanent admin

---

## 12. Audit Logs

The system records important activity such as:

- Admin access changes
- Draft saves
- Published changes
- Password setup activity

This is useful for:

- Tracking who changed content
- Troubleshooting unexpected edits
- Reviewing admin actions

---

## 13. Day-to-Day Operating Routine

For normal weekly use, follow this routine:

1. Log in to `admin.html`
2. Open the page that needs updates
3. Make the content changes
4. Save draft
5. Preview
6. Check mobile and desktop appearance
7. Publish
8. Open the live page and confirm the change

---

## 14. Recommended Rules for Your Team

To avoid mistakes, I recommend these operating rules:

### Content editing rules

- Do not publish without previewing first
- Do not edit multiple important pages at once unless necessary
- Double-check all external links
- Keep button text short and clear

### Team rules

- Give each admin their own login
- Do not share one password across multiple people
- Let only super admins manage admin access
- Keep a short internal note of major changes

---

## 15. Files You Should Not Edit Manually

Unless a developer is helping you, do not manually edit:

- `js/`
- `supabase/`
- `admin-cms.html`
- Python scripts such as `patch_*`, `fix_*`, `check_*`
- Temporary files such as `tmp-*`

These are technical project files and are not part of normal client use.

If something breaks, contact a developer instead of changing these files directly.

---

## 16. Important Technical Notes for Handover

These are useful for the person responsible for access and platform ownership.

### Hosting

The project includes a `vercel.json` file, so it is set up to work with Vercel-style deployment behavior.

### Database / backend

The project uses Supabase for:

- Content storage
- Admin authentication
- Admin approval
- Audit logs
- Image storage

### Key dependency

Admin access and CMS content depend on Supabase working correctly. If Supabase credentials, policies, functions, or tables are changed incorrectly, the dashboard may stop working.

---

## 17. If the Login Stops Working

Check these in order:

1. Is the correct email being used?
2. Is that email approved as an admin?
3. Is the password correct?
4. Has the user tried the password reset page?
5. Is Supabase online and connected?

If the person can authenticate but still cannot enter the dashboard, it usually means:

- Their email is not approved in the admin table
- Their role/access is restricted

---

## 18. If Content Changes Do Not Appear Live

Check these in order:

1. Was the content only saved as draft?
2. Was the page actually published?
3. Was the correct page edited?
4. Is the shared navigation or footer being checked on the right page?
5. Is the browser showing a cached version?

Then:

- Refresh the page
- Open in an incognito/private window
- Check the live URL directly

---

## 19. If an Uploaded Image Looks Wrong

Check:

- Is the file too large?
- Is the image shape unsuitable for the section?
- Is the image being cropped on mobile?
- Was the image uploaded to the intended field?

If needed:

1. Re-upload a better-sized version
2. Preview again
3. Publish only after checking both desktop and mobile

---

## 20. Best Practice Before Giving Access to Staff

Before handing the project to team members:

1. Confirm who should be `super_admin`
2. Confirm who should be regular `admin`
3. Remove old or unused admin access
4. Test one full login flow
5. Test one real content update
6. Test one publish action
7. Test one password reset

---

## 21. Recommended Handover Checklist

Use this checklist when delivering the project to the client team:

- Admin login page is reachable
- At least one super admin account works
- Backup admin account exists
- CMS opens correctly
- Navigation edits work
- Footer edits work
- Image upload works
- Draft save works
- Preview works
- Publish works
- Password reset works
- Legal page links work
- Contact details are correct

---

## 22. When To Contact a Developer

You should contact a developer if:

- The admin dashboard does not open
- Logins fail for approved users
- Publish stops working
- Images stop uploading
- A page layout breaks badly
- A button no longer links correctly and cannot be fixed in the CMS
- Supabase settings need changes
- Hosting or deployment needs changes

---

## 23. Simple Summary for Non-Technical Users

If you only remember one workflow, remember this:

1. Log in
2. Edit the page
3. Save draft
4. Preview
5. Publish
6. Check the live page

That is the normal working process for this project.

---

## 24. Files Included for Technical Owners

For the technical owner or future developer, the most important files are:

- `admin.html`
- `admin-login.html`
- `js/admin-auth.js`
- `js/admin-settings.js`
- `js/admin-content-audit.js`
- `js/site-nav.js`
- `js/site-footer.js`
- `supabase/`
- `vercel.json`

---

## 25. Final Handover Advice

This project is usable for non-developers through the admin dashboard, but it also contains technical maintenance files from development work.

For the client team:

- Use the admin dashboard for normal content management
- Avoid editing code files directly
- Keep admin access limited and organized
- Always preview before publishing

For any structural or technical changes, use a developer.

