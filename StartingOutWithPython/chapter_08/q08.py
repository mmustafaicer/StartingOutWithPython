# sentence capitalizer

def main():
    # get the string from user
    user_string=input("Enter a string: ")
    
    # after each exclamation mark, it gets capitalized
    sentence=user_string.split(".")
    print(sentence)
    
    # strip for deleting whitespace after.
    # sentences start like "asdsad. New sentence" there is one space after dot
    for i in sentence:
        print(i.strip().capitalize() + ". ", end="")
    
# call the main function
main()