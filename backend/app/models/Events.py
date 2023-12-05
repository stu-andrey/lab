from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from datetime import date as date_type

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..config.db import Base

class Events(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    date: Mapped[date_type] = mapped_column(TIMESTAMP nullable=False)
    title: Mapped[str] = mapped_column(String(70), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    place: Mapped[str] = mapped_column(String(30), nullable=False)
    category: Mapped[str] = mapped_column(String(10), nullable=False)
    phone: Mapped[str] = mapped_column(String(17), nullable=False)
