class Car():
    def __init__(self,
                 VIN,
                 brand,
                 model_type,
                 model_year,
                 model_name,
                 customer_id) -> None:
        self.VIN = VIN
        self.brand = brand
        self.model_type = model_type
        self.model_year = model_year
        self.model_name = model_name
        self.customer_id = customer_id
    
    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass