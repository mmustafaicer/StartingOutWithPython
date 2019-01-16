import random

# the Coin class simulates a coin that can
# be flipped

class Coin:
    # the __init__ method initializes the
    # sideup data attribute with "Heads"
    
    def __init__(self):
        self.sideup="Heads"
        
    # the toss method generates a random number
    # in the range of 0 through 1.If the number
    # is 0, then sideup is set to "Heads".
    # otherwise, sideup is set to "Tails".
    
    def toss(self):
        if random.randint(0,1) ==0:
            self.sideup="Heads"
        else:
            self.sideup="Tails"
            
    # the get_sideup method returns the value
    # referenced by sideup.
    def get_sideup(self):
        return self.sideup
    
# the main function
def main():
    # create an object from the Coin class.
    my_coin=Coin()
    
    # display the side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())
    
    # toss the coin.
    print("I am tossing the coin....")
    my_coin.toss()
    
    # display the side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())
    
# call the main function.
main()