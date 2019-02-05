# pennies for pay
# updated

# ask user number of days
days=int(input("Enter the number of days to calculate: "))

# print headings
print()
print("Days\tSalary in $")
print("-----------------------------")

# set an accumulator and create loop structure
salary=0.01 # the first day is one penny
total=0
for d in range(1,days+1,1):
    print(d,"\t$", salary)
    total += salary
    salary*=2
    
# show total   
print() 
print("The total earnings is ${}".format(total, ",.2f"))



