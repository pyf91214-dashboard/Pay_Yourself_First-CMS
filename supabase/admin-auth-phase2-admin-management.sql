create extension if not exists pgcrypto;

alter table public.admin_users
    add column if not exists id uuid,
    add column if not exists email text,
    add column if not exists added_by uuid null references auth.users (id);

update public.admin_users
set id = gen_random_uuid()
where id is null;

alter table public.admin_users
    alter column id set default gen_random_uuid(),
    alter column id set not null,
    alter column role set default 'admin';

do $$
begin
    if exists (
        select 1
        from pg_constraint con
        join pg_class rel on rel.oid = con.conrelid
        join pg_namespace nsp on nsp.oid = rel.relnamespace
        join pg_attribute att on att.attrelid = con.conrelid and att.attnum = any(con.conkey)
        where nsp.nspname = 'public'
          and rel.relname = 'admin_users'
          and con.contype = 'p'
          and con.conname = 'admin_users_pkey'
          and att.attname = 'user_id'
    ) then
        alter table public.admin_users drop constraint admin_users_pkey;
    end if;

    if not exists (
        select 1
        from pg_constraint con
        join pg_class rel on rel.oid = con.conrelid
        join pg_namespace nsp on nsp.oid = rel.relnamespace
        where nsp.nspname = 'public'
          and rel.relname = 'admin_users'
          and con.contype = 'p'
    ) then
        alter table public.admin_users add constraint admin_users_pkey primary key (id);
    end if;
end
$$;

alter table public.admin_users
    alter column user_id drop not null;

update public.admin_users as admin
set email = lower(users.email)
from auth.users as users
where admin.user_id = users.id
  and users.email is not null
  and coalesce(trim(admin.email), '') = '';

update public.admin_users
set email = lower(trim(email))
where email is not null;

update public.admin_users as admin
set user_id = users.id
from auth.users as users
where admin.user_id is null
  and admin.email is not null
  and lower(users.email) = admin.email;

create unique index if not exists admin_users_user_id_unique
    on public.admin_users (user_id)
    where user_id is not null;

create unique index if not exists admin_users_email_unique
    on public.admin_users (lower(email));

create index if not exists admin_users_added_by_idx
    on public.admin_users (added_by);

do $$
begin
    if not exists (
        select 1
        from pg_constraint con
        join pg_class rel on rel.oid = con.conrelid
        join pg_namespace nsp on nsp.oid = rel.relnamespace
        where nsp.nspname = 'public'
          and rel.relname = 'admin_users'
          and con.conname = 'admin_users_identity_check'
    ) then
        alter table public.admin_users
            add constraint admin_users_identity_check
            check (user_id is not null or coalesce(trim(email), '') <> '');
    end if;
end
$$;

create or replace function public.prepare_admin_user_row()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
    if new.email is not null then
        new.email := lower(trim(new.email));

        if new.email = '' then
            new.email := null;
        end if;
    end if;

    if new.role is null or trim(new.role) = '' then
        new.role := 'admin';
    end if;

    if new.added_by is null and auth.uid() is not null then
        new.added_by := auth.uid();
    end if;

    if new.email is null and new.user_id is not null then
        select lower(users.email)
        into new.email
        from auth.users as users
        where users.id = new.user_id;
    end if;

    if new.user_id is null and new.email is not null then
        select users.id
        into new.user_id
        from auth.users as users
        where lower(users.email) = new.email
        limit 1;
    end if;

    return new;
end;
$$;

drop trigger if exists admin_users_prepare_row on public.admin_users;
create trigger admin_users_prepare_row
before insert or update on public.admin_users
for each row
execute function public.prepare_admin_user_row();

create or replace function public.is_admin_user(check_user_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
    with caller as (
        select lower(nullif(trim(coalesce(auth.jwt() ->> 'email', '')), '')) as email
    )
    select exists (
        select 1
        from public.admin_users as admin
        cross join caller
        where admin.is_active = true
          and (
              (check_user_id is not null and admin.user_id = check_user_id)
              or (caller.email is not null and lower(coalesce(admin.email, '')) = caller.email)
          )
    );
$$;

create or replace function public.claim_admin_user()
returns public.admin_users
language plpgsql
security definer
set search_path = public
as $$
declare
    current_user_id uuid := auth.uid();
    current_email text := lower(nullif(trim(coalesce(auth.jwt() ->> 'email', '')), ''));
    claimed_row public.admin_users;
begin
    if current_user_id is null or current_email is null then
        raise exception 'Authenticated admin session required.';
    end if;

    update public.admin_users
    set user_id = coalesce(user_id, current_user_id),
        email = coalesce(email, current_email)
    where is_active = true
      and lower(coalesce(email, '')) = current_email
      and (user_id is null or user_id = current_user_id)
    returning *
    into claimed_row;

    if claimed_row.id is null then
        select *
        into claimed_row
        from public.admin_users
        where is_active = true
          and user_id = current_user_id
        order by created_at asc
        limit 1;
    end if;

    return claimed_row;
end;
$$;

grant execute on function public.claim_admin_user() to authenticated;
