from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher  
from cipher.railfence import RailFenceCipher  
from cipher.playfair import PlayfairCipher  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypt_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Route cho Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    vigenere = VigenereCipher()
    encrypt_text = vigenere.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Route cho RailFence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/api/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    railfence = RailFenceCipher()
    encrypt_text = railfence.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/api/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Route cho Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    playfair = PlayfairCipher()
    encrypt_text = playfair.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    playfair = PlayfairCipher()
    decrypted_text = playfair.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Hàm chính
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
