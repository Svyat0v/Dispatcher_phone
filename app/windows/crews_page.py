from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QDialog
)

from app.services.crew_service import get_all_crews
from app.windows.crew_dialog import CrewDialog
from app.services.order_service import get_active_orders_by_crew


class CrewsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Управление бригадами")

        self.add_button = QPushButton("Добавить бригаду")
        self.add_button.clicked.connect(self.open_crew_dialog)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Название",
            "Ответственный",
            "Телефон",
            "Статус"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(title)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

        self.load_crews()

    def load_crews(self):

        crews = get_all_crews()

        self.table.setRowCount(len(crews))

        for row, crew in enumerate(crews):

            active_orders = get_active_orders_by_crew(crew.id)

            if active_orders:
                status = "На выезде"
            else:
                status = "Свободна"

            values = [
                str(crew.id),
                crew.name,
                crew.leader,
                crew.phone or "",
                status
            ]

            for column, value in enumerate(values):
                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(value)
                )

    def open_crew_dialog(self):
        dialog = CrewDialog()

        if dialog.exec_() == QDialog.DialogCode.Accepted:
            self.load_crews()