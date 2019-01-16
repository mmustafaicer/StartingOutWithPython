# number analysis program

def main():
    print("In this program you will enter 20 numbers.")
    num_list=get_numbers()
    print()
    # print the results.
    print("The lowest number in this list is", min(num_list))
    print("The maximum number in this list is", max(num_list))
    print("The total of numbers is", sum(num_list))     # sum function sums the numbers in a given list.
    print("The average of numbers is", sum(num_list)/len(num_list))
    
def get_numbers():
    # create an empty list
    num_list=[]  
    
    # get the numbers from the user.
    for i in range(20):
        print("Enter the number #", i+1, sep="", end="")
        num_list.append(int(input(": "))) 
        
    return num_list

# call the main function
main()