from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from flask_cors import CORS
import os
import platform
import subprocess
app = Flask(__name__)
CORS(app)
# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORM_POPUP_DIR = os.path.join(BASE_DIR,"TEST")


@app.route('/run_command', methods=['POST'])
def run_command():
    data = request.json
    command = data.get('command12')
    print("EXUTE : {command}")
    if command == "caesar":
        command_to_run = "python caesar_cipher.py"
    elif command == "vigenere":
        command_to_run = "python vigenere_cipher.py"
    elif command == "railfence":
        command_to_run = "python railfence_cipher.py"
    elif command == "playfair":
        command_to_run = "python playfair_cipher.py"
    else:
        return {"error": "Invalid command"}, 400
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Thay đổi thư mục làm việc đến thư mục form_popup
        os.chdir(FORM_POPUP_DIR)

        # In thông tin debug
        print(f"Executing command: {command_to_run}")
        print(f"Current directory: {os.getcwd()}")

        # Tạo đối tượng Popen với các tham số phù hợp cho từng hệ điều hành
        if platform.system() == 'Windows':
            process = subprocess.Popen(
                command_to_run,
                shell=True,
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.getcwd()  # Đảm bảo chạy trong đúng thư mục
            )
        else:
            process = subprocess.Popen(
                command_to_run,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.getcwd()  # Đảm bảo chạy trong đúng thư mục
            )

        # Đọc lỗi nếu có
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return jsonify({
                'error': f'Command failed with return code {process.returncode}',
                'stderr': stderr,
                'stdout': stdout,
                'command': command_to_run,
                'cwd': os.getcwd()
            }), 500

        # Không cần đợi process kết thúc
        return jsonify({
            'success': True,
            'pid': process.pid,
            'command': command_to_run,
            'cwd': os.getcwd()
        })

    except Exception as e:
        error_msg = str(e)
        print(f"Error in run_command: {error_msg}")
        return jsonify({
            'error': error_msg,
            'cwd': os.getcwd(),
            'command': command,
            'type': type(e).__name__
        }), 500


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()


@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()


@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM


playfair_cipher = PlayfairCipher()


@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(
        plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(
        cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
