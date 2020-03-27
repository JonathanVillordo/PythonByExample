# 057 Update program 056 so that it tells the user if they are too high or too low before they pick again.
import random

def wholenumber():
  numbers = random.randint(1,10)
  pick = int(input("Enter a number: "))

  while numbers != pick:
    if numbers > pick:
      print("Your number si to low")
      pick = int(input("Enter a number: "))
    else:
      print("Your number si to high")
      pick = int(input("Enter a number: "))


wholenumber()
