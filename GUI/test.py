from tkinter import *

def set_text(text):
    e.delete(0,END)
    e.insert(0,text)
    return

win = Tk()

e = Entry(win,width=10)
e.pack()

b1 = Button(win,text="animal",command=lambda:set_text("animal"))
b1.pack()

b2 = Button(win,text="plant",command=lambda:set_text("plant"))
b2.pack()

win.mainloop()