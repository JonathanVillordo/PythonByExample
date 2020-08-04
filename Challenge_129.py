#129 Create a window that will ask the user to enter a number in a text box. When they click on a button it will use the code variable.isdigit()
#to check to see if it is a whole number. If it is a whole number, add it to a list box, otherwise clear the entry box. Add another button that will clear the list.

from tkinter import*

def click():
    
    number = number_box.get()
    if number.isdigit():
        listbox.insert(END,number)
        number_box.delete(0,'end')

def btnclear():

    listbox.delete(0,'end')



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


window.mainloop()
