import customtkinter as ctk
import hashlib, os, json
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageTk, ImageDraw
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
        self.preferences = ctk.CTkFrame(self.profil_frame, fg_color="green", corner_radius=20, height=250)
        self.preferences.pack(fill="x", padx=(40, 20), pady=20)
        
        ctk.CTkLabel(self.profil_frame, text="Privacy and security", text_color="black", font=("Inter", 17, "bold")).pack(padx=40, pady=20, anchor="w")
        self.privacy = ctk.CTkFrame(self.profil_frame, fg_color="green", corner_radius=20, height=250)
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
         
        frame2 = ctk.CTkFrame(self.my_profile_frame, fg_color="#D8D8D8", border_width=1, border_color="#747474")
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