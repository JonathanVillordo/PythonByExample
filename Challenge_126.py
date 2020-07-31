#126 Create a program that will ask the user to enter a number in a box.
#When they click on a button it will add that number to a total and display it in another box. This can be repeated as many times as they want and
#keep adding to the total. There should be another button that resets the total back to 0 and empties the original text box, ready for them to start again.
from tkinter import *

def click():
   
    number = int(text_box.get())
    answer = text_box2["text"]
    answer = int(answer)
    total = number + answer
    text_box2["text"] = total
    

def reset():
    total = 0
    text_box2["text"] = 0
    enter_txt.delete(0,END)
    enter_txt.focus()



window = Tk()
window.title("Counting and Reset")
window.geometry("500x200")

label = Label(text = "Enter a number: ")
label.place(x = 30, y = 20)

text_box = Entry(text = 0)
text_box.place(x = 150, y = 20, width = 200, height = 25)
text_box["justify"] = "center"
text_box.focus()

button = Button(text='Press me', command = click)
button.place(x = 30, y = 50, width = 120, height = 25)

text_box2 = Message(text=0)
text_box2.place(x = 150, y = 50, width = 200, height = 25)
text_box2["bg"] = "white"
text_box2["relief"] = "sunken"

clear_btn = Button(text = "clear", command = reset)
clear_btn.place(x= 300, y = 50, width = 50, height = 25)

window.mainloop()




