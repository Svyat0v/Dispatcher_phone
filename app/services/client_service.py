from app.database.connection import SessionLocal
from app.models.client import Client
from sqlalchemy.orm import session


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

        return True

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

def get_client_by_id(client_id):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.id == client_id
            ).first()

        if client:
            print("Клиента найден!")
            return client

        return None

    finally:
        session.close()

def update_client(client_id, full_name, phone, address, email):

    session = SessionLocal()

    try:
        client = session.query(Client).filter(
            Client.id == client_id
            ).first()

        if not client:
            return False

        client.full_name = full_name
        client.phone = phone
        client.address = address
        client.email = email

        session.commit()
        return True

    except Exception as error:
        session.rollback()
        print(f"Ошибка обновления клиента: {error}")
        return False

    finally:
        session.close()

