# average rainfall

years=int(input("How many years of data you want to enter?: "))
months=12
total_rainfall=0.0      # this is accumulator

# there will be a nested loop. One for year one for months within year loop.
for y in range(1,years+1):
    print()
    print("Enter the data for year", y)
    print("------------------------")
    for m in range(1, months+1):
        print("Please enter year", y, "month", m, "rainfall amount in inches", end='')
        rainfall=float(input(": "))
        total_rainfall+=rainfall

print()
print("There are ", years*months, "months in the data.")
print("Total inches of rain is", total_rainfall)
print("Average rainfall per month is ", format(total_rainfall/(years*months), ",.2f"))
        