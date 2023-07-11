from tkinter import *


def calculator():
    miles = float(mile_input.get())
    kms = miles * 1.689
    km_output.config(text=f"{kms}")


window = Tk()
window.title("Mile/Km Convertor")
window.minsize(width=280, height=140)
window.config(padx=40, pady=40)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

km_output = Label(text="0")
km_output.grid(column=1, row=1)
km_output.config(padx=10, pady=10)

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label1 = Label(text="is equal to")
km_label1.grid(column=0, row=1)

km_label2 = Label(text="Km")
km_label2.grid(column=2, row=1)

window.mainloop()