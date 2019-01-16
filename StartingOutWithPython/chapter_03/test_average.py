high_score=95

# Get the three exam scores
test1=int(input("Enter the grade for test 1: "))
test2=int(input("Enter the grade for test 2: "))
test3=int(input("Enter the grade for test 3: "))

# Calculate the average test score
average=(test1+test2+test3)/3

# print the average
print("The average score is", format(average, ".2f"))

# If the average is higher than 95 congratulate the user
print()
if average>=high_score:
    print("Congratulations! Your average is above 95.")
    
# Check point page 89
# 3.6

#if y==20:
#    x=0

# 3.7

#if sales>=10000:
#    commissionRate:0.2