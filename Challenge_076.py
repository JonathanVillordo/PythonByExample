#076 Ask the user to enter the names of three people they want to invite to a party and store them in a list.
#After they have entered all three names, ask them if they want to add another.
#If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party.

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

    print(len(names))

party()
