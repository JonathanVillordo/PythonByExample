#088 Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order.

from array import *

def numbers():

    numbersa = array('i',[])
    
    for i in range(5):
        number = (int(input('Enter a number: ')))
        numbersa.append(number)
    
    numbersa = sorted(numbersa)
    numbersa.reverse()

    print(numbersa)

numbers()
