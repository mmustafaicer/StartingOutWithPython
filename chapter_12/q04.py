# largest file item

def main():
    # create a sample list for our purposes.
    list=[1,2,3,950,5,7,8,16,200,250]
    
    index=len(list)-1   # last item on the list is (n-1) th item.
    
    # execute function and display it
    largest=get_largest(list, index)
    print("The largest number in this given list is", largest[0])        
    # since there is only one element, our index is 0
    
# define function. our algorithm:
# get the last item on the list and compare it to the item before that
# remove the smaller one from the list and pass the list argument to
# the same function until there is only one element on the list (which is
# our largest number)

def get_largest(list, index):
    if index==0:        # if it is last element left
        return list
    elif index>0:
        if list[index]>list[index-1]:
            # delete the smaller of two
            del list[index-1]
            # and pass it to function
            return get_largest(list, index-1)       # also list shrinked by 1
        else:
            # delete the smaller of two
            del list[index]
            # and pass it to function
            return get_largest(list, index-1)       # again list shrinked by 1
            
# call the main function
main()