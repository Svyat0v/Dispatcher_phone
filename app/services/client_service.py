from app.database.connection import SessionLocal
from app.models.client import Client


def add_client(full_name,
               phone,
               address=None,
               comment=None,
               email=None
               ):

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

def get_all_clients():

    session = SessionLocal()

    try:
        clients = session.query(Client).all()

        return clients

    finally:
        session.close()

def get_client_by_phone(phone):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.phone == phone
        ).first()

        return client

    finally:
        session.close()


def get_client_by_name(full_name):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.full_name == full_name
        ).first()

        return client

    finally:
        session.close()

def update_client_phone(new_phone, client_id):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.id == client_id
        ).first()

        if client:

            client.phone = new_phone

            session.commit()

            return True

        else:
            print("Клиент не был обновлен")
            return False

    finally:
        session.close()

def delete_client(client_id):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.id == client_id
        ).first()

        if client:

            session.delete(client)
            session.commit()
            return True

        else:
            print("Клиент не был удален")
            return False

    finally:
        session.close()



