from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.database.connection import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    client_name = Column(String(150), nullable=False)

    phone = Column(String(30), nullable=False)

    address = Column(String(250), nullable=False)

    description = Column(String(1000), nullable=False)

    priority = Column(String(30), default="Обычная")

    status = Column(String(30), default="Новая")

    created_at = Column(DateTime, default=datetime.now)