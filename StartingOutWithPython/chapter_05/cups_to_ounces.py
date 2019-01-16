# this program converts cups to fluid ounces.

def main():
    # display the intro screen
    intro()
    # get the number of cups.
    cups_needed=int(input("Enter the number of cups: "))
    # convert cups to ounces.
    cups_to_ounces(cups_needed)

# the intro function displays an introductior screen
def intro():
    print("This program converts measurements.")
    print("in cups to fluid ounces. For your reference the formula is")
    print("    1 cup = 8 fluid ounces.")
    print()
    
# the cups_to_ounces function accepts a number of cups
# and displays the equivalent number of ounces.
def cups_to_ounces(cups):
    ounces=cups*8
    print("That converts to", ounces, "ounces.")

# call the main function
main()
    