alter table public.admin_users
    add column if not exists invite_status text not null default 'active',
    add column if not exists last_invited_at timestamptz null,
    add column if not exists invite_sent_count integer not null default 0,
    add column if not exists last_invite_error text null;

update public.admin_users
set invite_status = case
        when user_id is not null then 'active'
        when coalesce(last_invite_error, '') <> '' then 'invite_failed'
        else 'pending_auth'
    end
where invite_status is null
   or invite_status not in ('active', 'pending_auth', 'invite_sent', 'existing_auth', 'invite_failed');

update public.admin_users
set invite_status = 'active',
    last_invite_error = null
where user_id is not null
  and invite_status <> 'active';

do $$
begin
    if not exists (
        select 1
        from pg_constraint con
        join pg_class rel on rel.oid = con.conrelid
        join pg_namespace nsp on nsp.oid = rel.relnamespace
        where nsp.nspname = 'public'
          and rel.relname = 'admin_users'
          and con.conname = 'admin_users_invite_status_check'
    ) then
        alter table public.admin_users
            add constraint admin_users_invite_status_check
            check (invite_status in ('active', 'pending_auth', 'invite_sent', 'existing_auth', 'invite_failed'));
    end if;
end
$$;

create index if not exists admin_users_invite_status_idx
    on public.admin_users (invite_status);

create index if not exists admin_users_last_invited_at_idx
    on public.admin_users (last_invited_at desc);

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
    set user_id = current_user_id,
        email = coalesce(email, current_email),
        invite_status = 'active',
        last_invite_error = null
    where is_active = true
      and lower(coalesce(email, '')) = current_email
      and user_id is null
    returning *
    into claimed_row;

    if found then
        insert into public.admin_audit_logs (
            action,
            status,
            actor_user_id,
            actor_email,
            target_email,
            target_admin_user_id,
            details
        )
        values (
            'admin_claim_activated',
            'success',
            current_user_id,
            current_email,
            current_email,
            current_user_id,
            jsonb_build_object('source', 'claim_admin_user')
        );

        return claimed_row;
    end if;

    select *
    into claimed_row
    from public.admin_users
    where is_active = true
      and user_id = current_user_id
    order by created_at asc
    limit 1;

    return claimed_row;
end;
$$;
