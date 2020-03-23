#054 Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice.
#If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”.
# At the end, tell the user if the computer selected heads or tails.
import random

def choose():
  choose = ["h","t"]

  answer = input("Choose h or t: ")

  if answer == random.choice(choose):
    print("You win")
  else:
    print("Bad luck")
choose()

