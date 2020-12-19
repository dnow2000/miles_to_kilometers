from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.configure(padx=20, pady=40)

label = Label(text="Is equal to: ")
label.grid(column=1, row=3, padx=(5, 20))

entry = Entry(width=15)
entry.grid(column=2, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=2, padx=(15, 0))

km_answer_label = Label(text="0")
km_answer_label.grid(column=2, row=3, padx=(15, 0))

km_label = Label(text="Km")
km_label.grid(column=3, row=3)


def calculate():
    result = int(entry.get()) * 1.609344
    km_answer_label.config(text=str(round(result, 2)))


button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=4, padx=(10, 0))

window.mainloop()
