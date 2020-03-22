# 045 Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number.
# Add that number to the total and print the message “The total is... [total]”. Stop the loop when the total is over 50.

def whilecounting():
  total = 0

  while total < 50:
    num = int(input("Enter a number: "))
    total = total + num
  print ("The total is {0}".format(total))

whilecounting()
