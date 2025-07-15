# Secure File Storage System with AES-256 (PyQt5 GUI)

This project includes two separate applications for secure file exchange using AES-256 encryption. Built with Python and PyQt5, it provides a GUI interface for both the sender and the receiver.

---

## Project Structure

### 1. `secure_file_storage_gui_advanced/` (Sender's App)
This is the full-featured application for the sender, who has:
- Ability to encrypt files using AES-256  
- Ability to decrypt previously encrypted files  
- A log viewer for tracking file activity  
- Automatic logging of filename, time, hash, and operation (Encrypt/Decrypt)  
- Optional drag-and-drop support  
- SQLite-based metadata storage  

> Encrypted files are saved in `/encrypted/`  
> Decrypted files are saved in `/decrypted/`

---

### 2. `decrypt_only_app/` (Receiver's App)
This is a lightweight version for the receiver:
- Can only decrypt `.enc` files received from the sender  
- Cannot encrypt new files  
- Cannot view logs  
- Decrypted file is saved in the same location as the selected `.enc` file  

> This folder should be shared along with the encrypted file by the sender.

---

## How It Works

1. The sender encrypts a file using the full app and a password.  
2. The encrypted file (e.g., `file.pdf.enc`) is saved in `/encrypted/`.  
3. The sender sends the `.enc` file and the `decrypt_only_app` folder to the receiver.  
4. The receiver runs `decrypt_only_app`, selects the file, and enters the password to decrypt.  
5. The decrypted file is restored in the same location.

---

## Installation

Install the required Python libraries:

```bash 
pip install pyqt5 cryptography

```
## Running the Applications

Sender App:

```bash
cd secure_file_storage_gui_advanced
python main.py
 ```

Reciver App:

```bash
cd decrypt_only_app
python decryptor.py
```

## 📁 Folder Structure
```
project_root/
├── secure_file_storage_gui_advanced/
│   ├── main.py
│   ├── crypto_utils.py
│   ├── db_utils.py
│   ├── logs/
│   ├── encrypted/
│   ├── decrypted/
│   └── screenshots/          ← GUI and feature images
│
├── decrypt_only_app/
│   ├── decryptor.py
│   ├── crypto_utils.py
│   └── screenshots/          ← UI of the decrypt-only app
│
└── README.md
```
## Security Features
- AES-256 encryption with CFB mode

- Password-based key derivation using PBKDF2 and salt

- SHA-256 hash verification for file integrity

- Activity logs stored securely in SQLite

## MIT License

MIT License

Copyright (c) 2025 sambrama-M

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


