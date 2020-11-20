#Create a simple program that shows a drop-down list containing several colours and a Click Me button.
#When the user selects a colour from the list and clicks the button it should change the background of the window to that colour.
#For an extra challenge, try to avoid using an if statement to do this.

from tkinter import *

def click():
    sel = selectcolour.get()
    window.configure(background = sel)





window = Tk()
window.title("colors")
window.geometry("450x450")

selectcolour = StringVar(window)
selectcolour.set("Grey")

colourlist = OptionMenu(window, selectcolour, "Grey","Red","Blue","Green","Yellow")
colourlist.place(x = 50, y = 30)

button = Button(text = "Click here",command = click)
button.place(x = 30, y = 50, width = 120, height = 25)

window.mainloop()

