# Sales Prediction

# Ask user to enter the projected amount of total sales
total_sales_projected=float(input("What is the projected amount of total sales?: "))

# Display the annual profit. %23 of total sales
profit=total_sales_projected*0.23
# Format to use comma to show thousands in dollars by using format function.
# Use sep= argument to write after $ sign.
print("The expected annual profit is $", format(profit, ',.1f'), sep='')