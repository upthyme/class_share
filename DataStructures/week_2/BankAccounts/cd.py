# The CD account represents a certificate of
# deposit (CD) account. It is a subclass of
# the Account class.


import account

class CD(account.Account):

    # The init method accepts arguments for the
    # account number, interest rate, balance, and
    # maturity date.
    
    def __init__(self, account_num, name, interest_rate, bal, mat_date):
        # Call the superclass __init__ method.
        account.Account.__init__(self, account_num, name, bal)

        # Initialize the __maturity_date and interest_rate attributes.
        self.__maturity_date = mat_date
        self.__interest_rate = interest_rate

    # The set_maturity_date is a mutator for the
    # __maturity_date attribute.

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    def set_interest_rate(self, interest):
         self._interest_rate = interest

    # The get_maturity_date method is an accessor
    # for the __maturity_date attribute.
    def get_maturity_date(self):
        return self.__maturity_date

    def get_interest_rate(self):
        return self.__interest_rate

    def __str__(self):
        return (super().__str__()+ "\nInterest Rate: "+ str(self.get_interest_rate()) +  \
        "\nMaturity Date: "+ self.get_maturity_date() )
                       
