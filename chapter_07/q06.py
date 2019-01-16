# larger than n

def main():
    # create the list.
    try:
        list=[10,9,6,5,4,12,18,19,25]
        user_n=int(input("Please enter an integer: "))
        print("The numbers greater than", user_n, "in the list are listed below:")
        print("-----------------------")
        
        # pass these arguments to our function.
        greater=CompareNumbers(list,user_n)
    except ValueError:
        print("You entered non integer value.")     
        main()
def CompareNumbers(list,n):
    index=0 
    status=False
    # compare each item
    while index<len(list):
        if n<list[index]:
            print(list[index])
            status=True
        index+=1
    # print a message if there is none greater numbers.
    if not status:
        print("There are 0 numbers that are greater than the number you provided:", n)
# call the main function:
main()
    
    