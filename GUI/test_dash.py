import customtkinter as ctk



# Daschboard
app = ctk.CTk()
app.title("Lernportal Dashboard")
app.geometry("800x600")

y_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#333", width=app.winfo_screenwidth() // 6, height=app.winfo_screenheight())
y_frame.pack(fill="y", side="left", pady=10)

x_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#333", width=app.winfo_screenwidth()- (app.winfo_screenwidth() // 6), height=app.winfo_screenheight())
x_frame.pack(pady=10, padx=10)

app.mainloop()