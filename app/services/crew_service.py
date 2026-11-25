from app.database.connection import SessionLocal
from app.models.crew import Crew


def add_crew(name, leader, phone=None):

    session = SessionLocal()

    try:
        crew = Crew(
            name=name,
            leader=leader,
            phone=phone,
            status="Свободна"
        )

        session.add(crew)
        session.commit()

        return crew.id

    except Exception as error:
        session.rollback()
        print(f"Ошибка создания бригады: {error}")
        return None

    finally:
        session.close()


def get_all_crews():

    session = SessionLocal()

    try:
        return session.query(Crew).order_by(
            Crew.id
        ).all()

    finally:
        session.close()