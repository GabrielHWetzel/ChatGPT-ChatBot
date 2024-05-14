import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        # Window config
        self.setFixedSize(730, 400)

        # Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 710, 340)
        self.chat_area.setReadOnly(True)

        # Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 360, 600, 30)
        self.input_field.returnPressed.connect(self.send_message)

        # Send Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(620, 360, 100, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"You: {user_input}")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_response, args=(user_input, ))
        thread.start()

    def get_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
