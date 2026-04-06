import customtkinter as ctk
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
from daschboard import Daschbord
from courses import Courses
from statistik import Statistics
from settings import Settings

class App(ctk.CTkFrame):
    def __init__(self, master, *agrs, **kwargs):
        super().__init__(master, **kwargs)
        self.args = agrs
        self.master = master
        self._create_app_frames()
        self._nav_widget()
        self.create_image(self.button_frame, self.image_liste)
        self._create_button(self.button_frame, self.button_list)

        
    # to separate the both principal frame one with all button and the second with all information about it   
    
    
    def choice_frame(self, frame):
        frame.tkraise()
        
         
    def _create_app_frames(self):
        
        l= self.winfo_width() / 4
        r = self.winfo_width() - l                
        self.left_frame = ctk.CTkFrame(self, bg_color="#86c0f7", fg_color="#86c0f7", width= l, corner_radius=0, border_color="#292827")   
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#97AEB7", bg_color="#97AEB7", width=r)  
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=1)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        
        self.columnconfigure(1, weight=20)
        self.rowconfigure(0, weight=1)
        
        self.o = Statistics(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.o.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.p = Courses(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.p.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.m = Daschbord(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.m.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.n = Settings(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.n.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        
        
        
        
        
    # enthält alle button für die navigation in der app    
    def _nav_widget(self):
        self.button_list = ["Dashboard", "Courses", "Progress", "Settings", "Support"]
        self.image_liste = ["image/dash.png", "image/course.png", "image/stat.png", "image/setting.png", "image/suport 1.png"]
        self.nav_frame = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.nav_frame.pack(fill="x", padx=(10, 40))
        
        ctk.CTkLabel(self.nav_frame, text="", fg_color="#1d89ee", font=("Inter", 35), corner_radius=6,  image=ctk.CTkImage(light_image=Image.open("image/brain 1.png"), size=(30, 30))).grid(row=0, column=0, sticky="w", padx=(10, 10), pady=30, ipady=5, ipadx=1)
        ctk.CTkLabel(self.nav_frame, font=("Inter", 30, "bold"), text="Lerntrack", text_color="#2C2B2B").grid(row=0, column=0, padx=(0, 10), pady=30, ipadx=0, sticky="e")
        
        self.button_frame = ctk.CTkFrame(self.nav_frame, fg_color=self.nav_frame.cget("fg_color"))
        self.button_frame.grid(row=2, column=0, pady=(00, 250), padx=(10, 30), sticky="w")
        
        ctk.CTkLabel(self.nav_frame, text="WORKSPACE", font=("Inter", 18, "normal"), text_color="#6b7280").grid(row=1, column=0, sticky="w", pady=(50, 0), padx=10)
        
    # make the fonction more global so that any other class can use it external 
    def create_image(self, master,  agrs):
        m = list(map(lambda a : ctk.CTkImage(light_image=Image.open(a), size=(25, 25)), agrs))
        list(map(lambda a : ctk.CTkLabel(master, image=a[1], text="").grid(row=a[0], column=0, padx=(0, 20), pady=20), enumerate(m)))
        
    def _create_button(self, master, liste):
        list(map(lambda a : ctk.CTkButton(master, text=a[1], text_color="white",font= ("Inter", 17), hover_color="#1687d8", command=lambda: showinfo(title='Info',message='Dieses fenster ist noch nicht bereit.') if a[0] == 4 else self.choice_frame(self.m) ).grid(row=a[0], column=1, pady=20), enumerate(liste)))

        self.test = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.test.pack(side="bottom", pady=20, padx=20, anchor="w")
        img = Image.open('image/third.gif').resize((75,75))
        new_img = Image.new("RGBA", img.size, "#86c0f7")
        mask = Image.new("L", (75,75), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, 75, 75), fill=255, outline=True, radius=10)
        new_img.paste(img, (0,0), mask)
        self.tk_img = ImageTk.PhotoImage(new_img)
        self.egal = tk.Label(self.test, image=self.tk_img, font=("Verdana", 30, "bold"), fg=self.left_frame.cget("fg_color"), borderwidth=0, text="JE suis unc on ")
        self.egal.grid(row=0, column=0)
        self.text = ctk.CTkLabel(self.test, text="Username\nName", text_color="#433F3F", font=("Inter", 20))
        self.text.grid(row=0, column=1, sticky="n")
        
        
        self.canva = Canvas(self.left_frame, width=220, height=10, bg=self.left_frame.cget("fg_color"), bd=0, borderwidth=0, highlightthickness=0)
        self.canva.create_line(10, 5, 215, 5, width=2.5, fill="#908A8A")
        self.canva.pack(side="bottom", padx=10, pady=10)
        