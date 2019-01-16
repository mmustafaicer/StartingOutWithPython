# pennies for pay

# ask user number of days
days=int(input("Enter the number of days to calculate: "))

# print headings
print()
print("Days\t\tEarnings in $")
print("-----------------------------")

# set an accumulator and create loop structure
total=1.0       # the first day is one penny
for d in range(1,days+1,1):
    total*=2
    print(d, "\t\t", format(total/100, ".2f"))



