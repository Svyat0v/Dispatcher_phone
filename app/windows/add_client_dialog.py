from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)
from app.services.client_service import add_client, update_client
from PySide6.QtWidgets import QMessageBox


class AddClientDialog(QDialog):

    def __init__(self, parent=None, client=None):
        super().__init__(parent)

        self.client = client

        self.setWindowTitle("Добавление клиента")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()
        self.email_input = QLineEdit()

        if self.client:
            self.name_input.setText(self.client.full_name)
            self.phone_input.setText(self.client.phone)
            self.address_input.setText(self.client.address)
            self.email_input.setText(self.client.email)

        layout.addWidget(QLabel("ФИО:"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Телефон:"))
        layout.addWidget(self.phone_input)

        layout.addWidget(QLabel("Адрес:"))
        layout.addWidget(self.address_input)

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_client)
        layout.addWidget(self.save_button)

    def save_client(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.text().strip()
        email = self.email_input.text().strip()

        if not name or not phone:
            print("Заполните ФИО и Телефон!")
            return

        if self.client:
            success = update_client(
                client_id=self.client.id,
                full_name=name,
                phone=phone,
                address=address,
                email=email
            )
        else:
            success = add_client(
                full_name=name,
                phone=phone,
                address=address,
                email=email
            )

        if success:
            self.accept()
        else:
            QMessageBox.warning(
                self,
                "Ошибка сохранения",
                "Не удалось добавить клиента. Возможно, номер телефона уже существует."
            )
