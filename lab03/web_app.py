from flask import Flask, render_template, request, jsonify
import sys
import os

# Import các cipher modules
from caesar_cipher import CaesarCipher
from playfair_cipher import PlayfairCipher
from railfence_cipher import RailFenceCipher
from vigenere_cipher import VigenereCipher

app = Flask(__name__)

# Khởi tạo các cipher objects
caesar = CaesarCipher()
playfair = PlayfairCipher()
railfence = RailFenceCipher()
vigenere = VigenereCipher()

@app.route('/')
def index():
    """Trang chính với các link đến các cipher"""
    return render_template('index.html')

@app.route('/caesar')
def caesar_page():
    """Trang Caesar Cipher"""
    return render_template('caesar.html')

@app.route('/playfair')
def playfair_page():
    """Trang Playfair Cipher"""
    return render_template('playfair.html')

@app.route('/railfence')
def railfence_page():
    """Trang Rail Fence Cipher"""
    return render_template('railfence.html')

@app.route('/vigenere')
def vigenere_page():
    """Trang Vigenere Cipher"""
    return render_template('vigenere.html')

# API endpoints cho Caesar Cipher
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    
    try:
        key = int(key)
        encrypted = caesar.encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted})
    except ValueError:
        return jsonify({'error': 'Key must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    
    try:
        key = int(key)
        decrypted = caesar.decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted})
    except ValueError:
        return jsonify({'error': 'Key must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoints cho Playfair Cipher
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    
    try:
        encrypted = playfair.encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    
    try:
        decrypted = playfair.decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoints cho Rail Fence Cipher
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    
    try:
        key = int(key)
        encrypted = railfence.encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted})
    except ValueError:
        return jsonify({'error': 'Key must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    
    try:
        key = int(key)
        decrypted = railfence.decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted})
    except ValueError:
        return jsonify({'error': 'Key must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoints cho Vigenere Cipher
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    
    try:
        encrypted = vigenere.encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    
    try:
        decrypted = vigenere.decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 