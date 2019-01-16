# stadium seating

def main():
    # ask user to enter number of seats sold for each class.
    class_a_numbers=int(input("How many Class A tickets are sold?: "))
    class_b_numbers=int(input("How many Class B tickets are sold?: "))
    class_c_numbers=int(input("How many Class C tickets are sold?: "))
    print()
    total(class_a_numbers,class_b_numbers,class_c_numbers)

# remember arguments are passed in their relative order. 
# Notice that we just entered a,b, and c.    
def total(a,b,c):
    total=20*a+15*b+10*c
    print("The total income generated from tickets are $", format(total, ",.2f"), sep='')

main()