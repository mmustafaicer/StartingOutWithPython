# body mass index

# ask user to enter weight and height

user_weight=float(input("Enter the weight in pounds: "))
user_height=float(input("Enter the height in inches: "))
print()

# calculate body mass index
bmi=user_weight*(703/(user_height**2))

# create decision structure for categories

if bmi>=18.5 and bmi<=25:
    print("Your body mass index (BMI) is", format(bmi, ",.2f"), "and your category is optimal.")
elif bmi<18.5:
    print("Your body mass index (BMI) is", format(bmi, ",.2f"), "and your category is under-weight.")
elif bmi>25:
    print("Your body mass index (BMI) is", format(bmi, ",.2f"), "and your category is over-weight.")
else:
    print("ERROR: Invalid Value.")