from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()
root.title("Database")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("350x600")

# creation de la fonction effacer données
def delete():
    # connection a une database
    conn = sqlite3.connect('C:/Users/eriol/Desktop/gui_tkinter/ressources/address_book.db')
    # creation du curseur
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())  
    delete_box.delete(0,END)


    # ajoute les modifications
    conn.commit()
    # On ferme la connection 
    conn.close()


def submit():

    # connection a une database
    conn = sqlite3.connect('C:/Users/eriol/Desktop/gui_tkinter/ressources/address_book.db')
    # creation du curseur
    c = conn.cursor()

    # on insert les données dans la table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
        {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    # ajoute les modifications
    conn.commit()
    # On ferme la connection
    conn.close()

    #on nettoie les text
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    # connection a une database
    conn = sqlite3.connect('C:/Users/eriol/Desktop/gui_tkinter/ressources/address_book.db')
    # creation du curseur
    c = conn.cursor()
    
    # query? la db!
    c.execute("SELECT *,oid FROM addresses")
    records =c.fetchall()    # fetchall prends tout, fetchone un et fetchmany(unnombre): le nombre de...
    # print(records)
 
    print_records = ""
    for record in records:
        print_records += str(record[1]) + " " + str(record[0]) + " " + "\t" + str(record[-1]) + "\n"  # si on fait str(record[0]) on aura que les noms
       
    query_label= Label(root,text=print_records)    
    query_label.grid(row=12, column=0, columnspan=2)

    # ajoute les modifications
    conn.commit()
    # On ferme la connection
    conn.close()


# Creation des textBox
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10,0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width =30)
delete_box.grid(row=9, column=1, pady=5)

# creation des labels
first_name_label = Label(root, text="First name")
first_name_label.grid(row=0, column=0, pady=(10,0))
last_name_label = Label(root, text="Last name")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text=" Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)

# creation du bouton submit
button_submit = Button(root,text="Submit", command=submit)
button_submit.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=139)

# query button afficher les donnees de la db
query_button= Button(root, text="Afficher", command=query)
query_button.grid(row=11,column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# creation du bouton delete
delete_button = Button(root, text= "Effacer", command=delete)
delete_button.grid(row=10,column=0, columnspan=2, padx=10, pady=10, ipadx=139)

quit_button = Button(root, text="Quitter", command=quit)
quit_button.grid(row=13,column=0, columnspan=2, padx=10, pady=10, ipadx=139)


root.mainloop()
