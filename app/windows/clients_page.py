from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)
from app.services.client_service import get_all_clients
from PySide6.QtWidgets import QPushButton
from app.windows.add_client_dialog import AddClientDialog


class ClientsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Управление клиентами")
        self.add_button = QPushButton("Добавить клиента")
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.open_add_dialog)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "ФИО",
            "Телефон",
            "Адрес",
            "Email"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # self.table.setRowCount(1)
        #
        # client_id = QTableWidgetItem("1")
        # item = QTableWidgetItem("Иван Иванов")
        # phone = QTableWidgetItem("+7900123456")
        #
        # self.table.setItem(0, 0, client_id)
        # self.table.setItem(0,1, item)
        # self.table.setItem(0, 2, phone)

        layout.addWidget(title)
        layout.addWidget(self.table)
        self.load_clients()

    def load_clients(self):
        clients = get_all_clients()

        self.table.setRowCount(len(clients))

        for row, client in enumerate(clients):
            self.table.setItem(
                row, 0, QTableWidgetItem(str(client.id))
            )

            self.table.setItem(
                row, 1, QTableWidgetItem(client.full_name)
            )

            self.table.setItem(
                row, 2, QTableWidgetItem(client.phone)
            )

            self.table.setItem(
                row, 3, QTableWidgetItem(client.address or "")
            )

            self.table.setItem(
                row, 4, QTableWidgetItem(client.email or "")
            )

    def open_add_dialog(self):
        dialog = AddClientDialog()
        dialog.exec()
