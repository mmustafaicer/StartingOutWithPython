# this program uses a function to calculate the
# total of the values in a list.

def main():
    # create a list.
    numbers=[2,4,6,8,10]
    
    # display the total of the list elements.
    print("The total is", get_total(numbers))
    
# the get total function accepts a list as an
# argument returns the total of the values in the list

def get_total(value_list):
    # create a variable to use as an accumulator.
    total=0
    
    # calculate the total of the list elements.
    for num in value_list:
        total+=num
        
    return total

# call the main function
main()