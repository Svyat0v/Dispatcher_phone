from typing import final

from app.database.connection import SessionLocal
from app.models.call import Call
from sqlalchemy import true
from sqlalchemy.orm import session
from sqlalchemy.sql.dml import ReturningDelete


def add_call(phone, call_type, status):

	session = SessionLocal()

	try:
		call = Call(
			phone=phone,
			call_type=call_type,
			status=status
		)

		session.add(call)
		session.commit()

		return call.id

	except Exception as error:
		session.rollback()
		print(f"Ошибка сохранения звонка: {error}")
		return False

	finally:
		session.close()


def get_all_calls():

    session = SessionLocal()

    try:
        calls = session.query(Call).order_by(
            Call.created_at.desc()
        ).all()

        return calls

    finally:
        session.close()


def update_call_status(call_id, new_status):

	session = SessionLocal()

	try:
		call = session.query(Call).filter(
			Call.id == call_id
			).first()

		if not call:
			return False

		call.status = new_status

		session.commit()

		return True

	except Exception as error:
		session.rollback()
		print(f"Ошибка изменения статуса: {error}")
		return False

	finally:
		session.close()


def get_call_by_id(call_id):

	session = SessionLocal()

	try:
		call = session.query(Call).filter(
			Call.id == call_id
			).first()

		if call:
			return call

		else:
			return None

	finally:
		session.close()