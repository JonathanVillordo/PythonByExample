#094 Display an array of five numbers. Ask the user to select one of the numbers. 
#Once they have selected a number, display the position of that item in the array. If they enter something that is not in the array,
#ask them to try again until they select a relevant item
from array import*

def numbers():
    
    numbers = array('i',[1,5,3,4,9])
    print(numbers)
    choice = int(input('Select a number from array: '))
    
    while choice not in numbers:
        choice = int(input('Try again enter a number: '))
    print(numbers.index(choice))
    

numbers()



