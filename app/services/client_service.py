from app.database.connection import SessionLocal
from app.models.client import Client


def add_client(full_name, phone, address=None, comment=None, email=None):

    session = SessionLocal()

    try:
        client = Client(
            full_name=full_name,
            phone=phone,
            address=address,
            comment=comment,
            email=email
        )

        session.add(client)
        session.commit()

        print("Клиент успешно добавлен!")

    except Exception as error:
        session.rollback()
        print(f"Ошибка при добавлении клиента: {error}")

    finally:
        session.close()
