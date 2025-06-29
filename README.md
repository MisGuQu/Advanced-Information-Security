# BMTTNC-hutech-2280602235
TranDaoPhuongNhi-2280602235

## Giới thiệu
Đây là project tổng hợp các bài thực hành môn Bảo Mật Thông Tin, gồm 5 lab với các chủ đề về mã hóa, giải mã, giao diện ứng dụng, lập trình socket, hash, Diffie-Hellman, AES/RSA và giấu tin trong ảnh.

---

## Yêu cầu phần mềm & hệ điều hành

- **Python 3.8+** (khuyến nghị Python 3.10)
- Hệ điều hành: Windows, Linux hoặc MacOS đều chạy tốt
- Nên sử dụng môi trường ảo (virtualenv, venv, hoặc conda)
- Một số lab yêu cầu cài đặt thêm: Qt Designer (cho PyQt5), Pillow, cryptography, pycryptodome, tornado, flask, requests...

---

## Cấu trúc thư mục tổng quát

```
lab01/           # Bài tập Python cơ bản về mã hóa
lab02/           # Xây dựng API mã hóa cổ điển (Flask)
lab03/           # Ứng dụng mã hóa cổ điển với giao diện PyQt5
lab04/           # Lập trình socket, hash, Diffie-Hellman, AES/RSA
lab05/           # Ứng dụng tổng hợp & giấu tin trong ảnh
README.md        # File hướng dẫn tổng quan
```

---

## Hướng dẫn cài đặt requirements

Vào từng thư mục lab và chạy:

```
pip install -r requirements.txt
```

**Chi tiết requirements:**
- `lab02/requirements.txt`: Flask>=2.3.2
- `lab03/requirements.txt`: PyQt5, requests
- `lab04/websocket/requirements.txt`: tornado
- `lab04/dh_key_pair/requirements.txt`: cryptography
- `lab04/aes_rsa_socket/requirements.txt`: pycryptodome
- `lab05/TEST/requirements.txt`: flask-cors
- `lab05/img-hidden/requirements.txt`: Pillow, cryptography

---

## Mô tả chi tiết từng Lab

### Lab 01: Các bài tập Python cơ bản về mã hóa
- **Thư mục:** `lab01/`
- **Nội dung:** Gồm các file `ex02_01.py` đến `ex02_09.py`.
- **Chức năng:** Cài đặt các thuật toán mã hóa/giải mã đơn giản, luyện tập thao tác với chuỗi, số, và các hàm cơ bản trong Python.
- **Cách chạy:**  
  ```
  python ex02_01.py
  ```
  (Tương tự cho các file khác.)

---

### Lab 02: Xây dựng API mã hóa cổ điển với Flask
- **Thư mục:** `lab02/`
- **Cấu trúc:**
  - `api.py`, `app.py`: Chạy server Flask.
  - `cipher/`: Chứa các thuật toán mã hóa:
    - **Caesar Cipher** (`caesar/caesar_cipher.py`)
    - **Playfair Cipher** (`playfair/playfair_cipher.py`)
    - **Rail Fence Cipher** (`railfence/railfence_cipher.py`)
    - **Vigenère Cipher** (`vigenere/vigenere_cipher.py`)
  - `templates/`: Giao diện web mẫu (HTML).
- **Chức năng:**  
  - Cung cấp API RESTful cho từng thuật toán mã hóa/giải mã.
  - Giao diện web nhập liệu và nhận kết quả.
- **Cách chạy:**

**1. Chuyển file .ui sang .py:**
```sh
pyuic5 -x ./ui/caesar.ui -o ./ui/caesar.py
# hoặc
python -m PyQt5.uic.pyuic -x ./ui/caesar.ui -o ./ui/caesar.py
```

**2. Nếu gặp lỗi về plugin Qt, hãy thêm vào đầu file `caesar.py`:**
```python
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
```

**3. Chạy ứng dụng:**

- **Cách 1: Chạy API và script riêng biệt**
  - Mở 2 terminal:
    - Terminal 1:
      ```sh
      cd lab02
      python api.py
      ```
    - Terminal 2:
      ```sh
      python caesar_cipher.py
      ```

- **Cách 2: Chạy web app**
  ```sh
  python web_app.py
  ```

- **Chi tiết thuật toán:**
  - **Caesar Cipher:** Dịch chuyển ký tự theo khóa số nguyên.
  - **Playfair Cipher:** Mã hóa theo ma trận 5x5, xử lý cặp ký tự.
  - **Rail Fence Cipher:** Sắp xếp ký tự theo hình ziczac với số rail tùy chọn.
  - **Vigenère Cipher:** Mã hóa đa bảng với khóa là chuỗi ký tự.

---

### Lab 03: Ứng dụng mã hóa cổ điển với giao diện PyQt5
- **Thư mục:** `lab03/`
- **Cấu trúc:**
  - `ui/`: File giao diện `.ui` và code giao diện `.py` cho từng thuật toán.
  - `caesar_cipher.py`, `playfair_cipher.py`, `railfence_cipher.py`, `vigenere_cipher.py`: Cài đặt thuật toán.
  - `web_app.py`: Chạy ứng dụng web tổng hợp.
  - `templates/`: Giao diện web mẫu.
- **Chức năng:**  
  - Ứng dụng desktop với giao diện người dùng cho từng thuật toán mã hóa/giải mã.
  - Có thể chạy từng file hoặc chạy web_app.py để dùng giao diện web.
- **Cách chạy:**  
pyuic5 -x ./ui/caesar.ui -o ./ui/caesar.py          
//import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"// vào caesar.py
python -m PyQt5.uic.pyuic -x ./ui/caesar.ui -o ./ui/caesar.py
  ---
  Terminal 1
  cd lab02
  python api.py       
  Terminal 2
  python caser_cipher.py   
  ```
  hoặc
  ```
  python web_app.py
  ```

---

### Lab 04: Lập trình socket, hash, Diffie-Hellman, AES/RSA
- **Thư mục:** `lab04/`
- **Cấu trúc:**
  - `websocket/`: Lập trình client-server với Tornado websocket.
    - `client.py`, `server.py`
  - `hash/`: Cài đặt các thuật toán băm:
    - `md5_hash.py`, `md5_library.py`, `sha-256.py`, `sha-3.py`, `blake2.py`
  - `dh_key_pair/`: Mô phỏng trao đổi khóa Diffie-Hellman.
    - `client.py`, `server.py`
  - `aes_rsa_socket/`: Mã hóa AES/RSA qua socket.
    - `client.py`, `server.py`
- **Chức năng:**  
  - Giao tiếp client-server qua socket, websocket.
  - Thực hiện các thuật toán hash phổ biến.
  - Mô phỏng trao đổi khóa và mã hóa đối xứng/bất đối xứng.
- **Cách chạy:**  
  
  #### 1. websocket/ (Giao tiếp client-server qua websocket)
  - **Mở 2 terminal:**
    - Terminal 1:
      ```
      cd lab04/websocket
      python server.py
      ```
    - Terminal 2:
      ```
      cd lab04/websocket
      python client.py
      ```
    - **server.py** phải chạy trước để lắng nghe kết nối, sau đó mới chạy **client.py** để kết nối và gửi/nhận dữ liệu.

  #### 2. dh_key_pair/ (Trao đổi khóa Diffie-Hellman)
  - **Mở 2 terminal:**
    - Terminal 1:
      ```
      cd lab04/dh_key_pair
      python server.py
      ```
    - Terminal 2:
      ```
      cd lab04/dh_key_pair
      python client.py
      ```
    - **server.py** chạy trước để tạo server nhận kết nối, sau đó mới chạy **client.py** để thực hiện trao đổi khóa.

  #### 3. aes_rsa_socket/ (Mã hóa AES/RSA qua socket)
  - **Mở 2 terminal:**
    - Terminal 1:
      ```
      cd lab04/aes_rsa_socket
      python server.py
      ```
    - Terminal 2:
      ```
      cd lab04/aes_rsa_socket
      python client.py
      ```
    - **server.py** chạy trước để lắng nghe kết nối, sau đó mới chạy **client.py** để gửi/nhận dữ liệu đã mã hóa.

  #### 4. hash/ (Các thuật toán băm)
  - **Chỉ cần 1 terminal cho mỗi file:**
    ```
    cd lab04/hash
    python md5_hash.py
    python sha-256.py
    python sha-3.py
    python blake2.py
    python md5_library.py
    ```
  - Các file hash là script độc lập, không cần chạy song song.

---

### Lab 05: Ứng dụng tổng hợp & giấu tin trong ảnh
- **Thư mục:** `lab05/`
- **Cấu trúc:**
  - `img-hidden/`: Cài đặt thuật toán giấu tin trong ảnh (steganography).
    - `encrypt.py`, `decrypt.py`
  - `TEST/`: Ứng dụng tổng hợp các thuật toán mã hóa cổ điển với giao diện PyQt5, API Flask, và giao diện web.
    - `api.py`, `app.py`: Chạy server Flask.
    - `cipher/`: Các thuật toán mã hóa.
    - `ui/`: Giao diện PyQt5 cho từng thuật toán.
    - `templates/`: Giao diện web cho từng thuật toán.
    - `static/`: File hình ảnh mẫu.
- **Chức năng:**  
  - Giấu tin vào ảnh và giải mã tin từ ảnh.
  - Ứng dụng tổng hợp mã hóa cổ điển với giao diện người dùng và web.
- **Cách chạy:**  
  - Giấu tin trong ảnh:
    ```
    cd img-hidden
    python encrypt.py
    python decrypt.py
    ```
  - Ứng dụng tổng hợp:
    ```
    cd TEST
    python app.py
    python api.py
    ```
    Truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Liên hệ
Nếu có thắc mắc hoặc góp ý, vui lòng liên hệ qua sách thực hành bảo mật thông tin nâng cao hoặc trực tiếp với tác giả.
