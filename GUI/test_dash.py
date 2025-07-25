import customtkinter as ctk
from login import create_login_frame


class hauptpage:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title = ("hauptpage")
        self.app.geometry = ("800x400")
   
        
        
        self.neue_frame = ctk.CTkFrame(self.app, width=500, height=400)
        self.neue_frame.pack(expand=True, padx=20, pady=50)
        self.login_frame = create_login_frame(self.neue_frame)
        self.login_frame.pack()
        self.app.mainloop()
    

hauptpage()
