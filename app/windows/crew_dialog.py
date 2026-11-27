
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from app.services.crew_service import add_crew


class CrewDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Добавление бригады")
        self.resize(400, 250)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.name_input = QLineEdit()
        self.leader_input = QLineEdit()
        self.phone_input = QLineEdit()

        form.addRow("Название:", self.name_input)
        form.addRow("Ответственный:", self.leader_input)
        form.addRow("Телефон:", self.phone_input)

        layout.addLayout(form)

        self.save_button = QPushButton("Сохранить")
        layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_crew)

    def save_crew(self):
        name = self.name_input.text().strip()
        leader = self.leader_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not leader:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Заполните название и ответственного!"
            )
            return

        crew_id = add_crew(
            name=name,
            leader=leader,
            phone=phone or None
        )

        if crew_id is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Не удалось создать бригаду. Проверьте название."
            )
            return

        self.accept()
