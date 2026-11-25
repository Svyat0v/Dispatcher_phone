from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Crew(Base):

    __tablename__ = "crews"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)

    leader = Column(String(150), nullable=False)

    phone = Column(String(30), nullable=True)

    status = Column(String(30), default="Свободна")