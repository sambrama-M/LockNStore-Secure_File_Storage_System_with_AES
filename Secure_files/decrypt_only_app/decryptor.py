import sys, os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QLineEdit, QVBoxLayout, QMessageBox
)
from crypto_utils import decrypt_data

class DecryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AES File Decryptor")
        self.setFixedSize(400, 200)
        self.file_path = None

        self.label = QLabel("Select a .enc file to decrypt:")
        self.file_btn = QPushButton("Browse")
        self.file_btn.clicked.connect(self.select_file)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter decryption key")

        self.decrypt_btn = QPushButton("Decrypt File")
        self.decrypt_btn.clicked.connect(self.decrypt_file)

        self.status = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.file_btn)
        layout.addWidget(self.password_input)
        layout.addWidget(self.decrypt_btn)
        layout.addWidget(self.status)
        self.setLayout(layout)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select .enc File")
        if file:
            self.file_path = file
            self.status.setText(f"Selected: {os.path.basename(file)}")

    def decrypt_file(self):
        if not self.file_path or not self.password_input.text():
            self.status.setText("File and password required.")
            return

        with open(self.file_path, "rb") as f:
            enc_data = f.read()

        try:
            decrypted = decrypt_data(enc_data, self.password_input.text())
        except Exception:
            self.status.setText("Decryption failed.")
            return

        out_path = os.path.join(os.path.dirname(self.file_path), os.path.basename(self.file_path).replace(".enc", ""))
        with open(out_path, "wb") as f:
            f.write(decrypted)

        self.status.setText(f"Decrypted: {out_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecryptorApp()
    window.show()
    sys.exit(app.exec_())
