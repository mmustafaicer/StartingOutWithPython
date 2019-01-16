# pattern 1
# print the following using loop structures.

# *******
# ******
# *****
# ****
# ***
# **
# *

# we will use descending for in range structure
# do not forget to use "-1" to show it will decrease one by one
for r in range(8,1,-1):
    for c in range(r,1,-1):
        print("*", end='')      # using end to command that "Do not go to new line"
    print()