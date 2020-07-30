#125 Write a program that can be used instead of rolling a six-sided die in a board game. When the user clicks a
#button it should display a random whole number between 1 to 6 (inclusive).
from tkinter import * 
import random

def Call():
    
    number = random.randint(1,6)
    msg = Label(window, text= 'Your number is '+ str(number)+' !!!')
    msg.place(x = 100, y = 50)
    msg['fg'] = "red"




window = Tk()
window.title("Dice")
window.geometry("400x400")
button = Button(text = "Press me",command = Call)
button.place(x = 100, y = 200, width = 120, height = 25)
window.mainloop()
