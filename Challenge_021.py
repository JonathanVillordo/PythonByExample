# 021 Ask the user to enter their first name and then ask them to enter their surname.
# Join them together with a space between and display the name and the length of whole name.
def fullnamelen():

    name = input("Enter your name: ")
    surname = input("Enter your Surname: ")

    lengthname = len(name) + len(surname)

    print('{0} {1} {2}'.format(name,surname,lengthname))


fullnamelen()
