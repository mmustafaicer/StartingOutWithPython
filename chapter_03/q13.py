# shipping charges

# ask user to enter the weight of a package
user_weight=float(input("Enter the weight of the package: "))
print()

# create decision structure shipping charges
if user_weight>0 and user_weight<=2:
    rate_per_pound=1.50
    charge=rate_per_pound*user_weight
    print("Your total shipping charge is $", format(charge, ",.2f"), sep='')
elif user_weight>2 and user_weight<=6:
    rate_per_pound=3.00
    charge=rate_per_pound*user_weight
    print("Your total shipping charge is $", format(charge, ",.2f"), sep='')
elif user_weight>6 and user_weight<=10:
    rate_per_pound=4.00
    charge=rate_per_pound*user_weight
    print("Your total shipping charge is $", format(charge, ",.2f"), sep='')
elif user_weight>10:
    rate_per_pound=4.75
    charge=rate_per_pound*user_weight
    print("Your total shipping charge is $", format(charge, ",.2f"), sep='')
else:
    print("ERROR: You entered an invalid number.")
    