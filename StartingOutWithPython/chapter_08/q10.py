# most frequent character

def main():
    user_string=input("Enter a string: ")
    
    # create a space for most frequent char and
    # accumulator for it.
    mFreqChar=[]
    occurence=0
    
    # initialize index
    index=0
    
    # read every character in the string
    for ch in user_string:
        # initialize character counter for 1st, 2nd, 3rd... and elements.
        occu=0
        while index<len(user_string):    
            if ch.lower()==user_string[index].lower():      # compare if repeats again
                occu+=1
                index+=1
            # if new count is greater than previous count change our display variables
            else:
                index+=1
            if occu>occurence:
                occurence=occu
                mFreqChar=ch    
            
    print("The most frequently occuring letter is", mFreqChar, "with", occurence, "occurences.")
            
# call the main function
main()
            
    