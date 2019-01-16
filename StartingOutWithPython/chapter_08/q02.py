# sum of digits in a string

def main():
    try:
        # get the numbers from user
        numbers=get_numbers()
        total=0
        
        # access each digit by index number. use len(numbers)
        index=0
        while index<len(numbers):
            total+=int(numbers[index])        # do not forget to convert into integer
            index+=1
        
        print("The sum of digits in the number of", numbers, "is", total)
    
    # in case user enters letters, create an exception.    
    except ValueError:
        print("You can't enter letters in the numbers string. Try again!")
        print("---------------------------------------------------------")
        main()

def get_numbers():
    numbers=input("Enter a series of single-digit numbers (such as 12445): ")
    return numbers    

# call the main function
main()