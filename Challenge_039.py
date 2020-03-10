#039 Ask the user to enter a number between 1 and 12 and then display the times table for that number.
def tablenumber():
    number = int(input("Enter a number: "))

    for i in range(1,13):
        answer = (i * number)
        print(i, "x", number, "=", answer)

tablenumber()
