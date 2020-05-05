# 097 Using the 2D list from program 096, ask the user to select a row and a column and display that value.

def dlist():

    twoD = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
    print(twoD)
    column = int(input('Select a column from array: '))
    row = int(input('Select a row from array: '))

    print(twoD[row][column])

dlist()
