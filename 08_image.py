from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title ("My personal Image viewer")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/photo.ico")

# On choisit l'image voulue
my_img = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/ressources/pinou.png"))
# on la met dans un label
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root,text="Quit", command=root.quit)
button_quit.pack()

root.mainloop()


