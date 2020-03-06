# 038 Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered.

def repeatname():
    name = input("Enter your name: ")
    number = int(input("Enter a number: "))

    for i in range(number):
        for g in name:
            print(g)

repeatname()
