# recursive end

def main():
    # create asterisk and numinner variable.
    ast="*"
    num=1
    
    # ask user how many end
    end=int(input("How many end of asterisks: "))
    print()
    
    # execute function
    print_asterisk(ast, num, end)
    
# define function.
# here is the algorithm:
# if end>num >>>> print "*" nth times. (which is num in our case)
    # for example: for num=1: print "*" 1 times and go to second line (num=2)
    # then for num=2: print "*" 2 times and go to third line etc. etc.
    # and return same function with num increased by 1 for next line (num+1)th line

# if end==num >>>> print "*" (end)th time. (final line) and do not
# return anything.
def print_asterisk(ast, num, end):
    if end>num:
        print(ast*num) # remember you can multiply the string.
        num+=1
        return print_asterisk(ast, num, end)
    elif end==num:
        print(ast*num) 
        
# call the main function
main()