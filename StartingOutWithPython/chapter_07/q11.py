# lo shu magic square

# this is a really long question and got help
# from community at stackoverflow.

ROWS=3
COLS=3

def main():    
    # create the two dimensional list
    square = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    # need 9 numbers from user. numbers should be between 1-9 and 
    # each number should be identical. for that lets create a list to store user inputs.
    # so we can check if user entered same input or not. if not append it to list.
    # and go to next index.
    
    user_numbers=[]
    index=0
    while index<9:
        inp=int(input("Enter a number from 1 to 9: "))
        if 1<=inp<=9 and inp not in user_numbers:
            print("Success")
            user_numbers.append(inp)
            index+=1
        else:
            print("Your number is already entered or isn't in range 1-9. Please enter again.")
    
    # now these inputs are on one-dimensional list.
    # write them into two dimension list. (3x3 grid)
    index2=0
    for r in range(ROWS):
        for c in range(COLS):
            square[r][c]=user_numbers[index2]
            index2+=1
    print()
    print()
    
    # display the square for clarification        
    print("Your square is below")
    for r in range(ROWS):
        for c in range(COLS):
            print(square[r][c], end="\t")
        print()
    
    # get the totals from functions and assign them to variables    
    row1,row2,row3=SumofRows(square)
    col1,col2,col3=SumofCols(square)    
    diag1,diag2=SumofDiagonal(square)
    
    # compare them if they are equal.
    if row1==row2==row3==col1==col2==col3==diag1==diag2:
        print("It is a Lo Shu Magic Square.")
    else:
        print("It is not a Lo Shu Magic Square.")
 
def SumofRows(square):
    totalrow1=0
    for c in range(COLS):
        totalrow1+=square[0][c-1]
    totalrow2=0
    for c in range(COLS):
        totalrow2+=square[1][c-1]
    totalrow3=0
    for c in range(COLS):
        totalrow3+=square[2][c-1]
    return totalrow1, totalrow2, totalrow3

def SumofCols(square):
    totalcol1=0
    for r in range(ROWS):
        totalcol1+=square[r-1][0]
    totalcol2=0
    for r in range(ROWS):
        totalcol2+=square[r-1][1]
    totalcol3=0
    for r in range(ROWS):
        totalcol3+=square[r-1][2]    
    return totalcol1,totalcol2,totalcol3

def SumofDiagonal(square):
    # calculate manually
    first_diag=square[0][0] + square[1][1] + square[2][2]
    second_diag=square[0][2] + square[1][1] + square[2][0]
    return first_diag, second_diag    
        
# call the main function.
main()