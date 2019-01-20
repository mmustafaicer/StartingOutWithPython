# recursive printing

def main():
    # explain the program
    print("This program displays the numbers from \
1 up through the 'n' that you stated")
    print()
    
    # get the number from the user.
    beg_num=1
    end_num=int(input("Please enter an integer: "))
    print()
    
    print_numbers(beg_num, end_num)

# algorithm: if beg_num<end_num  print beg_num and return print_numbers(beg_num+1, end_num)
#            if beg_num==n  print end_num
def print_numbers(b,e):
    if b<e:
        print(b)
        return print_numbers(b+1, e)        # this is our recursion. func within same func
    elif b==e:          # when reached final number, just print it. dont return
        print(e)
        
# call the main function
main()