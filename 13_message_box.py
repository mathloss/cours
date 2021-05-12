from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root= Tk()
root.title("Message_box")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/photo.ico")

""" messagebox : showinfo retourne ok
                 showwarning retourne ok
                 showerror retourne ok
                 askquestion retourne yes ou no
                 askokcancel retourne 0 ou 1
                 askyesno retoune 0 ou 1
                 """

def popup():
    # tout au debut le type de message puis (en 1er le nom du popup , 2eme le message)
    response  = messagebox.askyesno("this is my popup", "HELLO TUTTI!!")
    # l'icone du message et le son du signal changent
    # label = Label(root, text=response) .pack()
    if response == 1:
        label = Label(root, text="You say yes") .pack()
    else:
        label = Label(root, text="You say no") .pack()


button= Button(root,text="Popup", command=popup).pack()
button2 = Button(root, text="Quit", command=quit).pack()
root.mainloop()