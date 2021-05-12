from tkinter import *
# import nécessaires pour les images:
from PIL import ImageTk, Image

# Amelioration du code de la calculatrice
# Fait par Mathloss
# 2021


root = Tk()
# root.iconbitmap('C:/Users/eriol/Desktop/gui_tkinter/ressources/math.ico')
root.title("Calculatrice")

e = Entry(root, width=35,borderwidth=5, fg="green", bg ="black")
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

# fonction d'afichage des chiffres
def button_click(number):
    # e.delete(0,END)
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

#fonction de calcul + - X / et +/-
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_opposite():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    if f_num > 0:
        e.insert(0, '-')
    else:
        e.delete(0, 1)

# Fonction égal qui fait le calcul suivant une variable global math
def button_equal():
    second_number= e.get()
    e.delete(0, END)
    if math ==  "addition":
        if (f_num + float(second_number)) - int(f_num + float(second_number)) == 0:
            e.insert(0, int(f_num + float(second_number)))
        else :
            e.insert(0, f_num + float(second_number))
    elif math ==  "subtraction":
        if (f_num - float(second_number)) - int(f_num - float(second_number)) == 0:
            e.insert(0, int(f_num - float(second_number)))
        else :
            e.insert(0, f_num - float(second_number))
    elif math ==  "multiplication":
        if (f_num * float(second_number)) - int(f_num * float(second_number)) == 0:
            e.insert(0, int(f_num * float(second_number)))
        else :
            e.insert(0, f_num * float(second_number))
    elif math ==  "division":
        if f_num % float(second_number) == 0:
            e.insert(0, int(f_num / int(second_number)))
        else:
            e.insert(0, f_num / float(second_number))

# fonction nettoyage écran
def button_clear():
    e.delete(0, END)

# Les boutons de nombres
button_1 = Button(root, text="1", padx= 40, pady= 20, command=lambda: button_click(1), fg="green", bg ="black")
button_2 = Button(root, text="2", padx= 40, pady= 20, command=lambda: button_click(2), fg="green", bg ="black")
button_3 = Button(root, text="3", padx= 40, pady= 20, command=lambda: button_click(3), fg="green", bg ="black")
button_4 = Button(root, text="4", padx= 40, pady= 20, command=lambda: button_click(4), fg="green", bg ="black")
button_5 = Button(root, text="5", padx= 40, pady= 20, command=lambda: button_click(5), fg="green", bg ="black")
button_6 = Button(root, text="6", padx= 40, pady= 20, command=lambda: button_click(6), fg="green", bg ="black")
button_7 = Button(root, text="7", padx= 40, pady= 20, command=lambda: button_click(7), fg="green", bg ="black")
button_8 = Button(root, text="8", padx= 40, pady= 20, command=lambda: button_click(8), fg="green", bg ="black")
button_9 = Button(root, text="9", padx= 40, pady= 20, command=lambda: button_click(9), fg="green", bg ="black")
button_0 = Button(root, text="0", padx= 40, pady= 20, command=lambda: button_click(0), fg="green", bg ="black")

# boutons de calculs
button_add = Button(root, text="+", padx= 39, pady= 20, command=button_add, fg="green", bg ="black")
button_subtract = Button(root, text="-", padx= 41, pady= 20, command=button_subtract, fg="green", bg ="black")
button_multiply = Button(root, text="X", padx= 40, pady= 20, command=button_multiply, fg="green", bg ="black")
button_divide = Button(root, text="/", padx= 40, pady= 20, command=button_divide, fg="green", bg ="black")
button_equal = Button(root, text="=", padx= 40, pady= 20, command=button_equal, fg="green", bg ="black")
button_opposite = Button(root, text="-/+", padx=34 , pady= 20, command=button_opposite, fg="green", bg ="black")
button_dot = Button(root, text=".", padx=40 , pady= 20, command=lambda: button_click("."), fg="green", bg ="black")
# bouton de nettoyage écran
button_clear = Button(root, text="Clear", padx= 30, pady= 20, command=button_clear, fg="green", bg ="black")

# mettre les bouton a l'ecran
# Les boutons de nombres
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)

# boutons de calculs
button_add.grid(row=4,column=0)
button_subtract.grid(row=4,column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_equal.grid(row=6,column=2)
button_opposite.grid(row=5, column=2)
button_dot.grid(row=6,column=1)

# bouton de nettoyage écran
button_clear.grid(row=6,column=0) 

# lancement du gui
root.mainloop() 