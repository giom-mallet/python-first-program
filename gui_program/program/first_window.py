from tkinter import *

## Instrospection in Pyth
window = Tk()

def km_to_miles() :
    txt=""
    try:
        km = float(e1_value.get())
        miles = km*1.6
        txt="{} km is {} miles".format(km, miles)
    except:
       txt="You must input a number"

    print(txt)
    t1.delete(1.0, END)
    t1.insert(END, txt)

button=Button(window, text="Hello World!", command=km_to_miles)
button.grid(row=0,column=0,rowspan=1,columnspan=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1,columnspan=2)

t1=Text(window, height=2, width=20)
t1.grid(row=1,column=0,columnspan=3)

window.mainloop()