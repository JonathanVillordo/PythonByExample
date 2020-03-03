# 034 Display the following message:
# If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and display the area.
# If they type in anything else, it should give them a suitable error message.

def squaretriangule():
    select = int(input("1) Square\n2) Triangle\n\nEnter a number: "))

    if select == 1:
        
        square = int(input("Enter the length of one of its sides: "))
        print("Square Area {0}".format(square**2))
        
    elif select == 2:
        
        base = int(input("Enter the base of triangle: "))
        height = int(input("Enter the height of triangle: \n\n"))

        print("Triangle Area {0}".format(base * height /2))
    else:

        print("Choose the correct answer")
        


squaretriangule()
