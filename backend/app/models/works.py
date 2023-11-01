from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from ..config.db import Base

class Works(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    type = Column(String(20), nullable=False)
    image = Column(String(50), nullable=False)
    author_photo = Column(String(50), nullable=False)