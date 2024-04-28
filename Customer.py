from Person import Person
class Customer(Person):
    def __init__(self,
                 person_iD,
                 email,
                 first_name,
                 sur_name,
                 last_name,
                 birthday,
                 sex,
                 phonenumber,
                 address):
        super().__init__(person_iD,
                         email,
                         first_name,
                         sur_name,
                         last_name,
                         birthday,
                         sex,
                         phonenumber)
        self.address = address

    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass