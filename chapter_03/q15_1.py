# time calculator alternative
# in case that I misunderstood the question

# ask user to enter a number of seconds

user_seconds=int(input("Enter the number of seconds: "))
print()

# create starter values
days=0
hours=0
minutes=0
seconds=0

# calculate the total days,hours,minutes, and seconds.

# total day
days = user_seconds//86400
# remainder from day
day_remainder = user_seconds%86400
if day_remainder > 0:
    # total_hours
    hours= day_remainder//3600
    # remainder from hours
    hours_remainder = day_remainder%3600
    
    # if there are still seconds calculate minutes.
    if hours_remainder>0:
        minutes = hours_remainder//60
        minutes_remainder = hours_remainder%60
        seconds=minutes_remainder
        
# display the result.
print(f"There are {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds in that {user_seconds} seconds that you entered.")

