from tkinter import *

root = Tk()

# on crée un widget
myLabel1 = Label(root, text= "Hello!!")
myLabel2 = Label(root, text= "A l'aide!!")
myLabel3 = Label(root, text= "Au secours!!")
myLabel4 = Label(root, text= "Fais chier!")

#on envoie le widget sur l'écran
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
myLabel3.grid(row = 0, column = 2)
myLabel4.grid(row = 2, column = 2)

root.mainloop()