#092Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array.
#Sort this large array and display it so that each number appears on a separate line.

from array import*
import random

def numbers():

    arr1 = array('i',[])
    arr2 = array('i',[random.randint(0,5) for i in range(5)])
    
    for i in range(3):
        num = int(input('Enter a number: '))
        arr1.append(num)

    arr3 = arr1 + arr2

    for g in arr3:
        print(g)

numbers()
