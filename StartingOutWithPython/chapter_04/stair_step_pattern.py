# this program displays a stair step pattern
num_steps=6

# create the repetition structure.
for r in range(num_steps):
    for c in range(r):
        print(' ', end='')      # do not forget to put a space between ' '
    print("#")