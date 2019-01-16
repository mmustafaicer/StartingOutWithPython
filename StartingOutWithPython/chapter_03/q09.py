# roulette wheel colors

# ask user to enter a pocket number

p_num=int(input("Enter a pocket number between 0 and 36: "))

# create decision structure carefully.
print()
if p_num==0:
    print("Pocket", p_num, "is green.")
elif p_num>=1 and p_num<=10:
    if p_num%2==0:      # this means if p_num is even number
        print("Pocket", p_num, "is black.")
    else:
        print("Pocket", p_num, "is red.")
elif p_num>=11 and p_num<=18:
    if p_num%2==0:      # this means if p_num is even number
        print("Pocket", p_num, "is red.")
    else:
        print("Pocket", p_num, "is black.")
elif p_num>=19 and p_num<=28:
    if p_num%2==0:      # this means if p_num is even number
        print("Pocket", p_num, "is black.")
    else:
        print("Pocket", p_num, "is red.")
elif p_num>=29 and p_num<=36:
    if p_num%2==0:      # this means if p_num is even number
        print("Pocket", p_num, "is red.")
    else:
        print("Pocket", p_num, "is black.")
else:
    print("ERROR: You entered a number that is not within the range of 1-36.")

