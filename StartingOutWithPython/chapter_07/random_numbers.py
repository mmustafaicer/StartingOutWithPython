# this program assigns random numbers to a 
# two-dimensional list.
import random

# constants for rows and columns
ROWS=3
COLS=4

def main():
    # create a two-dimensional list.
    values=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    
    # fill the list with random numbers.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c]=random.randint(1,100)
            
    # display the random numbers.
    print(values)
    
    # or
    
#     for r in range(ROWS):
#         for c in range(COLS):
#            print(values[r][c])
    
# call the main function
main()