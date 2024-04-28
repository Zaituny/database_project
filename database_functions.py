from database_connection import *
import datetime

def find_engineer_by_ssn(ssn):
    cursor.execute(f"""SELECT FirstName, SurName, LastName, Email FROM Employee
                   JOIN Engineer ON Engineer.EngSSN = Employee.SSN
                   WHERE EngSSN = '{ssn}';""")
    return cursor.fetchone()

def find_order_by_id(order_id):
    cursor.execute(f"SELECT * FROM RepairOrder WHERE OrderID = {order_id}")
    return cursor.fetchone()


def find_tasks_by_brand(brand, EngSSN):
    cursor.execute(f"""SELECT *
                       FROM MaintenanceTask mt
                       JOIN Fix f ON mt.TaskID = f.TaskID
                       JOIN Car c ON f.VIN = c.VIN
                       JOIN Performs p ON mt.TaskID = p.TaskID
                       JOIN Engineer e ON p.EngSSN = e.EngSSN
                       WHERE e.EngSSN = '{EngSSN}'
                       AND c.Brand = '{brand}';""")

    return cursor.fetchall()


def find_Orders_by_EngSSN(EngSSN):
    cursor.execute(f"""SELECT ro.OrderID, ro.Status, c.Brand, c.ModelName
                       FROM RepairOrder ro
                       JOIN MaintenanceTask mt ON ro.OrderID = mt.OrderID
                       JOIN Performs p ON mt.TaskID = p.TaskID
                       JOIN Fix f ON mt.TaskID = f.TaskID
                       JOIN Car c ON f.VIN = c.VIN
                       WHERE p.EngSSN = '{EngSSN}';""")

    return cursor.fetchall()

def find_tasks_by_EngSSN(EngSSN):
    cursor.execute(f"""SELECT mt.TaskID, mt.TaskDescription, c.VIN, c.Brand, c.ModelName
                       FROM MaintenanceTask mt
                       JOIN Performs p ON mt.TaskID = p.TaskID
                       JOIN Fix f ON mt.TaskID = f.TaskID
                       JOIN Car c ON f.VIN = c.VIN
                       WHERE p.EngSSN = '{EngSSN}';""")

    return cursor.fetchall()

def find_admin_by_ssn(SSN):
    cursor.execute(f"""SELECT FirstName, SurName, LastName, Email FROM Employee
                   WHERE SSN = '{SSN}' AND position='admin';""")
    return cursor.fetchone()

def add_employee(SSN, FirstName, SurName, LastName, Email, DOB, Sex, Salary, Position, CenterNumber):
    string = f"""INSERT INTO Employee (SSN, FirstName, SurName, LastName, Email, Dob, Sex, Salary, Position, CenterNumber)
                   VALUES ('{SSN}',
                   '{FirstName}',
                   '{SurName}',
                   '{LastName}',
                   '{Email}',
                   '{DOB}',
                   '{Sex}',
                   {Salary},
                   '{Position}',
                   '{CenterNumber}');"""
    print(cursor.execute(string))
    conn.commit()

def add_engineer(SSN, Spec, YOE):
    cursor.execute(f"""INSERT INTO Engineer (EngSSN, Spec, YearOfExperience)
                   VALUES ('{SSN}', '{Spec}', {YOE});""")
    conn.commit()


def add_new_order():
    cursor.execute(f"""INSERT INTO RepairOrder(Status) VALUES ('not')""")
    conn.commit()
    cursor.execute("SELECT @@IDENTITY")
    return cursor.fetchone()

def add_new_task(Description, Labour, Order_ID, CenterNumber):
    string = f"""INSERT INTO MaintenanceTask(TaskDescription, Date, Labour, OrderID, CenterNumber)
                    VALUES ('{Description}', '{datetime.date.today()}', '{Labour}', {Order_ID}, '{CenterNumber}');"""
    cursor.execute(string)
    conn.commit()

    