#112 Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file.
#Display each row of the .csv file on a separate line.
import csv

def addbook():

    file = open("Books.csv","a")
    bookTitle = input('Enter a  Book Title: ' )
    bookAuthor = input('Enter Book Author: ')
    bookYear = input('Enter Year Released: ')
    newRecord = bookTitle + "," + bookAuthor + "," + bookYear + "\n"
    file.write(str(newRecord))
    file.close()

    file = open("Books.csv","r")
    for i in file:
        print(i)

addbook()
