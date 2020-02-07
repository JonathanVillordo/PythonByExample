# 011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller
# number goes into the larger number in a user-friendly format.

def timesmaller():

    over = int(input('Enter a number over 100 :'))
    smaller = int(input('Enter a number under 10 :'))

    print("The smaller number goes into the large number",over / smaller)



timesmaller()
