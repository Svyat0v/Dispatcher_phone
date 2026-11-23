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