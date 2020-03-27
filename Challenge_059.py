#059 Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well done”,
#otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”.
#Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly.
import random

def colors():
  colors = ['red','blue','white','green','gray']
  answer = input("Choose one color"+','.join(colors)+": ")
  choice = random.choice(colors)
   
  while answer != choice:
    print("I bet you are {0} with envy or Your are probably feeling {1} right now".format(choice,answer))
    answer = input("Guess again: ")
  print("Well Done!!")
  
colors()
