from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
    QLineEdit
)

from app.models import client
from app.services.client_service import (
    get_all_clients,
    get_client_by_id,
    delete_client,
    )

from PySide6.QtWidgets import QPushButton, QAbstractItemView, QDialog
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

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
            )

        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
            )

        # Кнопка редактирования клиента
        self.edit_button = QPushButton("Редактирование клиента")
        layout.addWidget(self.edit_button)
        self.edit_button.clicked.connect(self.edit_client)

        # Кнопка удаления клиента
        self.delete_button = QPushButton("Удалить клиента")
        layout.addWidget(self.delete_button)
        self.delete_button.clicked.connect(self.delete_selected_client)

        # Поиск клиентов 
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по ФИО или телефону...")
        self.search_input.textChanged.connect(self.search_clients)


        layout.addWidget(self.search_input)
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
        dialog = AddClientDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_clients()

    def edit_client(self):

        row = self.table.currentRow()

        if row == -1:
            print("Выберите клиента!")
            return

        client_id = int(self.table.item(row, 0).text())

        client = get_client_by_id(client_id)

        if client:
            dialog = AddClientDialog(self, client=client)

            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.load_clients()

    def delete_selected_client(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите клиента для удаления!"
            )
            return

        client_id = int(self.table.item(row, 0).text())

        answer = QMessageBox.question(
            self,
            "Подтверждение удаления",
            "Вы уверены, что хотите удалить клиента?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            success = delete_client(client_id)

            if success:
                self.load_clients()
                QMessageBox.information(
                    self,
                    "Успешно",
                    "Клиент удалён!"
                )
            else:
                QMessageBox.warning(
                    self,
                    "Ошибка",
                    "Не удалось удалить клиента!"
                )

    def search_clients(self, text):

         text = text.lower().strip()

         for row in range(self.table.rowCount()):

            name = self.table.item(row, 1).text().lower()
            phone = self.table.item(row, 2).text().lower()

            found = text in name or text in phone

            self.table.setRowHidden(row, not found)
    
