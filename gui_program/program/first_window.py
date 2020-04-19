from tkinter import *

window = Tk()

button=Button(window, text="Hello World!")
button.grid(row=1,column=1,rowspan=2,columnspan=2)

window.mainloop()