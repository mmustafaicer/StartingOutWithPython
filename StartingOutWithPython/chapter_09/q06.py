# file analysis

def main():
    
    # read two files
    myfile1=open("fileanalysis_1.txt", "r")
    myfile2=open("fileanalysis_2.txt", "r")
    
    # read the lines
    lines1=myfile1.readlines()
    lines2=myfile2.readlines()
    
    # close the files
    myfile1.close()
    myfile2.close()
    
    # display unique words
    unique_words1=UniqueWords(lines1)
    unique_words2=UniqueWords(lines2)
    
    print("Unique words for <<<fileanalysis_1.txt>>> are listed below.")
    print(unique_words1)
    print()
    print("Unique words for <<<fileanalysis_2.txt>>> are listed below.")
    print(unique_words2)
    
    # display a list of words that appear in both files.
    print()
    print("List of words that appear in both files:")
    print(unique_words1.intersection(unique_words2))
    
    #  display a list of words that appear in the first file but not the second.
    print()
    print("List of words that appear in the first file but not the second:")
    print(unique_words1.difference(unique_words2))
    
    # display a list of words that appear in the second file but not the first.
    print()
    print("List of words that appear in the second file but not the first:")
    print(unique_words2.difference(unique_words1))
    
    # display a list of words that appear in either the first or second file
    # but noth both.
    print()
    print("List of words that appear in either the first or second file but not both:")
    print(unique_words1.symmetric_difference(unique_words2))
    
def UniqueWords(lines):
    unique_words=set()
    
    # read each word.
    for line in lines:      # each line
        for word in line.split():   # each word: split words by space (a.k.a. word)
            unique_words.add(word)  # add the word to set
            
    # remember. Set does not have duplicate items. So you can just iterate
    # unique_words.add(word) without checking >>>> if word is not in unique_words. etc.
    
    return unique_words
# call the main function
main()