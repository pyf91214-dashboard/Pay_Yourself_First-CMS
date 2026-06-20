create extension if not exists pgcrypto;

create table if not exists public.admin_audit_logs (
    id uuid primary key default gen_random_uuid(),
    action text not null,
    status text not null default 'info',
    actor_user_id uuid null references auth.users (id) on delete set null,
    actor_email text null,
    target_email text null,
    target_admin_user_id uuid null references auth.users (id) on delete set null,
    details jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create index if not exists admin_audit_logs_created_at_idx
    on public.admin_audit_logs (created_at desc);

create index if not exists admin_audit_logs_actor_user_id_idx
    on public.admin_audit_logs (actor_user_id);

create index if not exists admin_audit_logs_target_admin_user_id_idx
    on public.admin_audit_logs (target_admin_user_id);

create index if not exists admin_audit_logs_target_email_idx
    on public.admin_audit_logs (lower(target_email));

alter table public.admin_audit_logs enable row level security;

drop policy if exists "Admins can read admin audit logs" on public.admin_audit_logs;
create policy "Admins can read admin audit logs"
on public.admin_audit_logs
for select
to authenticated
using (public.is_admin_user(auth.uid()));

comment on table public.admin_audit_logs is 'Audit trail for sensitive CMS admin actions.';

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
        email = coalesce(email, current_email)
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
