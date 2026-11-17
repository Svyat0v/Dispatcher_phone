from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    phone = Column(String(30), unique=True, nullable=False)
    address = Column(String(250), nullable=True)
    comment = Column(String(500), nullable=True)
    email = Column(String(120), nullable=True)
