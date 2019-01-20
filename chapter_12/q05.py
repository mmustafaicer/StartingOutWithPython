# recursive list sum

def main():
    # create a sample list for our purposes.
    list=[12,18,24,36,63,57]
    
    # indicator for total
    total_counter=0
    
    # execute function
    total=get_total(list, 0, total_counter)
    
    print("The total of the numbers in the given list is", total)
    
# define function. my algorithm here:
# take first element of the list and add it the total.
# then delete that element and pass the new list to the function.
# keep on executing function until there is no element.

def get_total(list, index, total_counter):
    while len(list)>0:      # while there are elements on the list keep adding
        # add first item to the total
        total_counter+=list[index]
        # del first item after adding
        del list[index]
        # pass the new list to the function and return it
        return get_total(list, 0, total_counter)    
    else:                   # when there is 0 element in the list.
        return total_counter
# call the main function
main()