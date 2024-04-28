import pyodbc as odbc

DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
SERVER_NAME = 'LAPTOP-BI65VNTK'

connection_string = f'DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};Trusted_Connection=yes;Encrypt=no;TrustServerCertificate=yes;'

conn = odbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()

def init_database():
    cursor.execute(f"""IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'Car Repair Managment System')
                   BEGIN
                   CREATE DATABASE [Car Repair Managment System]
                   END
                   """)
    cursor.execute(f"USE [Car Repair Managment System];")
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Customer')
                   BEGIN
                    CREATE TABLE Customer (CustomerID INT IDENTITY(1, 1) NOT NULL,
                    FirstName VARCHAR(50),
                    SurName VARCHAR(50),
                    LastName VARCHAR(50),
                    Email VARCHAR(50),
                    Dob DATE,
                    Sex CHAR(1),
                    City VARCHAR(50),
                    District VARCHAR(50),
                    Street VARCHAR(50),
                    BuildingNumber VARCHAR(5),
                    CONSTRAINT customer_constraint_pk PRIMARY KEY(CustomerID))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Car')
                     BEGIN
                    CREATE TABLE Car (VIN CHAR(17) NOT NULL,
                    Brand VARCHAR(50),
                    ModelType VARCHAR(50),
                    ModelName VARCHAR(50),
                    ModelYear INT,
                    CustomerID INT,
                    CONSTRAINT car_constraint_pk PRIMARY KEY(VIN),
                    CONSTRAINT car_constraint_fk FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID))
                    END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Part')
                     BEGIN
                    CREATE TABLE Part (PartNumber INT IDENTITY(1, 1) NOT NULL,
                    PartName VARCHAR(50),
                    PartType VARCHAR(50),
                    Price DECIMAL(10, 2),
                    Note VARCHAR(50),
                    CONSTRAINT part_constraint_pk PRIMARY KEY(PartNumber))
                    END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'RepairOrder')
                   BEGIN
                   CREATE TABLE RepairOrder (OrderID INT IDENTITY(1, 1) NOT NULL,
                    RepairDate DATE,
                    Status VARCHAR(10),
                    PaymentMethod VARCHAR(50),
                    Cost DECIMAL(10, 2),
                    CustomerID INT,
                    CONSTRAINT repair_constraint_pk PRIMARY KEY(OrderID),
                    CONSTRAINT repair_constraint_fk FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Employee')
                     BEGIN
                   CREATE TABLE Employee (SSN CHAR(14) NOT NULL,
                    EmployeeID INT IDENTITY(1, 1) NOT NULL,
                    FirstName VARCHAR(50),
                    SurName VARCHAR(50),
                    LastName VARCHAR(50),
                    Email VARCHAR(50),
                    Dob DATE,
                    Sex CHAR(1),
                    Salary DECIMAL(10, 2),
                    Position VARCHAR(50),
                    CenterNumber CHAR(5),
                    CONSTRAINT employee_constraint_pk PRIMARY KEY(SSN))
                   END
                   """)

    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'ServiceCenter')
                     BEGIN
                   CREATE TABLE ServiceCenter (CenterNumber CHAR(5) NOT NULL,
                   BuildingNumber CHAR(5),
                   City VARCHAR(50),
                   District VARCHAR(50),
                   Street VARCHAR(50),
                   MSSN CHAR(14),
                   CONSTRAINT service_constraint_pk PRIMARY KEY(CenterNumber),
                   CONSTRAINT service_constraint_fk FOREIGN KEY(MSSN) REFERENCES Employee(SSN))
                   END
                    """)

    cursor.execute("""IF NOT EXISTS(SELECT * FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_NAME = 'employee_constraint_fk')
                   BEGIN
                   ALTER TABLE Employee ADD CONSTRAINT employee_constraint_fk FOREIGN KEY(CenterNumber) REFERENCES ServiceCenter(CenterNumber)
                   END""")


    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'MaintenanceTask')
                     BEGIN
                   CREATE TABLE MaintenanceTask (TaskID INT IDENTITY(1, 1) NOT NULL,
                   TaskDescription VARCHAR(300),
                    Date DATE,
                    Labour DECIMAL(10, 2),
                    OrderID INT,
                    CenterNumber CHAR(5),
                    CONSTRAINT maintenance_constraint_pk PRIMARY KEY(TaskID),
                    CONSTRAINT maintenance_constraint_fk FOREIGN KEY(OrderID) REFERENCES RepairOrder(OrderID),
                    CONSTRAINT maintenance_constraint_fk2 FOREIGN KEY(CenterNumber) REFERENCES ServiceCenter(CenterNumber))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Supplier')
                    BEGIN
                   CREATE TABLE Supplier (CompanyID INT IDENTITY(1, 1) NOT NULL,
                    Name VARCHAR(50),
                    Website VarChar(200),
                    CONSTRAINT supplier_constraint_pk PRIMARY KEY(CompanyID))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Engineer')
                   BEGIN
                   CREATE TABLE Engineer (EngSSN CHAR(14) NOT NULL,
                    Spec VARCHAR(50),
                    YearOfExperience INT,
                    CONSTRAINT engineer_constraint_pk PRIMARY KEY(EngSSN),
                    CONSTRAINT engineer_constraint_fk FOREIGN KEY(EngSSN) REFERENCES Employee(SSN))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Performs')
                   BEGIN
                   CREATE TABLE Performs (TaskID INT,
                    EngSSN CHAR(14),
                    CONSTRAINT performs_constraint_pk PRIMARY KEY(TaskID, EngSSN),
                    CONSTRAINT performs_constraint_fk FOREIGN KEY(TaskID) REFERENCES MaintenanceTask(TaskID),
                    CONSTRAINT performs_constraint_fk2 FOREIGN KEY(EngSSN) REFERENCES Engineer(EngSSN))
                   END
                   """)
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Brings')
                   BEGIN
                   CREATE TABLE Brings (PartNumber INT,
                    CompanyID INT,
                    CONSTRAINT brings_constraint_pk PRIMARY KEY(PartNumber, CompanyID),
                    CONSTRAINT brings_constraint_fk FOREIGN KEY(PartNumber) REFERENCES Part(PartNumber),
                    CONSTRAINT brings_constraint_fk2 FOREIGN KEY(CompanyID) REFERENCES Supplier(CompanyID))
                   END""")
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Fix')
                   BEGIN
                   CREATE TABLE Fix (VIN CHAR(17),
                    TaskID INT UNIQUE,
                    PartNumber INT,
                    CONSTRAINT fix_constraint_pk PRIMARY KEY(VIN, TaskID, PartNumber),
                    CONSTRAINT fix_constraint_fk FOREIGN KEY(VIN) REFERENCES Car(VIN),
                    CONSTRAINT fix_constraint_fk2 FOREIGN KEY(TaskID) REFERENCES MaintenanceTask(TaskID),
                    CONSTRAINT fix_constraint_fk3 FOREIGN KEY(PartNumber) REFERENCES Part(PartNumber))
                   END""")
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'EmployeePhone')
                     BEGIN
                   CREATE TABLE EmployeePhone (SSN CHAR(14),
                    PhoneNumber CHAR(11),
                    CONSTRAINT employee_phone_constraint_pk PRIMARY KEY(SSN, PhoneNumber),
                    CONSTRAINT employee_phone_constraint_fk FOREIGN KEY(SSN) REFERENCES Employee(SSN))
                   END""")
    
    cursor.execute("""IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'CustomerPhone')
                   BEGIN
                   CREATE TABLE CustomerPhone (CustomerID INT,
                    PhoneNumber CHAR(11),
                    CONSTRAINT customer_phone_constraint_pk PRIMARY KEY(CustomerID, PhoneNumber),
                    CONSTRAINT customer_phone_constraint_fk FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID))
                   END""")
    

init_database()
