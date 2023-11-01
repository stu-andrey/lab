from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config.db import get_db

from ..models import Works as WorksModel

from ..schemas import BaseWork, Work

from sqlalchemy.orm import Session

from typing import List


router = APIRouter(
    prefix="/api/works",
    tags=["Works"]
)

@router.get("/", response_description="List of all works", response_model=List[Work], status_code=status.HTTP_200_OK)
def get_all_works(db: Session=Depends(get_db)):
    works = db.query(WorksModel).all()

    if works == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return works


@router.get("/id/", response_description="Get work by id", response_model=Work, status_code=status.HTTP_200_OK)
def get_work_by_id(id: int, db: Session=Depends(get_db)):
    work = db.query(WorksModel).filter(WorksModel.id == id).first()

    if work is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return work


@router.post("/", response_description="Create new work", response_model=Work, status_code=status.HTTP_201_CREATED)
def create_work(work: BaseWork, db: Session=Depends(get_db)):
    new_work = WorksModel(**work.model_dump())

    db.add(new_work)
    db.commit()
    db.refresh(new_work)

    return new_work