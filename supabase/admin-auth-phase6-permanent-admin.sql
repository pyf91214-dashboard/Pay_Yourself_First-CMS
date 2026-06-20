create or replace function public.is_permanent_admin_email(check_email text)
returns boolean
language sql
stable
set search_path = public
as $$
    select lower(coalesce(trim(check_email), '')) = 'info@payyourselffirst.com';
$$;

update public.admin_users
set email = 'info@payyourselffirst.com',
    role = 'admin',
    is_active = true
where public.is_permanent_admin_email(email);

insert into public.admin_users (email, role, is_active)
select 'info@payyourselffirst.com', 'admin', true
where not exists (
    select 1
    from public.admin_users
    where public.is_permanent_admin_email(email)
);

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

        if lower(coalesce(trim(new.role), '')) <> 'admin' then
            raise exception 'The permanent admin role cannot be downgraded.';
        end if;
    end if;

    return new;
end;
$$;

drop trigger if exists admin_users_protect_permanent_admin on public.admin_users;
create trigger admin_users_protect_permanent_admin
before update or delete on public.admin_users
for each row
execute function public.protect_permanent_admin_users();
