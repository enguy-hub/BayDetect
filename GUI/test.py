import tkinter as tk

r = tk.Tk()


var = tk.StringVar()

e = tk.Entry(r, width=60, font=20, borderwidth=5, textvariable=var)
e.insert(0, '...')
e.configure(state='normal')
e.grid(row=0, column=0)

b = tk.Button(text="text here")
b.grid(row=1)


def capture(*args):
    if e.get() == "open":
        b['state'] = 'normal'
    else:
        b['state'] = 'disabled'


var.trace('w', capture)


r.mainloop()
