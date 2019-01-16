# this program divides a number by another number

def main():
    # get two numbers.
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    
    # divide num1 by num2 and display the result.
    result=num1/num2
    print(num1, "divided by", num2, "is", result)
    
# call the main function.
main()