# this program demonstrates the BankAccount class.
# with the __str__ method added to it.

import bankaccount2

def main():
    # get the starting balance.
    start_bal=float(input("Please enter your starting balance: "))
    
    # create a BankAccount object.
    savings=bankaccount2.BankAccount(start_bal)
    
    # deposit the user's paycheck.
    pay=float(input("How much were you paid this week?: "))
    print("I will deposit that into your account.")
    savings.deposit(pay)
    
    # display the balance.
    print(savings)
    
    # get the amount to withdraw.
    cash=float(input("How much would you like to withdraw?: "))
    print("I will withdraw that from your account.")
    savings.withdraw(cash)
    
    # display the balance.
    print(savings)
    
# call the main function
main()