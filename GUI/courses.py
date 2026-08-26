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
from ImageRounder import rounded_image


class Courses(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args  
        self._courses_frames()
        self._title_management()
        self._create_last_courses_frame()
        self._create_my_courses()
        
        
        
    def _courses_frames(self):
        self.search_var = ctk.StringVar()
        self.titel_frame = ctk.CTkFrame(self, height=150, fg_color="#97AEB7")
        self.titel_frame.pack(fill="x")
        self.just_description = ctk.CTkFrame(self, fg_color="#97AEB7")
        self.just_description.pack(fill="x", pady=(0, 25))
        
        self.courses_frames = ctk.CTkFrame(self, height=150, fg_color="red", corner_radius=50, border_color="white", border_width=2)
        self.courses_frames.pack(fill="both", expand="true")

    def _title_management(self):
        ctk.CTkLabel(self.titel_frame, text="Courses", font=("Inter", 30, "bold"), text_color="black").pack(anchor="w", side="left", padx=20, pady=(20, 0))
        ctk.CTkLabel(self.just_description, text="Manage your learning journey and track your progress", text_color="#3B3B3B").pack(side="left", anchor="w", padx=20)
        
        self.add_courses = ctk.CTkButton(self.titel_frame, text="New Course")
        self.add_courses.pack(anchor="e", padx=20, side="right", pady=(20, 0))
        
        self.search_courses = ctk.CTkEntry(self.titel_frame, width=175, placeholder_text="Find...", fg_color="white", border_color="#7A7777", textvariable=self.search_var, text_color="black")
        self.search_courses.pack(anchor="e", padx=20, side="right", pady=(20, 0))
        
    def _create_last_courses_frame(self):
        self.last_course_frame = ctk.CTkFrame(self.courses_frames, fg_color="#625E5E", corner_radius=15)
        self.last_course_frame.pack(fill="x", padx=20, pady=(5, 20))
        self.img_last = rounded_image('image/third.gif', "#625E5E", (120, 120))
        ctk.CTkLabel(self.last_course_frame, text="", image=self.img_last).grid(column=0, row=0, rowspan=4, sticky="w", padx=20, pady=20)
        ctk.CTkLabel(self.last_course_frame, text="Progress", fg_color="#2A7AC9", text_color="#032BAD", font=("verdana", 13, "bold"), corner_radius=15).grid(row=0, column=1, sticky="w", padx=20, pady=20)
        ctk.CTkLabel(self.last_course_frame, text="Programmierung", font=("verdana", 20, "bold"), text_color="black").grid(row=1, column=1, sticky="w", padx=20)
        ctk.CTkLabel(self.last_course_frame, text="Introduction to Funktions", font=("verdana", 13), text_color="#3B3B3B").grid(row=2, column=1, sticky="w", padx=20)
        ctk.CTkProgressBar(self.last_course_frame, width=300, progress_color="#0D68D0", orientation="horizontal").grid(row=3, column=1, sticky="w", padx=20)
        ctk.CTkLabel(self.last_course_frame, text="Last studied: Today  ·  Lesson 15 of 20", font=("verdana", 10), text_color="#3B3B3B").grid(row=4, column=1, sticky="w", padx=20)
        ctk.CTkButton(self.last_course_frame, text="Continue Learning >", text_color="white", fg_color="#0D68D0").grid(row=4, column=2, sticky="e", pady=20, padx=20)
        self.last_course_frame.columnconfigure(0, weight=0)
        self.last_course_frame.columnconfigure(1, weight=0)
        self.last_course_frame.columnconfigure(2, weight=1)



    def _create_my_courses(self):
        ctk.CTkLabel(self.courses_frames, text="My Courses", font=("Inter", 22, "bold"), text_color="black").pack(anchor="w", pady=(10, 0), padx=20)
        ctk.CTkLabel(self.courses_frames, text="", width=50, height=50, border_color="yellow", border_width=1, corner_radius=10).pack(anchor="e", padx=15, pady=0)
        self.my_courses_frame = ctk.CTkScrollableFrame(self.courses_frames, fg_color="blue", corner_radius=18)
        self.my_courses_frame.pack(fill="both", expand="true", pady=(10, 20),padx=20)
        self.my_list = ["proggra", "Mathhe", "rechner", "alodat", "forza"]
        self.mn = [i for i in range(5)]
        self.my_courses_frame.columnconfigure(0, weight=1)
        list(map(lambda a : self.my_courses_frame.rowconfigure(a, weight=1), self.mn))
        list(map(lambda frame: ctk.CTkLabel(self.my_courses_frame, height=200, border_color="yellow", border_width=1, text=frame, corner_radius=20).grid(row=self.my_list.index(frame), column=0, sticky="ew", padx=20, ipadx=20, pady=10), self.my_list))
