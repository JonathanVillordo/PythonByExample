#Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two values and store it in a variable called “comp_num”.
#Define another subprogram that will give the instruction “I am thinking of a number...” and then ask the user to guess the number they are thinking of.
#Define a third subprogram that will check to see if the comp_num is the same as the user’s guess.
#If it is, it should display the message “Correct, you win”, otherwise it should keep looping,
#telling the user if they are too low or too high and asking them to guess again until they guess correctly.
import random

def get_number():

    print('Enter a low and high number')
    low = int(input('Enter a low number: '))
    high = int(input('Enter a high number: '))
    comp_num = random.randrange(low,high)

    return comp_num

def thinking():
    
    print('I am thinking of a number....')
    guess = int(input('Guess the number you are thinking of: '))
    
    return guess

def check(comp_num,guess):

    while comp_num != guess:
        if comp_num > guess:
            print('To low')
            guess = int(input('Enter a number: '))
        else:
            print('To high')
            guess = int(input('Enter a number: '))
    print("Correct you win")

def main():

    comp_num = get_number()
    guess = thinking()
    check(comp_num,guess)

main()
