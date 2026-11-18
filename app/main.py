import sys

from PySide6.QtWidgets import QApplication
from app.windows.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()








#
# import sys
#
# from PySide6.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
#     QHBoxLayout,
#     QStackedWidget,
# )
#
# from PySide6.QtCore import Qt
#
#
# class DispatcherWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Dispatcher System")
#         self.setMinimumSize(1000, 650)
#
#         # Главный контейнер
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         main_layout = QHBoxLayout(central_widget)
#
#         # Левая панель
#         sidebar = QVBoxLayout()
#
#         title = QLabel("ДИСПЕТЧЕРСКАЯ")
#         title.setStyleSheet(
#             "font-size: 20px; font-weight: bold;"
#         )
#
#         self.home_button = QPushButton("Главная")
#         self.clients_button = QPushButton("Клиенты")
#         self.calls_button = QPushButton("Звонки")
#         self.orders_button = QPushButton("Заявки")
#         self.crew_button = QPushButton("Бригада")
#
#         sidebar.addWidget(title)
#         sidebar.addSpacing(20)
#         sidebar.addWidget(self.home_button)
#         sidebar.addWidget(self.clients_button)
#         sidebar.addWidget(self.calls_button)
#         sidebar.addWidget(self.orders_button)
#         sidebar.addWidget(self.crew_button)
#         sidebar.addStretch()
#
#         # Контейнер страниц
#         self.pages = QStackedWidget()
#
#         self.pages.addWidget(
#             self.create_page("Главная", "Рабочее место диспетчера")
#         )
#
#         self.pages.addWidget(
#             self.create_page("Клиенты", "Справочник клиентов")
#         )
#
#         self.pages.addWidget(
#             self.create_page("Звонки", "История телефонных звонков")
#         )
#
#         self.pages.addWidget(
#             self.create_page("Заявки", "Управление заявками")
#         )
#
#         self.pages.addWidget(
#             self.create_page("Бригада", "Список занятости")
#         )
#
#
#         # Подключаем кнопки к функциям
#         self.home_button.clicked.connect(self.open_home)
#         self.clients_button.clicked.connect(self.open_clients)
#         self.calls_button.clicked.connect(self.open_calls)
#         self.orders_button.clicked.connect(self.open_orders)
#         self.crew_button.clicked.connect(self.open_crew)
#
#         # Собираем интерфейс
#         main_layout.addLayout(sidebar, 1)
#         main_layout.addWidget(self.pages, 4)
#
#     def create_page(self, title, description):
#
#         page = QWidget()
#         layout = QVBoxLayout(page)
#
#         heading = QLabel(title)
#         heading.setStyleSheet(
#             "font-size: 26px; font-weight: bold;"
#         )
#
#         info = QLabel(description)
#
#         layout.addWidget(heading)
#         layout.addWidget(info)
#         layout.addStretch()
#
#         return page
#
#     # Функции переключения страниц
#
#     def open_home(self):
#         self.pages.setCurrentIndex(0)
#
#     def open_clients(self):
#         self.pages.setCurrentIndex(1)
#
#     def open_calls(self):
#         self.pages.setCurrentIndex(2)
#
#     def open_orders(self):
#         self.pages.setCurrentIndex(3)
#
#     def open_crew(self):
#         self.pages.setCurrentIndex(4)
#
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#
#     window = DispatcherWindow()
#     window.show()
#
#     sys.exit(app.exec())
