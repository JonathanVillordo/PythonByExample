#132 Using the .csv file you created for the last challenge, create a program that will allow people to add names and ages
#to the list and create a button that will display the contents of the .csv file by importng it to a list box.
from tkinter import*

def clicksave():
    file = open('gaby.csv','a')

    name = ent_name.get()
    age = ent_age.get()
    new_row = name+','+ age + '\n'

    file.write(new_row)
    file.close()

    ent_name.delete(0,'end')
    ent_age.delete(0,'end')


window = Tk()
window.title("Adding Names")
window.geometry("800x500")

#Name
lbl_name = Label(text = "Enter a Name: ")
lbl_name.place(x = 30, y = 40)
ent_name = Entry(text = '')
ent_name.place(x = 150, y = 40)

#Age
lbl_age = Label(text = "Enter an Age: ")
lbl_age.place(x = 400, y = 40)
ent_age = Entry(text = '')
ent_age.place(x = 500, y = 40)

#Btn
btn_save = Button(text = 'Save', command = clicksave)
btn_save.place(x = 200, y = 90)


window.mainloop()
