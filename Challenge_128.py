#128 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres.
#Using these figures, make a program that will allow the user to convert between miles and kilometres.
from tkinter import*

def click():
    
    km = float(miles_box.get())
    miles = str(round(km / 1.6093,2))
    output_box["justify"] = "center"
    output_box["fg"] = "red"
    output_box["text"] = miles

window = Tk()
window.geometry("400x400")
window.title('Convert Miles to Kilometers')


label = Label(text = "Enter Miles: ")
label.place(x = 30, y = 20)
miles_box = Entry(text = 0)
miles_box.place(x = 120, y = 20)

lable_km = Label(text = "Kilometers: ")
lable_km.place(x = 30, y = 100)
output_box = Message(text = 0)
output_box.place(x = 120, y = 100, width = 200, height = 25 )

button = Button(text = 'Convert', command = click)
button.place(x = 30, y = 150)

window.mainloop()
