from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("New_window")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("400x400")

#variation avec le slider 

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack() 
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=400, to=200)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()



button = Button(root, text="Clic ! ", command=slide).pack()
mainloop()