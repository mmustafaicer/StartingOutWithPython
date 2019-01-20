# this program uses recursion to print number
# from the Fibonacci series.

def main():
    print("The first 10 numbers in the \
    Fibonacci series are")
    
    for number in range(1,11):
        print(fib(number))
        
# the fib function returns the nth number
# in the fibonacci series

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return fib(n-1) + fib(n-2)
    
# call the main function.
main()