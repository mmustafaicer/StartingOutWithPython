# this program determines whether a bank customer qualifies for a loan.
min_salary=30000.       # The minimum annual salary
min_years=2             # The minimum years on the job

# get the customer's salary
salary=float(input("Enter your annual salary: "))
# get the years on job
years=int(input("Enter the number of years employed: "))
# Determine whether the customer qualifies

if salary>=min_salary:
    if years>=min_years:
        print("Congratulations you qualify for a loan.")
    else:
        print("You must have been employed for at least", min_years, "years to qualify.")
else:
    print("You must earn at least $", format(min_salary, ',.2f'), " per year to qualify.", sep='')
