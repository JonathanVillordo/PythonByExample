#047 Ask the user to enter a number and then enter another number.
#Add these two numbers together and then ask if they want to add another number.
#If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”.
#Once the loop has stopped, display the total.

def addingnumbers():
  number1 = int(input("Enter a number: "))
  total = number1
  another = 'y'

  
  while another == 'y':
    
    number2 = int(input("Enter another number: "))
    total = total + number2
    another = input("Do you want add another number? ")

  print("Your total is {0}".format(total))

addingnumbers()    
