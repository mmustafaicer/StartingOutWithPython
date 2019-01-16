# vowels and consonants

def main():
    user_string=input("Enter a string to count vowels and consonants: ").lower()    # lowercase it.
    vowel,consonant=VowelConsonantCounter(user_string)
    
    # display the results.
    print()
    print("Number of vowels:", vowel, "and number of consonants is", consonant)
    
def VowelConsonantCounter(a):
    
    # create a list for vowel
    vowel_list=["a", "e", "i", "o", "u"]
    
    # set accumulators
    vowel=0
    consonant=0
    
    # read every character from the string
    for ch in a:
        # make sure it is alphabetical character
        if ch.isalpha():
            # then decide consonant or vowels.
            if ch in vowel_list:
                vowel+=1
            else:               # since it is alphabetical rest will be consonant.
                consonant+=1
    return vowel,consonant 

# call the main function
main()