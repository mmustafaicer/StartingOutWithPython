# Tip, Tax, and Total

# ask user to enter the charge for the food
price_def=float(input("Please enter the charge for the food: "))

tip=price_def*0.18
sales_tax=price_def*0.07

total=price_def+tip+sales_tax

# Display the data

print()
print("Your subtotal is", price_def)
print("Your tip amount is $", tip, sep='')
print("Your sales tax is $", format(sales_tax, ".2f"), sep='')
print()
print("Your total is $", total, sep='')