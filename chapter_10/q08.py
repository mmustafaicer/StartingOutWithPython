# Trivia Game

class Question:
    # took hours. **** If you have any counter within a class. Do not put under __init__
    player_1=0
    player_2=0
    
    def __init__(self, question, answer, c_answer):
        self.question=question
        self.answer=answer
        self.c_answer=c_answer
       
    def test1(self):
        if self.c_answer.lower()==self.answer:    
            print("Correct")
            print()
            Question.player_1+=1
        else:
            print("Wrong! The correct answer is", self.answer)
            print()
    
    def get_test1(self):
        return Question.player_1
            
    def test2(self):
        if self.c_answer.lower()==self.answer:    
            print("Correct")
            print()
            Question.player_2+=1
        else:
            print("Wrong! The correct answer is", self.answer)
            print()
        
    def get_test2(self):
        return Question.player_2
    
    def __str__(self):
        return "Player 1: " + str(Question.player_1) + "\n" +\
            "Player 2: " + str(Question.player_2)
    