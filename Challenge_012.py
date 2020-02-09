#012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number,
#otherwise show the first number first and then the second.
def twonumbers():
    a = int(input("Enter a number :"))
    b = int(input("Enter a number :"))

    if a > b:
        print (a , b)
    else:
        print (b , a)


twonumbers()
