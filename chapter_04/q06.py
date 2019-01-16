# celcius to fahrenheit table

# print headings
print("Celcius\t\tFahrenheit")
print("--------------------------")

# create loop structure
for c in range(0,21,1):
    fahrenheit=((9/5)*c)+32
    print(c,"\t\t", format(fahrenheit, ".2f"))
    