#114 Using the Books.csv file, ask the user to enter a starting year and an end year.
#Display all books released between those two years.
import csv

def books():

    startyear = int(input('Enter a start year: '))
    endyear = int(input('Enter a end year: '))

    file = list(csv.reader(open("Books.csv")))
    tmp = []
    for row in file:
        tmp.append(row)

    x = 0
    for row in tmp:
        if int(tmp[x][2]) >= startyear and int(tmp[x][2]) <= endyear:
            print(tmp[x])
        x = x+1

books()
