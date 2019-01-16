# this program demonstrates the BankAccount class.

# if import bankaccount shows a "Unresolved import"
# right click on project>Properties. Then click PyDev - PYTHONPATH
# click "External Libraries" . Then click add.
# choose the folder that the module is stored. Add apply
# restart the Eclipse

import bankaccount

def main():
    # get the starting balance.
    start_bal=float(input("Please enter your starting balance: "))
    
    # create a BankAccount object.
    savings=bankaccount.BankAccount(start_bal)
    
    # deposit the user's paycheck.
    pay=float(input("How much were you paid this week?: "))
    print("I will deposit that into your account.")
    savings.deposit(pay)
    
    # display the balance.
    print("Your account balance is $", format(savings.get_balance(), ",.2f"), sep="")
    
    # get the amount to withdraw.
    cash=float(input("How much would you like to withdraw?: "))
    print("I will withdraw that from your account.")
    savings.withdraw(cash)
    
    # display the balance.
    print("Your account balance is $", format(savings.get_balance(), ",.2f"), sep="")
    
# call the main function
main()