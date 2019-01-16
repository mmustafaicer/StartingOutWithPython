# this program demonstrates the repetition operator.

def main():
    # print nine rows increasing in length.
    for count in range(1,10):
        print("Z"*count)
        
    # print nine rows decreasing in length.
    for count in range(8,0,-1):
        print("Z"*count)
        
# call the main function.
main()