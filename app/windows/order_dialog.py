from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QMessageBox
)

from app.services.order_service import add_order


class OrderDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Новая заявка")
        self.resize(500, 450)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        self.description_input = QTextEdit()

        self.priority_input = QComboBox()
        self.priority_input.addItems([
            "Обычная",
            "Срочная",
            "Аварийная"
        ])

        form.addRow("ФИО:", self.name_input)
        form.addRow("Телефон:", self.phone_input)
        form.addRow("Адрес:", self.address_input)
        form.addRow("Описание:", self.description_input)
        form.addRow("Приоритет:", self.priority_input)

        layout.addLayout(form)

        self.save_button = QPushButton("Создать заявку")
        layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_order)

    def save_order(self):

        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.text().strip()

        description = self.description_input.toPlainText().strip()
        priority = self.priority_input.currentText()

        if not name or not phone or not address or not description:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Заполните все обязательные поля!"
            )
            return

        order_id = add_order(
            client_name=name,
            phone=phone,
            address=address,
            description=description,
            priority=priority
        )

        if order_id is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Не удалось сохранить заявку!"
            )
            return

        QMessageBox.information(
            self,
            "Заявка создана",
            f"Успешно создана заявка № {order_id}"
        )

        self.accept()