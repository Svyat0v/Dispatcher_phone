
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class DispatcherWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Настройки главного окна
        self.setWindowTitle("Dispatcher System")
        self.setMinimumSize(1000, 650)

        # Создаём центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной макет
        main_layout = QHBoxLayout(central_widget)

        # Левая панель
        sidebar = QVBoxLayout()

        title = QLabel("ДИСПЕТЧЕРСКАЯ")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        clients_button = QPushButton("Клиенты")
        calls_button = QPushButton("Звонки")
        orders_button = QPushButton("Заявки")
        brigades_button = QPushButton("Бригады")

        sidebar.addWidget(title)
        sidebar.addSpacing(20)
        sidebar.addWidget(clients_button)
        sidebar.addWidget(calls_button)
        sidebar.addWidget(orders_button)
        sidebar.addWidget(brigades_button)
        sidebar.addStretch()

        # Центральная область
        content = QVBoxLayout()

        welcome = QLabel("Рабочее место диспетчера")
        welcome.setStyleSheet(
            "font-size: 26px; font-weight: bold;"
        )

        description = QLabel(
            "Система управления звонками и заявками"
        )

        incoming_call_button = QPushButton(
            "Имитировать входящий звонок"
        )

        incoming_call_button.clicked.connect(
            self.simulate_incoming_call
        )

        content.addWidget(welcome)
        content.addWidget(description)
        content.addSpacing(30)
        content.addWidget(incoming_call_button)
        content.addStretch()

        # Собираем интерфейс
        main_layout.addLayout(sidebar, 1)
        main_layout.addLayout(content, 4)

    def simulate_incoming_call(self):
        QMessageBox.information(
            self,
            "Входящий звонок",
            "Номер: +7 900 123-45-67\n"
            "Клиент: пока не найден\n\n"
            "Это тестовый звонок."
        )


# Запуск приложения
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DispatcherWindow()
    window.show()

    sys.exit(app.exec())
