# recursive multiplication

def main():
    
    # prompt user to enter the data.
    x=int(input("Enter a positive non-zero integer for X: "))
    y=int(input("Enter a positive non-zero integer for Y: "))
    
    # execute multiplication
    # example 7x4=4+4+4+4+4+4+4 or x+y= y + y + y (xth times)
    result=multiply(x,y)
    
    # display the result
    print()
    print("The multiplication of", x , "and", y, "is", result)

# define the function. here is the algorithm:
# if x==1 return y
# if x>1 return y+multiply(x-1,y) >>> in other words: x is "how many y's are to be added"
# then reduce it by one every time the function works. That is why it is "x-1"
def multiply(x,y):
    if x>1:
        return y + multiply(x-1,y)
    if x==1:
        return y
    
# call the main function
main()