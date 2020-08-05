#130 Alter program 129 to add a third button that will save the list to a .csv file. The code tmp_list = num_list.get(0,END)
#can be used to save the contents of a list box as a tuple called tmp_list.
from tkinter import*
import csv

def click():
    
    number = number_box.get()
    if number.isdigit():
        listbox.insert(END,number)
        number_box.delete(0,'end')

def btnclear():

    listbox.delete(0,'end')

def btnsave():

    tmp_list = listbox.get(0,END)
    
    digits_file = open("Digits.csv","w")
    for i in tmp_list:
        digits_file.write(i+'\n')
    digits_file.close()



window = Tk()
window.title("Is Digit?")
window.geometry("500x500")

label = Label(text = "Enter a number: ")
label.place(x = 30, y = 20)

number_box = Entry(text = 0)
number_box.place(x = 150, y = 20)
number_box["bg"] = "red"
number_box["justify"] = "center"

listbox = Listbox(window)
listbox.pack(pady = 100)

button = Button(text = 'Verify Number', command = click)
button.place(x = 30, y = 50)

button_clr = Button(text = 'Clear List', command = btnclear)
button_clr.place(x = 30, y = 300)

button_sv = Button(text = 'Save List', command = btnsave)
button_sv.place(x = 200, y = 300)

window.mainloop()
