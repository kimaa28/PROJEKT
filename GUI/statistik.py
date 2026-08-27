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
        self._progress_header()
        self._create_overview()
        self._create_details_progress()
    
    def _stat_frame(self):
        self.header_frame = ctk.CTkFrame(self, corner_radius=2)
        self.header_frame.pack(fill="x")
        
        self.stat_overview_frame = ctk.CTkFrame(self, corner_radius=2, fg_color="blue")
        self.stat_overview_frame.pack(fill="x")
        
        self.detail_progress_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="red")
        self.detail_progress_frame.pack(fill="both", expand="true")
        

    def _progress_header(self):
        self.list = ["May18 - May28", "April1 - April30"]
        self.list1 = ["All courses", "just any", "just progra"]
        ctk.CTkLabel(self.header_frame, text="Progress", font=("Inter", 25, "bold"), text_color="black").grid(row=0, column=0, sticky="w", padx=20, pady=(20, 0))
        ctk.CTkLabel(self.header_frame, text="Track your learning PRogress and how far you've come", text_color="#5D5757", font=("verdana", 15)).grid(row=1, column=0, sticky="nw", padx=20, pady=(0, 20))
        self.progress_per_month = ctk.CTkOptionMenu(self.header_frame, values=self.list, dropdown_fg_color="white", text_color="black", fg_color="white")
        self.progress_per_month.grid(row=1, column=1, sticky="ne", pady=(0, 20))
        self.show_courses = ctk.CTkOptionMenu(self.header_frame, text_color="black", values=self.list1, dropdown_fg_color="white", fg_color="white", text_color_disabled="black", dropdown_text_color="black", dropdown_hover_color="#CA9C9C")
        self.show_courses.grid(row=1, column=2, sticky="ne", padx=20, pady=(0, 20))
        self.header_frame.columnconfigure(1, weight=1)
        
    def _create_overview(self):
        
       
        self.overall_frame = ctk.CTkFrame(self.stat_overview_frame, fg_color="#E9E7E7", corner_radius=15)
        self.overall_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.completed_lesson = ctk.CTkFrame(self.stat_overview_frame, fg_color="#E9E7E7", corner_radius=15)
        self.completed_lesson.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.study_time = ctk.CTkFrame(self.stat_overview_frame, fg_color="#E9E7E7", corner_radius=15)
        self.study_time.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
        self.streak = ctk.CTkFrame(self.stat_overview_frame, fg_color="#E9E7E7", corner_radius=15)
        self.streak.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")
        
        self.int = [i for i in range(4)]
        list(map(lambda a: self.stat_overview_frame.columnconfigure(a, weight=1), self.int))
        self.stat_overview_frame.rowconfigure(0, weight=1)
        self.my_dict = {
            "Overall Progress": [self.overall_frame, 'image/plholder.png', "68%", "Keep it up! You're doing great.", "blue"],
            "Completed Lessons": [self.completed_lesson, 'image/plholder.png', "48", "Out of 70 Lessons", "black"],
            "Study time": [self.study_time, 'image/plholder.png', "32h 45m", "+5h 20m this week", "blue"],
            "Streak": [self.streak, 'image/plholder.png', "12 Days", "Best: 21 Days", "blue"]
        }
        
        list(map(lambda item: ctk.CTkLabel(item[1][0], text="", image=ctk.CTkImage(light_image=Image.open(item[1][1]), size=(70, 70))).grid(row=0, column=0, padx=(20, 0), pady=20, rowspan=2, sticky="nw"), self.my_dict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[0], font=("verdana", 15, "bold"), text_color="black").grid(row=0, column=1, sticky="w", pady=(20, 0), padx=20), self.my_dict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[1][2], font=("verdana", 25, "bold"), text_color=item[1][-1]).grid(row=1, column=1, sticky="w", padx=20), self.my_dict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[1][3], font=("verdana", 10), text_color="#393939").grid(row=2, column=1, sticky="w", pady=(0, 20), padx=20), self.my_dict.items()))


    def _create_details_progress(self):
        self.progress_bar = ctk.CTkFrame(self.detail_progress_frame, fg_color="#E9E7E7", corner_radius=15)
        self.progress_bar.grid(row=0, column=0, sticky="nsew", padx=(20,10), pady=(20,10))
        
        self.progress_by_courses = ctk.CTkFrame(self.detail_progress_frame, fg_color="#E9E7E7", corner_radius=15)
        self.progress_by_courses.grid(row=0, column=1, sticky="nsew", padx=(10,20), pady=(20,10))
                
        self.recent_activity = ctk.CTkFrame(self.detail_progress_frame, fg_color="#E9E7E7", corner_radius=15)
        self.recent_activity.grid(row=1, column=0, sticky="nsew", padx=(20,10), pady=(10,20))
                        
        self.streng_improvement = ctk.CTkFrame(self.detail_progress_frame, fg_color="#E9E7E7", corner_radius=15)
        self.streng_improvement.grid(row=1, column=1, sticky="nsew", padx=(10,20), pady=(10,20))
        
        
        list(map(lambda a: self.detail_progress_frame.rowconfigure(a, weight=1), [0, 1]))
        list(map(lambda a: self.detail_progress_frame.columnconfigure(a, weight=1), [0, 1]))
