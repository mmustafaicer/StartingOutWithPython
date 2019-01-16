# this program gets a series of test scores and 
# calculates the average of the scores with the
# lowest score dropped.

def main():
    # get the test scores from the user.
    scores=get_scores()
    
    # get the total of test scores.
    total=get_total(scores)
    
    # get the lowest score
    lowest=min(scores)
    
    # substract the lowest from the total.
    total-=lowest
    
    # calculate the average. Note that we divide by 1 less than
    # the number of scores because the lowest score was dropped.
    average=total/(len(scores)-1)
    
    # display the average
    print("The average, with the lowest score dropped is:", average)
    
# the get_scores function gets a series of test scores from the user
# and stores them in a list. A reference to the list is returned.
def get_scores():
    # create an empty list.
    test_scores=[]
    
    # create a variable to control the loop.
    again="y"
    
    # get the scores from the user and add them to the list.
    while again=="y" or again=="Y":
        # get a score and add it to the list. 
        value=float(input("Enter a test score: "))
        test_scores.append(value)
        
        # want to do this again?
        print("Do you want to add another score?")
        again=input("y=yes, anything else=no: ")
        print()
        
    # return the list
    return test_scores

# the get_total function accepts a list as an argument
# returns the total of the values in the list.

def get_total(value_list):
    # create a variable to use as an accumulator.
    total=0.0
    
    # calculate the total of the list elements.
    for num in value_list:
        total+=num
    
    # return the total
    return total

# call the main function
main()
        