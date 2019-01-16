# argument of end. You can print all print functions in same line using end="" argument.

print("One", end=" ")
print("Two", end=" ")
print("Three")

# There is also separator argument

print("One", "Two", "Three", sep=" ** ") # Separate the three different arguments using two asterisks (**)

# Escape characters \n is an escape character that goes to next line.
print()
print("One\nTwo\nThree")

# \t next tab position on same line
print()
print("Mon\tTues\tWed")
print("Thur\tFri\tSat")

# concatenation

print("You suck at " + \
      "computer gaming. "+\
      "Get the hell out of here.")