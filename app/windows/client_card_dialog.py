from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox
)

from app.services.client_service import get_client_by_id


class ClientCardDialog(QDialog):

    def __init__(self, client_id, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Карточка клиента")
        self.resize(450, 300)

        layout = QVBoxLayout(self)

        client = get_client_by_id(client_id)

        if client is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Клиент не найден!"
            )
            return

        layout.addWidget(QLabel(f"ID: {client.id}"))
        layout.addWidget(QLabel(f"ФИО: {client.full_name}"))
        layout.addWidget(QLabel(f"Телефон: {client.phone}"))
        layout.addWidget(QLabel(f"Адрес: {client.address or 'Не указан'}"))
        layout.addWidget(QLabel(f"Email: {client.email or 'Не указан'}"))
        layout.addWidget(QLabel(f"Комментарий: {client.comment or 'Нет'}"))

        self.close_button = QPushButton("Закрыть")

        layout.addWidget(self.close_button)

        self.close_button.clicked.connect(self.accept)