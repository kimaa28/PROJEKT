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
        self.path = "Passlib.json"
        self.passlib = load_passwort(self.path)
        self.passwort_list = ["123456","password", "123456789","12345678","12345", "1234567", "admin","qwerty","abc123","password1", "111111", "123123", "000000", "iloveyou", "welcome", "monkey","dragon","sunshine","letmein", "football", "princess", "login", "passw0rd", "master", "hello", "freedom","whatever","qazwsx", "trustno1","starwars"]
    
   

    
        self._variables()
        self.neue_frame = ctk.CTkFrame(self.app, fg_color=self.app.cget("fg_color"))
        self.neue_frame.pack(pady=20, padx=20, expand= True)
        self.register = create_register_frame(self.neue_frame, self.uservar, self.passvar,self.second_pass, self.emailvar, self.sexvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]), self._registrierung)
        self.reset = create_reset_frame(self.neue_frame, self.uservar, self.passvar, self.second_pass, self.emailvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]), lambda: self._choice_frame(self.register["register_frame"]), self._reset, self._load_check)
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
    def _delete_L(self):
        user_entry = self.login["user_entry"]
        passwort_entry = self.login["passwort_entry"]
        for entry in [user_entry, passwort_entry]:
            entry.delete(0, "end") # TODO: eventuel die deletefunktion in einer klasse bauen, sodass ich es nicht 100% mal definiere
    def _lo(self):
        self.login["raise_msg"].configure(text="")
        self.login["bar"].start()
        self.app.after(5000, self._check_login )
        
    def _check_login(self):
            uservar = self.uservar.get()
            passvar = self.passvar.get()
            self.login["bar"].stop()

            
            if not uservar :
                self.login["raise_msg"].configure(text="Username darf nicht leer sein", text_color="red")
                self._delete_L()
            elif uservar in self.passlib:
                if not passvar:
                    self.login["raise_msg"].configure(text="Passwort darf nicht leer sein", text_color="red")
                    self._delete_L()
                elif hashed_passwort(passvar) == self.passlib[uservar]["passwort"]:
                    self.login["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
                    self._delete_L()
                else:
                    self.login["raise_msg"].configure(text="Ungültige Eingabe", text_color="red")
                    self._delete_L()
            else:
                self.login["raise_msg"].configure(text="Username falsch", text_color="red")
                self._delete_L()
    def _delete_R(self):
        user_entry =self.register["user_entry"]
        passwort_entry = self.register["passwort_entry"]
        passwort_w = self.register["passwort_w"]
        email_entry = self.register["email_entry"]
        secret_code = self.register["secret_code"]
        for entry in [user_entry, passwort_entry, passwort_w, email_entry, secret_code]:
            entry.delete(0, "end")

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
        for value in self.passlib.values():
            self.value = value["email"]

        self.register["bar"].stop()
        if not all([uservar, passvar, emailvar, sexvar, secret_codevar]):
            self.register["raise_msg"].configure(text="Füllen alle Felder aus", text_color="red")
            self._delete_R()
        elif len(uservar) < 4:
            self.register["raise_msg"].configure(text="Username zu kurz", text_color="red")
            self._delete_R()
        elif uservar in self.passlib:
            self.register["raise_msg"].configure(text="Username bereit existiert", text_color="red")
            self._delete_R()
        else:
            if emailvar in self.value  or not ("@" in emailvar or "." in emailvar):
                self.register["raise_msg"].configure(text="Email bereit vergeben oder ungültig", text_color="red")
                self._delete_R()
                
            elif len(passvar) < 5 or passvar in self.passwort_list:
                self.register["raise_msg"].configure(text="Passwort zu kurz oder unsicher", text_color="red")
                self._delete_R()
            elif passvar != second_pass:
                self.register["raise_msg"].configure(text="Passwort unterschiedlich", text_color="red")
                self._delete_R()

            else:
                self.passlib[uservar] = {"passwort": hashed_passwort(passvar), "email": emailvar, "sex": sexvar, "secret_code": hashed_passwort(secret_codevar)}
                save_passwort(self.path, self.passlib)
                self.register["raise_msg"].configure(text="Erfolgreich registriert", text_color="green")
                self._delete_R()
        
        
    def _delete_re(self):
        user_entry = self.reset["username"]
        passwort_entry = self.reset["neue_passwort_entry"]
        passwort_w = self.reset["passwort_w"]
        email_entry = self.reset["email"]
        secret_entry = self.reset["secret_code"]
        for entry  in [user_entry, passwort_entry, passwort_w, secret_entry, email_entry]:
            entry.delete(0, "end")



    def _reset(self):
        self.reset["raise_msg"].configure(text="")
        self.reset["bar"].start()
        self.app.after(2000, self._reset_check)
    def _reset_check(self):
        bar = self.reset["bar"]
        uservar = self.uservar.get()
        emailvar = self.emailvar.get()
        secret_codevar = self.secret_code.get()
        raise_msg = self.reset["raise_msg"]
        bar.stop()
        if not all([uservar, emailvar, secret_codevar]):
            raise_msg.configure(text="Füllen alle Felder aus", text_color="red")
            self._delete_re()
        elif emailvar != self.passlib[uservar]["email"] or hashed_passwort(secret_codevar) != self.passlib[uservar]["secret_code"]:
            raise_msg.configure(text="Ungültige Eingabe", text_color="red")
            self._delete_re()
        else:
            raise_msg.configure(text="Jetzt können sie den neuen passwort eingeben", text_color="green")
            self.reset["reset"].configure(state="normal")
            self.reset["check"].configure(state="disabled")
            self._delete_re()
            
    def _load_check(self):
        bar = self.reset["bar"]
        bar.start()
        self.app.after(3000, self._check_passwort)
    def _check_passwort(self):
        bar = self.reset["bar"]
        bar.stop()
        user_entry = self.reset["username"]
        email_entry = self.reset["email"]
        secret_entry = self.reset["secret_code"]
        uservar = self.uservar.get()
        neue_entry = self.reset["neue_passwort"]
        passwort_w = self.reset["passwort_w"]
        raise_msg = self.reset["raise_msg"]
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        
        if not passvar :
            raise_msg.configure(text="Prüfen Sie zuerst ihre Informationen", text_color="red")
            self._delete_re()
        elif passvar != second_pass or len(passvar) < 8 or passvar in self.passwort_list :
            raise_msg.configure(text="passwort unterschiedlich or zu schwach", text_color="red")
            self._delete_re()
        else:
            self.passlib[uservar]["passwort"] = hashed_passwort(passvar)
            save_passwort(self.path, self.passlib)
            raise_msg.configure(text="Passwort erfolgreich  geändert", text_color="green")
            self._delete_re()
    
      
        
        



    
    

hauptpage()
