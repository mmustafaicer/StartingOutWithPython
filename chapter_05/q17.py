# prime numbers

def main():
    # ask user to enter a number to check
    user_number=int(input("Please enter a number to check if it is prime or not: "))
    print()
    
    # if user enters 1 it is not prime
    if user_number == 1:
        print("1 is not a prime number.")
    else:   
        if is_prime(user_number):
            print("Your number", user_number, "is a prime number.")
        else:
            print("Your number", user_number, "is NOT a prime number.")
    
def is_prime(user_number):
    # we create a for loop structure so we can divide our number
    # to each number that is less than it.
    status=True
    for i in range(2,user_number):
        if user_number%i==0:            
            print("It can be divided by", i) 
            status=False
    return status 
main()

# percentage is remainder option. If it is divided evenly by any number (except 1 and itself)
# it is not prime number so status=False