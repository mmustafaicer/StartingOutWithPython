# get the grades from user
a_score=90
b_score=80
c_score=70
d_score=60

# get a test score from the user
score=int(input("Enter your test score: "))

# Determine the grade
# Be careful on indentation.
if score>=a_score:
    print("Your grade is A.")
else:
    if score>=b_score:
        print("Your grade is B.")
    else:
        if score>=c_score:
            print("Your grade is C.")
        else:
            print("Your grade is D.")