#083 Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase.
def uppercase():

    word = input('Enter a word in upper case: ')

    while word.islower():
        print('Try again')
        word = (input('Enter a word in upper case: '))
    print(word)

uppercase()
