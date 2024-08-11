from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
)
from PySide6.QtGui import QCloseEvent, QPixmap, QFont
from PySide6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.login_line_edit = None
        self.password_line_edit = None

        self.setup()

    def setup(self):
        self.setFixedSize(400, 600)
        self.setWindowTitle("Login Window")
        self.setStyleSheet("background-color: #f0f0f0;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 30, 50, 30)

        pix_label = QLabel(self)
        pixmap = QPixmap(
            r"C:\Users\Paweł\Desktop\Documnets\af4d35e50215136900a7c2994e117b9a.jpg"
        ).scaled(250, 250)
        pix_label.setPixmap(pixmap)
        pix_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_line_edit = QLineEdit(self)
        self.login_line_edit.setPlaceholderText("Username")
        self.login_line_edit.setFixedHeight(35)
        self.login_line_edit.setStyleSheet("padding: 5px; color: #000000;")
        self.login_line_edit.setFont(QFont("Arial", 12))

        self.password_line_edit = QLineEdit(self)
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setFixedHeight(35)
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit.setStyleSheet("padding: 5px; color: #000000;")
        self.password_line_edit.setFont(QFont("Arial", 12))

        submit_btn = QPushButton("Submit", self)
        submit_btn.setFixedHeight(40)
        submit_btn.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 5px; font-size: 14px;"
        )
        submit_btn.clicked.connect(self.submit)

        quit_btn = QPushButton("Quit", self)
        quit_btn.setFixedHeight(40)
        quit_btn.setStyleSheet(
            "background-color: #f44336; color: white; border-radius: 5px; font-size: 14px;"
        )
        quit_btn.clicked.connect(QApplication.instance().quit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_btn)
        button_layout.addWidget(quit_btn)

        main_layout.addWidget(pix_label)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.login_line_edit)
        main_layout.addWidget(self.password_line_edit)
        main_layout.addSpacing(20)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.show()

    def submit(self):
        username = self.login_line_edit.text()
        QMessageBox.information(self, "Login Info", f"Username: {username}")

    def closeEvent(self, event: QCloseEvent):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Close App")
        message_box.setText("Do you want to close?")
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.No)
        message_box.setStyleSheet("QLabel{color: #000000;} QPushButton{color: #000000;}")

        response = message_box.exec()

        if response == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()
