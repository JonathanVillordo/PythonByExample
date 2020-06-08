#110 Using the Names.txt file you created earlier, display the list of names in Python.
#Ask the user to type in one of the names and then save all the names except the #one they entered into a new file called Names2.txt.

def openfile():
    
    names = []
    file = open('Names.txt','r')

    for data in file.readlines():
        print(data.strip('\n'))
        names.append(data.strip('\n'))
    
    file = open('Names.txt','w')
    file.truncate(0)
    name = input('Choose name from list: ')
    names.remove(name)
    for i in names:
        file.write(i+'\n')
    file.close()
    

openfile()
