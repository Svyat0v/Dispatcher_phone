from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QMessageBox
)
from PySide6.QtWidgets import QTableWidgetItem

from app.services.client_service import get_client_by_phone
from app.services.call_service import get_all_calls, add_call, update_call_status
from app.windows.incoming_call_dialog import IncomingCallDialog


class CallsPage(QWidget):

	def __init__(self):
		super().__init__()

		layout = QVBoxLayout(self)

		title = QLabel("Управлегие звонками")

		self.test_button = QPushButton(
			"Имитировать входящих звонок"
		)

		self.table = QTableWidget()

		self.table.setColumnCount(6)

		self.table.setHorizontalHeaderLabels([
			"ID",
			"Номер телефон",
			"Клиента",
			"Дата и время",
			"Статус",
			"Тип звонка"
		])

		self.table.horizontalHeader().setSectionResizeMode(
			QHeaderView.ResizeMode.Stretch
		)

		layout.addWidget(title)
		layout.addWidget(self.test_button)
		layout.addWidget(self.table)

		self.test_button.clicked.connect(
			self.simulate_call
		)
		self.load_calls()


	def simulate_call(self):
		phone = "+7900123456"

		# Сохраняем новый звонок
		call_id = add_call(
	        phone=phone,
	        call_type="incoming",
	        status="ringing"
	    )

		if call_id is False:
			QMessageBox.warning(
	            self,
	            "Ошибка",
	            "Не удалось сохранить звонок!"
	        )
			return

		self.load_calls()

	    # Определяем звонящего
		client = get_client_by_phone(phone)
		print("Номер входящего звонка:", repr(phone))
		print("Клиент найден:", client)

		if client:
			print("ID:", client.id)
			print("ФИО:", client.full_name)
			print("Телефон из базы:", repr(client.phone))
			print("Адрес:", client.address)
		else:
		    print("Клиент с таким номером отсутствует!")

		client_name = (
	        client.full_name if client else "Неизвестный клиент"
	    )

		client_address = client.address if client else None
		client_id = client.id if client else None

	    # Показываем окно входящего звонка
		dialog = IncomingCallDialog(
		    phone=phone,
		    client_name=client_name,
		    address=client_address,
		    client_id=client_id,
		    parent=self
		)
		result = dialog.exec()

	    # Определяем новый статус
		if result == 1:
			new_status = "answered"

		elif result == 2:
			new_status = "rejected"

		else:
			new_status = "missed"

	    # Обновляем запись в SQLite
		success = update_call_status(call_id, new_status)

		if not success:
			QMessageBox.warning(
	            self,
	            "Ошибка",
	            "Не удалось обновить статус звонка!"
	        )

		self.load_calls()

	def load_calls(self):

		calls = get_all_calls()

		self.table.setRowCount(len(calls))

		for row, call in enumerate(calls):

			client = get_client_by_phone(call.phone)

			if client:
				client_name = client.full_name
			else:
				client_name = "Неизвестный клиент"

			self.table.setItem(
				row, 0, QTableWidgetItem(str(call.id))
			)

			self.table.setItem(
				row, 1, QTableWidgetItem(str(call.phone))
			)

			self.table.setItem(
				row, 2, QTableWidgetItem(client_name)
			)

			self.table.setItem(
				row, 3,
				QTableWidgetItem(
					call.created_at.strftime("%d.%m.%Y %H:%M:%S")
					)
			)

			self.table.setItem(
				row, 4, QTableWidgetItem(call.status)
			)
