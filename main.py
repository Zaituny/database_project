
from database_functions import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QTabWidget, QTableWidget, QTableWidgetItem

engineer_window = None
admin_window = None
receptionist_window = None

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # SSN Field
        self.ssn_label = QLabel("SSN:")
        self.ssn_field = QLineEdit()
        layout.addWidget(self.ssn_label)
        layout.addWidget(self.ssn_field)

        # Role Dropdown
        self.role_label = QLabel("Role:")
        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["Admin", "Engineer", "Receptionist"])
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_dropdown)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        global engineer_window
        ssn = self.ssn_field.text()
        role = self.role_dropdown.currentText()
        if role == "Engineer":
            try:
                first_name, sur_name, last_name, email =  find_engineer_by_ssn(ssn)
            except:
                print("engineer not found")
            self.close()
            engineer_window = EngineerWindow(ssn, first_name, sur_name, last_name, email)
            engineer_window.show()

class EngineerWindow(QWidget):
    def __init__(self, EngSSN,first_name, sur_name, last_name, email):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        data = find_Orders_by_EngSSN(EngSSN)



        self.table = QTableWidget()
        self.table.setColumnCount(len(data[0]))
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(["OrderID", "Status", "Brand", "Model Name"])

        for row, (OrderID, Status, Brand, Model_name) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(OrderID)))
            self.table.setItem(row, 1, QTableWidgetItem(Status))
            self.table.setItem(row, 2, QTableWidgetItem(Brand))
            self.table.setItem(row, 3, QTableWidgetItem(Model_name))

        # Create tabs
        self.tabs = QTabWidget()
        self.account_tab = QWidget()
        self.order_tab = QWidget()
        self.tasks_tab = QWidget()

        # Account Tab
        self.account_layout = QVBoxLayout()
        self.account_layout.addWidget(QLabel(f"First Name: {first_name}"))
        self.account_layout.addWidget(QLabel(f"Surname: {sur_name}"))
        self.account_layout.addWidget(QLabel(f"Last Name: {last_name}"))
        self.account_layout.addWidget(QLabel(f"Email: {email}"))
        self.account_tab.setLayout(self.account_layout)

        # Order Tab
        # Add some content for order tab
        self.order_tab.setLayout(QVBoxLayout())
        self.order_tab.layout().addWidget(self.table)

        # Tasks Tab
        # Add some content for tasks tab
        self.tasks_tab.setLayout(QVBoxLayout())
        self.tasks_tab.layout().addWidget(QLabel("Tasks tab content"))

        # Add tabs to tab widget
        self.tabs.addTab(self.account_tab, "Account")
        self.tabs.addTab(self.order_tab, "Order")
        self.tabs.addTab(self.tasks_tab, "Tasks")

        layout.addWidget(self.tabs)

        # Logout Button
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def logout(self):
        self.close()  # Close the current window (main window)
        login_window.show()  # Show the login window again


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the login window
    login_window = LoginScreen()
    # Create the main window
    login_window.show()  # Show the login window initially
    sys.exit(app.exec_())


