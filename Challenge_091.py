#091 Create an array which contains five numbers (two of which should be repeated).
#Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list.

from array import *

def numbers():

    num = array('i',[2,2,3,4,5])
    print(num)
    choose = int(input('Select a number: '))
    print(num.count(choose))

numbers()
