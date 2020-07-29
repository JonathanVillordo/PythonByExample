#124 Create a window that will ask the user to enter their name.
#When they click on a button it should display the message
#Hello and their name and change the background colour and font colour of the message box.

from tkinter import *

def call():
    
    name = entry_box.get()

    output_box = Message(text='Hello'+' '+name)
    output_box.place(x=30,y=120,width=300,height=100)
    output_box["bg"] = "red"

    name.set("")


window = Tk()
window.title("Window Title")
window.geometry("450x300")
label = Label(text = "Enter Your Name: ")
label.place(x=30,y=20)

name = StringVar()
entry_box = Entry(textvariable = name)
entry_box.place(x=30,y=50,width=120,height=25)


button = Button(text = "Press me", command = call)
button.place(x=30,y=80,width=120,height=25)
window.mainloop()
