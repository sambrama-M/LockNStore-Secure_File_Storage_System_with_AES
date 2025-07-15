# 🔐 Secure File Storage System with AES (Advanced PyQt5 Version)

This project is a GUI-based secure file encryption/decryption system built using Python, PyQt5, and AES (256-bit).

## ✅ Features
- AES-256 Encryption & Decryption (with PBKDF2 key derivation)
- Salted password hashing
- Drag-and-Drop file support
- File integrity check (SHA-256)
- SQLite-based logs of all encrypted/decrypted files
- Export logs as CSV
- Better UI with improved layout
- Folder structure for encrypted/decrypted/logs
- Future-ready for multi-user support

## ▶️ How to Run
```bash
pip install pyqt5 cryptography
python main.py
```

## 📁 Folder Structure
- `encrypted/` - stores .enc files
- `decrypted/` - stores restored files
- `logs/` - optional exported logs
- `filedata.db` - SQLite file metadata

## 📸 Screenshot
_Include your screenshots or a demo GIF here_

## 📦 Packaging
You can convert to `.exe` using:
```bash
pyinstaller --noconfirm --onefile --windowed main.py
```

## 👨‍💻 Author
Shammi Salian