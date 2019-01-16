# Sales Tax

# get the amount of purchase

purchase=float(input("Enter the amount of purchase: "))

# Calculate state and county sales tax
state_tax=purchase*0.05
county_tax=purchase*0.025
total_tax=state_tax+county_tax

# Display the results.

print()
print("Your purchase amount is $", purchase, sep='')
print("Your state tax is $", format(state_tax, ".2f"), sep='')
print("Your county tax is $", format(county_tax, ".2f"), sep='')
print("Your total tax is $", total_tax, sep='')
print()
print("Your total is $", purchase+total_tax, sep='')