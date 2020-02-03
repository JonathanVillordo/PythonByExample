# 007 Ask the user for their name and their age. Add 1 to their age
#and display the output [Name] next birthday you will be [new age].

def birthday():

    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))

    print(Name,"next birthday you will be",Age+1)


birthday()
