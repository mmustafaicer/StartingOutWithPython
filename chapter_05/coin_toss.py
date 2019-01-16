# this program simulates 10 tosses of a coin.
import random

# constants
HEADS=1
TAILS=2
TOSSES=10

def main():
    for toss in range(TOSSES):
        # simulate the coin toss.
        if random.randint(HEADS,TAILS)==HEADS:
            print("Heads")
        else:
            print("Tails")
# call the main function.
main()


# My version

#def main():
#    coin_toss()
    
#def coin_toss():
#    for i in range(10):
#        number=random.randint(1,2)
#        if number==1:
#            print("Heads")
#        else:
#            print("Tails")
#main()