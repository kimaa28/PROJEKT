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
        self.path = "passlib.json"
        self.passlib = load_passwort(self.path)
        self.passwort_list = ["123456","password", "123456789","12345678","12345", "1234567", "admin","qwerty","abc123","password1", "111111", "123123", "000000", "iloveyou", "welcome", "monkey","dragon","sunshine","letmein", "football", "princess", "login", "passw0rd", "master", "hello", "freedom","whatever","qazwsx", "trustno1","starwars"]
    
   

    
        self._variables()
        self.neue_frame = ctk.CTkFrame(self.app, fg_color=self.app.cget("fg_color"))
        self.neue_frame.pack(pady=20, padx=20, expand= True)
        self.register = create_register_frame(self.neue_frame, self.uservar, self.passvar,self.second_pass, self.emailvar, self.sexvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]), self._registrierung)
        self.reset = create_reset_frame(self.neue_frame, self.uservar, self.passvar,self.second_pass, self.emailvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]), lambda: self._choice_frame(self.register["register_frame"]), lambda: print("already checked"), lambda: print("hello darliun"))
        self.login = create_login_frame(self.neue_frame, self.uservar, self.passvar,lambda: self._choice_frame(self.reset["reset_frame"]),lambda: self._choice_frame(self.register["register_frame"]), self._lo)        
        
        self._set_frame()

        self.app.mainloop()

    def _variables(self):
        # all my variables
        self.uservar = ctk.StringVar()
        self.passvar = ctk.StringVar()
        self.second_pass = ctk.StringVar()
        self.emailvar = ctk.StringVar()
        self.sexvar = ctk.StringVar()
        self.secret_code = ctk.StringVar()
        
    # switch the window
    def _choice_frame(self, frame):
        frame.tkraise()
    def _set_frame(self):
        for frame in (self.register["register_frame"], self.reset["reset_frame"], self.login["login_frame"]):
            frame.grid(row=0, column=0, sticky="nsew")

    # check the login values   
    def _lo(self):
        self.login["bar"].start()
        self.app.after(5000, self._check_login )
    def _check_login(self):
            uservar = self.uservar.get()
            passvar = self.passvar.get()
            self.login["bar"].stop()

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

    #check the register value and register
    def _registrierung(self):
        self.register["bar"].start()
        self.app.after(5000, self._register_check)
    def _register_check(self):
        # set al variable for checking
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        emailvar = self.emailvar.get()
        sexvar = self.sexvar.get()
        secret_codevar = self.secret_code.get()

        self.register["bar"].stop()
        if not all([uservar, passvar, emailvar, sexvar, secret_codevar]):
            self.register["raise_msg"].configure(text="Füllen alle Felder aus", text_color="red")
        elif len(uservar) < 3:
            self.register["raise_msg"].configure(text="Username zu kurz", text_color="red")
        elif uservar in self.passlib:
            self.register["raise_msg"].configure(text="Username bereit existiert", text_color="red")
        else:
            for key in self.passlib:
                if emailvar == key["email"] or  all(["@", "."]) not in emailvar:
                    self.register["raise_msg"].configure(text="Email beriet vergeben oder ungültig", text_color="red")
                elif len(passvar) < 5 or passvar in self.passwort_list:
                    self.register["raise_msg"].configure(text="Passwort zu kurz oder unsicher", text_color="red")
                elif passvar != second_pass:
                    self.register["raise_msg"].configure(text="Passwort unterschiedlich", text_color="red")

                else:
                    self.passlib[uservar] = {"passwort": hashed_passwort(passvar), "email": emailvar, "sex": sexvar, "secret_code": hashed_passwort(secret_codevar)}
                    save_passwort(self.path, self.passlib)
                    self.register["raise_msg"].configure(text="Erfolgreich registriert", text_color="red")

            
        

        


    
      
        
        



    
    

hauptpage()
