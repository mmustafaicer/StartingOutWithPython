# recursive power method

def main():
    # explain the program
    print("This program exponentiate the number you gave: ")
    print("X: The number to be exponentiated")
    print("Y: The power to exponentiate")
    print()
    
    # get the data
    x=int(input("Please enter the value for X: "))
    y=int(input("Please enter the value for Y: "))
    
    # execute function
    result=power_calculate(x,y)
    
    # display the result.
    print("The result is", result)

# got an error message TypeError. Because my function name was
# "power". Also the name of one of the passing argument was "power".
# do not make that mistake.


# algorithm: 1st power of each number is itself. Like 2^1=2
# therefore, if we multiply our number nth time until we reduce 
# the power value to 1, basically we will perform power function.

# example: so if user gives 2^4. it will be 2 * (2^3)
# then 2*2*(2^2) >> then 2*2*2*(2^1) and then  >> 2*2*2*2
    
def power_calculate(num,power):
    if power>1:
        return num * power_calculate(num, power-1)
    elif power==1:
        return num 
    
# call the main function
main()