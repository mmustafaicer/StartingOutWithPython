# word frequency

def main():
    # create a dictionary to populate "word": "frequency"
    frequency={}
    
    # read the file.
    lines=ReadFile()
    
    # calculate frequencies
    freq_dict=Counter(frequency, lines)
    
    print(freq_dict)
    
    # ask user to enter a key\ and display the frequency.
    print()
    key=input("Enter a word to see its frequency in given text: ").lower()
    print(freq_dict[key])
    
def Counter(frequency,lines):
    # read each word
    for line in lines:
        for word in line.split():
            if word not in frequency:   # if word is new, create a new key
                frequency[word.lower()]=1       # assign 1 to value.
            else:
                frequency[word.lower()]+=1        # if word (key) exists, increase the value by 1
    return frequency   

def ReadFile():    
    # open a file to read.
    myfile=open("uniquewords.txt", "r")
    
    # read the lines
    lines=myfile.readlines()
    
    # close the file.
    myfile.close()
    return lines
            
# call the main function
main()