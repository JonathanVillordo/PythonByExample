#102 Ask the user to enter the name, age and shoe size for four people.
#Ask for the name of one of the people in the list and display their age and shoe size.

def names():

    names = {}

    for i in range(4):
        name = input('Enter a name: ')
        age = int(input('Enter age: '))
        size = int(input('Enter shoe size: '))
        names[name]={'A':[age],'S':[size]}
    
    select = input('Enter a name from list: ')
    print(names[select])

names()
