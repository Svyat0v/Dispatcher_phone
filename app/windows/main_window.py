from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget
)
from app.windows.clients_page import ClientsPage
from app.windows.calls_page import CallsPage
from app.windows.orders_page import OrdersPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Диспетчерская система")
        self.resize(1100, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        sidebar = QVBoxLayout()

        self.pages = QStackedWidget()

        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.pages, 4)

        self.clients_button = QPushButton("Клиенты")
        self.calls_button = QPushButton("Звонки")
        self.orders_button = QPushButton("Заявки")
        self.crews_button = QPushButton("Бригады")
        self.reports_button = QPushButton("Отчеты")

        sidebar.addWidget(QLabel("ДИСПЕТЧЕРСКАЯ"))
        sidebar.addWidget(self.clients_button)
        sidebar.addWidget(self.calls_button)
        sidebar.addWidget(self.orders_button)
        sidebar.addWidget(self.crews_button)
        sidebar.addWidget(self.reports_button)
        sidebar.addStretch()

        self.pages.addWidget(ClientsPage())
        self.pages.addWidget(CallsPage())
        self.pages.addWidget(OrdersPage())
        self.pages.addWidget(QLabel("Страница бригад"))
        self.pages.addWidget(QLabel("Отчеты"))

        self.clients_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(0)
        )

        self.calls_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(1)
        )

        self.orders_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(2)
        )

        self.crews_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(3)
        )

        self.reports_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(4)
        )
