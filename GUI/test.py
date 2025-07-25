import customtkinter

app = customtkinter.CTk()
app.overrideredirect(True)
app.geometry("400x300+200+200")

entry = customtkinter.CTkEntry(app)
entry.pack(pady=20)
entry.focus_set()

app.mainloop()
