#  CS232 week two example of inheritance
# This program is used to illustrate the use of inheritance in Python
# This is a driver program that creates instances of three different types of
# bank accounts (checking, savings, cd) via the use of three subclasses,
# one for each type of account, and a parent class

# parent 
import account
# sub-classes
import cd
import savings
import checking

def main():
    # Get the account number, account name interest rate,
    # and account balance for a savings account.
    print('Enter the following data for a savings account.')
    acct_num = input('Account number: ')
    acct_name = input('Account Name: ')
    int_rate = input("Interest Rate: ")
    balance = float(input('Balance: '))

    # Create a SavingsAccount object.
    save = savings.Savings(acct_num, acct_name, int_rate, balance)


    # Get the account number, interest rate,
    # account balance, and maturity date for a CD.
    print()
    print('Enter the following data for a CD.')
    acct_num = input('Account number: ')
    acct_name = input('Account Name: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))
    maturity = input('Maturity date: ')

    # Create a CD object.
    certif = cd.CD(acct_num, acct_name, int_rate, balance, maturity)

    # Now create a checking account
    # Get the account number, account name,
    # account balance, monthly fee
    print()
    print('Enter the following data for a checking account.')
    acct_num = input('Account number: ')
    acct_name = input('Account Name: ')
    balance = float(input('Balance: '))
    monthly_fee = float(input("Monthly fee: "))

    # Create a checking object.
    check= checking.Checking(acct_num, acct_name, balance, monthly_fee)
    
    
    
    # Display the data entered
    print()
    print('Here is the data you entered:')
    print()
    print("Savings Account")
    print("---------------")
    print (save)
    print()

    # show how set and get can be used to change account name for savings
    new_name = input("Enter new name for the savings account: ")
    print ("changing name of savings account from "+save.get_name()+ " to "+new_name)
    save.set_account_name(new_name)
    print()
    print(save)
    
    print()
    print("Certificate of Deposit")
    print("----------------------")
    print(certif)
    print()
    print("Checking Account")
    print("----------------")
    print(check)

    print()
    if (save == certif):
        print("The savings and CD balances are equal")
    else:
        print("The CD and savings account balances are different")

    if (save < certif):
        print("There is less money in the saving account than the CD")

    if (save > certif):
        print("There is more money in the savings acount than the CD")
   
# Call the main function.
main()


    
