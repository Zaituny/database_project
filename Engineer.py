from Employee import Employee
class Engineer(Employee):
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
                 position,
                 years_of_experience,
                 spec):
        super().__init__(person_iD,
                         email,
                         first_name,
                         sur_name,
                         last_name,
                         birthday,
                         sex,
                         phonenumber,
                         ssn,
                         salary,
                         position)

        self.years_of_experience = years_of_experience
        self.spec = spec
    
    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass