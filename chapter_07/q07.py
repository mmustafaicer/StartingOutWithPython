# driver's license exam

def main():
    # create the list as given on book.
    correct_answers=["A", "C", "A", "A", "D",
                     "B", "C", "A", "C", "B",
                     "A", "D", "C", "A", "D",
                     "C", "B", "B", "D", "A"]
    
    # read the answers from your file.
    myfile=open("answers.txt", "r")
    # read the lines from your file
    my_answers=myfile.readlines()
    
    # strip all the \n from the elements
    index=0
    while index<len(my_answers):
        my_answers[index]=my_answers[index].rstrip("\n")
        index+=1
    
    total_correct=CompareAnswers(correct_answers, my_answers)
    print()
    
    # if equals and more than 15 it passes exam.
    if total_correct>=15:
        print("Congratulations! You passed the exam. You have", total_correct, "answers.")
    else:
        print("You failed the exam. You have", total_correct, "answers.")
    
def CompareAnswers(a,b):
    # accumulator for correct answers
    total_correct=0
    
    # compare the two list.
    index=0
    while index<len(a):
        if a[index]==b[index]:
            total_correct+=1
        else:
            print("The question #", index+1, " is wrong!", sep="")
        index+=1        
    return total_correct    
    
# call the main function
main()
    
