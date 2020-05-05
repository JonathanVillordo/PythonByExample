#099 Change your previous program to ask the user which row they want displayed.
#Display that row. Ask which column in that row they want displayed and display the value that is held there.
#Ask the user if they want to change the value. If they do, ask for a new value and change the data. Finally, display the whole row again.

def twolist():

    dlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
    print(dlist)
    row = int(input('Which row would you like displayed?: '))
    print(dlist[row])
    column = int(input('Choose a column: '))
    print (dlist[row][column])
    change = input('Do you want change the value?y/n : ')

    if change == 'y':
        numb = int(input('Enter a number: '))
        dlist[row][column] = numb
    

    print(dlist[row])


twolist()
