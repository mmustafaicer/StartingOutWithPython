# most frequent character

def main():
    user_string=input("Enter a string: ")
    
    # create an empty list space for characters and
    # occurences list with same shared-index.
    char_list=[]
    occurences=[]
    
    # initialize index
    
    # read every character in the string
    for ch in user_string.lower():
        # if it is not in the list append it
        if ch not in char_list:
            char_list.append(ch)
            # and increase occurence for it
            occurences.append(1)
        
        # if it is ON THE LIST
        elif ch in char_list:
            
            # find its index
            index = char_list.index(ch)
            
            # increase its occurence by 1
            occurences[index]+=1
            
    # Now determine the winner.
    # step by step:
    # 1) find the maximum value of occurences
    # 2) get the index of it
    # 3) since the indexes are same, find corresponding character in char_list
    winner = char_list[occurences.index(max(occurences))]

    print("\nThe most frequently occuring letter is", winner, "with", max(occurences), "occurences.")
            
# call the main function
main()
            
    