"""
Webhook Handler for Stripe Events
Handles subscription lifecycle events and triggers appropriate actions.
"""

import logging
from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from enterprise_ai_platform.common.config import settings

logger = logging.getLogger("salesgenie.billing.webhooks")


class StripeWebhookHandler:
    """Handles Stripe webhook events for subscription lifecycle."""

    def __init__(self):
        from enterprise_ai_platform.billing_service.src.stripe_billing import stripe
        self._stripe = stripe

    async def handle_event(self, event: dict) -> dict:
        """Process incoming Stripe webhook event."""
        event_type = event.get("type", "")
        data = event.get("data", {}).get("object", {})

        handlers = {
            "customer.subscription.created": self._handle_subscription_created,
            "customer.subscription.updated": self._handle_subscription_updated,
            "customer.subscription.deleted": self._handle_subscription_deleted,
            "invoice.payment_succeeded": self._handle_payment_succeeded,
            "invoice.payment_failed": self._handle_payment_failed,
            "customer.subscription.paused": self._handle_subscription_pause,
        }

        handler = handlers.get(event_type, self._handle_unknown_event)
        return await handler(event_type, data)

    async def _handle_subscription_created(self, event_type: str, data: dict) -> dict:
        """Handle new subscription creation."""
        logger.info("Subscription created: id=%s", data.get("id"))
        return {"status": "processed", "action": "subscription_created"}

    async def _handle_subscription_updated(self, event_type: str, data: dict) -> dict:
        """Handle subscription updates (plan changes, status changes)."""
        logger.info("Subscription updated: id=%s", data.get("id"))
        return {"status": "processed", "action": "subscription_updated"}

    async def _handle_subscription_deleted(self, event_type: str, data: dict) -> dict:
        """Handle subscription cancellation."""
        logger.info("Subscription deleted: id=%s", data.get("id"))
        return {"status": "processed", "action": "subscription_canceled"}

    async def _handle_payment_succeeded(self, event_type: str, data: dict) -> dict:
        """Handle successful payment."""
        logger.info("Payment succeeded: id=%s", data.get("id"))
        return {"status": "processed", "action": "payment_succeeded"}

    async def _handle_payment_failed(self, event_type: str, data: dict) -> dict:
        """Handle failed payment - triggers reminder notification."""
        logger.warning("Payment failed: id=%s", data.get("id"))
        return {"status": "processed", "action": "payment_failed", "requires_attention": True}

    async def _handle_subscription_pause(self, event_type: str, data: dict) -> dict:
        """Handle subscription pause."""
        logger.info("Subscription paused: id=%s", data.get("id"))
        return {"status": "processed", "action": "subscription_paused"}

    async def _handle_unknown_event(self, event_type: str, data: dict) -> dict:
        """Handle unknown event types."""
        logger.warning("Unhandled webhook event: %s", event_type)
        return {"status": "processed", "action": "unknown_event"}


webhook_handler = StripeWebhookHandler()

router = APIRouter(prefix="/api/v1/billing/webhooks", tags=["Billing Webhooks"])


@router.post("/stripe")
async def stripe_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
):
    """
    Stripe webhook endpoint for subscription lifecycle events.
    Signature is verified using the Stripe webhook secret.
    """
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    try:
        event = webhook_handler._stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        logger.error("Invalid webhook payload from Stripe")
        raise HTTPException(status_code=400, detail="Invalid payload")
    except webhook_handler._stripe.error.SignatureVerificationError:
        logger.error("Invalid Stripe webhook signature")
        raise HTTPException(status_code=400, detail="Invalid signature")

    result = await webhook_handler.handle_event(event)

    background_tasks.add_task(log_webhook_event, event, result)

    return JSONResponse(result)


async def log_webhook_event(event: dict, result: dict):
    """Log webhook event processing result."""
    logger.info("Webhook event %s: %s", event.get("type"), result.get("action", "unknown"))
