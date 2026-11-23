import re

from PySide6.QtGui import qAlpha
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)
from app.models import client
from app.windows.client_card_dialog import ClientCardDialog



class IncomingCallDialog(QDialog):

    def __init__(
        self,
        phone,
        client_name,
        address=None,
        client_id=None,
        parent=None
    ):
        super().__init__(parent)

        self.client_id = client_id

        self.setWindowTitle("Входящий звонок")
        self.resize(400, 220)

        layout = QVBoxLayout(self)

        self.phone_label = QLabel(f"Номер: {phone}")
        self.client_label = QLabel(f"Клиент: {client_name}")
        self.address_label = QLabel(
            f"Адресс: {address or 'Не указан'}"
            )

        buttons_layout = QHBoxLayout()

        self.answer_button = QPushButton("Принять")
        self.reject_button = QPushButton("Отклонить")
        self.client_button = QPushButton("Карточка клиента")

        buttons_layout.addWidget(self.answer_button)
        buttons_layout.addWidget(self.reject_button)

        self.answer_button.clicked.connect(self.answer_call)
        self.reject_button.clicked.connect(self.reject_call)

        layout.addWidget(self.client_button)
        layout.addWidget(self.address_label)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.client_label)
        layout.addLayout(buttons_layout)


    def answer_call(self):
        self.done(1)


    def reject_call(self):
        self.done(2)

    def open_client_card(self):

        if self.client_id is None:
            QMessageBox.warning(
                self,
                "Клиент не найден",
                "Этот номер отсутсвует в базе клиентов."
            )
        return 

        dialog = ClientCardDialog(
            client_id=self.client_id,
            parent=self
        )

        dialog.exec()