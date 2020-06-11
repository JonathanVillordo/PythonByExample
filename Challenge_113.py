#113 Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
#After all the data has been added, ask for an author and display all the books in the list by that author.
#If there are no books by that author in the list, display a suitable message.
import csv
def morebooks():

    number  = int(input('How many books do you want add: '))
    file = open("Books.csv","a")
    for i in range(number):
        book = input ('Enter a Title Book: ')
        author = input('Enter Author: ')
        year = input('Enter year released: ')

        newbook = book+","+author+","+year+"\n"
        file.write(str(newbook))
    file.close()

    file = open("Books.csv","r")
    count = 0
    searchauthor = input('Enter and Author name: ')
    reader = csv.reader(file)
    for row in file:
        if searchauthor in str(row):
            print(row)
            count = count + 1
    if count == 0:
        print("There are no books by that author in this list.")
    file.close()


morebooks()


