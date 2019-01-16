# this program calculates a salesperson's pay
# at Make Your Own Music
def main():
    # get the amount of sales
    sales=get_sales()
    # get the amount of advanced pay
    advanced_pay=get_advanced_pay()
    # determine the commission rate
    comm_rate=determine_comm_rate(sales)
    # calculate the pay
    pay=sales*comm_rate-advanced_pay
    # display the amount of pay
    print("The pay is $", format(pay, ",.2f"), sep='')
    
    # determine whether the pay is negative.
    if pay<0:
        print("The salesperson must reimburse the company.")
        
# the get_sales function gets a salesperson's
# monthly sales from the user and returns that value
def get_sales():
    # get the amount of monthly sales.
    monthly_sales=float(input("Enter the monthly sales: "))
    # return the amount entered.
    return monthly_sales
# the get_advanced_pay function gets the amount of advanced pay given
# to the salesperson and returns that amount
def get_advanced_pay():
    # get the amount of advanced pay
    print("Enter the amount of advanced pay, or enter 0 if no advanced pay was given.")
    advanced=float(input("Advanced pay: "))
    #return the amount entered
    return advanced
# the determine_comm_rate function accepts
# the amount of sales as an argument and returns the applicable commission rate

def determine_comm_rate(sales):
    # determine the commission rate
    if sales<10000.00:
        rate=0.10
    elif sales>10000 and sales<=14999.99:
        rate=0.12
    elif sales>=15000 and sales<=17999.99:
        rate=0.14
    elif sales>=18000 and sales<=21999.99:
        rate=0.16
    else:
        rate=0.18
    # return the commission rate
    return rate

main()
        