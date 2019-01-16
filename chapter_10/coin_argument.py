# this program passes a Coin object as
# an argument to a function.
import coin

# main function
def main():
    # create a Coin object (an instance of it)
    my_coin=coin.Coin()
    
    # this will display "Heads"
    print(my_coin.get_sideup())
    
    # pass the object to the flip function
    flip(my_coin)
    
    # this might display "Heads", or it might
    # display "Tails".
    print(my_coin.get_sideup())

# the flip function flips a coin.
def flip(coin_obj):
    coin_obj.toss()
    
# call the main function
main()