# This program demonstrates how a floating-point
# number is displayed with no formatting.
amount_due=5000.0
monthly_payment=amount_due/12.0
print("The monthly payment is", monthly_payment)
# As you see float numbers have 12 digits after decimal point.

# we have a format function we can use. 2f: 2 means two digits ; f means float 
print()
print("The monthly payment is", format(monthly_payment, '.2f'))
