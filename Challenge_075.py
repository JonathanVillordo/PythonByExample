#075 Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line.
#Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list,
#otherwise display the message “That is not in the list”.

def digits():

    digits = [123,989,567]
    for i in digits:
        print(i)
    choose = int(input('Enter a 3 digit number: '))

    if choose in digits:
        print(digits.index(choose))
    else:
        print('That is not in the list')

digits()
