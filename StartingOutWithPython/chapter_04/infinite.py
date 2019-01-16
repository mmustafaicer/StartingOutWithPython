# this program demonstrates an infinite loop
# create a variable to control the loop
keep_going="y"

# Warning Infinite Loop
while keep_going=="y":
    sales=float(input("Enter the amount of sales: "))
    comm_rate=float(input("Enter the commission rate: "))
    
    # calculate commission
    commission=sales*comm_rate
    
    # display the commission
    print("The commission is $", format(commission, ',.2f'), sep='')