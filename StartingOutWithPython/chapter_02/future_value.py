# Get the desired future value
future=float(input("Enter the desired future value: "))
# Get the annual interest rate
rate=float(input("What is the annual interest rate?: "))
# Get the number of years that the money will sit in the account
years=float(input("Enter the number of years the money will grow: "))
# Calculate the amount that will have to be deposited
present_amount=future/((1+rate)**years)


print("You need to deposit" \
      , present_amount, "dollars.")