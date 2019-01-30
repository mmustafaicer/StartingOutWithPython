# time calculator

# ask user to enter a number of seconds

user_seconds=int(input("Enter the number of seconds: "))
print()

# create decision structure
if user_seconds>=86400:
    days=user_seconds//86400
    print("There are", days, "days in", user_seconds, "seconds.")
elif user_seconds>=3600:
    hours=user_seconds//3600
    print("There are", hours, "hours in", user_seconds, "seconds.")
elif user_seconds>=60:
    minutes=user_seconds//60
    print("There are", minutes, "minutes in ", user_seconds, "seconds.")
else:
    print("ERROR: Invalid Response.")