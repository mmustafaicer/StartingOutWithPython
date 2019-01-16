# calories burned

cal_per_min=4.2

# print the headers
print("Minutes\t\tCalories")
print("------------------------")

for mins in range(10,31,5):
    calories=mins*cal_per_min
    print(mins,"\t\t",calories)