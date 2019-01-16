# distance traveled

# ask user to enter the speed of the vehicle in mph

speed=int(input("Please enter the speed of vehicle in mph: "))
hours=int(input("Please enter hours that you traveled on that speed: "))

# print the headings for table-like view
print("Hour\t\tDistance Traveled")
print("____________________________")

# for structure. Hours will start from 1.
for hour in range(1, hours+1):
    distance=hour*speed
    print(hour,"\t\t", distance)