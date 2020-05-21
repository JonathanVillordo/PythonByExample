#105 Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line and only separated by a comma.
#Once you have run the program, look in the location where your program is stored and you should see that the file has been created.
#The easiest way to view the contents of the new text file on a Windows system is to read it using Notepad.

def file():

    files = open('Numbers.txt','w')
    files.write('1,')
    files.write('2,')
    files.write('3,')
    files.write('4,')
    files.write('5')
    files.close()

file()
