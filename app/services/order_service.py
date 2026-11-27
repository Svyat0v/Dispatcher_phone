from app.database.connection import SessionLocal
from app.models.order import Order
from app.models.crew import Crew


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
            "Выполнена",
            "Отменена"
        ]

        if new_status not in allowed_statuses:
            return False

        # Запрещаем начало работы без бригады
        if new_status == "В работе" and order.crew_id is None:
            print("Сначала назначьте бригаду!")
            return False

        # Проверяем занятость бригады
        if new_status == "В работе":

            active_order = session.query(Order).filter(
                Order.crew_id == order.crew_id,
                Order.status == "В работе",
                Order.id != order_id
            ).first()

            if active_order:
                print(
                    f"Бригада уже выполняет заявку № {active_order.id}"
                )
                return False

        order.status = new_status

        session.commit()
        return True

    except Exception as error:
        session.rollback()
        print(f"Ошибка обновления заявки: {error}")
        return False

    finally:
        session.close()


def assign_crew(order_id, crew_id):

    session = SessionLocal()

    try:
        order = session.query(Order).filter(
            Order.id == order_id
        ).first()

        crew = session.query(Crew).filter(
            Crew.id == crew_id
        ).first()

        if order is None or crew is None:
            return False

        active_orders = session.query(Order).filter(
            Order.crew_id == crew_id,
            Order.status == "В работе",
            Order.id != order_id
        ).all()

        if active_orders:
            print("Бригада уже выполняет другую заявку!")
            return False

        order.crew_id = crew.id

        session.commit()
        return True

    except Exception as error:
        session.rollback()
        print(f"Ошибка назначения: {error}")
        return False

    finally:
        session.close()


def get_active_orders_by_crew(crew_id):

    session = SessionLocal()

    try:
        orders = session.query(Order).filter(
            Order.crew_id == crew_id,
            Order.status == "В работе"
        ).all()

        return orders

    finally:
        session.close()


def is_crew_available(crew_id):

    active_orders = get_active_orders_by_crew(crew_id)

    if active_orders:
        return False

    return True
