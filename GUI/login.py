import customtkinter as ctk


def start_move(event):
    app.x = event.x
    app.y = event.y

def do_move(event):
    x = app.winfo_x() - app.x + event.x
    y = app.winfo_y() - app.y + event.y
    app.geometry(f"+{x}+{y}")

# login.py
# This script creates a custom login window using customtkinter.
# It includes a title bar, username and password fields, and buttons for login and account creation.

# Initialize the customtkinter application

app = ctk.CTk()
app.geometry("400x300")
app.title("Login Window")
app.overrideredirect(True)  # Remove window decorations
app.after(10, lambda: app.focus_force())  # Set focus to the window
app.attributes("-topmost", True)  # Keep the window on top
app.attributes("-alpha", 0.95)  # Set transparency
app.resizable(False, False)  # Disable resizing
app.geometry("700x500")  # Set initial size

# Create a custom title bar
over_frame = ctk.CTkFrame(app, corner_radius=0, bg_color="black",fg_color="#111", height=30)
over_frame.pack(fill="x", side="top")
app_title = ctk.CTkLabel(over_frame, text="Login", bg_color="#111", text_color="white", font=("Arial", 16))
app_title.pack(side="left", padx=10)
close_button = ctk.CTkButton(over_frame, text="X", command=app.destroy, width=30, height=30, fg_color="red", corner_radius=3, hover_color="darkred")
close_button.pack(side="right", padx=5, pady=5)
scale_button = ctk.CTkButton(over_frame, text="◻", command=lambda: ctk.set_window_scaling(2), width=30, height=30, corner_radius=3)
scale_button.pack(side="right", pady=5)

over_frame.bind("<Button-1>", start_move)
over_frame.bind("<B1-Motion>", do_move)
app_title.bind("<Button-1>", start_move)
app_title.bind("<B1-Motion>", do_move)

longin_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#333", width=600, height=600)
longin_frame.pack(expand=True, padx=20, pady=20)

welcome_label = ctk.CTkLabel(longin_frame, text="Welcome to the Login Page", text_color="white", font=("Arial", 30))
welcome_label.pack( padx=20, pady=20)
userpasswoert_frame = ctk.CTkFrame(longin_frame, corner_radius=20, fg_color="#333", width=400, height=200)
userpasswoert_frame.pack(expand=True, padx=20, pady=20)
username_label = ctk.CTkLabel(userpasswoert_frame, text="Username:", text_color="white", font=("Arial", 20))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = ctk.CTkEntry(userpasswoert_frame, width=200, height=30, corner_radius=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label = ctk.CTkLabel(userpasswoert_frame, text="Password:", text_color="white", font=("Arial", 20))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = ctk.CTkEntry(userpasswoert_frame, width=200, height=30, corner_radius=10, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
#passwort vergessen button
forgot_password_button = ctk.CTkButton(userpasswoert_frame, text="Forgot Password?", command=lambda: print("Forgot Password clicked"), text_color="#19C", fg_color="#333")
forgot_password_button.grid(row=2, columnspan=2, sticky="e")
login_button = ctk.CTkButton(longin_frame, text="Login", command=lambda: print("Login clicked"), width=100, height=40, corner_radius=10)
login_button.pack( fill="x", padx=20)
# frame for create an account
create_account_frame = ctk.CTkFrame(longin_frame, fg_color="#333")
create_account_frame.pack(expand=True)
#create account label
create_account_label = ctk.CTkLabel(create_account_frame, text="Noch keinen Account?", text_color="white", font=("Arial", 13))
create_account_label.grid(row=0, column=0, pady=10)
#create a creste account button
create_account_button = ctk.CTkButton(create_account_frame, text="Neue Account", command=lambda: print("Create Account clicked"), fg_color="#333", text_color="#19C")
create_account_button.grid(row=0, column=1)


app.mainloop()