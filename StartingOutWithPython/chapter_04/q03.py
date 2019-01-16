# budget analysis

# ask user for budgeted amount
user_budget=float(input("Please enter the budgeted amount for this month: "))

keep_going="y"
total_expense=0
counter=0

while keep_going=="y" or keep_going=="Y":
    print("Please enter the expense", counter+1, end='')
    expense=float(input(":"))
    total_expense+=expense
    print("If you want to add another expense please type 'y'. To end type 'n'", end="")
    keep_going=input(":")
    counter+=1      # this is for to make expense 1 expense 2 expense 3. It is better.

# Show the result
print()
print("Your budget is ", user_budget)
print("Your total expenses is ", total_expense)

if user_budget>total_expense:
    print("You are under budget.")
else:
    print("You are over budget.")
    