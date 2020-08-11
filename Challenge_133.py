#133 Create your own icon that consists of several vertical multi-coloured lines. Create a logo which measures 200 x 150, 
#using Paint or another graphics package. Create the following window using your own icon and logo.
from tkinter import*
import os 


def clickme():
    
    name = name_box.get()
    message = str('Hello '+name)
    answer['text'] = message
    name_box.delete(0,'end')



dirname = os.path.dirname(__file__)
print(os.path.join(dirname,"downloads","nba.jpg"))
print(dirname)

window = Tk()
window.geometry("500x500")
window.wm_iconbitmap("nba.ico")

logo = PhotoImage(file = '/Users/villordomendoza/downloads/minion.gif')
logoimage = Label(image = logo)
logoimage.place(x = 100, y = 20, width = 200, height = 150)

#name
lbl_name = Label(text = "Enter your name: ")
lbl_name.place(x = 30, y = 200)
name_box = Entry(text='')
name_box.place(x = 150, y = 200)
name_box.focus()

#btn
button = Button(text = "Press me", command = clickme)
button.place (x = 30, y = 250)

answer = Message(text = "")
answer.place(x = 150, y = 250, width = 200, height = 25)
answer["bg"] = "green"






window.mainloop()
