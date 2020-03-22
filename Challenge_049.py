#049 Create a variable called compnum and set the value to 50. Ask the user to enter a number.
#While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess.
#If they enter the same value as compnum, display the message “Well done, you took [count] attempts”.

def guess():

  compnum = 50
  attempts = 0

  number = int(input("Enter a number: "))

  while number != compnum:
    number = int(input("Your number is too low or to high Enter a number:"))
    attempts += 1
    
  print("Well done, you took {0} attempts".format(attempts))

guess()
