do $$
declare
    role_constraint_name text;
begin
    select con.conname
    into role_constraint_name
    from pg_constraint con
    join pg_class rel on rel.oid = con.conrelid
    join pg_namespace nsp on nsp.oid = rel.relnamespace
    where nsp.nspname = 'public'
      and rel.relname = 'admin_users'
      and con.contype = 'c'
      and pg_get_constraintdef(con.oid) ilike '%role in%';

    if role_constraint_name is not null then
        execute format('alter table public.admin_users drop constraint %I', role_constraint_name);
    end if;
end
$$;

alter table public.admin_users
    add constraint admin_users_role_check
    check (lower(coalesce(trim(role), '')) in ('editor', 'publisher', 'admin', 'super_admin'));

update public.admin_users
set role = 'super_admin'
where role is null
   or lower(trim(role)) in ('editor', 'publisher', 'admin');

insert into public.admin_users (email, role, is_active)
select 'info@payyourselffirst.com', 'super_admin', true
where not exists (
    select 1
    from public.admin_users
    where lower(email) = 'info@payyourselffirst.com'
);

update public.admin_users
set email = 'info@payyourselffirst.com',
    role = 'super_admin',
    is_active = true
where lower(email) = 'info@payyourselffirst.com';

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
    else
        new.role := lower(trim(new.role));
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

    if new.user_id is not null then
        new.invite_status := 'active';
        new.last_invite_error := null;
    elsif new.invite_status is null or trim(new.invite_status) = '' then
        new.invite_status := 'pending_auth';
    end if;

    if new.invite_sent_count is null then
        new.invite_sent_count := 0;
    end if;

    return new;
end;
$$;

create or replace function public.is_super_admin_user(check_user_id uuid)
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
          and lower(coalesce(admin.role, '')) = 'super_admin'
          and (
              (check_user_id is not null and admin.user_id = check_user_id)
              or (caller.email is not null and lower(coalesce(admin.email, '')) = caller.email)
          )
    );
$$;

grant execute on function public.is_super_admin_user(uuid) to anon, authenticated;

drop policy if exists "Admins can manage admin users" on public.admin_users;
drop policy if exists "Super admins can manage admin users" on public.admin_users;
create policy "Super admins can manage admin users"
on public.admin_users
for all
to authenticated
using (public.is_super_admin_user(auth.uid()))
with check (public.is_super_admin_user(auth.uid()));

create or replace function public.protect_permanent_admin_users()
returns trigger
language plpgsql
set search_path = public
as $$
begin
    if tg_op = 'DELETE' then
        if public.is_permanent_admin_email(old.email) then
            raise exception 'The permanent admin % cannot be removed.', lower(old.email);
        end if;

        return old;
    end if;

    if public.is_permanent_admin_email(old.email) then
        if not public.is_permanent_admin_email(new.email) then
            raise exception 'The permanent admin email cannot be changed.';
        end if;

        if coalesce(new.is_active, false) = false then
            raise exception 'The permanent admin must remain active.';
        end if;

        if lower(coalesce(trim(new.role), '')) <> 'super_admin' then
            raise exception 'The permanent admin role cannot be downgraded.';
        end if;
    end if;

    return new;
end;
$$;
