# initials.

def main():
    # get the first, middle, and last name from user.
    name=get_name()
    
    # using split method separate them into first, middle, and last.
    name_separated=name.split()
    
    # display the result.
    print("Your initials")
    
    # read every piece as a separate with for loop.
    for ch in name_separated:
        print(ch[0], ".", sep='', end="")
    
def get_name():
    name=input("Enter your full name: ")
    return name

# call the main function
main()
