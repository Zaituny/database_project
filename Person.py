import datetime

class Person():
    def __init__(self,
                 person_iD,
                 email,
                 first_name,
                 sur_name,
                 last_name,
                 birthday,
                 sex,
                 phonenumber):
        self.person_id = person_iD
        self.email = email
        self.first_name = first_name
        self.sur_name = sur_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.phonenumber = phonenumber
        self.age = datetime.now() - self.birthday
    
    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
    
