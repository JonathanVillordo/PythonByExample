#108 Open the Names.txt file. Ask the user to input a new name.
#Add this to the end of the file and display the entire file.

def addName():

    file = open('Names.txt','a')
    name = input('Enter a new name: ')
    file.write(name + "\n")
    file.close

    file = open('Names.txt','r')
    print(file.read())
    file.close

addName()
