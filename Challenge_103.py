#103 Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe size.

def displayname():

    names = {}
    for i in range(4):
        name = input('Enter a name: ')
        age = int(input('Enter age: '))
        size = int(input('Enter shoe size: '))
        names[name]={'A':[age],'S':[size]}

    for k,v in names.items():
        print(k,v['A'])

displayname()

