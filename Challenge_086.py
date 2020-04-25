#086 Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”.
#If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”.

def password():

    pass1 = (input('Enter your password: '))
    pass2 = (input('Enter again your password: '))

    if pass1 == pass2:
        print('Thank you.')
    elif (pass1.isupper() and pass2.islower()) or (pass1.islower() and pass2.isupper()):
        print('They must be in the same case')
    else:
        print('Incorrect')

password()
