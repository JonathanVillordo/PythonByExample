#090 Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message “Outside the range”.
#Once five numbers have been successfully added, display the message “Thank you” and display the array with each item shown on a separate line.

from array import *

def numbers():

    num = array('i',[])

    for i in range(5):
        number = int(input('Enter a number: '))
        
        if number < 10 or number > 20:
            print('Outside the range')
        else:
            num.append(number)
    print('Thank you')
    print(num)

numbers()


