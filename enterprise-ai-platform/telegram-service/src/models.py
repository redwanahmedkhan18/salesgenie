"""
Telegram Service Models
"""

from pydantic import BaseModel
from typing import Optional

class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None

class Message(BaseModel):
    message_id: int
    chat: Chat
    date: int
    text: Optional[str] = None

class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None

class SendMessageRequest(BaseModel):
    chat_id: int
    text: str
