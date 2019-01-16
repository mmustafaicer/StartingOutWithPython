# bug collector

# set an accumulator for bugs
bugs_total=0.0

# set repetition structure.
for day in range(5):     # it is five days.
    print("Enter the collected bugs for day", day+1, end='')
    bugs=int(input(": "))
    # add bugs to accumulator
    bugs_total+=bugs
# display the total bugs
print()
print("The total bugs collected: ", bugs_total)