# 120
import random

def get_add():

    ad_answer = 0
    print('Add next numbers: ')
    for  i in range(2):
        num = random.randrange(5,20)
        ad_answer += num
        print(num)
    user_answer =int(input('Enter your answer: ')) 

    return (ad_answer,user_answer)

def get_sub():
    
    print('Subract next numbers: ')
    num1 = random.randrange(25,50)
    num2 = random.randrange(1,25)
    print (num1)
    print(num2)
    sub_answer = num1 - num2
    user_answer = int(input('Enter your answer: '))

    return (sub_answer,user_answer)

def get_check(answer,user_answer):

    if answer == user_answer:
        print('Correct!!!!')
    else:
        print('Incorrect!!!!')

def main():

    print('1) Addition ')
    print('2) Subtraction ')
    choice = int(input('Enter 1 or 2: '))

    if choice == 1:
       answer,user_answer = get_add()
       get_check(answer,user_answer)
    elif choice ==2:
       answer,user_answer =  get_sub()
       get_check(answer,user_answer)
    else:
        print('Incorrect Selection!!!!')

main()
