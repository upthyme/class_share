# The Account parent class represents an account

class Account:
    
    # The __init__ method accepts arguments for the
    # account number, account name, and balance.
    
    def __init__(self, num, name, bal):
        self.__account_num = num
        self.__account_name = name
        self.__balance = bal

    # The following methods are mutators for the
    # data attributes.

    def set_account_num(self, num):
        self.__account_num = num

    def set_account_name(self,name):
        self.__account_name = name

    def set_balance(self, bal):
        self.__balance = bal

    # The following methods are accessors for the
    # data attributes.

    def get_account_num(self):
        return self.__account_num

    def get_name(self):
        return self.__account_name

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return ("Account Number: "+str(self.get_account_num())+ \
                "\nName: "+str(self.get_name())+ \
                "\nBalance:  "+str(self.get_balance()))

    def __eq__(self, other):
        if (self.__balance == other.__balance):
            return True
        else:
            return False

    def __lt__(self,other):
        if (self.__balance < other.__balance):
            return True
        else:
            return False

