# This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay=5000.0
annual_pay=monthly_pay*12
print("Your annual pay is $", \
      format(annual_pay, ",.2f"), sep='')

# We use sep='', so there will be a no space between $ sign and amount of dollar.