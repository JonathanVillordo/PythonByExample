#077 Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list.
#Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”,
#delete that entry from the list and display the list again.

def party():

    names = []
    more = 'yes'

    print('Enter 3 names to invite a party: ')
    for i in range(1,4):
        names.append(input('Enter a name: '))

    more = input('Do you want invite more?: ')
    while more == 'yes':
        names.append(input('Enter a name: '))
        more = input('Do you want invite more?: ')

    print(names)
    asknames  = input('Type one of the names: ')
    print(names.index(asknames))

    invite = input('Do you want invite it?: ')

    if invite == 'no':
        names.remove(asknames)
        print(names)

party()

