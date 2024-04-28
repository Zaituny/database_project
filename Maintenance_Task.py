class Maintenance_Task():
    def __init__(self,
                 task_id,
                 task_date,
                 labour_cost,
                 order_id,
                 center_number):
        self.task_id = task_id
        self.task_date = task_date
        self.labour_cost = labour_cost
        self.order_id = order_id
        self.center_number = center_number

    def save(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass