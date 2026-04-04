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

class Daschbord(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args
        self._create_dash_frame()
        self._create_resume_widget()
    
    
    def _create_dash_frame(self):
        self.titel_frame = ctk.CTkFrame(self, fg_color="red", height=100)
        self.titel_frame.pack(fill="x")    
        ctk.CTkLabel(self.titel_frame, text="Welcome back Jordan", text_color="black", font=("Inter", 30, "bold")).pack(anchor="w", padx=30, pady=(25, 10))
        ctk.CTkLabel(self.titel_frame, text="Here is what's happening in your workspace today.", text_color="#5B5B5B", font=("Inter", 20, "bold")).pack(anchor="w", padx=30, pady=5 )
        self.resume_frame = ctk.CTkFrame(self, fg_color="blue")
        self.resume_frame.pack(fill="both", expand="true")
        self.stat_bar = ctk.CTkFrame(self, fg_color="green", height=400)
        self.stat_bar.pack(fill="x")
    def _create_resume_widget(self):
        self.resume_frame.grid_columnconfigure(0, weight=1)
        self.resume_frame.grid_columnconfigure(1, weight=1)
        self.resume_frame.grid_columnconfigure(2, weight=1)
        self.resume_frame.grid_rowconfigure(0, weight=1)
        self.resume_frame.grid_rowconfigure(1, weight=1)
        
        self.inspi_frame = ctk.CTkFrame(self.resume_frame, fg_color="black", corner_radius=20, border_color="white", border_width=2)
        self.inspi_frame.grid(row=0, column=0, rowspan=2, padx=20, pady=30, sticky="nsew")
        self.ranking_frame = ctk.CTkFrame(self.resume_frame, fg_color="yellow", corner_radius=10, border_color="white", border_width=2)
        self.ranking_frame.grid(row=0, column=1, sticky="nsew", pady=(20, 10), padx=20)
        self.unknow = ctk.CTkFrame(self.resume_frame, fg_color="yellow", corner_radius=10, border_color="white", border_width=2)
        self.unknow.grid(row=1, column=1, sticky="nsew", pady=(10, 20), padx=20)
        self.last_course_frame = ctk.CTkFrame(self.resume_frame, fg_color="black", corner_radius=20, border_color="white", border_width=2)
        self.last_course_frame.grid(row=0, column=2, rowspan=2, padx=20, pady=30, sticky="nsew")
        
        
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        x = np.linspace(0, 10, 100)
        ax.bar(x, np.sin(x))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        canvas = FigureCanvasTkAgg(fig, master=self.stat_bar)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)