from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config import get_db

from ..models import Events as EventsModel

from ..schemas import BaseEvent, Event, EventPreview

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from typing import List

router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)

@router.get("/", response_description="List of events", response_model=List[EventPreview], status_code=status.HTTP_200_OK)
def get_all_events(db: Session=Depends(get_db)):

    stmt = select(EventsModel.id)

    events = db.execute(stmt).fetchall()

    if events == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Are you missed something?"
        )
    return events

@router.get("/id/{id}", response_description="Get event with id", response_model=Event, status_code=status.HTTP_200_OK)
def get_event_by_id(id: int, db: Session=Depends(get_db)):
    
    stmt = select(EventsModel).where(EventsModel.id == id).limit(1)
    event = db.execute(stmt).scalar()

    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'You are not even supposed to be here today!'
        )
    return event

@router.get("/type/{type}", response_description="Get events by type", response_model=List[EventPreview], status_code=status.HTTP_200_OK)
def get_events_by_type(type: str, db: Session=Depends(get_db)):

    stmt = select(EventsModel).where(EventsModel.type == type)
    events = db.execte(stmt).fetchall()

    if events == []:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"Looks like you've lost! Are you sure about that type {type}?"
        )
    return events

@router.post("/", response_description="Create new event", response_model=Event, status_code=status.HTTP_200_OK)
def create_event(event: BaseEvent, db: Session=Depends(get_db)):

    try:
        new_event= db.execute(
            insert(EventsModel).returning(EventsModel),
            [{**event.model_dump()}]
        ).scalar()
    except:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cannot add an event"
        )
    else:
        db.commit()
        return new_event
