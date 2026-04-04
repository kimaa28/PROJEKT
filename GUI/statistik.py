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

class Statistics(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args 
        self._stat_frame()
    
    def _stat_frame(self):
        self.overview = ctk.CTkFrame(self, corner_radius=2, border_color="red", border_width=1, height=200)
        self.overview.pack(fill="x")
        self.barAndprogress = ctk.CTkFrame(self, corner_radius=20, fg_color="red")
        self.barAndprogress.pack(fill="both", expand="true")
        self.git_stat = ctk.CTkFrame(self, corner_radius=2, border_color="red", border_width=1, height=200, fg_color="blue")
        self.git_stat.pack(fill="x")

