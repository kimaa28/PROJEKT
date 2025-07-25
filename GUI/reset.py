import customtkinter as czk



app = czk.CTk()
app.title("Reset Password")



reset_frame = czk.CTkFrame(app, corner_radius=20, fg_color="#333", width=400, height=400)
reset_frame.pack(expand=True, padx=20, pady=20)
forgot_label = czk.CTkLabel(reset_frame, text="Reset Password", text_color="white", font=("verdana", 30))
forgot_label.pack(padx=20, pady=20)
description_label = czk.CTkLabel(reset_frame, text="Geben sie folgenden informationen, um ihren Passwort", text_color="#BBB", font=("verdana", 15))
description_label.pack(padx=20, pady=10)
second_description_label = czk.CTkLabel(reset_frame, text="zurückzusetzen", text_color="#BBB", font=("verdana", 15))
second_description_label.pack(padx=20)

# username field
email_frame = czk.CTkFrame(reset_frame, corner_radius=20, fg_color="#333")
email_frame.pack(expand=True, padx=20, pady=20)

username_label = czk.CTkLabel(email_frame, text="Username:", text_color="white", font=("Arial", 20))
username_label.grid(row=0, column=0, pady=10)
username_entry = czk.CTkEntry(email_frame, width=300, height=30, corner_radius=10)
username_entry.grid(row=0, column=1, pady=20)

#Email field

email_label = czk.CTkLabel(email_frame, text="Email:", text_color="white", font=("Arial", 20))
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = czk.CTkEntry(email_frame, width=300, height=30, corner_radius=10)
email_entry.grid(row=1, column=1, padx=10, pady=20) 

#secret code field
secret_code_label = czk.CTkLabel(email_frame, text="Secret Code:", text_color="white", font=("Arial", 20))      
secret_code_label.grid(row=2, column=0, padx=10, pady=10)
secret_code_entry = czk.CTkEntry(email_frame, width=300, height=30, corner_radius=10)
secret_code_entry.grid(row=2, column=1, padx=10, pady=20)

#button to reset password
reset_button = czk.CTkButton(reset_frame, text="Reset Password", command=lambda: print("Reset Password clicked"), width=150, height=40, corner_radius=10)   
reset_button.pack(fill="x", padx=20, pady=20) 

# frame for back to login
back_frame = czk.CTkFrame(reset_frame, fg_color="#333")
back_frame.pack(expand=True)
#back to login label
back_label = czk.CTkLabel(back_frame, text="Back to Login?", text_color="white", font=("Arial", 13))
back_label.grid(row=0, column=0, pady=10)
#back to login button
back_button = czk.CTkButton(back_frame, text="Login", command=lambda: print("Back to Login clicked"), fg_color="#333", text_color="#19C")
back_button.grid(row=0, column=1)
or_label = czk.CTkLabel(back_frame, text="or", text_color="white", font=("Arial", 13))
or_label.grid(row=0, column=2)
# registration button
registrierung_btton = czk.CTkButton(back_frame, text="Register", command=lambda: print("Register clicked"), fg_color="#333", text_color="#19C")
registrierung_btton.grid(row=0, column=3, pady=10)

app.mainloop()