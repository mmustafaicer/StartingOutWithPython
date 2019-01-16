# Get the total seconds from user
total_seconds=float(input("Enter a number of seconds: "))

hours=total_seconds//3600 # Because there is 3600 seconds in 1 hour. We do not want fraction.
minutes=(total_seconds//60)%60
seconds=total_seconds%60

# Display the results
print("Here is the time in hours, minutes, and seconds:")
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)