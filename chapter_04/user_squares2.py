# this program uses a loop to display a 
# table of numbers and their squares

# get the ending limits
print("This program display a list of numbers")
print("(starting at) 1 and their squares.")

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
print()

# print the table headings
print("Number\tSquare")
print("---------------")

# print the numbers and their squares.
for num in range (start,end+1):
    square=num**2
    print(num,"\t", square)