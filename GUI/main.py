import customtkinter as ctk
import hashlib, os, json
from login import create_login_frame
from register import create_register_frame
from reset import create_reset_frame 
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageDraw
import random as rd
import webbrowser as web
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk

# funktion to hashed the password
def hashed_passwort(passwort):
    return hashlib.blake2b(passwort.encode(), digest_size=32).hexdigest()
# create the json file
def load_passwort(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, "r") as datei:
        return json.load(datei)
# save the json file    
def save_passwort(pfad, passwort):
    with open(pfad, "w") as datei:
        json.dump(passwort, datei, indent=4)

user = None
count = 0

class Main:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Main")
        self.path = "../daten/Passlib.json"
        self.passlib = load_passwort(self.path)
        self.low_passwort_list = ["123456","password", "123456789","12345678","12345", "1234567", "admin","qwerty","abc123","password1", "111111", "123123", "000000", "iloveyou", "welcome", "monkey","dragon","sunshine","letmein", "football", "princess", "login", "passw0rd", "master", "hello", "freedom","whatever","qazwsx", "trustno1","starwars"]
        self.color = ("white", "black")


        self._variables()
        # frame who take my login, register and reset frame (first frame to be show)
        self.neue_frame = ctk.CTkFrame(self.app, fg_color=self.app.cget("fg_color"))
        self.neue_frame.pack(fill="both", expand="true")
        # if the login info are true then the daschboard can be show 
        self.daschboar = ctk.CTkFrame(self.app, fg_color=self.color, corner_radius=0)
             
        # create all login, register and reset frame and set the first to be show
        self.register = create_register_frame(self.neue_frame, self.uservar, self.passvar, self.second_pass, self.emailvar, self.sexvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]) or self.app.title("Main"), self._registrierung)
        self.reset = create_reset_frame(self.neue_frame, self.uservar, self.passvar, self.second_pass, self.emailvar, self.secret_code, lambda: self._choice_frame(self.login["login_frame"]) or self.app.title("Main"), lambda: self._choice_frame(self.register["register_frame"]) or self.app.title("Register"), self._reset, self._load_check)
        self.login = create_login_frame(self.neue_frame, self.uservar, self.passvar,lambda: self._choice_frame(self.reset["reset_frame"]) or self.app.title("Reset passwort"),lambda: self._choice_frame(self.register["register_frame"]) or self.app.title("Register"), self._lo)        
      
        # set funktion enable to grid all frame
        self._set_frame()
        

    
        self.app.mainloop()

   

    #funkttion to create all my user variables
    def _variables(self):
        self.uservar = ctk.StringVar() 
        self.passvar = ctk.StringVar()
        self.second_pass = ctk.StringVar()
        self.emailvar = ctk.StringVar()
        self.sexvar = ctk.StringVar()
        self.secret_code = ctk.StringVar()
        
    # switch into the three frame
    def _choice_frame(self, frame):
        frame.tkraise()
    # set the default frame and grid it
    def _set_frame(self):
        for frame in (self.register["register_frame"], self.reset["reset_frame"], self.login["login_frame"]):
            frame.grid(row=0, column=0, sticky="nsew")


    # delete all entry after the the click on button to secure the prozess 
    def _delete_entry(self, liste):     
        for entry in liste:
            entry.delete(0, "end") 

    # login frame waiting time for answer
    def _lo(self):
        self.login["raise_msg"].configure(text="")
        self.login["bar"].start()
        self.app.after(2000, self._check_login )
        

 
    # funtion for checking the loging information
    def _check_login(self):
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        self.login["bar"].stop()
        self.liste_l = [self.login["user_entry"], self.login["passwort_entry"]]
     
        if not uservar :
            self.login["raise_msg"].configure(text="Username darf nicht leer sein", text_color="red")
            self._delete_entry(self.liste_l)
        elif uservar in self.passlib:
            if not passvar:
                self.login["raise_msg"].configure(text="Passwort darf nicht leer sein", text_color="red")
                self._delete_entry(self.liste_l)
            elif hashed_passwort(passvar) == self.passlib[uservar]["passwort"]:
                self.login["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
                global user, count
                user = uservar
                count = 1
                self.neue_frame.pack_forget()
                self.app.geometry("500x500")
                self.neue = App(self.app, bg_color="blue", fg_color="#111", )
                self.neue.pack(expand="true", fill="both")
                
                
            else:
                self.login["raise_msg"].configure(text="Ungültige Eingabe", text_color="red")
                self._delete_entry(self.liste_l)
        else:
            self.login["raise_msg"].configure(text="Username falsch", text_color="red")
            self._delete_entry(self.liste_l)

    # delete the register info if one of them false or has already been allocated

    #check the register value and register if all are corect
    def _registrierung(self):
        self.register["bar"].start()
        self.app.after(5000, self._register_check)
        
    def _register_check(self):
        # set all variable for checking
        self.liste_R = [self.register["user_entry"], self.register["passwort_entry"], self.register["passwort_w"], self.register["email_entry"], self.register["secret_code"]]
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        emailvar = self.emailvar.get()
        sexvar = self.sexvar.get()
        secret_codevar = self.secret_code.get()
        self.value = []
        for value in self.passlib.values():
            self.value.append(value["email"])
        

        self.register["bar"].stop()
        if not all([uservar, passvar, emailvar, sexvar, secret_codevar]):
            self.register["raise_msg"].configure(text="Füllen alle Felder aus", text_color="red")
            self._delete_entry(self.liste_R)
        elif len(uservar) < 4:
            self.register["raise_msg"].configure(text="Username zu kurz", text_color="red")
            self._delete_entry(self.liste_R)
        elif uservar in self.passlib:
            self.register["raise_msg"].configure(text="Username bereit vergeben", text_color="red")
            self._delete_entry(self.liste_R)
        else:
            if emailvar in self.value  or not ("@" in emailvar or "." in emailvar):
                self.register["raise_msg"].configure(text="Email bereit vergeben oder ungültig", text_color="red")
                self._delete_entry(self.liste_R)
                
            elif len(passvar) < 5 or passvar in self.low_passwort_list:
                self.register["raise_msg"].configure(text="Passwort zu kurz oder unsicher", text_color="red")
                self._delete_entry(self.liste_R)
            elif passvar != second_pass:
                self.register["raise_msg"].configure(text="Passwort unterschiedlich", text_color="red")
                self._delete_entry(self.liste_R)
            else:
                self.passlib[uservar] = {"passwort": hashed_passwort(passvar), "email": emailvar, "sex": sexvar, "secret_code": hashed_passwort(secret_codevar)}
                save_passwort(self.path, self.passlib)
                self.register["raise_msg"].configure(text="Erfolgreich registriert", text_color="green")
                self._delete_entry(self.liste_R)
        
    # delete entry if somethings wrong

    # funktion for resetting the users informations TODO: after that i learn APi i would create an automatic mail sender so that, if the users his info complet forget the can always reset it
    def _reset(self):
        self.reset["raise_msg"].configure(text="")
        self.reset["bar"].start()
        self.app.after(2000, self._reset_check)
    def _reset_check(self):
        self.liste_r = [self.reset["username"], self.reset["neue_passwort"], self.reset["passwort_w"], self.reset["email"], self.reset["secret_code"]]
        bar = self.reset["bar"]
        uservar = self.uservar.get()
        emailvar = self.emailvar.get()
        secret_codevar = self.secret_code.get()
        raise_msg = self.reset["raise_msg"]
        bar.stop()
        if not all([uservar, emailvar, secret_codevar]):
            raise_msg.configure(text="Füllen alle Felder aus", text_color="red")
            self._delete_entry(self.liste_r)
        else:
            try:
                if emailvar == self.passlib[uservar]["email"] and hashed_passwort(secret_codevar) == self.passlib[uservar]["secret_code"]:
                    raise_msg.configure(text="Jetzt können sie den neuen passwort eingeben", text_color="green")
                    self.reset["reset"].configure(state="normal")
                    self.reset["check"].configure(state="disabled") 
                    
            except:
                raise_msg.configure(text="Ungültige Eingabe", text_color="red")
                self._delete_entry(self.liste_r)
            
     # reset the informations if the secret code username and email correct else await       
    def _load_check(self):
        bar = self.reset["bar"]
        bar.start()
        self.app.after(3000, self._check_passwort)
    def _check_passwort(self):
        bar = self.reset["bar"]
        bar.stop()
        uservar = self.uservar.get()    
        raise_msg = self.reset["raise_msg"]
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        
        if not passvar :
            raise_msg.configure(text="Prüfen Sie zuerst ihre Informationen", text_color="red")
            self._delete_entry(self.liste_r)
        elif passvar != second_pass or len(passvar) < 8 or passvar in self.low_passwort_list:
            raise_msg.configure(text="passwort unterschiedlich oder zu schwach", text_color="red")
            self._delete_entry(self.liste_r)
        else:
            self.passlib[uservar]["passwort"] = hashed_passwort(passvar)
            save_passwort(self.path, self.passlib)
            raise_msg.configure(text="Passwort erfolgreich  geändert", text_color="green")
            self._delete_entry(self.liste_r)



class App(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._define_frame_width()
        self._create_dash_frames()
        
    def _define_frame_width(self):
        self.w = self.winfo_width()
        self.lwidth = self.w / 4 
        self.rwidth = self.w - self.lwidth
        
    def _create_dash_frames(self):
        self.right_frame = ctk.CTkFrame(self, width=self.rwidth, corner_radius=30, fg_color="#C1B98F", bg_color="#BAB1B1")   
        self.right_frame.pack(fill="y", expand="true")
        self.left_frame = ctk.CTkFrame(self, width=self.lwidth, corner_radius=30, border_width=2, bg_color="#BAB1B1", fg_color="#C1B98F")
        self.left_frame.pack(fill="y", expand="true")
                


if __name__== "__main__":           
    Main()
 
   

