from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi cần băm SHA3-256: ").encode('utf-8')
    hash_text = sha3(text)
    
    print("Chuỗi băm SHA3-256 đã nhập: ", text.decode('utf-8'))
    print("Giá trị băm SHA3-256: ", hash_text.hex())
    
if __name__ == "__main__":
    main()