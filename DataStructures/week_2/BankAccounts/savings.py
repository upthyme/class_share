# The Savings class represents a
# savings account.

import account

class Savings(account.Account):
    
    # The __init__ method accepts arguments for the
    # account number, account name, balance and interest rate.
    
    def __init__(self, account_num, name, int_rate, bal):
        account.Account.__init__(self,account_num,name,bal)
        self.__interest_rate = int_rate
        

    # The following methods are mutators for the
    # data attributes.

    
    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    
    # The following methods are accessors for the
    # data attributes.

    def get_interest_rate(self):
        return self.__interest_rate

    
    def __str__(self):
        return (super().__str__()+ "\nInterest Rate: "+ str(self.get_interest_rate()) )
    

