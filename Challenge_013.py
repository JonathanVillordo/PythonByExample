# 013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more,
# display the message “Too high”, otherwise display “Thank you”.

def toohigh():
    number = int(input("Enter a number under 20: "))

    if number >= 20:
        print("Too high!!")
    else:
        print("Thank you")



toohigh()
