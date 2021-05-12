from tkinter import *

root = Tk()

# on crée un widget
myLabel = Label(root, text= "Hello!!")

#on envoie le widget sur l'écran
myLabel.pack()

root.mainloop()