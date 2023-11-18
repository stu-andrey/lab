from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config.db import get_db

from ..models import Works as WorksModel

from ..schemas import BaseWork, Work, WorkPreview

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from typing import List

router = APIRouter(
    prefix="/api/works",
    tags=["Works"]
)

@router.get("/", response_description="List of all works", response_model=List[WorkPreview], status_code=status.HTTP_200_OK)
def get_all_works(db: Session=Depends(get_db)):

    stmt = select(WorksModel.id, WorksModel.image)
    # print(stmt)
    works = db.execute(stmt).fetchall()

    if works == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return works


@router.get("/id/{id}", response_description="Get work by id", response_model=Work, status_code=status.HTTP_200_OK)
def get_work_by_id(id: int, db: Session=Depends(get_db)):

    stmt = select(WorksModel).where(WorksModel.id == id).limit(1)
    work = db.execute(stmt).scalar()

    if work is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return work


@router.post("/", response_description="Create new work", response_model=Work, status_code=status.HTTP_201_CREATED)
def create_work(work: BaseWork, db: Session=Depends(get_db)):

    try:
        new_work = db.execute(
            insert(WorksModel).returning(WorksModel), 
            [{**work.model_dump()}]
        ).scalar()

    except:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Не удалось добавить новую работу"
        )
    
    else:
        db.commit()
        return new_work