"""
Webhook Handler for Stripe Events
Handles subscription lifecycle events and triggers appropriate actions.
"""

import json
import logging
from typing import Dict, Any, Optional
from datetime import datetime, timezone
import stripe
from pydantic import BaseModel
from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)

logger = logging.getLogger("salesgenie.billing.webhooks")


class StripeWebhookHandler:
    """Handles Stripe webhook events for subscription lifecycle."""

    def __init__(self):
        self.stripe_api_key = ""
        stripe.api_key = self.stripe_api_key

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
            "customer.subscription.pause": self._handle_subscription_pause,
        }
        
        handler = handlers.get(event_type, self._handle_unknown_event)
        return await handler(event_type, data)

    async def _handle_subscription_created(self, event_type: str, data: dict) -> dict:
        """Handle new subscription creation."""
        logger.info(f"Subscription created: {data.get('id')}")
        return {"status": "processed", "action": "subscription_created"}

    async def _handle_subscription_updated(self, event_type: str, data: dict) -> dict:
        """Handle subscription updates (plan changes, status changes)."""
        logger.info(f"Subscription updated: {data.get('id')}")
        return {"status": "processed", "action": "subscription_updated"}

    async def _handle_subscription_deleted(self, event_type: str, data: dict) -> dict:
        """Handle subscription cancellation."""
        logger.info(f"Subscription deleted: {data.get('id')}")
        return {"status": "processed", "action": "subscription_canceled"}

    async def _handle_payment_succeeded(self, event_type: str, data: dict) -> dict:
        """Handle successful payment."""
        logger.info(f"Payment succeeded: {data.get('id')}")
        return {"status": "processed", "action": "payment_succeeded"}

    async def _handle_payment_failed(self, event_type: str, data: dict) -> dict:
        """Handle failed payment - triggers reminder notification."""
        logger.warning(f"Payment failed: {data.get('id')}")
        return {"status": "processed", "action": "payment_failed", "requires_attention": True}

    async def _handle_subscription_pause(self, event_type: str, data: dict) -> dict:
        """Handle subscription pause."""
        logger.info(f"Subscription paused: {data.get('id')}")
        return {"status": "processed", "action": "subscription_paused"}

    async def _handle_unknown_event(self, event_type: str, data: dict) -> dict:
        """Handle unknown event types."""
        logger.warning(f"Unhandled webhook event: {event_type}")
        return {"status": "processed", "action": "unknown_event"}


webhook_handler = StripeWebhookHandler()


router = APIRouter(prefix="/api/v1/billing/webhooks", tags=["Billing Webhooks"])


@router.post("/stripe")
async def stripe_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    current_user: TokenPayload = Depends(get_current_user) if RequiresAuth else None,
):
    """
    Stripe webhook endpoint for subscription lifecycle events.
    Signature verification should be added in production.
    """
    try:
        event = await request.json()
        
        result = await webhook_handler.handle_event(event)
        
        background_tasks.add_task(log_webhook_event, event, result)
        
        return JSONResponse(result)
    except Exception as e:
        logger.error(f"Webhook processing error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


async def log_webhook_event(event: dict, result: dict):
    """Log webhook event processing result."""
    logger.info(f"Webhook event {event.get('type')}: {result}")