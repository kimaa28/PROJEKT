import customtkinter as ctk
from login import create_login_frame
from register import create_register_frame
from reset import create_reset_frame 
import hashlib, os, json

def hashed_passwort(passwort):
    return hashlib.blake2b(passwort.encode(), digest_size=32).hexdigest()

def load_passwort(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, "r") as datei:
        return json.load(datei)
    
def save_passwort(pfad, passwort):
    with open(pfad, "w") as datei:
        json.dump(passwort, datei, indent=4)

class hauptpage:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("hauptpage")
        self.app.geometry = ("800x400")
        self.gehashed_passwort = hashed_passwort("1234")
        self.load_passwort = load_passwort("passlib.json")
        self.save_passwort = save_passwort("passlib.json", self.gehashed_passwort)
        
        
        self.neue_frame = ctk.CTkFrame(self.app, width=500, height=400)
        self.neue_frame.pack(expand=True, padx=20, pady=50)
        
        self.register_frame = create_register_frame(self.neue_frame)
        self.register_frame.grid(row=0, column=0, sticky="nsew")
        self.login_frame = create_login_frame(self.neue_frame)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.reset = create_reset_frame(self.neue_frame, lambda: print("erfolgreich gespeichert"))
        self.reset["reset_frame"].grid(row=0, column=0, sticky="nsew")
        
        self.app.mainloop()
    

hauptpage()
