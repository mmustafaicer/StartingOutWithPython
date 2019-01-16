# this program imports the coin module and
# creates an instance of the Coin class.

import coin

def main():
    # create an object from the Coin class.
    my_coin=coin.Coin()
    
    # display the side of the coin that is facing up.
    print("This side is up:", my_coin.get_sideup())
    
    # toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
        
# call the main function
main()
    