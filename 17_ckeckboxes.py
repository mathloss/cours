from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("New_window")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("400x400")

# retourne un integer voir 17b pour autre valeur

var=IntVar()

def update():
    my_label= Label(root, text= var.get()).pack()

c =  Checkbutton(root, text="Checkbox", variable= var)
c.pack()

button = Button(root,text="Upate", command=update).pack()
button2 = Button(root,text="Quit",command=quit).pack()

root.mainloop()