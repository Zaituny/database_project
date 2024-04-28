class Repair_Order():
    def __init__(self,
                 order_id,
                 order_date,
                 status,
                 payment_method,
                 customer_id) -> None:
        self.order_id = order_id
        self.order_date = order_date
        self.status = status
        self.payment_method = payment_method
        self.customer_id = customer_id

    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
        