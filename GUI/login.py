import customtkinter as ctk


import customtkinter as ctk

def create_login_frame(parent, uservar, passvar):
    login_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color="#333", width=600, height=600)

    welcome_label = ctk.CTkLabel(login_frame, text="Welcome to the Login Page", text_color="white", font=("Arial", 30))
    welcome_label.pack(padx=20, pady=20)

    userpasswoert_frame = ctk.CTkFrame(login_frame, corner_radius=20, fg_color="#333", width=400, height=200)
    userpasswoert_frame.pack(expand=True, padx=20, pady=20)

    username_label = ctk.CTkLabel(userpasswoert_frame, text="Username:", text_color="white", font=("Arial", 20))
    username_label.grid(row=0, column=0, padx=10, pady=10)

    username_entry = ctk.CTkEntry(userpasswoert_frame, width=200, height=30, corner_radius=10, textvariable=uservar)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = ctk.CTkLabel(userpasswoert_frame, text="Password:", text_color="white", font=("Arial", 20))
    password_label.grid(row=1, column=0, padx=10, pady=10)

    password_entry = ctk.CTkEntry(userpasswoert_frame, width=200, height=30, corner_radius=10, show="*", textvariable=passvar)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    forgot_password_button = ctk.CTkButton(userpasswoert_frame, text="Forgot Password?", command=lambda: print("Forgo Password clicked"), text_color="#19C", fg_color="#333")
    forgot_password_button.grid(row=2, columnspan=2, sticky="e")

    login_button = ctk.CTkButton(login_frame, text="Login", command=lambda: print(uservar.get(), passvar.get()), width=100, height=40, corner_radius=10)
    login_button.pack(fill="x", padx=20)

    create_account_frame = ctk.CTkFrame(login_frame, fg_color="#333")
    create_account_frame.pack(expand=True)

    create_account_label = ctk.CTkLabel(create_account_frame, text="Noch keinen Account?", text_color="white", font=("Arial", 13))
    create_account_label.grid(row=0, column=0, pady=10)

    create_account_button = ctk.CTkButton(create_account_frame, text="Neue Account", command=lambda: print("Create Account clicked"), fg_color="#333", text_color="#19C")
    create_account_button.grid(row=0, column=1)

    return {
        "login_frame": login_frame

    }

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Login Window")
    app.geometry("800x600")
    uservar = ctk.StringVar()
    passvar = ctk.StringVar()
    frame = create_login_frame(app, uservar, passvar)
    frame["login_frame"].pack(expand=True, padx=20, pady=20)

    app.mainloop()
