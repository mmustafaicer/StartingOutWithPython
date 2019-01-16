# morse code converter

def main():
    
    # get the string input from user
    user_input=input("Enter a string to be converted into morse code: ")
    
    # convert the string to uppercase
    user_input=user_input.upper()
    
    # split string into character list. use list function
    user_input_list=list(user_input)
    print(user_input_list)
    
    morse_code=converter(user_input_list)
    
def converter(a):
    # create two lists with same order (same index number) by looking at table
    character=[" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7",\
               "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
               "W", "X", "Y", "Z"]
    morse=[" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--", \
           "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", \
           "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", \
           ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.-", "--.."]
    
    # get the index code of user input in character list
    index=0
    while index<len(a):
        
        # to get the index use index object.
        position=character.index(a[index])
        print(morse[position], end=" ")         # give a space break after each ch in morse
        index+=1
    
# call the main function
main()
        