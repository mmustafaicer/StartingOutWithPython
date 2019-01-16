# Land Calculation

area=float(input("Enter the total square feet in your land: "))
acres=float(area/43560)

# If you want to have 2 digits after decimal, you need to put that argument in format parantheses.
print("Your area is", format(acres, '.2f'), "acres")