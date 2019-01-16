# most frequent character

def main():
    print("Example: StopAndSmellTheRoses")
    user_string=input("Enter a string like one above: ")
    
    separator(user_string)
   
    
def separator(string):
    # separate it by uppercase letter.
    # first letter would be capital
    print (string[0].upper(), end="")
    
    # since we skip first letter, index=1
    index=1
    while index<len(string):
        if string[index].isupper():
            print(" ", end="")
            print(string[index].lower(), end="")
        else:
            print(string[index].lower(), end="")
        index+=1
        
    print(".")
# call the main function
main()