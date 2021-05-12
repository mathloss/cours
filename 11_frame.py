from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")

global label

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b1 = Button(frame, text="Clic", command=quit)
b2 = Button(frame, text="Clic2")
label = Label(frame, text="")
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)


root.mainloop()