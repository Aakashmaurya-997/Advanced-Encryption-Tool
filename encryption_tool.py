
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def load_key(filename):
    with open(filename, 'rb') as file:
        return file.read()

def encrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(filepath + ".enc", 'wb') as file:
        file.write(encrypted)

def decrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filepath.replace(".enc", ""), 'wb') as file:
        file.write(decrypted)

if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice: ")

    if choice == "1":
        key = generate_key()
        save_key(key, 'secret.key')
        print("[SUCCESS] Key generated and saved.")
    elif choice == "2":
        key = load_key('secret.key')
        filepath = input("Enter file path to encrypt: ")
        encrypt_file(filepath, key)
        print("[SUCCESS] File encrypted.")
    elif choice == "3":
        key = load_key('secret.key')
        filepath = input("Enter file path to decrypt: ")
        decrypt_file(filepath, key)
        print("[SUCCESS] File decrypted.")
    else:
        print("Invalid choice.")
