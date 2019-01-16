# this program displays gross pay
# get the number of hours workerd

hours=int(input("Enter the hours worked this week: "))

# get the hourly pay rate
pay_rate=float(input("Enter the hourly pay rate: "))

# calculate the gross pay.
gross_pay=hours*pay_rate

# display the gross pay.
print("Gross pay: $", format(gross_pay, ",.2f"), sep='')