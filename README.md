# 📂 Advanced-Encryption-Tool

---

**🏢 COMPANY**: CODTECH IT SOLUTIONS PVT. LTD

**👤 NAME**: AAKASH JAYDEV MAURYA

**🆔 INTERN ID**: CT04WS67

**🌐 DOMAIN**: CYBER SECURITY & ETHICAL HACKING

**🕓 DURATION**: 4 WEEKS

**👨‍🏫 MENTOR**: NEELA SANTOSH KUMAR

---

## 📜 DESCRIPTION OF THE TASK

---

### 🔹 Introduction

Data encryption is a pillar of modern cybersecurity practices.  
Protecting sensitive information through strong encryption techniques prevents unauthorized access and ensures privacy.  
For this task, a **file encryption and decryption tool** using **AES-256 encryption** was built using Python’s **cryptography** library.

---

### 🔹 Working Principle

- **Key Generation**:  
  A secure symmetric encryption key is generated and saved securely.

- **Encryption**:  
  Given a file, the tool encrypts its contents and saves a new `.enc` encrypted version.

- **Decryption**:  
  Users can decrypt any `.enc` file back to its original form using the saved key.

The tool uses **Fernet encryption** from the `cryptography` module, which internally applies AES-256.

---

### 🔹 Key Features

- **AES-256 Standard Security**: One of the strongest symmetric encryption algorithms known.
- **Easy Key Management**: Keys are generated and stored in a separate `secret.key` file.
- **User-Friendly CLI**: Provides options for generating a key, encrypting, or decrypting files with minimal effort.

---

### 🔹 Importance

Encryption is essential to protect:
- Personal data
- Financial records
- Medical data
- Intellectual property

Without strong encryption, data at rest or in transit becomes extremely vulnerable to theft, espionage, or leakage.

---

### 🔹 Use Cases

- Encrypting confidential documents on laptops.
- Securing backups on USB drives.
- Protecting sensitive logs and configuration files in cloud storage.

---

### 🔹 Technologies Used

- Python
- Cryptography (Fernet - AES-256)

---

### 🔹 Future Enhancements

- Develop a GUI (Graphical User Interface) for easier file selection.
- Encrypt entire folders recursively.
- Implement password-protected decryption keys.

---

### 🔹 Conclusion

This **Advanced Encryption Tool** successfully shows how to implement military-grade encryption standards in Python with simplicity and reliability.  
It makes high-end security accessible even for beginner-level users and emphasizes the importance of data confidentiality.

---

## 📷 OUTPUT

![Image1](https://github.com/user-attachments/assets/49067e89-2eed-4e8d-970c-a75db2bbb9d2)  
![Image2](https://github.com/user-attachments/assets/03c3103f-4e2c-49d1-98af-ca7d30ae8031)  
![Image3](https://github.com/user-attachments/assets/2ba6f383-62ce-4c0d-955b-448bcf64c2e3)

---

## ⚙️ How to Run

---

### Step 1: Install Required Libraries

```bash
pip install cryptography
```

### Step 2: Run the Script

```bash
python encryption_tool.py
```

---

# 🚀 Enjoy Secure File Encryption and Decryption!
