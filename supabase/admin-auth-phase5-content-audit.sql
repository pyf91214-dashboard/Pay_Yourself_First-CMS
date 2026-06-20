create or replace function public.log_admin_content_change(
    p_action text,
    p_page_id text,
    p_page_name text,
    p_status text default 'success',
    p_changes jsonb default '[]'::jsonb,
    p_metadata jsonb default '{}'::jsonb
)
returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare
    current_user_id uuid := auth.uid();
    current_email text := lower(nullif(trim(coalesce(auth.jwt() ->> 'email', '')), ''));
    inserted_id uuid;
begin
    if current_user_id is null or not public.is_admin_user(current_user_id) then
        raise exception 'Approved admin session required.';
    end if;

    insert into public.admin_audit_logs (
        action,
        status,
        actor_user_id,
        actor_email,
        details
    )
    values (
        coalesce(nullif(trim(p_action), ''), 'content_updated'),
        coalesce(nullif(trim(p_status), ''), 'success'),
        current_user_id,
        current_email,
        jsonb_strip_nulls(
            jsonb_build_object(
                'page_id', nullif(trim(coalesce(p_page_id, '')), ''),
                'page_name', nullif(trim(coalesce(p_page_name, '')), ''),
                'change_count', coalesce(jsonb_array_length(coalesce(p_changes, '[]'::jsonb)), 0),
                'changes', coalesce(p_changes, '[]'::jsonb)
            ) || coalesce(p_metadata, '{}'::jsonb)
        )
    )
    returning id into inserted_id;

    return inserted_id;
end;
$$;

grant execute on function public.log_admin_content_change(text, text, text, text, jsonb, jsonb) to authenticated;

comment on function public.log_admin_content_change(text, text, text, text, jsonb, jsonb)
is 'Writes a structured audit entry for CMS content changes performed by an approved admin.';
