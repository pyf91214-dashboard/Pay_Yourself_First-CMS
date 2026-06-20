import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";

const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
};

const PERMANENT_ADMIN_EMAILS = new Set([
    "info@payyourselffirst.com"
]);

type RemovePayload = {
    id?: string;
    email?: string;
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

function isPermanentAdminEmail(email: string) {
    return PERMANENT_ADMIN_EMAILS.has(normalizeEmail(email));
}

function normalizeRole(role: string) {
    return role.trim().toLowerCase();
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
        return json({ error: "Only approved admins can remove admin access." }, 403);
    }

    if (normalizeRole(callerAdmin.role || "admin") !== "super_admin") {
        await logAuditEvent(serviceClient, {
            action: "admin_access_remove_blocked",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            details: {
                reason: "super_admin_required"
            }
        });

        return json({ error: "Only super admins can manage admin access." }, 403);
    }

    let payload: RemovePayload = {};

    try {
        payload = await req.json();
    } catch (_error) {
        return json({ error: "Invalid request body." }, 400);
    }

    const targetId = typeof payload.id === "string" ? payload.id.trim() : "";
    const fallbackEmail = typeof payload.email === "string" ? normalizeEmail(payload.email) : "";

    if (!targetId && !fallbackEmail) {
        return json({ error: "A target admin record is required." }, 400);
    }

    let targetQuery = serviceClient
        .from("admin_users")
        .select("id, user_id, email, role, invite_status, is_active")
        .limit(1);

    if (targetId) {
        targetQuery = targetQuery.eq("id", targetId);
    } else {
        targetQuery = targetQuery.eq("email", fallbackEmail);
    }

    const { data: targetRows, error: targetError } = await targetQuery;

    if (targetError) {
        return json({ error: targetError.message || "Unable to load the target admin." }, 500);
    }

    const targetAdmin = Array.isArray(targetRows) ? targetRows[0] : null;

    if (!targetAdmin) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_remove_blocked",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail: fallbackEmail || null,
            details: {
                reason: "target_not_found"
            }
        });

        return json({ error: "That admin record no longer exists." }, 404);
    }

    const targetEmail = normalizeEmail(targetAdmin.email || fallbackEmail);
    const isSelfRemoval = targetAdmin.user_id === currentUser.id || targetEmail === currentEmail;

    if (isPermanentAdminEmail(targetEmail)) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_remove_blocked",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail,
            targetAdminUserId: targetAdmin.user_id || null,
            details: {
                reason: "permanent_admin_protected"
            }
        });

        return json({ error: "info@payyourselffirst.com is the permanent admin and cannot be removed." }, 403);
    }

    if (isSelfRemoval) {
        await logAuditEvent(serviceClient, {
            action: "admin_access_remove_blocked",
            status: "blocked",
            actorUserId: currentUser.id,
            actorEmail: currentEmail,
            targetEmail,
            targetAdminUserId: targetAdmin.user_id || null,
            details: {
                reason: "self_removal_attempt"
            }
        });

        return json({ error: "You cannot remove your own admin account from this screen." }, 403);
    }

    if (targetAdmin.user_id) {
        const { error: clearAddedByError } = await serviceClient
            .from("admin_users")
            .update({
                added_by: null
            })
            .eq("added_by", targetAdmin.user_id);

        if (clearAddedByError) {
            await logAuditEvent(serviceClient, {
                action: "admin_access_remove_failed",
                status: "error",
                actorUserId: currentUser.id,
                actorEmail: currentEmail,
                targetEmail,
                targetAdminUserId: targetAdmin.user_id || null,
                details: {
                    stage: "clear_added_by_references",
                    error: clearAddedByError.message || "Unable to detach dependent admin records."
                }
            });

            return json({ error: clearAddedByError.message || "Unable to detach dependent admin records." }, 500);
        }

        const { error: authDeleteError } = await serviceClient.auth.admin.deleteUser(targetAdmin.user_id, false);

        if (authDeleteError) {
            await logAuditEvent(serviceClient, {
                action: "admin_access_remove_failed",
                status: "error",
                actorUserId: currentUser.id,
                actorEmail: currentEmail,
                targetEmail,
                targetAdminUserId: targetAdmin.user_id || null,
                details: {
                    stage: "delete_auth_user",
                    error: authDeleteError.message || "Unable to remove admin login access."
                }
            });

            return json({ error: authDeleteError.message || "Unable to remove admin login access." }, 500);
        }
    } else {
        const { error: deleteError } = await serviceClient
            .from("admin_users")
            .delete()
            .eq("id", targetAdmin.id);

        if (deleteError) {
            await logAuditEvent(serviceClient, {
                action: "admin_access_remove_failed",
                status: "error",
                actorUserId: currentUser.id,
                actorEmail: currentEmail,
                targetEmail,
                details: {
                    stage: "delete_admin_row",
                    error: deleteError.message || "Unable to remove admin access."
                }
            });

            return json({ error: deleteError.message || "Unable to remove admin access." }, 500);
        }
    }

    await logAuditEvent(serviceClient, {
        action: "admin_access_removed",
        status: "success",
        actorUserId: currentUser.id,
        actorEmail: currentEmail,
        targetEmail,
        details: {
            removed_role: targetAdmin.role || "admin",
            removed_state: targetAdmin.user_id ? "active" : (targetAdmin.invite_status || "pending_auth"),
            removed_auth_user_id: targetAdmin.user_id || null
        }
    });

    return json({
        ok: true,
        message: targetAdmin.user_id
            ? "Admin access and login account removed successfully."
            : "Pending admin access removed successfully."
    });
});
