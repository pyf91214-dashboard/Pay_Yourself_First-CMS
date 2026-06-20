create table if not exists public.admin_users (
    user_id uuid primary key references auth.users (id) on delete cascade,
    role text not null default 'editor' check (role in ('editor', 'publisher', 'admin')),
    is_active boolean not null default true,
    created_at timestamptz not null default now()
);

alter table public.admin_users enable row level security;
alter table public.site_content enable row level security;

create or replace function public.is_admin_user(check_user_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
    select exists (
        select 1
        from public.admin_users
        where user_id = check_user_id
          and is_active = true
    );
$$;

grant execute on function public.is_admin_user(uuid) to anon, authenticated;

drop policy if exists "Public can read site content" on public.site_content;
create policy "Public can read site content"
on public.site_content
for select
to anon, authenticated
using (true);

drop policy if exists "Admins can insert site content" on public.site_content;
create policy "Admins can insert site content"
on public.site_content
for insert
to authenticated
with check (public.is_admin_user(auth.uid()));

drop policy if exists "Admins can update site content" on public.site_content;
create policy "Admins can update site content"
on public.site_content
for update
to authenticated
using (public.is_admin_user(auth.uid()))
with check (public.is_admin_user(auth.uid()));

drop policy if exists "Admins can read admin users" on public.admin_users;
create policy "Admins can read admin users"
on public.admin_users
for select
to authenticated
using (public.is_admin_user(auth.uid()));

drop policy if exists "Admins can manage admin users" on public.admin_users;
create policy "Admins can manage admin users"
on public.admin_users
for all
to authenticated
using (public.is_admin_user(auth.uid()))
with check (public.is_admin_user(auth.uid()));

insert into storage.buckets (id, name, public)
values ('cms_images', 'cms_images', true)
on conflict (id) do nothing;

drop policy if exists "Public can read cms images" on storage.objects;
create policy "Public can read cms images"
on storage.objects
for select
to anon, authenticated
using (bucket_id = 'cms_images');

drop policy if exists "Admins can upload cms images" on storage.objects;
create policy "Admins can upload cms images"
on storage.objects
for insert
to authenticated
with check (
    bucket_id = 'cms_images'
    and public.is_admin_user(auth.uid())
);

drop policy if exists "Admins can update cms images" on storage.objects;
create policy "Admins can update cms images"
on storage.objects
for update
to authenticated
using (
    bucket_id = 'cms_images'
    and public.is_admin_user(auth.uid())
)
with check (
    bucket_id = 'cms_images'
    and public.is_admin_user(auth.uid())
);

drop policy if exists "Admins can delete cms images" on storage.objects;
create policy "Admins can delete cms images"
on storage.objects
for delete
to authenticated
using (
    bucket_id = 'cms_images'
    and public.is_admin_user(auth.uid())
);

comment on table public.admin_users is 'Admin and editor allow-list for CMS access.';
