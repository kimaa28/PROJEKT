import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

# Container
container = ctk.CTkFrame(app)
container.pack(fill="both", expand=True)

# Zwei Frames im Container
frame1 = ctk.CTkFrame(container, fg_color="lightblue")
frame2 = ctk.CTkFrame(container, fg_color="lightgreen")

for frame in (frame1, frame2):
    frame.pack(fill="both", expand=True)

# Inhalt für Frame 1
ctk.CTkLabel(frame1, text="Dies ist Frame 1").pack(pady=20)
ctk.CTkButton(frame1, text="Zu Frame 2", command=lambda: frame2.tkraise()).pack()

# Inhalt für Frame 2
ctk.CTkLabel(frame2, text="Dies ist Frame 2").pack(pady=20)
ctk.CTkButton(frame2, text="Zu Frame 1", command=lambda: frame1.tkraise()).pack()

# Start mit Frame 1
frame1.tkraise()

app.mainloop()
