# this program has a recursive function.

def main():
    # by passing the argument 5 to the message
    # function we are telling it to display the 
    # message five times.
    message(5)
    
def message(times):
    if times>0:
        print("This is a recursive function.")
        message(times-1)
        
# call the main function.
main()
