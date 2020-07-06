#116 Import the data from the Books.csv file into a list.
#Display the list to the user. Ask them to select which row from the list they want to delete and remove it from the list.
#Ask the user which data they want to change and allow them to change it. Write the data back to the original .csv file,
#overwriting the existing data with the amended data.
import csv

def remove():
    
    tmp = []
    file = list(csv.reader(open('Books.csv')))
    for row in file:
        print(row)
        tmp.append(row)

    row = int((input('What row do you want remove?: ')))
    del tmp[row]
    file = open('Books.csv','w')
    for i in tmp:
        file.write(i[0])
    file.close()
remove()
