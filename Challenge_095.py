#095 Create an array of five numbers between 10 and 100 which each have two decimal places.
#Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message and ask them to try again until
#they enter a valid amount. Divide each of the numbers in the array by the number the user entered and display the answers shown to two decimal places.

from array import *

def numbers():

    numb = array('d',[10.99,45.54,36.4,100.45,76.54])
    choice = int(input('Enter a number between 2 and 5: '))

    while choice not in [2,3,4,5]:
        choice = int(input('Try again: '))

    for i in numb:
        print("{0:.2f}".format(i/choice) )

numbers()
