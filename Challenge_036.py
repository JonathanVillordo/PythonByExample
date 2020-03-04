# 036 Alter program 035 so that it will ask the user to enter their name and a number and then display their name that number of times.
def loopname():

    name = input("Enter your name: ")
    number = int(input("Enter number to repeat: "))

    for i in range(number):
        print(name)

loopname()
