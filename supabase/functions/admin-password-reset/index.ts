import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
};

type PasswordResetPayload = {
    email?: string;
    redirectTo?: string;
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

    let payload: PasswordResetPayload = {};

    try {
        payload = await req.json();
    } catch (_error) {
        return json({ error: "Invalid request body." }, 400);
    }

    const email = normalizeEmail(typeof payload.email === "string" ? payload.email : "");

    if (!email || !isValidEmail(email)) {
        return json({ error: "Please enter a valid admin email." }, 400);
    }

    const origin = req.headers.get("Origin");
    const fallbackRedirect = origin ? `${origin.replace(/\/$/, "")}/admin-reset.html` : null;
    let redirectTo = fallbackRedirect;

    if (typeof payload.redirectTo === "string" && payload.redirectTo.trim()) {
        try {
            const parsedRedirect = new URL(payload.redirectTo);
            if (!origin || parsedRedirect.origin === origin) {
                redirectTo = parsedRedirect.toString();
            }
        } catch (_error) {
            return json({ error: "Invalid redirect URL." }, 400);
        }
    }

    const { data: adminRow, error: adminError } = await serviceClient
        .from("admin_users")
        .select("id, user_id, email, is_active")
        .eq("email", email)
        .eq("is_active", true)
        .maybeSingle();

    if (adminError) {
        return json({ error: adminError.message || "Unable to verify admin access." }, 500);
    }

    if (!adminRow) {
        await logAuditEvent(serviceClient, {
            action: "admin_password_reset_blocked",
            status: "blocked",
            actorEmail: email,
            targetEmail: email,
            details: {
                reason: "email_not_approved"
            }
        });

        return json({ error: "This email is not approved for admin access." }, 403);
    }

    const { error: resetError } = await serviceClient.auth.resetPasswordForEmail(email, {
        redirectTo: redirectTo || undefined
    });

    if (resetError) {
        await logAuditEvent(serviceClient, {
            action: "admin_password_reset_failed",
            status: "error",
            actorEmail: email,
            targetEmail: email,
            targetAdminUserId: adminRow.user_id || null,
            details: {
                error: resetError.message || "Unable to send password reset email."
            }
        });

        return json({ error: resetError.message || "Unable to send password reset email." }, 500);
    }

    await logAuditEvent(serviceClient, {
        action: "admin_password_reset_requested",
        status: "success",
        actorEmail: email,
        targetEmail: email,
        targetAdminUserId: adminRow.user_id || null,
        details: {
            source: "password_reset"
        }
    });

    return json({
        ok: true,
        message: "Password reset email sent."
    });
});
