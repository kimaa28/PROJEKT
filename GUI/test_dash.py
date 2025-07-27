import customtkinter as ctk
from login import create_login_frame
from register import create_register_frame
from reset import create_reset_frame 
from login import create_login_frame
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
        self.passlib = load_passwort("passlib.json")
    
        self._variables()
        self.neue_frame = ctk.CTkFrame(self.app, fg_color=self.app.cget("fg_color"))
        self.neue_frame.pack(pady=20, padx=20, expand= True)
        self.register = create_register_frame(self.neue_frame, self.uservar, self.passvar, self.emailvar, self.sexvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]),lambda: print("hello worrld"))
        self.reset = create_reset_frame(self.neue_frame, self.uservar, self.passvar, self.emailvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]), lambda: self._choice_frame(self.register["register_frame"]), lambda: print("already checked"), lambda: print("hello darliun"))
        self.login = create_login_frame(self.neue_frame, self.uservar, self.passvar,lambda: self._choice_frame(self.reset["reset_frame"]),lambda: self._choice_frame(self.register["register_frame"]), self._check_login)        
        
        self._set_frame()

        self.app.mainloop()

    def _variables(self):
        self.uservar = ctk.StringVar()
        self.passvar = ctk.StringVar()
        self.emailvar = ctk.StringVar()
        self.sexvar = ctk.StringVar()
        self.secret_code = ctk.StringVar()

    def _choice_frame(self, frame):
        frame.tkraise()

    def _set_frame(self):
        
        for frame in (self.register["register_frame"], self.reset["reset_frame"], self.login["login_frame"]):
            frame.grid(row=0, column=0, sticky="nsew")
        
    def _lo(self):
        self.login["bar"].start()
        self.app.after(5000, self._chek )

    def _chek(self):
            self.login["bar"].stop()

    def _check_login(self):
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        if not uservar :
            self.login["raise_msg"].configure(text="Username darf nicht leer sein", text_color="red")
        elif uservar in self.passlib:
            if not passvar:
                self.login["raise_msg"].configure(text="Passwort darf nicht leer sein", text_color="red")
            elif hashed_passwort(passvar) == self.passlib[uservar]["passwort"]:
                self.login["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
            else:
                self.login["raise_msg"].configure(text="Ungültige Eingabe", text_color="red")
        else:
            self.login["raise_msg"].configure(text="Ungültige Eingabe", text_color="red")

        


    
      
        
        



    
    

hauptpage()
