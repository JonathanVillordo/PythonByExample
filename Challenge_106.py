#106 Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines.
#Once you have run the program, look in the location where your program is stored and check that the file has been created properly.

def names():

    file = open('Names.txt','w')

    file.write('Gaby\n')
    file.write('Emma\n')
    file.write('Jonathan\n')
    file.write('Sonia\n')
    file.write('Casi')

    file.close()

names()
