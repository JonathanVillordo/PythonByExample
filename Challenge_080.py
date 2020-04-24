#080 Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname.
#Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space).

def name():

    name = input('Enter your name: ')
    print(len(name))
    surname = (input('Enter your surname: '))
    print(len(surname))
    completename = name+' '+surname
    print(completename)
    print(len(completename))

name()
