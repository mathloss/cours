from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "I didi it!!")
    myLabel.pack()

myButton = Button(root, text="Clic", padx = 60,pady = 60, command = myClick, fg= "white", bg = "#000000")
myButton.pack()


root.mainloop() 