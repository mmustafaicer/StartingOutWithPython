# blackjack simulation
# there is alternative using random library.

# this program uses a dictionary as a deck of cards.

def main():
    # create a deck of cards
    deck=create_deck()
    
    # deal the cards
    deal_cards(deck)
    
# the create_deck function returns a dictionary
# representing a deck of cards.

def create_deck():
    # create a dictionary with each card and its value
    # stored as key-value pairs.
    deck={"Ace of Spades": 1, "2 of Spades": 2, "3 of Spades": 3,
          "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6,    
          '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
          '10 of Spades':10, 'Jack of Spades':10,
          'Queen of Spades':10, 'King of Spades': 10,
        
          'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
          '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
          '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
          '10 of Hearts':10, 'Jack of Hearts':10,
          'Queen of Hearts':10, 'King of Hearts': 10,
        
           'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
           '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
           '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
           '10 of Clubs':10, 'Jack of Clubs':10,
           'Queen of Clubs':10, 'King of Clubs': 10,
        
           'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
           '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
           '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
           '10 of Diamonds':10, 'Jack of Diamonds':10,
           'Queen of Diamonds':10, 'King of Diamonds': 10}
    
    # return the deck.
    return deck

# the deal_cards function deals a specified number of cards from the deck
def deal_cards(deck):
    # initialize an accumulator for the hand value for both players
    player_1=0
    player_2=0
    
    # store player cards
    player_1_cards=[]
    player_2_cards=[]
    
    #
    while player_1<=21 and player_2<21:
        # deal the cards and accumulate their values.
        # player 1
        card, value=deck.popitem()
        if card=="Ace of Spades" or card=="Ace of Hearts" or card=="Ace of Clubs" or card=="Ace of Diamonds":
            if player_1+11<=21:
                player_1+=11
                player_1_cards.append(card)
        else:         
            player_1+=value
            player_1_cards.append(card)
        
        card, value=deck.popitem()
        if card=="Ace of Spades" or card=="Ace of Hearts" or card=="Ace of Clubs" or card=="Ace of Diamonds":
            if player_2+11<=21:
                player_2+=11
                player_2_cards.append(card)
        else:         
            player_2+=value
            player_2_cards.append(card)
    # display the winners.
    if player_1>=21 and player_2>=21:
        print("Both players' hand are over 21. No Winner!")
        print("Player 1 hands: ", player_1_cards)
        print("Player 2 hands: ", player_2_cards)
    elif player_1>=21:
        print("The winner is Player 2. And his cards are listed below" )
        print(player_2_cards)
    elif player_2>=21:
        print("The winner is Player 1. And his cards are listed below" )
        print(player_1_cards)
    
# call the main function
main()

# -__-NOTE-__-: deck.popitem() is supposed to remove 
# a key-value pair randomly from dictionary according to book.
# but **** according to stackoverflow, it is arbitrary but not random
# so if you enter same number again and again it will give the same result.
# instead use random library.