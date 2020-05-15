from tkinter import *

## Instrospection in Pyth
window = Tk()

button=Button(window, text="Hello World!")
button.grid(row=0,column=0,rowspan=1,columnspan=1)

e1=Entry(window)
e1.grid(row=0,column=1,columnspan=2)

t1=Text(window)
t1.grid(row=1,column=0,columnspan=3)

window.mainloop()