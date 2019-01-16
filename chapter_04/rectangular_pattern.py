# this program displays a rectangular pattern of asterisks
rows=int(input("How many rows?: "))
cols=int(input("How many columns?: "))
print()
for r in range(rows):
    for c in range(cols):
        print("*", end='')     # end states that " do not go to new line. put asterisk beside it.
    print()