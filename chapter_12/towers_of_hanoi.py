# this program simulates the Towers of Hanoi game

def main():
    # set up some initial values.
    num_discs=3
    from_peg=1
    to_peg=3
    temp_peg=2
    
    # play the game.
    move_discs(num_discs, from_peg, to_peg,temp_peg)
    print("All the pegs are moved.")
    
# the moveDiscs function displays a disc move in
# the Towers of Hanoi game.
# the parameters are:
# num: The number of discs to move.
# from_peg: The peg to move from.
# to_peg: The peg to move to.
# temp_peg: The temporary peg.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# Call the main function.
main()
