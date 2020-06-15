#115 Using the Books.csv file, display the data in the file along with the row nu#mber of each.
import csv

def numlines():

    file = open('Books.csv','r')
    reader = csv.reader(file)

    for n,r in enumerate(file):
        print(n,r)

numlines()

