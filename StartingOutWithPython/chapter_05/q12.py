# maximum of two values

def main():
    print("This program compares two numbers that you entered.")
    user_number1=int(input("Please enter the number 1: "))
    user_number2=int(input("Please enter the number 2: "))
    print()
    CalculateGreater(user_number1,user_number2)
    
def CalculateGreater(a,b):
    if a==b:
        print("The numbers are the same. The number you entered is", a)
    elif a>b:
        print("The number", a,"is greater than number",b)
    else:
        print("The number", b,"is greater than number", a)
                
# call the main function
main()
    