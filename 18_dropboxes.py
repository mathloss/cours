from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("New_window")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("400x400")

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thusrday", 
    "Friday"
] 

def show():
    my_label=Label(root, text= clicked.get()).pack()


# clicked est une avraible tkinter
clicked= StringVar()
# set met une valeur par défault

"""
# si liste voir 
clicked.set("Monday") 
"""

clicked.set(options[0])

"""
# on va remplacer les options par une liste
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thusrday", "Friday" )
drop.pack()
"""
# il faut passer par unre variable , attention à *
drop = OptionMenu(root, clicked, *options)
drop.pack()

button= Button(root, text= "Show selection", command=show).pack()

button2 = Button(root,text="Quit",command=quit).pack()

root.mainloop()