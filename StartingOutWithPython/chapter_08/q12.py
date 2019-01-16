# pig latin

def main():
    # ask user to enter a sentence
    string=input("Please enter a string: ").upper()
    # split each word using whitespace
    word_list=string.split()
    
    # process each word one by one
    for word in word_list:
        # concatenate strings using [index]
        print(word[1:],word[0], "AY ", sep="", end="")
        
# call the main function
main()