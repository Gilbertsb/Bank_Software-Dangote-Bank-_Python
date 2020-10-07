from Bank_account_class import *

class Current_acc(Account_class):
    def __init__(self, acc_number, acc_names, acc_opened_date, acc_amount, owner_adress, owner_phone,intrest_rate,
                 total_amount):
        super().__init__(acc_number, acc_names, acc_opened_date, acc_amount, owner_adress, owner_phone,)
        self.intrest_rate = intrest_rate
        self.total_amount = total_amount

    def total_amount(self):
        return self.acc_amount+self.intrest_rate