# this program calculates the average of the
# values in a list.

def main():
    # create a list.
    scores=[2.5,7.3,6.5,4.0,5.2]
    
    # create a variable to use as an accumulator
    total=0.0
    
    # calculate the total of the list elements.
    for value in scores:
        total+=value 
        
    # calculate the average of the elements.
    average=total/len(scores)
    
    # display the total of the list elements.
    print("The average of the elements is", average)
    
# call the main function
main()