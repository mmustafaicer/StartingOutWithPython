# this program demonstrates several string testing methods.

def main():
    # get a string from the user.
    user_string=input("Enter a string: ")
    
    print("This is what I found about your string:")
    print()
    
    # test the string
    if user_string.isalnum():
        print("The string is alphanumeric.")
    if user_string.isdigit():
        print("The string contains only digits.")
    if user_string.isalpha():
        print("The string contains only alphabetic characters.")
    if user_string.isspace():
        print("The string contains only whitespace characters.")
    if user_string.islower():
        print("The letters in the string are all lowercase.")
    if user_string.isupper():
        print("The letters in the string are all uppercase.")
        
# call the main function
main()