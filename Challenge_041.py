# 041 Ask the user to enter their name and a number.
# If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” three times.
def namenumber():
    name = input("Enter yor name: ")
    number = int(input("Enter a number: "))

    if number < 10:
        for i in range(number):
            print (name)
    else:
        for i in range(3):
            print ("Too high")


namenumber()
