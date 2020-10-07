from Bank_account_class import *

class Saving_acc(Account_class):
    def __init__(self, acc_number, acc_names, acc_opened_date, acc_amount, owner_adress, owner_phone,last_withdrw_time, intrest_rate,
                 total_amount):
        super().__init__(acc_number, acc_names, acc_opened_date, acc_amount, owner_adress, owner_phone)
        self.last_withdrw_time=last_withdrw_time
        self.intrest_rate = intrest_rate
        self.total_amount = total_amount

