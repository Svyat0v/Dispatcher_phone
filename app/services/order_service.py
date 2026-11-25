from app.database.connection import SessionLocal
from app.models.order import Order


def add_order(client_name, phone, address, description, priority):

    session = SessionLocal()

    try:
        order = Order(
            client_name=client_name,
            phone=phone,
            address=address,
            description=description,
            priority=priority,
            status="Новая"
        )

        session.add(order)
        session.commit()

        return order.id

    except Exception as error:
        session.rollback()
        print(f"Ошибка создания заявки: {error}")
        return None

    finally:
        session.close()


def get_all_orders():

    session = SessionLocal()

    try:
        orders = session.query(Order).order_by(
            Order.id.desc()
        ).all()

        return orders

    finally:
        session.close()

def update_order_status(order_id, new_status):
    session = SessionLocal()

    try:
        order = session.query(Order).filter(
            Order.id == order_id
        ).first()

        if order is None:
            return False

        allowed_statuses = [
            "Новая",
            "В работе",
            "Выполненая",
            "Отменёная"
        ]

        if new_status not in allowed_statuses:
            return False

        order.status = new_status

        session.commit()
        return True

    except Exception as errorr:
        session.rollback()
        print(f"Ошибка обновления заявки: {errorr}")
        return False

    finally:
        session.close()
