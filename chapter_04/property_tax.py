# this program display property taxes.
tax_factor=0.0065   # represents the tax factor given.

# get the first lot number
print("Enter the property lot number")
print("or enter 0 to end")
lot=int(input("Lot number: "))

# continue processing as long as the user
# does not enter lot number 0
while lot!=0:
    # get the property value.
    value=float(input("Enter the property value: "))
    
    # calculate the property tax
    tax=value*tax_factor
    
    # Display the tax
    print("Property tax: $", format(tax, ",.2f"), sep='')
    
    # get the next lot number
    print()
    print("Enter the next lot number or enter 0 to end.")
    lot=int(input("Lot number: "))