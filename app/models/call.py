from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.database.connection import Base


class Call(Base):

    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String(30), nullable=False)

    call_type = Column(String(20), nullable=False)

    status = Column(String(30), nullable=False)

    created_at = Column(DateTime, default=datetime.now)