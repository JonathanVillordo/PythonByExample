#131 Create a program that will allow the user to create a new .csv file.
#It should ask them to enter the name and age of a person and then allow them to add this to the end of the file they have just created.
from tkinter import*
import csv

def click_save():

    name = entryname.get()
    age = entryage.get()

    filename = name+'.csv'

    file = open(filename,"w")
    file.write(name+','+ age)
    file.close()

window = Tk()
window.title("CSV File")
window.geometry("500x500")

lblname = Label(text = 'Enter Name: ')
lblname.place(x = 30, y = 30)
entryname = Entry(text = '')
entryname.place(x = 120, y = 30)

lblage = Label(text = 'Enter Age: ')
lblage.place(x = 30, y = 70)
entryage = Entry(text = 0)
entryage.place(x = 120, y = 70 )

button = Button(text = 'Create File', command = click_save)
button.place(x = 60 , y = 150)

window.mainloop()
