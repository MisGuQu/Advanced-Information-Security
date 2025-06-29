import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plainText.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            data = response.json()  # Đọc phản hồi JSON
            print("Server Response:", data)  # Debug phản hồi API

            if response.status_code == 200 and "encrypted_text" in data:
                self.ui.txt_cipherText.setPlainText(data["encrypted_text"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                error_msg = data.get("error", "Unknown error occurred.")
                QMessageBox.critical(self, "Encryption Failed", error_msg)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Could not connect to API: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipherText.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            data = response.json()
            print("Server Response:", data)  # Debug phản hồi API

            if response.status_code == 200 and "decrypted_text" in data:
                self.ui.txt_plainText.setPlainText(data["decrypted_text"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                error_msg = data.get("error", "Unknown error occurred.")
                QMessageBox.critical(self, "Decryption Failed", error_msg)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Could not connect to API: {str(e)}")

# RailFenceCipher class cho Flask API
class RailFenceCipher:
    def encrypt(self, text, key):
        if key <= 1:
            return text
        rail = ['' for _ in range(key)]
        dir_down = False
        row = 0
        for char in text:
            rail[row] += char
            if row == 0 or row == key - 1:
                dir_down = not dir_down
            row += 1 if dir_down else -1
        return ''.join(rail)

    def decrypt(self, cipher, key):
        if key <= 1:
            return cipher
        rail = [['\n' for _ in range(len(cipher))]
                for _ in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if rail[i][j] == '*' and index < len(cipher):
                    rail[i][j] = cipher[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1
        return ''.join(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())