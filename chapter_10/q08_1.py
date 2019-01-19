# Trivia Game Main Program
import q08          # import Question class

def main():
    question_objects=[]
    
    # create a list of questions.
    questions=["What is the capital of Turkey?\n(a) Istanbul\n(b) Ankara\n(c) Izmir\n(d) Antalya",
               "What is the capital of France?\n(a) London\n(b) Paris\n(c) Moscow\n(d) Washington",
               "Where is the Great Pyramids?\n(a) Israel\n(b) Morocco\n(c) Egypt\n(d) Iraq",
               "What is the world's longest river?\n(a) Nile\n(b) Amazon\n(c) Colorado\n(d) Mississippi",
               "What is the capital of Spain?\n(a) Lisbon\n(b) Paris\n(c) Madrid\n(d) Cordoba",
               "When did the Cold War end?\n(a) 1989\n(b) 1990\n(c) 1985\n(d) 1992"]
    
    # create a list of answers with the same index number with
    # associated question.
    answers=["b", "b", "c", "b", "c", "a"]
    
    # for player 1 
    print("Player 1 questions:")
    print()
    for i in range(0,int(len(questions)/2), 1):      # half of the questions for Player 1
        print("Question: ", i+1)
        print(questions[i])
        user_answer=input("Enter correct answer (a,b,c,d): ")
        
        # create objects for player 1
        question=q08.Question(questions[i], answers[i], user_answer)
        question_objects.append(question)           # add it to questions list
        
        # test and get the total answer.
        question.test1()
        
    # clear the object list of questions
    question_objects=[]
    
    print("-------------------------------------------------------")
    print("Player 2 questions")
    print()      
    for i in range(int(len(questions)/2), len(questions),1):
        print("Question: ", i+1)
        print(questions[i])
        user_answer=input("Enter correct answer (a,b,c,d): ")
        
        # create objects for player player 2
        question=q08.Question(questions[i], answers[i], user_answer)
        question_objects.append(question)           # add it to questions list
        
        # test and get the total answer
        question.test2()
            
    # determine the winner/
    if question.get_test1()>question.get_test2():
        print("Player 1 has won.")
    elif question.get_test2()>question.get_test1():
        print("Player 2 has won.")
    else:
        print("It is a draw.")
    print()
    print("Player 1 score: ", question.get_test1())
    print("Player 2 score: ",question.get_test2())
        
# call the main function
main()