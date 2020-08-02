#127 Create a window that will ask the user to enter a name in a text box.
#When they click on a button it will add it to the end of the list that is displayed on the screen. Create another button which will clear the list.
from tkinter import*

def Call():
    name = nametxt.get()
    output_box["text"] = name

def reset():
    nametxt.delete(0, END)
    output_box["text"] = ''
    nametxt.focus()


window = Tk()
window.title = ("Name")
window.geometry("500x200")

label = Label(text = "Enter yor name ")
label.place(x = 30, y = 20)

nametxt = Entry(text='')
nametxt.place(x = 150,y = 20)

button = Button(text = 'Press me', command = Call)
button.place(x = 30, y = 50)

output_box = Message(text = '')
output_box.place(x = 150, y = 50, width = 100, height = 25)
output_box ["fg"] = "red"

clear_btn = Button(text = "Clear", command = reset)
clear_btn.place(x = 300, y = 50, width = 50, height = 25)
    

window.mainloop()
