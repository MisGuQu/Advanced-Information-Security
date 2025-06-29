import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
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
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
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

# VigenereCipher class cho Flask API
class VigenereCipher:
    def generate_key(self, text, key):
        key = list(key)
        if len(key) == 0:
            return ""
        while len(key) < len(text):
            key.append(key[len(key) % len(key)])
        return "".join(key)

    def encrypt(self, text, key):
        key = self.generate_key(text, key)
        cipher_text = ""
        for i in range(len(text)):
            if text[i].isalpha():
                offset = 65 if text[i].isupper() else 97
                k = ord(key[i].upper()) - 65
                cipher_text += chr((ord(text[i]) - offset + k) % 26 + offset)
            else:
                cipher_text += text[i]
        return cipher_text

    def decrypt(self, cipher_text, key):
        key = self.generate_key(cipher_text, key)
        orig_text = ""
        for i in range(len(cipher_text)):
            if cipher_text[i].isalpha():
                offset = 65 if cipher_text[i].isupper() else 97
                k = ord(key[i].upper()) - 65
                orig_text += chr((ord(cipher_text[i]) - offset - k + 26) % 26 + offset)
            else:
                orig_text += cipher_text[i]
        return orig_text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())