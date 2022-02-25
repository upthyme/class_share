# The checking account is a subclass of
# the Account class.


import account

class Checking(account.Account):

    # The init method accepts arguments for the
    # account number, interest rate, balance, and
    # maturity date.
    
    def __init__(self, account_num, name, bal, fee):
        # Call the superclass __init__ method.
        account.Account.__init__(self, account_num, name, bal)

        # Initialize the monthly_fee.
        self.__monthly_fee = fee
    

    # The set_monthly fee is a mutator for the
    # __monthly_fee attribute.

    def set_monthly_fee(self, fee):
        self.__monthly_fee = fee

    def get_monthly_fee(self):
        return self.__monthly_fee

    def __str__(self):
        return (super().__str__()+ "\nMonthly Fee: "+ str(self.get_monthly_fee())  )
                       