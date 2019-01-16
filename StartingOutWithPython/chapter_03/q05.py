# mass and weight.

# ask user to enter a mass for an object
mass=float(input("Please enter the mass the object's mass: "))

# calculate the weight using formula given
weight=mass*9.8

# print outputs
print("Weight is", format(weight, ".2f"), "newtons.")
if weight>500:
    print("It is too heavy!")
elif weight<100:
    print("It is too light!")

