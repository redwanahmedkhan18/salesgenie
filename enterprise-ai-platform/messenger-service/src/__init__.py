"""
Facebook Messenger Service
Integration with Meta Facebook Messenger Platform for customer support and sales.
"""

from .router_messenger import router
from .models import Message, Conversation, PageSubscription

__all__ = ["router", "Message", "Conversation", "PageSubscription"]