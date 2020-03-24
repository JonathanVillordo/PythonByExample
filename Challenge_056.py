#056 Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.
import random

def wholenumber():
  numbers = random.randint(1,10)
  pick = int(input("Enter a number: "))
  
  while numbers != pick:
    pick = int(input("Enter a number: "))

 
wholenumber()
