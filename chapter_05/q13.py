# falling distance

# write constants
G=9.8

def main():
    # print headers
    print("Seconds\t\tDistance in Meters")
    print("----------------------------------")
    # to pass arguments from 1 to 10 write an for loop
    for t in range(1,11,1):
        distance=falling_distance(t)
        print(t, "\t\t", format(distance, ",.2f"))
    
# this is our falling_distance function. return distance to main function where
# it is called.
def falling_distance(falling_time):
    distance=(1/2)*G*(falling_time)**2
    return distance

# call the main function
main()