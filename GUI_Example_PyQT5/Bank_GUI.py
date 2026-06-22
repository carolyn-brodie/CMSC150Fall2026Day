from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BankAccount import *
import sys


class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Account Interface")
        self.setStyleSheet("background-color: lightblue;")
        self.setMinimumWidth(520)

        self.account: BankAccount

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(12)

        # --- Account Creation ---
        self.create_group = QGroupBox("Create / Load Account")
        create_form = QFormLayout()
        self.owner_input = QLineEdit()
        self.acct_input = QLineEdit()
        # self.acct_input.setValidator(QIntValidator(0, 2_147_483_647, self))
        self.init_bal_input = QLineEdit()
        self.init_bal_input.setPlaceholderText("0.00")

        create_form.addRow("Owner name:", self.owner_input)
        create_form.addRow("Account #:", self.acct_input)
        create_form.addRow("Initial balance:", self.init_bal_input)

        self.create_btn = QPushButton("Create Account")
        self.create_btn.setStyleSheet("background-color : white")
        self.create_btn.clicked.connect(self.create_account)
        create_form.addRow(self.create_btn)
        self.create_group.setLayout(create_form)
        layout.addWidget(self.create_group)

        # --- Actions (Deposit / Withdraw) ---
        self.actions_group = QGroupBox("Actions")
        actions_layout = QFormLayout()

        self.amount_input = QLineEdit()
        # self.amount_input.setValidator(dbl_validator)
        self.amount_input.setPlaceholderText("Amount (e.g., 50.00)")

        btn_row = QHBoxLayout()
        self.deposit_btn = QPushButton("Deposit")
        self.withdraw_btn = QPushButton("Withdraw")
        self.deposit_btn.clicked.connect(self.deposit_action)
        self.withdraw_btn.clicked.connect(self.withdraw_action)
        btn_row.addWidget(self.deposit_btn)
        btn_row.addWidget(self.withdraw_btn)

        actions_layout.addRow("Amount:", self.amount_input)
        actions_layout.addRow(btn_row)
        self.actions_group.setLayout(actions_layout)
        layout.addWidget(self.actions_group)

        # --- Status / Summary ---
        status_row = QHBoxLayout()
        self.owner_label = QLabel("Owner: —")
        self.acct_label = QLabel("Account: —")
        self.balance_label = QLabel("Balance: —")
        for lab in (self.owner_label, self.acct_label, self.balance_label):
            lab.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        status_row.addWidget(self.owner_label, 1)
        status_row.addWidget(self.acct_label, 1)
        status_row.addWidget(self.balance_label, 1)
        layout.addLayout(status_row)

        self.summary = QPlainTextEdit()
        self.summary.setReadOnly(True)
        self.summary.setPlaceholderText("Account summary will appear here…")
        layout.addWidget(self.summary)

        # Disable actions until an account exists
        self.set_actions_enabled(False)

        self.setCentralWidget(container)

    # ----- Helpers -----
    def set_actions_enabled(self, enabled: bool):
        self.actions_group.setEnabled(enabled)
        self.deposit_btn.setEnabled(enabled)
        self.withdraw_btn.setEnabled(enabled)
        self.amount_input.setEnabled(enabled)

    def update_status(self):
        if self.account is None:
            self.owner_label.setText("Owner: —")
            self.acct_label.setText("Account: —")
            self.balance_label.setText("Balance: —")
            self.summary.setPlainText("")
        else:
            self.owner_label.setText(f"Owner: {self.account.owner}")
            self.acct_label.setText(f"Account: {self.account.account_number}")
            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
            self.summary.setPlainText(str(self.account))

    def read_float(self, line_edit: QLineEdit) -> float | None:
        text = line_edit.text().strip()
        if text == "":
            return None
        try:
            return float(text)
        except ValueError:
            return None

    # ----- Slots -----
    def create_account(self):
        name = self.owner_input.text().strip()
        acct = self.acct_input.text().strip()
        init_balance = self.read_float(self.init_bal_input) or 0.0

        if not name:
            QMessageBox.warning(self, "Missing info", "Please enter an owner name.")
            return
        if not acct:
            QMessageBox.warning(self, "Missing info", "Please enter an account number.")
            return

        try:
            self.account = BankAccount(name, acct, init_balance)
        except Exception as e:
            QMessageBox.critical(self, "Error creating account", str(e))
            return

        self.set_actions_enabled(True)
        self.update_status()
        QMessageBox.information(self, "Account ready", "Account created/loaded successfully.")

    def deposit_action(self):
        if self.account is None:
            return
        amt = self.read_float(self.amount_input)
        if amt is None:
            QMessageBox.warning(self, "Amount needed", "Enter a valid deposit amount.")
            return
        try:
            self.account.deposit(amt)
        except Exception as e:
            QMessageBox.critical(self, "Deposit error", str(e))
            return
        self.amount_input.clear()
        self.update_status()

    def withdraw_action(self):
        if self.account is None:
            return
        amt = self.read_float(self.amount_input)
        if amt is None:
            QMessageBox.warning(self, "Amount needed", "Enter a valid withdrawal amount.")
            return
        try:
            self.account.withdraw(amt)
        except Exception as e:
            QMessageBox.critical(self, "Withdrawal error", str(e))
            return
        self.amount_input.clear()
        self.update_status()


def main():
    app = QApplication(sys.argv)
    win = AccountWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()