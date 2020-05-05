#098 Using the 2D list from program 096, ask the user which row they would like displayed and display just that row.
#Ask them to enter a new value and add it to the end of the row and display the row again.

def twolist():

    dlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
    print(dlist)
    row = int(input('Which row would you like displayed?: '))
    addnum = int(input('Enter a number: '))
    dlist[row].append(addnum)
    print(dlist)

twolist()
