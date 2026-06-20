import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
};

type ProvisionPayload = {
    email?: string;
    role?: string;
};

const MANAGEABLE_ROLES = new Set([
    "admin",
    "super_admin"
]);

function json(data: unknown, status = 200) {
    return new Response(JSON.stringify(data), {
        status,
        headers: {
            ...corsHeaders,
            "Content-Type": "application/json"
        }
    });
}

function normalizeEmail(email: string) {
    return email.trim().toLowerCase();
}

function isValidEmail(email: string) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function normalizeRole(role: string) {
    return role.trim().toLowerCase();
}

function isManageableRole(role: string) {
    return MANAGEABLE_ROLES.has(normalizeRole(role));
}

async function logAuditEvent(
    serviceClient: ReturnType<typeof createClient>,
    {
        action,
        status = "info",
        actorUserId = null,
        actorEmail = null,
        targetEmail = null,
        targetAdminUserId = null,
        details = {}
    }: {
        action: string;
        status?: string;
        actorUserId?: string | null;
        actorEmail?: string | null;
        targetEmail?: string | null;
        targetAdminUserId?: string | null;
        details?: Record<string, unknown>;
    }
) {
    const { error } = await serviceClient
        .from("admin_audit_logs")
        .insert({
            action,
            status,
            actor_user_id: actorUserId,
            actor_email: actorEmail,
            target_email: targetEmail,
            target_admin_user_id: targetAdminUserId,
            details
        });

    if (error) {
        console.error("Failed to write admin audit log", { action, status, targetEmail, error });
    }
}

Deno.serve(async (req) => {
    if (req.method === "OPTIONS") {
        return new Response("ok", { headers: corsHeaders });
    }

    if (req.method !== "POST") {
        return json({ error: "Method not allowed." }, 405);
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");

    if (!supabaseUrl || !serviceRoleKey) {
        return json({ error: "Missing Supabase server configuration." }, 500);
    }

    const authHeader = req.headers.get("Authorization");

    if (!authHeader || !authHeader.startsWith("Bearer ")) {
        return json({ error: "Missing authenticated admin session." }, 401);
    }

    const token = authHeader.replace(/^Bearer\s+/i, "");

    const serviceClient = createClient(supabaseUrl, serviceRoleKey, {
        auth: {
            persistSession: false,
            autoRefreshToken: false
        }
    });

    const {
        data: { user: currentUser },
        error: userError
    } = await serviceClient.auth.getUser(token);

    if (userError || !currentUser?.id || !currentUser.email) {
        return json({ error: "Invalid authenticated admin session." }, 401);
    }

    const currentEmail = normalizeEmail(currentUser.email);

    const { data: callerByUserId, error: callerByUserIdError } = await serviceClient
        .from("admin_users")
        .select("id, user_id, email, role, is_active")
        .eq("user_id", currentUser.id)
        .eq("is_active", true)
        .maybeSingle();

    if (callerByUserIdError) {
        return json({ error: callerByUserIdError.message || "Unable to verify admin access." }, 500);
    }

    let callerAdmin = callerByUserId;

    if (!callerAdmin) {
        const { data: callerByEmail, error: callerByEmailError } = await serviceClient
            .from("admin_users")
            .select("id, user_id, email, role, is_active")
            .eq("email", currentEmail)
            .eq("is_active", true)
            .maybeSingle();

        if (callerByEmailError) {
            return json({ error: callerByEmailError.message || "Unable to verify admin access." }, 500);
        }

        callerAdmin = callerByEmail;
    }

    if (!callerAdmin) {
        return json({ error: "Only approved admins can add another admin." }, 403);
    }

    if (normalizeRole(callerAdmin.role || "admin") !== "super_admin") {
        await logAuditEvent(serviceClient, {
            action: "admin_access_create_failed",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            details: {
                reason: "super_admin_required"
            }
        });

        return json({ error: "Only super admins can manage admin access." }, 403);
    }

    let payload: ProvisionPayload = {};

    try {
        payload = await req.json();
    } catch (_error) {
        return json({ error: "Invalid request body." }, 400);
    }

    const email = normalizeEmail(typeof payload.email === "string" ? payload.email : "");
    const requestedRole = normalizeRole(typeof payload.role === "string" ? payload.role : "admin");

    if (!email || !isValidEmail(email)) {
        return json({ error: "Please enter a valid admin email." }, 400);
    }

    if (!isManageableRole(requestedRole)) {
        return json({ error: "Please choose a valid admin role." }, 400);
    }

    const { data: existingAdmin, error: existingAdminError } = await serviceClient
        .from("admin_users")
        .select("id, user_id, email, role, created_at, invite_status, invite_sent_count")
        .eq("email", email)
        .maybeSingle();

    if (existingAdminError) {
        return json({ error: existingAdminError.message || "Unable to read admin records." }, 500);
    }

    if (existingAdmin?.user_id) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_duplicate",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail: email,
            targetAdminUserId: existingAdmin.user_id,
            details: {
                reason: "existing_active_admin"
            }
        });

        return json({ error: "Admin already exists" }, 409);
    }

    if (existingAdmin) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_duplicate",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail: email,
            details: {
                reason: "pending_admin_already_exists"
            }
        });

        return json({ error: "Admin already exists" }, 409);
    }

    const { error: insertError } = await serviceClient
        .from("admin_users")
        .insert({
            email,
            role: requestedRole,
            added_by: currentUser.id,
            invite_status: "pending_auth",
            last_invited_at: null,
            invite_sent_count: 0,
            last_invite_error: null
        });

    if (insertError) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_create_failed",
            status: "error",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail: email,
            details: {
                error: insertError.message || "Unable to add admin."
            }
        });

        return json({ error: insertError.message || "Unable to add admin." }, 500);
    }

    await logAuditEvent(serviceClient, {
        action: "admin_access_created",
        status: "success",
        actorUserId: currentUser.id,
        actorEmail: currentEmail,
        targetEmail: email,
        details: {
            source: "edge_function",
            assigned_role: requestedRole
        }
    });

    return json({
        ok: true,
        status: "approved",
        invite_status: "pending_auth",
        role: requestedRole,
        message: `${requestedRole === "super_admin" ? "Super admin" : "Admin"} email approved. The user can now create their own password from the login page and then sign in.`
    });
});
