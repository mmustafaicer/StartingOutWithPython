# this program uses recursion to find the GCD
# of two numbers.

def main():
    # get two numbers.
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    #Display the GCD.
    print('The greatest common divisor of')
    print('the two numbers is <<<', gcd(num1, num2), ">>>")

    # The gcd function returns the greatest common
    # divisor of two numbers.
def gcd(x, y):
    if x % y == 0:
        # print(y)         # if you want to see remainder uncomment it.
        return y
    else:
        # print(y)
        return gcd(x, x % y)

# Call the main function.
main()