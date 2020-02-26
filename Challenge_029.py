# 029 Ask the user to enter an integer that is over 500. Work out the square root of that number and display it
# to two decimal places.
import math
def square():
    number = int(input("Enter an integer over 500: "))

    print(round(float(math.sqrt(number)),2))



square()
