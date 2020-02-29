# 033 Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way
#(e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).
def divide():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print ("{0} divided by {1} is {2} with {3} remaining".format(a,b,a//b,a%b))

divide()
