# Total Purchase

# Ask user for the price of each item
item1=float(input("Enter the price of item 1: "))
item2=float(input("Enter the price of item 2: "))
item3=float(input("Enter the price of item 3: "))
item4=float(input("Enter the price of item 4: "))
item5=float(input("Enter the price of item 5: "))

# Display the subtotal
print()
subtotal=item1+item2+item3+item4+item5
print("Your subtotal is $", subtotal, sep='')

# Calculate the tax. It is 7 percent.
print()
tax_calculated=subtotal*0.07
print("Sales tax is $", format(tax_calculated, '.2f'), sep='')

# Calculate the total and display it
print()
total=subtotal+tax_calculated
print("Your total is $", total, sep='')