# 085 Ask the user to type in their name and then tell them how many vowels are in their name.

def vowels():

    vowels = ['a','e','i','o','u']
    name = input('Enter your name: ')
    count = 0

    for letter in name:
        if letter in vowels:
            count += 1
    print('Your name has {} vowels'.format(count))

vowels()
