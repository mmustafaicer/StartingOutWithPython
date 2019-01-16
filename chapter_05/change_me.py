# this program demonstrates what happens 
# when you change the value of a parameter

def main():
    value=99
    print("The value is", value)
    change_me(value)
    print("Back in main, the value is", value)

def change_me(arg):
    print("I am changing the value.")
    arg=0
    print("Now the value is", arg)

# call the main function
main()
