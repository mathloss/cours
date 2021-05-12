from tkinter import *

root = Tk()

e = Entry(root, width = 60, bg= "green", fg= "black", borderwidth = 3 )
e.pack()
e.insert(0,"enter your name here")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text="enter your name", padx = 60,pady = 60, command = myClick, fg= "white", bg = "#000000")
myButton.pack()
 

root.mainloop() 