from pydantic import BaseModel
from typing import Optional
from datetime import date

class BaseEvent(BaseMiodel):
    date: date
    title: str
    description: str
    place: str
    category: str
    phone: str

class Event(BaseEvent):
    id: int

class EventPreview(BaseModel):
    id: int