# this program uses a loop to display a 
# table showing the numbers 1 through 10
# and their squares

# print the table headings
print("Number\tSquare")
print("---------------")

# print the numbers 1 through 10
# backlash \t is for tab space remember from chapter 2
# range function does not use last number. See it does not print 11. 
for number in range (1,11):
    square=number**2
    print(number, '\t', square)