#Create a program that will ask the user to enter a name and then select the gender for that person from a drop-down list.
#It should then add the name and the gender (separated by a comma) to a list box when the user clicks on a button.

from tkinter import *

def save_name():
    name = name_box.get()
    gender = selectgender.get()
    
    name_list.insert(END,name+','+gender)



window = Tk()
window.title("Name Gender")
window.geometry("450x350")

#name
label = Label(text = "Enter your name: ")
label.place(x = 20, y = 20, width = 100, height = 25)
name_box = Entry(text = 0)
name_box.place(x = 120, y = 20, width = 100, height = 25)

#gender
selectgender = StringVar(window)
selectgender.set("Male")
genderlist = OptionMenu(window,selectgender,"Female","Male")
genderlist.place(x = 300, y = 20)

#button
button = Button(text = "Click me",command = save_name)
button.place(x = 120, y = 50, width = 100, height = 25)

#listbox
name_list = Listbox()
name_list.place(x = 120, y = 80, width = 230, height = 100)

window.mainloop()
