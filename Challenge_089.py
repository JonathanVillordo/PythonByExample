#089 Create an array which will store a list of integers. Generate five random numbers and store them in the array. Display the array (showing each item on a separate line).

from array import*
import random

def numbers():

    num = array('i',[])

    for i in range(5):
        num.append(random.randint(0,5))

    for n in num:
        print(n)

numbers()
