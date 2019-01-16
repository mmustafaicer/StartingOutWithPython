# population

# ask user to enter inputs
population=int(input("Enter the population of organisms: "))
daily_increase=float(input("Enter the daily increase as percentage (for example 30 for %30): " ))
days=int(input("Enter the days to multiply: "))

# convert percentage for calculation
daily_increase=daily_increase/100

# print headings
print("Days\t\tPopulation")
print("---------------------------")

# create loop structure
for d in range(1,days+1,1):
    print(d, "\t\t", format(population, ",.1f"))
    population=(population*daily_increase)+population
    
    