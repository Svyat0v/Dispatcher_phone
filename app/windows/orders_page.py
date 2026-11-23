from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QDialog
)

from app.services.order_service import get_all_orders
from app.windows.order_dialog import OrderDialog


class OrdersPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.add_button = QPushButton("Создать заявку")

        self.table = QTableWidget()
        self.table.setColumnCount(8)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Дата",
            "Заявитель",
            "Телефон",
            "Адрес",
            "Описание",
            "Приоритет",
            "Статус"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

        self.add_button.clicked.connect(self.open_order_dialog)

        self.load_orders()

    def load_orders(self):

        orders = get_all_orders()

        self.table.setRowCount(len(orders))

        for row, order in enumerate(orders):

            values = [
                str(order.id),
                order.created_at.strftime("%d.%m.%Y %H:%M"),
                order.client_name,
                order.phone,
                order.address,
                order.description,
                order.priority,
                order.status
            ]

            for column, value in enumerate(values):
                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(value)
                )

    def open_order_dialog(self):

        dialog = OrderDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_orders()