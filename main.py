
from database_functions import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit

engineer_window = None
admin_window = None
receptionist_window = None
newOrder_window = None

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()


        self.ssn_label = QLabel("SSN:")
        self.ssn_field = QLineEdit()
        layout.addWidget(self.ssn_label)
        layout.addWidget(self.ssn_field)


        self.role_label = QLabel("Role:")
        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["Admin", "Engineer", "Receptionist"])
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_dropdown)


        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        global engineer_window
        global admin_window
        global receptionist_window
        ssn = self.ssn_field.text()
        role = self.role_dropdown.currentText()
        if role == "Admin":
            try:
                first_name, sur_name, last_name, email = find_admin_by_ssn(ssn)
                self.close()
                admin_window = AdminWindow(first_name, sur_name, last_name, email)
                admin_window.show()
            except:
                print("admin not found")
        
        elif role == "Engineer":
            try:
                first_name, sur_name, last_name, email =  find_engineer_by_ssn(ssn)
                self.close()
                engineer_window = EngineerWindow(ssn, first_name, sur_name, last_name, email)
                engineer_window.show()
            except:
                print("engineer not found")

        elif role == "Receptionist":
            try:
                self.close()
                receptionist_window = ReceptionistWindow()
                receptionist_window.show()
            except:
                print("Receptionist not found")

class AdminWindow(QWidget):
    def __init__(self, first_name, sur_name, last_name, email):
        super().__init__()
        self.setWindowTitle("Admin")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.ssn_field = QLineEdit()
        self.firstname_field = QLineEdit()
        self.surname_field = QLineEdit()
        self.lastname_field = QLineEdit()
        self.email_field = QLineEdit()
        self.dob_field = QLineEdit()
        self.sex_field = QLineEdit()
        self.salary_field = QLineEdit()
        self.position_field = QLineEdit()
        self.centernumber_field = QLineEdit()
        self.spec = QLineEdit()
        self.yoe = QLineEdit()

        self.position_label = QLabel("Position: ")
        self.spec_label = QLabel("Specialization: ")
        self.yoe_label = QLabel("Years of Experience: ")

        self.tabs = QTabWidget()
        self.add_tab = QWidget()
        self.remove_tab = QWidget()

        self.role_dropdown = QComboBox()
        self.role_dropdown.addItems(["Engineer", "Employee"])


        self.add_layout = QVBoxLayout()
        self.role_label = QLabel(f"Add new {self.role_dropdown.currentText()}:")
        self.add_layout.addWidget(self.role_label)
        self.role_dropdown.currentTextChanged.connect(self.update_role_fields)
        self.add_layout.addWidget(self.role_dropdown)
        self.add_layout.addWidget(QLabel("SSN: "))
        self.add_layout.addWidget(self.ssn_field)
        self.add_layout.addWidget(QLabel("firstname:"))
        self.add_layout.addWidget(self.firstname_field)
        self.add_layout.addWidget(QLabel("Surname:"))
        self.add_layout.addWidget(self.surname_field)
        self.add_layout.addWidget(QLabel("Last Name:"))
        self.add_layout.addWidget(self.lastname_field)
        self.add_layout.addWidget(QLabel("Email:"))
        self.add_layout.addWidget(self.email_field)
        self.add_layout.addWidget(QLabel("DOB:"))
        self.add_layout.addWidget(self.dob_field)
        self.add_layout.addWidget(QLabel("Sex:"))
        self.add_layout.addWidget(self.sex_field)
        self.add_layout.addWidget(QLabel("Salary:"))
        self.add_layout.addWidget(self.salary_field)
        self.add_layout.addWidget(self.position_label)
        self.add_layout.addWidget(self.position_field)
        self.position_field.hide()
        self.position_label.hide()
        self.add_layout.addWidget(QLabel("Center Number:"))
        self.add_layout.addWidget(self.centernumber_field)
        self.add_layout.addWidget(self.spec_label)
        self.add_layout.addWidget(self.spec)
        self.add_layout.addWidget(self.yoe_label)
        self.add_layout.addWidget(self.yoe)

        self.add_tab.setLayout(self.add_layout)


        self.remove_tab.setLayout(QVBoxLayout())
        self.remove_tab.layout().addWidget(QLabel("Remove Engineer or Receptionist:"))


        self.tabs.addTab(self.add_tab, "Add")
        self.tabs.addTab(self.remove_tab, "Remove")

        layout.addWidget(self.tabs)


        self.logout_button = QPushButton("Logout")
        self.add_button = QPushButton("Add")
        self.logout_button.clicked.connect(self.logout)
        self.add_button.clicked.connect(self.add)
        layout.addWidget(self.add_button)
        layout.addWidget(self.logout_button)
        

        self.setLayout(layout)

    def logout(self):
        self.close()
        login_window.show()

    def add(self):
        ssn = self.ssn_field.text()
        firstname = self.firstname_field.text()
        surname = self.surname_field.text()
        lastname = self.lastname_field.text()
        email = self.email_field.text()
        dob = self.dob_field.text()
        sex = self.sex_field.text()
        salary = self.salary_field.text()
        centernumber = self.centernumber_field.text()
        if self.role_dropdown.currentText() == "Engineer":
            try:
                add_employee(ssn, firstname, surname, lastname, email, dob, sex, salary, 'Engineer', centernumber)
            except:
                print("Employee already exists")
            spec = self.spec.text()
            yoe = self.yoe.text()
            try:
                add_engineer(ssn, spec, yoe)
            except:
                print("Engineer already exists")
        else:
            position = self.position_field.text()
            try:
                add_employee(ssn, firstname, surname, lastname, email, dob, sex, salary, position, centernumber)
            except:
                print("Employee already exists")

    def update_role_fields(self):
        self.role_label.setText(f"Add new {self.role_dropdown.currentText()}:")
        if self.role_dropdown.currentText() == "Engineer":
            self.position_label.hide()
            self.position_field.hide()
            self.spec_label.show()
            self.spec.show()
            self.yoe_label.show()
            self.yoe.show()
        else:
            self.position_label.show()
            self.position_field.show()
            self.spec_label.hide()
            self.spec.hide()
            self.yoe_label.hide()
            self.yoe.hide()
        

class EngineerWindow(QWidget):
    def __init__(self, EngSSN,first_name, sur_name, last_name, email):
        super().__init__()
        self.setWindowTitle("Engineer")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        order_data = find_Orders_by_EngSSN(EngSSN)

        task_data = find_tasks_by_EngSSN(EngSSN)

        self.table_orders = QTableWidget()
        self.table_orders.setColumnCount(len(order_data[0]))
        self.table_orders.setRowCount(len(order_data))
        self.table_orders.setHorizontalHeaderLabels(["OrderID", "Status", "Brand", "Model Name"])

        for row, (OrderID, Status, Brand, Model_name) in enumerate(order_data):
            self.table_orders.setItem(row, 0, QTableWidgetItem(str(OrderID)))
            self.table_orders.setItem(row, 1, QTableWidgetItem(Status))
            self.table_orders.setItem(row, 2, QTableWidgetItem(Brand))
            self.table_orders.setItem(row, 3, QTableWidgetItem(Model_name))

        self.table_tasks = QTableWidget()
        self.table_tasks.setColumnCount(len(task_data[0]))
        self.table_tasks.setRowCount(len(task_data))
        self.table_tasks.setHorizontalHeaderLabels(["TaskID", "Description","VIN", "Brand", "Model Name"])

        for row, (TaskID, Description,VIN, Brand, Model_name) in enumerate(task_data):
            self.table_tasks.setItem(row, 0, QTableWidgetItem(str(TaskID)))
            self.table_tasks.setItem(row, 1, QTableWidgetItem(Description))
            self.table_tasks.setItem(row, 2, QTableWidgetItem(VIN))
            self.table_tasks.setItem(row, 3, QTableWidgetItem(Brand))
            self.table_tasks.setItem(row, 4, QTableWidgetItem(Model_name))


        self.tabs = QTabWidget()
        self.account_tab = QWidget()
        self.order_tab = QWidget()
        self.tasks_tab = QWidget()


        self.account_layout = QVBoxLayout()
        self.account_layout.addWidget(QLabel(f"First Name: {first_name}"))
        self.account_layout.addWidget(QLabel(f"Surname: {sur_name}"))
        self.account_layout.addWidget(QLabel(f"Last Name: {last_name}"))
        self.account_layout.addWidget(QLabel(f"Email: {email}"))
        self.account_tab.setLayout(self.account_layout)

        self.order_tab.setLayout(QVBoxLayout())
        self.order_tab.layout().addWidget(self.table_orders)

        self.tasks_tab.setLayout(QVBoxLayout())
        self.tasks_tab.layout().addWidget(self.table_tasks)


        self.tabs.addTab(self.account_tab, "Account")
        self.tabs.addTab(self.order_tab, "Order")
        self.tabs.addTab(self.tasks_tab, "Tasks")

        layout.addWidget(self.tabs)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def logout(self):
        self.close()
        login_window.show()


class ReceptionistWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Receptionist")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        
        self.add_new_task_btn = QPushButton('Add New Task', self)
        self.add_new_order_btn = QPushButton('Add New Order', self)
        layout.addStretch(1)  # Add stretching space to center buttons
        layout.addWidget(self.add_new_task_btn)
        layout.addWidget(self.add_new_order_btn)
        layout.addStretch(1)  # Add stretching space to center buttons
        self.add_new_order_btn.clicked.connect(self.createNewOrder)
        self.add_new_task_btn.clicked.connect(self.createNewTask)


        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)
        

        self.setLayout(layout)

    def logout(self):
        self.close()
        login_window.show()

    def createNewOrder(self):
        global newOrder_window
        newOrder_window = newOrder(add_new_order()[0])
        self.close()
        newOrder_window.show()

    def createNewTask(self):
        pass


class newOrder(QWidget):
    def __init__(self, Order_ID):
        super().__init__()
        self.Order_ID = Order_ID
        self.setWindowTitle("New Order")
        self.setGeometry(100, 100, 400, 300)

        self.add_layout = QVBoxLayout()
        

        
        self.description = QTextEdit()
        self.labour = QLineEdit()
        self.centerNumber = QLineEdit()


        self.add_layout = QVBoxLayout()
        self.add_layout.addWidget(QLabel("Task Description: "))
        self.add_layout.addWidget(self.description)
        self.add_layout.addWidget(QLabel("Labour Cost: "))
        self.add_layout.addWidget(self.labour)
        self.add_layout.addWidget(QLabel("Center Number: "))
        self.add_layout.addWidget(self.centerNumber)

        self.add_new_task_btn = QPushButton('Add New Task', self)
        self.add_layout.addStretch(1)  # Add stretching space to center buttons
        self.add_layout.addWidget(self.add_new_task_btn)
        self.add_new_task_btn.clicked.connect(self.addTask)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        self.add_layout.addWidget(self.logout_button)
        

        self.setLayout(self.add_layout)

    def logout(self):
        self.close()
        login_window.show()

    def addTask(self):
        add_new_task(self.description.toPlainText(), self.labour.text(), self.Order_ID, self.centerNumber.text())
        self.description.setText("")
        self.labour.setText("")
        self.centerNumber.setText("")



def row_to_string(row):
    result = ""
    for column in row.cursor_description:
        result += str(getattr(row, column[0])) + " "
    return result.strip()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginScreen()

    login_window.show()
    sys.exit(app.exec_())


