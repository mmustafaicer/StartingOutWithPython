# pattern

# there are 6 rows
rows=6

# create loop structure
# there will be a 6 six row
# there will be 0 space between #'s. And 1 space bw #'s. and so and so forth.

for r in range(0,rows,1):
    print("#", end="")      # every line starts with #. So, every outer loop will have this command.
    for col in range(0,r,1):    # this is for space between two # signs.
        print(" ", end="")
    print("#")
    
        