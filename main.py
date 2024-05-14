import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window config
        self.setFixedSize(730, 400)

        # Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 600, 340)
        self.chat_area.setReadOnly(True)

        # Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 360, 600, 30)

        # Send Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(620, 360, 100, 30)
        self.button.clicked.connect("""""")

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

