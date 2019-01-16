# this program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string.

def main():
    # create a variable to use to hold the count.
    # the variabel must start with 0.
    count=0
    
    # get a string from the user.
    my_string=input("Enter a sentence: ")
    
    # count the Ts.
    for ch in my_string:
        if ch=="T" or ch=="t":
            count+=1
    
    # print the result.
    print("The letter T appears", count, "times.")

# call the main function.
main()