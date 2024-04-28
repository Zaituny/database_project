from database_connection import *

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
