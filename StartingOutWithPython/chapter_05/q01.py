# kilometer converter

def main():
    # ask user to enter a distance in km
    km=int(input("Enter a distance in km: "))
    convert(km)
    
# now create convert function
def convert(kilometer):
    miles=kilometer*0.6214
    print(kilometer, "km is equal to", format(miles, ",.2f"), "miles.")
        
# call main function
main()