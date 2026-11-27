from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QMessageBox,
    QDialog
)
from app.services.order_service import (
    get_all_orders,
    update_order_status,
    assign_crew
)
from app.services.crew_service import get_all_crews
from app.windows.order_dialog import OrderDialog


class OrdersPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Кнопка создания заявки
        self.add_button = QPushButton("Создать заявку")

        # Выбор статуса заявки
        self.status_combo = QComboBox()

        self.status_combo.addItems([
            "Новая",
            "В работе",
            "Выполнена",
            "Отменена"
        ])

        # Кнопка изменения статуса
        self.change_status_button = QPushButton(
            "Изменить статус"
        )

        self.crew_combo = QComboBox()

        self.assign_crew_button = QPushButton(
            "Назначить бригаду"
        )

        crew_layout = QHBoxLayout()
        crew_layout.addWidget(self.crew_combo)
        crew_layout.addWidget(self.assign_crew_button)

        status_layout = QHBoxLayout()
        status_layout.addWidget(self.status_combo)
        status_layout.addWidget(self.change_status_button)

        # Создание таблицы заявок
        self.table = QTableWidget()

        self.table.setColumnCount(9)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Дата",
            "Заявитель",
            "Телефон",
            "Адрес",
            "Описание",
            "Приоритет",
            "Статус",
            "Бригада"
        ])

        # Растягиваем столбцы
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Выделение всей строки
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        # Можно выбрать только одну заявку
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        # Расположение элементов
        layout.addWidget(self.add_button)
        layout.addLayout(status_layout)
        layout.addLayout(crew_layout)
        layout.addWidget(self.table)

        # Подключение кнопок
        self.add_button.clicked.connect(
            self.open_order_dialog
        )

        self.change_status_button.clicked.connect(
            self.change_order_status
        )

        self.assign_crew_button.clicked.connect(
            self.assign_selected_crew
        )

        # Загружаем заявки при открытии
        self.load_orders()

        self.load_crews_combo()

    def change_order_status(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Сначала выберите заявку!"
            )
            return

        order_id = int(
            self.table.item(row, 0).text()
        )

        new_status = self.status_combo.currentText()

        success = update_order_status(
            order_id=order_id,
            new_status=new_status
        )

        if success:

            self.load_orders()

            QMessageBox.information(
                self,
                "Успешно",
                "Статус заявки обновлён!"
            )

        else:

            QMessageBox.warning(
                self,
                "Ошибка",
                "Не удалось изменить статус заявки!"
            )

    def load_orders(self):

        orders = get_all_orders()

        crews = get_all_crews()

        crew_names = {
            crew.id: crew.name
            for crew in crews
        }

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
                order.status,
                crew_names.get(order.crew_id, "Не назначена"),
            ]

            for column, value in enumerate(values):

                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(value)
                )

    def load_crews_combo(self):

        self.crew_combo.clear()

        crews = get_all_crews()

        for crew in crews:
            self.crew_combo.addItem(
                crew.name,
                crew.id
            )

    def assign_selected_crew(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Сначало выберите заявку"
            )
            return

        order_id = int(
            self.table.item(row, 0).text()
        )

        crew_id = self.crew_combo.currentData()

        if crew_id is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Нет доступных бригад для выбора!"
            )
            return

        success = assign_crew(
            order_id=order_id,
            crew_id=crew_id
        )

        if success:
            self.load_orders()

            QMessageBox.information(
                self,
                "Успешно",
                "Бригада назначена на заявку!"
            )

        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Не удалось назначить бригаду!"
            )


    def open_order_dialog(self):

        dialog = OrderDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_orders()
