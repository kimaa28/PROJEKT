import customtkinter as ctk

app = ctk.CTk()

app.title("register Window")


# Create a custom title bar

register_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#333", width=600, height=600)
register_frame.pack(expand=True, padx=20, pady=20)
welcome_label = ctk.CTkLabel(register_frame, text="Welcome to the Register Page", text_color="white", font=("Arial", 35))
welcome_label.pack(padx=50, pady=20)

userpasswoert_frame = ctk.CTkFrame(register_frame, corner_radius=20, fg_color="#333")
userpasswoert_frame.pack(expand=True)
#Username field
uservar = ctk.StringVar()
uservar.set("")  # Set initial value to empty string
username_label = ctk.CTkLabel(userpasswoert_frame, text="Username:", text_color="white", font=("Arial", 20))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = ctk.CTkEntry(userpasswoert_frame, width=300, height=30, corner_radius=10, textvariable=uservar)
username_entry.grid(row=0, column=1, padx=10, pady=20)
#Password field
password_label = ctk.CTkLabel(userpasswoert_frame, text="Password:", text_color="white", font=("Arial", 20))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = ctk.CTkEntry(userpasswoert_frame, width=300, height=30, corner_radius=10, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=20)
#password wiederholen field
repeat_password_label = ctk.CTkLabel(userpasswoert_frame, text="Confirm Password:", text_color="white", font=("Arial", 20))
repeat_password_label.grid(row=2, column=0, padx=10, pady=10)
repeat_password_entry = ctk.CTkEntry(userpasswoert_frame, width=300, height=30, corner_radius=10, show="*")
repeat_password_entry.grid(row=2, column=1, padx=10, pady=20)
#email field
email_label = ctk.CTkLabel(userpasswoert_frame, text="Email:", text_color="white", font=("Arial", 20))
email_label.grid(row=3, column=0, padx=10, pady=10)
email_entry = ctk.CTkEntry(userpasswoert_frame, width=300, height=30, corner_radius=10)
email_entry.grid(row=3, column=1, padx=10, pady=20)
#sex field
sex_text = ctk.CTkLabel(userpasswoert_frame, text="Sex:", text_color="white", font=("Arial", 20))
sex_text.grid(row=4, column=0, padx=10, pady=10)
sex_combo = ctk.CTkOptionMenu(userpasswoert_frame, values=["male", "female", "other"], width=300, height=30, corner_radius=10, dropdown_font=("Arial", 20), fg_color=email_entry.cget("fg_color"))
sex_combo.grid(row=4, column=1, padx=10, pady=20)
#secret code field
secret_code_label = ctk.CTkLabel(userpasswoert_frame, text="Secret Code:", text_color="white", font=("Arial", 20))
secret_code_label.grid(row=5, column=0, padx=10, pady=10)
secret_code_entry = ctk.CTkEntry(userpasswoert_frame, width=300, height=30, corner_radius=10)
secret_code_entry.grid(row=5, column=1, padx=10, pady=20)
#sign up button
sign_up_button = ctk.CTkButton(register_frame, text="Sign Up", command=lambda: print("Sign Up clicked"), width=100, height=40, corner_radius=10)
sign_up_button.pack(fill="x", padx=20, pady=20)
# frame for already have an account
create_account_frame = ctk.CTkFrame(register_frame, fg_color="#333")
create_account_frame.pack(expand=True)
#create account label
create_account_label = ctk.CTkLabel(create_account_frame, text="Already have an account?", text_color="white", font=("Arial", 13))
create_account_label.grid(row=0, column=0, pady=10)
#create a create account button
create_account_button = ctk.CTkButton(create_account_frame, text="Login", command=lambda: print("Login clicked"), fg_color="#333", text_color="#19C")
create_account_button.grid(row=0, column=1)
neue_label = ctk.CTkLabel(app, text="je suis un con")
neue_label.pack()

if __name__ == "__main__":
    app.mainloop()