# Ackermann's Function

def main():
    # ask user for data
    m=int(input("Enter a positive integer for m: "))
    n=int(input("Enter a positive integer for n: "))
    
    # call the function
    result=ackermann(m,n)
    print(result)
    
# define the function. algorithm given in the book
def ackermann(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))
    
# call the main function
main()