from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("New_window")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("Le Pinou")
    top.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/photo.ico")
    #label = Label(top, text="Hello world").pack()
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/ressources/pinou.png"))
    my_label = Label(top, image= my_img).pack()
    btn3 = Button(top, text="Close window)", command=top.destroy).pack()
    

btn = Button(root, text="Open 2nd Window", command=open).pack()
btn2 = Button(root,text="Quit", command=quit).pack()

mainloop()