import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests

# PlayfairCipher class cho Flask API
class PlayfairCipher:
    def __init__(self):
        pass

    def generate_key_square(self, key):
        key = key.upper().replace('J', 'I')
        result = []
        for c in key:
            if c not in result and c.isalpha():
                result.append(c)
        for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if c not in result:
                result.append(c)
        return [result[i*5:(i+1)*5] for i in range(5)]

    def process_text(self, text):
        text = text.upper().replace('J', 'I')
        processed = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'X'
            if a == b:
                processed += a + 'X'
                i += 1
            else:
                processed += a + b
                i += 2
        if len(processed) % 2 != 0:
            processed += 'X'
        return processed

    def find_position(self, key_square, char):
        for i in range(5):
            for j in range(5):
                if key_square[i][j] == char:
                    return i, j
        return None, None

    def encrypt(self, text, key):
        key_square = self.generate_key_square(key)
        text = self.process_text(''.join(filter(str.isalpha, text)))
        result = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            row1, col1 = self.find_position(key_square, a)
            row2, col2 = self.find_position(key_square, b)
            if row1 == row2:
                result += key_square[row1][(col1+1)%5]
                result += key_square[row2][(col2+1)%5]
            elif col1 == col2:
                result += key_square[(row1+1)%5][col1]
                result += key_square[(row2+1)%5][col2]
            else:
                result += key_square[row1][col2]
                result += key_square[row2][col1]
        return result

    def decrypt(self, text, key):
        key_square = self.generate_key_square(key)
        text = ''.join(filter(str.isalpha, text.upper()))
        result = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            row1, col1 = self.find_position(key_square, a)
            row2, col2 = self.find_position(key_square, b)
            if row1 == row2:
                result += key_square[row1][(col1-1)%5]
                result += key_square[row2][(col2-1)%5]
            elif col1 == col2:
                result += key_square[(row1-1)%5][col1]
                result += key_square[(row2-1)%5][col2]
            else:
                result += key_square[row1][col2]
                result += key_square[row2][col1]
        return result

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
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
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())