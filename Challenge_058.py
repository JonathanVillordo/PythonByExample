#058 Make a maths quiz that asks five questions by randomly generating two whole numbers to make
#the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add
#a point to their score. At the end of the quiz, tell them how many they got correct out of five.
import random

def maths():
  score = 0
 
  for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print (num1, "+", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
      score = score + 1
  print("Your scored {} out of 5".format(score))
  

maths()
