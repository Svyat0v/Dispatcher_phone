from app.database.connection import Base, engine

# Импортируем модели
from app.models.client import Client
from app.models.call import Call
from app.models.order import Order



def create_database():

    Base.metadata.create_all(bind=engine)

    print("База данных успешно создана!")


if __name__ == "__main__":
    create_database()
