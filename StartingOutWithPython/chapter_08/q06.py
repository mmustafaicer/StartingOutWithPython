# average number of words
# NOTE: I did not have a text.txt file. 
# So I created mine in the same directory.

def main():
    
    # open the file
    infile=open("text.txt", "r")
    
    # read the lines. remember it creates a list.
    lines=infile.readlines()
    
    # to print the lines uncomment below
    #print(lines)
    
    # set accumulators.
    line_count=0
    total_word_count=0
    
    # read each element in lines list. each element is a sentence.
    for line in lines:
        line_count+=1
        
        # remember: By default, the split method uses spaces as separators 
        # (that is, it returns a list of the words
        # in the string that are separated by spaces). 
        word_count=len(line.split())        
        total_word_count+=word_count
        
    # calculate the average
    average=total_word_count/line_count
    
    #print the average
    print("The average number of words per sentence is", format(average, ",.2f"))
    
    # ask user to see if they want to see the table.
    print()
    table=input("If you want to see the table of each line with a count of words enter y: ")
    print()
    
    while table=="y" or table=="Y":
        line_count=0
        total_word_count=0
        print("Line\t\tWord Count")
        print("------------------------")
        for line in lines:
            line_count+=1
            print(line_count, end="\t\t")
            word_count=len(line.split())
            print(word_count)
        break
      
# call the main function
main()