import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
};

type SetupPayload = {
    email?: string;
    password?: string;
};

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

function isAlreadyRegisteredError(message: string) {
    return /already registered|already been registered|user already exists/i.test(message);
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

    const serviceClient = createClient(supabaseUrl, serviceRoleKey, {
        auth: {
            persistSession: false,
            autoRefreshToken: false
        }
    });

    let payload: SetupPayload = {};

    try {
        payload = await req.json();
    } catch (_error) {
        return json({ error: "Invalid request body." }, 400);
    }

    const email = normalizeEmail(typeof payload.email === "string" ? payload.email : "");
    const password = typeof payload.password === "string" ? payload.password : "";

    if (!email || !isValidEmail(email)) {
        return json({ error: "Please enter a valid admin email." }, 400);
    }

    if (password.length < 8) {
        return json({ error: "Password must be at least 8 characters long." }, 400);
    }

    const { data: adminRow, error: adminRowError } = await serviceClient
        .from("admin_users")
        .select("id, user_id, email, is_active")
        .eq("email", email)
        .eq("is_active", true)
        .maybeSingle();

    if (adminRowError) {
        return json({ error: adminRowError.message || "Unable to verify admin access." }, 500);
    }

    if (!adminRow) {
        await logAuditEvent(serviceClient, {
            action: "admin_self_register_blocked",
            status: "blocked",
            actorEmail: email,
            targetEmail: email,
            details: {
                reason: "email_not_approved"
            }
        });

        return json({ error: "This email is not approved for admin access." }, 403);
    }

    if (adminRow.user_id) {
        await logAuditEvent(serviceClient, {
            action: "admin_self_register_blocked",
            status: "blocked",
            actorEmail: email,
            targetEmail: email,
            targetAdminUserId: adminRow.user_id,
            details: {
                reason: "account_already_linked"
            }
        });

        return json({ error: "An admin account already exists for this email. Please sign in or reset your password." }, 409);
    }

    const { data: createdUser, error: createUserError } = await serviceClient.auth.admin.createUser({
        email,
        password,
        email_confirm: true
    });

    if (createUserError) {
        if (isAlreadyRegisteredError(createUserError.message || "")) {
            await serviceClient
                .from("admin_users")
                .update({
                    invite_status: "existing_auth",
                    last_invite_error: null
                })
                .eq("id", adminRow.id);

            await logAuditEvent(serviceClient, {
                action: "admin_self_register_blocked",
                status: "blocked",
                actorEmail: email,
                targetEmail: email,
                details: {
                    reason: "auth_account_already_exists"
                }
            });

            return json({ error: "An account already exists for this email. Please sign in or use Forgot Password." }, 409);
        }

        await logAuditEvent(serviceClient, {
            action: "admin_self_register_failed",
            status: "error",
            actorEmail: email,
            targetEmail: email,
            details: {
                error: createUserError.message || "Unable to create admin account."
            }
        });

        return json({ error: createUserError.message || "Unable to create admin account." }, 500);
    }

    await logAuditEvent(serviceClient, {
        action: "admin_self_register_created",
        status: "success",
        actorEmail: email,
        targetEmail: email,
        targetAdminUserId: createdUser.user?.id || null,
        details: {
            source: "self_register"
        }
    });

    return json({
        ok: true,
        message: "Password created successfully. Please sign in with your email and new password."
    });
});
