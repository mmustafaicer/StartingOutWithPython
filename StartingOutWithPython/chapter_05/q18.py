# prime number list

# prime numbers

def main():
    print("The prime numbers from 1 to 100 are listed below.")
    print()
    # first lets pass all numbers from 1 to 100 to our is_prime function.
    for num in range(2,101):
        if is_prime(num):
            print(num)
       
def is_prime(num):
    # we create a for loop structure so we can divide our number
    # to each number that is less than it.
    status=True
    # we set status to be True until it could be falsified. If it can be divided by any number
    # less than itself, status=False. Check the code below.
    for i in range(2,num):
        if num%i==0:            
            status=False
    return status
        
main()

# percentage is remainder option. If it is divided evenly by any number (except 1 and itself)
# it is not prime number so status=False
