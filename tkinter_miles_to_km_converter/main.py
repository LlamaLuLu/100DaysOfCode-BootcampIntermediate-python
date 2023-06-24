# 24/6/2023

from tkinter import *

def convert():
    distance = eval(entry.get())
    distance += 1.609
    result.config(text=round(distance, 1))

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# entry box
entry = Entry(width=10)
entry.grid(row=0, column=1)

# labels
miles = Label(text="miles", font=("Arial", 16))
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to", font=("Arial", 16))
is_equal_to.grid(row=1, column=0)

km = Label(text="km", font=("Arial", 16))
km.grid(row=1, column=2)

result = Label(text=0, font=("Arial", 16))
result.grid(row=1, column=1)

# button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
