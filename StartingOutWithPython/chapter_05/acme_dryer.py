# this program displays step-by-step instructions
# for disassembling an Acme Dryer.
# the main function performs the program's main logic.

def main():
    # display the startup message.
    startup_message()
    input("Press enter to see Step 1.")
    # display step 1
    step1()
    input("Press enter to see Step 2.")
    # display step 2
    step2()
    input("Press enter to see Step 3.")
    # display step 3
    step3()
    input("Press enter to see Step 4.")
    # display step 4
    step4()
    
# the startup message function displays the program's initial message on the screen
def startup_message():
    print("This program tells you how to disassemble an ACME laundry dryer")
    print("There are 4 steps in the process")
    print()
# the step1 function displays the instructions
def step1():
    print("Step 1: Unplug the dryer and move it away from the wall.")
    print()
def step2():
    print("Step 2: Remove the six screws from the back of the dryer.")
    print()
def step3():
    print("Step 3: Remove the back panel.")
    print()
def step4():
    print("Step 4: Pull the top of the dryer straight up.")
    print()
    
# call the main function to begin the program.
main()
    