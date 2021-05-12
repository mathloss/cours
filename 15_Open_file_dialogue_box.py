from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root= Tk()
root.title("Open File dialogue box")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")

"""
root.filename = filedialog.askopenfilename(initialdir = "C:/Users/eriol/Desktop/gui_tkinter/ressources", title = "Select a file", filetypes= (("png files", "*.png"),("all files", "*.*")))# pour tous les fichier ("allfiles", "*.*"")

# affiche l'addresse du fichier my_label = Label(root, text= root.filename).pack()
my_img = ImageTk.PhotoImage(Image.open(root.filename))
my_img_label = Label(image=my_img).pack()
"""
def open_file():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir = "C:/Users/eriol/Desktop/gui_tkinter/ressources", title = "Select a file", filetypes= (("png files", "*.png"),("all files", "*.*")))# pour tous les fichier ("allfiles", "*.*"")

    # affiche l'addresse du fichier my_label = Label(root, text= root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img).pack()


button2 = Button(root, text="Open file", command=open_file).pack()
button= Button(root, text="Quit", command=quit).pack()


root.mainloop()