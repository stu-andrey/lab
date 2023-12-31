from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from datetime import date as date_type

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..config.db import Base

class Works(Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    date: Mapped[date_type]= mapped_column(TIMESTAMP, nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    image: Mapped[str] = mapped_column(String(50), nullable=False)
    author_photo: Mapped[str] = mapped_column(String(50), nullable=False)