# get the substance's temperature

sub_temp=float(input("Enter the temperature of substance: "))
max_temp=102.5

while sub_temp>max_temp:
    print("Please turn down the thermostat and wait 5 minutes.")
    sub_temp=float(input("Enter the temperature of substance again: "))
print("The temperature is acceptable. Check it again in 15 minutes.")