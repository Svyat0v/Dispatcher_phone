from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QMessageBox
)
from app.services.client_service import get_client_by_phone

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

	def simulate_call(self):

		phone = "+7900123456"
		client = get_client_by_phone(phone)
		if client:
			message = (
	            f"Номер: {phone}\n"
	            f"ФИО: {client.full_name}\n"
	            f"Адрес: {client.address or 'Не указан'}"
	        )
		
		else:
			message = (
	            f"Номер: {phone}\n"
	            "Клиент не найден в базе данных!"
	        )

		QMessageBox.information(
	        self,
	        "Входящий звонок",
	        message
	    )
