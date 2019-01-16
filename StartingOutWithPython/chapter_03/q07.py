# color mixer

print("Red, blue, and yellow are primary colors.")
print()

# ask user to choose two primary colors to mix

color1=input("Enter the primary color 1 (red,blue, or yellow): ")
color2=input("Enter the primary color 2 (red,blue, or yellow): ")

# create secondary colors. Remember the two colors could be inputed in two different
# ways. Like color1=red color2=blue or color1=blue color2=red 

# purple
if color1=="red" and color2=="blue":
    print("The secondary color is purple.")
elif color1=="blue" and color2=="red":
    print("The secondary color is purple.")
# orange
elif color1=="red" and color2=="yellow":
    print("The secondary color is orange.")
elif color1=="red" and color2=="yellow":
    print("The secondary color is orange.")
# green
elif color1=="blue" and color2=="yellow":
    print("The secondary color is green.")
elif color1=="yellow" and color2=="blue":
    print("The secondary color is green.")
# error message
else:
    print("ERROR: You entered the primary colors wrong.")

