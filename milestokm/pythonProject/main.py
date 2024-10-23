from tkinter import *
import math

root = Tk()
root.title("Miles to Km Converter")
root.minsize(width=250, height=125)

label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=1)
label_miles.config(padx=20, pady=10)

entry = Entry()
entry.grid(column=1, row=1)

label_num = Label(text=" ", font=("Arial", 12))
label_num.grid(column=1, row=2)

def entry_get(event):
    number = entry.get()

    if number != '':
        number = float(entry.get())
        entry.delete(0, END)
        new_km = round((number * 1.60934), 2)

        label_num.config(text=str(new_km))
    else:
        pass



label_is_equal = Label(text="is equal to", font=("Arial", 12))
label_is_equal.grid(column=0, row=2)
label_is_equal.config(padx=15)

label_km = Label(text="KM", font=("Arial", 12))
label_km.grid(column=2, row=2)

button = Button(text="Calculate", height=1, width=10, pady=5, relief=GROOVE)
button.grid(column=1, row=3)
button.bind("<Button>", entry_get)
entry.bind("<Return>", entry_get)


root.mainloop()


