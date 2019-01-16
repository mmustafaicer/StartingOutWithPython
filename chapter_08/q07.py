# character analysis

# NOTE: I did not have a text.txt file. 
# So I created mine in the same directory.

def main():
    
    # open the file
    infile=open("text.txt", "r")
    
    # read the lines
    lines=infile.read().splitlines()
    
    # set the accumulators
    num_uppercase=0
    num_lowercase=0
    num_digits=0
    num_whitespace=0
    
    # for each element in list = each sentence
    for line in lines:
        # for each character in each sentence
        for ch in line:
            if ch.isupper():
                num_uppercase+=1
            elif ch.islower():
                num_lowercase+=1
            elif ch.isdigit():
                num_digits+=1
            elif ch.isspace():
                num_whitespace+=1
                
    # print the totals:
    print("The number of uppercase letters in the file is", num_uppercase)
    print("The number of lowercase letters in the file is", num_lowercase)
    print("The number of digits in the file is", num_digits)
    print("The number of whitespace characters in the file is", num_whitespace)
                
# call the main function
main()