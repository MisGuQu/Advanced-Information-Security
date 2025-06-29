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
        url = "http://127.0.0.1:5100/api/vigenere/encrypt"
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
        url = "http://127.0.0.1:5100/api/vigenere/decrypt"
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