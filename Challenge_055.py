#055 Randomly choose a number between 1 and 5. Ask the user to pick a number.
#If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number.
#If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”.
import random

def guessing():

  number = random.randint(1,5)
  guess = int(input("Enter a number:"))

  if number == guess:
    print("Wll done")
  else:
    print("Number to high or too low")
    guess = int(input("Enter a number: "))

  if number == guess:
    print("Correct")
  else:
    print("You lose")
  
guessing()
