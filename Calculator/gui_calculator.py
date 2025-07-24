#!python3
#GUI_Calculator.py

import tkinter as tk

# Callback function to handle button clicks

def click(value):
    current = entry_var.get()
    if value == "=":
        try:
            result = eval(current)
            entry_var.set(result)

        except:
            entry_var.set("Error")

    elif value == "C":
        entry_var.set("")

    else:
        entry_var.set(current + value)


# Create the main window

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("300x500")

# Display where the expression is shown

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable = entry_var, font = ("Arial",20), bd = 10, insertwidth = 2, width = 14)
entry.grid(row = 0, column = 0, columnspan = 4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
    ]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
         tk.Button(
            root,
            text=btn,
            padx=20,
            pady=20,
            font=("Arial", 14),
            command=lambda v=btn: click(v)
        ).grid(row=i + 1, column=j)

root.mainloop()
