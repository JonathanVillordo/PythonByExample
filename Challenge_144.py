#Challenge144 database
import sqlite3

file = open("BookList.txt","w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)

print()
selectauthor = input("Enter an author's name: ")
print()

cursor.execute("SELECT * FROM Books Where Author=?",[selectauthor])
for x in cursor.fetchall():
    newrecord = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n"
    file.write(newrecord)

file.close()
db.close()
