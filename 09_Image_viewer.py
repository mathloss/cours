from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title ("My personal Image viewer")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/photo.ico")

# On choisit l'image voulue
my_img_1 = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/images/image_1.jpg"))
my_img_2 = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/images/image_2.jpg"))
my_img_3 = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/images/image_3.jpg"))
my_img_4 = ImageTk.PhotoImage(Image.open("C:/Users/eriol/Desktop/gui_tkinter/images/image_4.jpg"))

# on crée une liste 
image_list = [my_img_1, my_img_2, my_img_3, my_img_4]


# on la met dans un label
my_label = Label(image = my_img_1)
my_label.grid(row=0, column=0, columnspan=3) 

def forward(image_number): 
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back= Button(root, text="<<", command=lambda:back(image_number-1))

    if image_number == 4:
        button_forward = Button(root,text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back= Button(root, text="<<", command=lambda:back(image_number-1))

    if image_number == 1:
        button_back = Button(root,text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root,text="<<", command=back, state=DISABLED)
button_quit = Button(root,text="Quitter", command=root.quit)
button_forward = Button(root,text=">>", command=lambda:forward(2))


button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)




root.mainloop()


