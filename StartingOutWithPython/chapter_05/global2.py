# create a global variable.
number=0

def main():
    global number
    number=int(input("Enter a number: "))
    show_number()
def show_number():
    print("The number you entered is", number)

# call the main function
main()