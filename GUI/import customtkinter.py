import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Oben")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Ganz unten")
label2.grid(row=1, column=0, sticky="s")

# Die obere Zeile darf wachsen
root.rowconfigure(0, weight=1)

root.mainloop()