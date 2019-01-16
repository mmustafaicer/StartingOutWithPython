# math quiz

# import random library to generate random numbers
import random

def main():
    first_num=random.randint(1,1000)
    second_num=random.randint(1,1000)
    print("Please calculate the sum of two numbers. The numbers are below:")
    print(first_num)
    print(second_num)
    total_num=CalculateTotal(first_num, second_num)
    user_answer=int(input("Please enter the total of these two numbers: "))
    print()
    CheckUserAnswer(total_num,user_answer)
def CalculateTotal(first_num,second_num):
    total=first_num+second_num
    return total
def CheckUserAnswer(total_num,user_answer):
    if total_num==user_answer:
        print("Congratulations! Your answer", total_num,"is correct.")
    else:
        print("Sorry! The answer is", total_num)


main()