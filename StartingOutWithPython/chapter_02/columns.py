# Specifying a minimum field width

print("The number is", format(12345.6789, '12,.2f'))
print()
print("The number is", format(12345.6789, '12.2f'))


# example on book

print()
# This program displays the following floating-point numbers in column
# with their decimal points aligned.
num1=127.899
num2=3465.148
num3=3.776
num4=264.821
num5=88.081
num6=799.999

# Display each number in a field of 7 spaces
# with 2 decimal places.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))


# Percentage

print(format(0.5, '.0%'))

# For integers
print(format(123456, '10d'))
# Or use comma
print(format(123456, '10,d'))