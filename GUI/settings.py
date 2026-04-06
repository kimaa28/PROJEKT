import customtkinter as ctk
import hashlib, os, json
from tkinter import PhotoImage, Canvas, simpledialog
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo
import webbrowser as web
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class Settings(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args 
        self._settings_frame()
        self._profil_widget()
        self._myprofile()
        self._preferences()
        self._privacy()
        
        
    def _settings_frame(self):         
        self.titel_frame = ctk.CTkFrame(self, fg_color="#97AEB7", border_width=0, corner_radius=0, border_color="black")
        self.titel_frame.pack(fill="x", padx=0, pady=0)
        
        ctk.CTkLabel(self.titel_frame, text="Settings", font=("Inter", 30, "bold"), text_color="#569C4E").pack(anchor="w", padx=40, pady=(45, 20))
        ctk.CTkLabel(self.titel_frame, text="Manage your account preferences and app settings.", font=("Inter", 20), text_color="#515151").pack(side="left", anchor="n", padx=40, pady=(0, 60))  
        
        self.profil_frame = ctk.CTkScrollableFrame(self, fg_color="#97AEB7", border_width=0, corner_radius=0,scrollbar_button_color="#97AEB7", scrollbar_button_hover_color="#0B630E")
        self.profil_frame.pack(fill="both", expand="true", padx=0, pady=0)
        
    def _profil_widget(self):
        ctk.CTkLabel(self.profil_frame, text="My Profile", text_color="#111111", font=("Inter", 17, "bold")).pack(anchor="w", padx=40, pady=20)
        self.my_profile_frame = ctk.CTkFrame(self.profil_frame, fg_color=self.titel_frame.cget("fg_color"), corner_radius=20, height=250)
        self.my_profile_frame.pack(fill="x", padx=(40, 20), pady=20)
    
        ctk.CTkLabel(self.profil_frame, text="Preferences", text_color="black", font=("Inter", 17, "bold")).pack(padx=40, pady=20, anchor="w")
        self.preferences = ctk.CTkFrame(self.profil_frame, fg_color=self.profil_frame.cget("fg_color"), corner_radius=20, height=250)
        self.preferences.pack(fill="x", padx=(40, 20), pady=20)
        
        ctk.CTkLabel(self.profil_frame, text="Privacy and security", text_color="red", font=("Inter", 17, "bold")).pack(padx=40, pady=20, anchor="w")
        self.privacy = ctk.CTkFrame(self.profil_frame, fg_color=self.profil_frame.cget("fg_color"), corner_radius=20, height=250, border_width=4)
        self.privacy.pack(fill="x", padx=(40, 20), pady=20)
        
    def _myprofile(self):
        self.my_profile_frame.rowconfigure(0, weight=1)
        self.my_profile_frame.rowconfigure(1, weight=1)
        self.my_profile_frame.rowconfigure(2, weight=1)
        self.my_profile_frame.columnconfigure(0, weight=1)
        
        frame1 = ctk.CTkFrame(self.my_profile_frame, fg_color="#D0D0D0", border_width=1, border_color="#5A5A5A")
        frame1.grid(row=0, column=0, sticky="nsew")
        
        img = Image.open('image/third.gif').resize((80,80))
        new_img = Image.new("RGBA", img.size, frame1.cget("fg_color"))
        mask = Image.new("L", (80,80), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 80, 80), fill=255, outline=True)
        new_img.paste(img, (0,0), mask)
        self.tk_img = ImageTk.PhotoImage(new_img)
        
        self.profil_img = tk.Label(frame1, image=self.tk_img, border=0, highlightthickness=0)
        self.profil_img.pack(padx=15, pady=15, side="left")
        
        self.btn_chg_img = ctk.CTkButton(frame1, text="Change Avatar", text_color="black",font=("Inter", 16), fg_color=frame1.cget("fg_color"), corner_radius=10, hover_color="green", hover=True, command=lambda: showinfo(title="Info", message="action noch nich verfügbar"), border_color="#535353", border_width=1, )
        self.btn_chg_img.pack(padx=20, side="right")
        
        self.user_name = ctk.CTkLabel(frame1, text="Jordan Kimaa", text_color="black", font=("Inter", 17, "bold"))
        self.user_name.pack(anchor="nw", padx=5, pady=(25, 0))
        
        self.user_status = ctk.CTkLabel(frame1, text="Administrator ๏ kimaa@gmail.com", text_color="#696969", font=("Inter", 15), anchor="w")
        self.user_status.pack(anchor="sw", padx=5, pady=(0, 20))
         
        frame2 = ctk.CTkFrame(self.my_profile_frame, fg_color="#C4C4C4", border_width=1, border_color="#747474")
        frame2.grid(row=1, column=0, sticky="nsew")
        
        ctk.CTkLabel(frame2, text="Display Name", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 10), padx=15)
        ctk.CTkLabel(frame2, text="This is how your name will appear in the app.", text_color="#464646", font=("Inter", 15)).pack(side="left", padx=15, pady=(0, 20))

        self.displ_name_btn = ctk.CTkButton(frame2, text="Save", text_color="black", fg_color="green", hover_color="#75D07D")
        self.displ_name_btn.pack(side="right", padx=20, pady=(0, 20), ipady=5)
        
        self.d_name = ctk.StringVar() 
        self.displ_name_entry = ctk.CTkEntry(frame2, textvariable=self.d_name,text_color="black", width=200, fg_color="#D4D4D4", border_width=1)
        self.displ_name_entry.pack(side="right", padx=0, pady=(0, 20))
        
        
        frame3 = ctk.CTkFrame(self.my_profile_frame, fg_color="#C4C4C4", border_width=1, border_color="#5D5D5D")
        frame3.grid(row=2, column=0, sticky="nsew")
        
        ctk.CTkLabel(frame3, text="Email Address", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 10), padx=20)
        ctk.CTkLabel(frame3, text="Used for login, Notifications and exchange with Others", text_color="#646363", font=("Inter", 15)).pack(side="left", padx=20, pady=(0, 25))
        
        self.email_btn = ctk.CTkButton(frame3, text="Save", text_color="black", fg_color="green", hover_color="#75D07D")
        self.email_btn.pack(side="right", padx=20, pady=(0, 20), ipady=5)
        
        self.email_var = ctk.StringVar() 
        self.email_entry = ctk.CTkEntry(frame3, textvariable=self.email_var,text_color="black", width=200, fg_color="#D4D4D4", border_width=1)
        self.email_entry.pack(side="right", padx=0, pady=(0, 20))
        
    def _preferences(self):
        self.preferences.rowconfigure(0, weight=1)
        self.preferences.rowconfigure(1, weight=1)
        self.preferences.rowconfigure(2, weight=1)
        self.preferences.columnconfigure(0, weight=1)
        frame1 = ctk.CTkFrame(self.preferences, fg_color="#D0D0D0", border_width=1, border_color="#5A5A5A")
        frame1.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(frame1, text="Daily study reminder", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20)
        ctk.CTkLabel(frame1, text="Receive a notifications at 9:00 AM you haven't studied yet.", text_color="#646363", font=("Inter", 15)).pack(side="left", padx=20, pady=(0, 25))
        
        self.reminder = ctk.IntVar()
        self.reminder_swt = ctk.CTkSwitch(frame1, corner_radius=20,text="", onvalue=1, offvalue=0, variable=self.reminder, command=lambda: print(self.reminder.get()), switch_height=25, switch_width=50, progress_color="green", button_color="white", width=50)
        self.reminder_swt.pack(side="right", padx=17, pady=(0, 20))

        frame2 = ctk.CTkFrame(self.preferences, fg_color="#D0D0D0", border_width=1, border_color="#5A5A5A")
        frame2.grid(row=1, column=0, sticky="nsew")
        
        ctk.CTkLabel(frame2, text="Visibility", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20)
        ctk.CTkLabel(frame2, text="This determines whether your name will be visible to other users and whether you can \nreceive messages from others while you're offline or online.", text_color="#646363", font=("Inter", 15), anchor="w", justify="left").pack(side="left", padx=20, pady=(0, 25))
        
        self.online = ctk.StringVar(value="no")
        self.online_swt = ctk.CTkSwitch(frame2, corner_radius=20, text="online", text_color="black", onvalue="yes", offvalue="no", variable=self.online, command=lambda: print(self.online.get()), switch_height=25, switch_width=50, progress_color="green", button_color="white", width=50)
        self.online_swt.pack(side="right", padx=17, pady=(0, 20))
        
        self.offline = ctk.StringVar(value="no")
        self.offline_swt = ctk.CTkSwitch(frame2, corner_radius=20, text="offline", text_color="black", onvalue="yes", offvalue="no", variable=self.offline, command=lambda: print(self.online.get()), switch_height=25, switch_width=50, progress_color="green", button_color="white", width=50)
        self.offline_swt.pack(side="right", padx=17, pady=(0, 20))
        
        frame3 = ctk.CTkFrame(self.preferences, fg_color="#D0D0D0", border_width=1, border_color="#5A5A5A")
        frame3.grid(row=2, column=0, sticky="nsew")
        
        ctk.CTkLabel(frame3, text="Theme color", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20)
        ctk.CTkLabel(frame3, text="Select your prefered accent color for the interface", text_color="#646363", font=("Inter", 15), anchor="w", justify="left").pack(side="left", padx=20, pady=(0, 25))
        
       
        self.color = ctk.StringVar(value="green") # in json 
        self.color_btn = ctk.CTkSegmentedButton(frame3, corner_radius=20, values=["green", "red", "brown", "yellow", "blue"], variable=self.color, fg_color= frame3.cget("fg_color"), selected_color="green", selected_hover_color="#C0C8BF", command= lambda a: self.color_btn.configure(selected_color=a))
        self.color_btn.pack(padx=20, pady=(0, 25), side="right", ipadx=5, ipady=5)

    
    def _privacy(self):
        self.privacy.rowconfigure(0, weight=1)
        self.privacy.rowconfigure(1, weight=1)
        self.privacy.rowconfigure(2, weight=1)
        self.privacy.columnconfigure(0, weight=1)
        
        frame1 = ctk.CTkFrame(self.privacy, fg_color="#E7C7C7", border_width=1, border_color="#C92525")
        frame1.grid(row=0, column=0, sticky="nsew", pady=(1,0), padx=1)
        
        ctk.CTkLabel(frame1, text="Export Data", text_color="black", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20)
        ctk.CTkLabel(frame1, text="Download all your flashcard and progress history.", text_color="#646363", font=("Inter", 15), anchor="w", justify="left").pack(side="left", padx=20, pady=(0, 25))

        self.export_data = ctk.CTkButton(frame1, text="Export Json", text_color="black", font=("Inter", 17), fg_color=frame1.cget("fg_color"),border_width=1, border_color="#7E7B7B", hover_color="#C2B196", image=ctk.CTkImage(light_image=Image.open('./image/import.png'), size=(20, 20)))
        self.export_data.pack(side="right", padx=20, pady=(0, 25), ipadx=2, ipady=3)
        
        frame2 = ctk.CTkFrame(self.privacy, fg_color="#E7C7C7", border_width=1, border_color="#C92525")
        frame2.grid(row=1, column=0, sticky="nsew", pady=(1,0), padx=1)
        
        ctk.CTkLabel(frame2, text="Change Passwort", text_color="red", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20)
        ctk.CTkLabel(frame2, text="This action will permanetly change your passwort.", text_color="#646363", font=("Inter", 15), anchor="w", justify="left").pack(side="left", padx=20, pady=(0, 25))
        
        self.chg_pass = ctk.CTkButton(frame2, text="Change passwort", text_color="red", fg_color=frame2.cget("fg_color"), hover_color="#C2B196", border_color="red", border_width=1, command=self.ask_chg)
        self.chg_pass.pack(side="right", padx=20, pady=(0, 25), ipadx=5, ipady=5)
        
        ctk.CTkButton(frame2, text="Forgot passwort ?", text_color="#4F4F4F", font=("Inter", 15, "underline"), fg_color=frame2.cget("fg_color"), hover_color=self.chg_pass.cget("hover_color"), command=lambda: showinfo("Was?", "Und wie hast du dich den angemeldet ? ", icon='question')).pack(side="right", padx=0, pady=(0, 25))

        frame3 = ctk.CTkFrame(self.privacy, fg_color="#E7C7C7", border_width=1, border_color="#C92525")
        frame3.grid(row=2, column=0, sticky="nsew", pady=(0,1), padx=1)
        
        ctk.CTkLabel(frame3, text="Delete", text_color="red", font=("Inter", 17, "bold")).pack(anchor="w", pady=(20, 0), padx=20) # blocked account
        ctk.CTkLabel(frame3, text="Permanently remove your account and all data. This cannot be undone.", text_color="#646363", font=("Inter", 15), anchor="w", justify="left").pack(side="left", padx=20, pady=(0, 25))
        

        self.del_account_btn = ctk.CTkButton(frame3, text="Delete Account", font=("inter", 16), text_color="red", fg_color=frame3.cget("fg_color"),  hover_color="#C2B196",border_color="red", border_width=1, command=self.ask_del)
        self.del_account_btn.pack(side="right", padx=20, pady=(0, 25), ipadx=5, ipady=5) # progressbar to wait untill all will load
        
    def ask_del(self):
        answer = messagebox.askyesno("Frage", "willst du fortfahren?")
        print(answer)
        
    def ask_chg(self):
        change = simpledialog.askstring("Passwort", "Gibt dein passwort ein", show="*")  
        print(change)