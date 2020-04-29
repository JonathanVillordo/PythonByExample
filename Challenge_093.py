#093 Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers.
#Remove it from the original array and save it in a new array.
from array import *

def numbers():

    numbers = array('i',[])
    for i in range(5):
        num =int(input('Enter a number: '))
        numbers.append(num)
    print(numbers)
    grid = int(input('Choose a number: '))
    numbers.remove(grid)
    print(numbers)

numbers()
