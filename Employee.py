from Person import Person

class Employee(Person):
    def __init__(self,
                 person_iD,
                 email,
                 first_name,
                 sur_name,
                 last_name,
                 birthday,
                 sex,
                 phonenumber,
                 ssn,
                 salary,
                 position):
        super().__init__(person_iD,
                         email,
                         first_name,
                         sur_name,
                         last_name,
                         birthday,
                         sex,
                         phonenumber)
        self.ssn = ssn
        self.salary = salary
        self.position = position
    
    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass