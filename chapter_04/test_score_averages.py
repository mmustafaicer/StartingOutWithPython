# this program averages test scores. it asks the user for the
# number of students and the number of test scores per student.

# get the number of students
num_students=int(input("How many students do you have?: "))

# get the number of test scores per student.
num_test_scores=int(input("How many test scores per student?: "))

# determine each student's average test score.
for student in range(num_students):
    # initialize an accumulator for test scores.
    total=0.0
    # get a student's test scores
    print("Student number", student+1)      # because it will start with 0 otherwise.
    print("--------------------------")
    
    for test_num in range(num_test_scores):
        print("Test number", test_num+1, end='')    # end here means no new line but give a space.
        score=float(input(":"))
        # add the score to the accumulator
        total+=score
        
    # calculate the average test score for this student.
    average=total/num_test_scores
    
    # display the average
    print("The average for student number", student+1, "is", average)
    print()
    