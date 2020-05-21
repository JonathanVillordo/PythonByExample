#104 After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from the list.
#Delete this row from the data and display the other rows on separate lines.

def displayname():

    names = {}
    for i in range(4):
        name = input('Enter a name: ')
        age = int(input('Enter age: '))
        size = int(input('Enter shoe size: '))
        names[name]={'A':[age],'S':[size]}

    getrid = input('Enter a name to remove: ')
    del names[getrid]

    for i in names:
        print(i)

displayname()
