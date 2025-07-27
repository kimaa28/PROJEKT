from asyncio import run
import customtkinter as ctk
import time

def lo():
    frame["raise_msg"].configure(text="")

    if len(uservar.get()) > 2:
        frame["bar"].start()  # Starte den Ladebalken

        def check_user():
            frame["bar"].stop()  # Stoppe den Ladebalken
            if uservar.get() == "lolo":
                frame["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
            else:
                frame["raise_msg"].configure(text="Benutzername falsch", text_color="red")

        app.after(5000, check_user)  # Führe die Prüfung nach 5 Sekunden aus


        


def create_login_frame(parent, uservar, passvar, forgot, neue_account, check_passwort):
    login_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color="#333", width=600, height=600)

    welcome_label = ctk.CTkLabel(login_frame, text="Welcome to the Login Page", text_color="white", font=("Arial", 30))
    welcome_label.pack(padx=20, pady=20)

    userpasswort_frame = ctk.CTkFrame(login_frame, corner_radius=20, fg_color="#333", width=400, height=200)
    userpasswort_frame.pack(expand=True, padx=20, pady=20)

    username_label = ctk.CTkLabel(userpasswort_frame, text="Username:", text_color="white", font=("Arial", 20))
    username_label.grid(row=0, column=0, padx=10, pady=10)

    username_entry = ctk.CTkEntry(userpasswort_frame, width=200, height=30, corner_radius=10, textvariable=uservar)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = ctk.CTkLabel(userpasswort_frame, text="Password:", text_color="white", font=("Arial", 20))
    password_label.grid(row=1, column=0, padx=10, pady=10)

    password_entry = ctk.CTkEntry(userpasswort_frame, width=200, height=30, corner_radius=10, show="*", textvariable=passvar)
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    #raise msg label
    raise_msg_label = ctk.CTkLabel(userpasswort_frame, text="", font=("Arial", 10))
    raise_msg_label.grid(row=2, column=1, sticky="e", padx=10)
    #forget passwort button
    forgot_password_button = ctk.CTkButton(userpasswort_frame, text="Forgot Password", command= forgot, text_color="#19C", fg_color="#333")
    forgot_password_button.grid(row=3, columnspan=2, sticky="e", padx=10)

    bar = ctk.CTkProgressBar(userpasswort_frame, orientation="horizontal", mode="determinate", determinate_speed=2, progress_color="#ABC", width=200, height=3)
    bar.grid(row=4, column=0, padx=10)

    login_button = ctk.CTkButton(login_frame, text="Login", command= check_passwort, width=100, height=40, corner_radius=10)
    login_button.pack(fill="x", padx=20)

    create_account_frame = ctk.CTkFrame(login_frame, fg_color="#333")
    create_account_frame.pack(expand=True)

    create_account_label = ctk.CTkLabel(create_account_frame, text="Noch keinen Account?", text_color="white", font=("Arial", 13))
    create_account_label.grid(row=0, column=0, pady=10)

    create_account_button = ctk.CTkButton(create_account_frame, text="Neue Account", command= neue_account, fg_color="#333", text_color="#19C")
    create_account_button.grid(row=0, column=1)

    return {
        "login_frame": login_frame, 
        "register_button": create_account_button,
        "raise_msg": raise_msg_label, 
        "user_entry": username_entry,
        "passwort_entry": password_entry, 
        "bar": bar

    }

 


    
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Login Window")
    app.geometry("800x600")
    uservar = ctk.StringVar()
    passvar = ctk.StringVar()
    frame = create_login_frame(app, uservar, passvar, lambda:  print("hello"), lambda: print("hi"), lo)
    frame["login_frame"].pack(expand=True, padx=20, pady=20)
   
    
    
    app.mainloop()
