# this program has a recursive function.

def main():
    i=1     # to track of how many times it appeard.
    message(i)

def message(i):
    print(i)
    print("This is a recursive function.")
    i+=1
    message(i)
    
# call the main function.
main()