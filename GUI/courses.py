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
from tkinter import filedialog
import fitz 


class Courses(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args  
        self._courses_frames()
    def _courses_frames(self):
        self.titel_frame = ctk.CTkFrame(self, height=150, fg_color="blue", corner_radius=20, border_color="red", border_width=2)
        self.titel_frame.pack(fill="x")
        
        self.courdes_frames = ctk.CTkFrame(self, height=150, fg_color="red", corner_radius=50, border_color="white", border_width=2)
        self.courdes_frames.pack(fill="both", expand="true")
        self.flip_frame = ctk.CTkFrame(self.courdes_frames, fg_color="red", corner_radius=20, border_color="white", border_width=2, width=50, height=50)
        self.flip_frame.pack(anchor="e", padx=10, pady=10)

