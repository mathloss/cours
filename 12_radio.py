from tkinter import *
from PIL import ImageTk, ImageTk


root = Tk()
root.title("Radio button")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")

# r= IntVar()
# r.set("2")

def clicked(value):
    mylabel  =Label(root, text= value)
    mylabel.pack()

# on crée une liste
MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

# mylabel  =Label(root, text= pizza.get())
# mylabel.pack()

mybutton = Button(root, text="click", command=lambda:clicked(pizza.get()))
mybutton.pack()
root.mainloop()