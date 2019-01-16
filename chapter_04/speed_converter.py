# this program converts the speeds 60 kph through 
# 130 kph (in 10 kph increments) to mph

start_speed=60      # Starting speed
end_speed=131       # Ending speed (remember range does not take last digit so, increment by 1) 
increment=10
conversion=0.6214

# print the table headings
print("KPH\tMPH")
print("------------------")

for kph in range (start_speed, end_speed, increment):
    # calculate conversion
    mph=kph*conversion
    print(kph,"\t", format(mph, ".1f"))