import sys, os, hashlib
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QLineEdit, QVBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView
)
from crypto_utils import encrypt_data, decrypt_data, generate_hash
from db_utils import init_db, log_file, fetch_logs

os.makedirs("encrypted", exist_ok=True)
os.makedirs("decrypted", exist_ok=True)
os.makedirs("logs", exist_ok=True)

class SecureFileStorage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure File Storage System (AES Advanced)")
        self.setFixedSize(600, 400)
        self.setAcceptDrops(True)
        self.file_path = None

        self.label = QLabel("Choose a file or drag-and-drop below:")
        self.file_btn = QPushButton("Select File")
        self.file_btn.clicked.connect(self.select_file)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter encryption key")

        self.encrypt_btn = QPushButton("Encrypt File")
        self.encrypt_btn.clicked.connect(self.encrypt_file)

        self.decrypt_btn = QPushButton("Decrypt File")
        self.decrypt_btn.clicked.connect(self.decrypt_file)

        self.export_btn = QPushButton("Export Logs")
        self.export_btn.clicked.connect(self.export_logs)

        self.status = QLabel("")
        self.logs_table = QTableWidget()
        self.logs_table.setColumnCount(4)
        self.logs_table.setHorizontalHeaderLabels(["Filename", "Action", "Hash", "Timestamp"])
        self.logs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.file_btn)
        layout.addWidget(self.password_input)
        layout.addWidget(self.encrypt_btn)
        layout.addWidget(self.decrypt_btn)
        layout.addWidget(self.export_btn)
        layout.addWidget(self.status)
        layout.addWidget(self.logs_table)
        self.setLayout(layout)

        init_db()
        self.load_logs()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.file_path = event.mimeData().urls()[0].toLocalFile()
        self.status.setText(f"File dropped: {self.file_path}")

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file:
            self.file_path = file
            self.status.setText(f"Selected: {os.path.basename(file)}")

    def encrypt_file(self):
        if not self.file_path or not self.password_input.text():
            self.status.setText("Select a file and enter password.")
            return

        with open(self.file_path, "rb") as f:
            data = f.read()

        encrypted = encrypt_data(data, self.password_input.text())
        out_path = os.path.join("encrypted", os.path.basename(self.file_path) + ".enc")
        with open(out_path, "wb") as f:
            f.write(encrypted)

        file_hash = generate_hash(data)
        log_file(os.path.basename(self.file_path), "Encrypt", file_hash)
        self.status.setText(f"Encrypted → {out_path}")
        self.load_logs()

    def decrypt_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select .enc File")
        if not file or not self.password_input.text():
            self.status.setText("Select a file and enter password.")
            return

        with open(file, "rb") as f:
            enc_data = f.read()

        try:
            decrypted = decrypt_data(enc_data, self.password_input.text())
        except:
            self.status.setText("Decryption failed.")
            return

        out_path = os.path.join("decrypted", os.path.basename(file).replace(".enc", ""))
        with open(out_path, "wb") as f:
            f.write(decrypted)

        file_hash = generate_hash(decrypted)
        log_file(os.path.basename(file), "Decrypt", file_hash)
        self.status.setText(f"Decrypted → {out_path}")
        self.load_logs()

    def load_logs(self):
        self.logs_table.setRowCount(0)
        for row_idx, row_data in enumerate(fetch_logs()):
            self.logs_table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.logs_table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def export_logs(self):
        import csv
        rows = fetch_logs()
        with open("logs/logs.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Filename", "Action", "Hash", "Timestamp"])
            writer.writerows(rows)
        self.status.setText("Logs exported to logs/logs.csv")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecureFileStorage()
    window.show()
    sys.exit(app.exec_())