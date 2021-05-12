from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()
root.title("Database")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("400x400")

# créons une database

conn = sqlite3.connect('C:/Users/eriol/Desktop/gui_tkinter/ressources/address_book.db')

# on crée un curseur qui va bosser pour nous

c = conn.cursor()

# Creation de la table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name,
    address text,
    city text,
    State text,
    zipcode integer
)""")

# ajoute les modifications
conn.commit()

# On ferme la connection
conn.close()

root.mainloop()