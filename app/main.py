import sys

from PySide6.QtWidgets import QApplication

from app.database.init_db import create_database
from app.windows.main_window import MainWindow


def main():
    create_database()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
