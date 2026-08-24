import customtkinter as ctk
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageTk, ImageDraw
from tkinter.messagebox import showerror, showwarning, showinfo
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import datetime as dt

class Dashboard(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.args = args
        self._create_dashboard_frame()
        self._create_summary_widgets()
        self._create_statistics_widget()
        self._create_inspiration_widget()
    
    
    def _create_dashboard_frame(self):
        self.title_frame = ctk.CTkFrame(self, fg_color="#97AEB7", height=100)
        self.title_frame.pack(fill="x")    
        
        ctk.CTkLabel(self.title_frame, text=f"Welcome back {dt.date.today()}", text_color="black", font=("Inter", 30, "bold")).pack(anchor="w", padx=30, pady=(30, 10))
        ctk.CTkLabel(self.title_frame, text="Here is what's happening in your workspace today.", text_color="#5B5B5B", font=("Inter", 20, "bold")).pack(anchor="w", padx=30, pady=(5, 25) )
        
        self.summary_frame = ctk.CTkFrame(self, fg_color="#97AEB7")
        self.summary_frame.pack(fill="both", expand="true")
        
        self.stat_bar = ctk.CTkFrame(self, fg_color="#97AEB7", height=200, corner_radius=20)
        self.stat_bar.pack(fill="x", pady=(0, 10))
        
        
    def _create_summary_widgets(self):
        self.summary_frame.grid_columnconfigure(1, weight=1)
        self.summary_frame.grid_columnconfigure(2, weight=1)
        self.summary_frame.grid_rowconfigure(0, weight=1)
        self.summary_frame.grid_rowconfigure(1, weight=1)
        
        self.inspiration_frame = ctk.CTkFrame(self.summary_frame, fg_color="#C7C7C7", corner_radius=20)
        self.inspiration_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=30, sticky="nsew")
          
        self.ranking_frame = ctk.CTkScrollableFrame(self.summary_frame, fg_color="#C7C7C7", corner_radius=10)
        self.ranking_frame.grid(row=0, column=1, sticky="nsew", pady=(20, 10), padx=10)
        
        self.messages_frame = ctk.CTkScrollableFrame(self.summary_frame, fg_color="#C7C7C7", corner_radius=10)
        self.messages_frame.grid(row=1, column=1, sticky="nsew", pady=(10, 20), padx=10)
        
        self.last_course_frame = ctk.CTkFrame(self.summary_frame, fg_color="#C7C7C7", corner_radius=20)
        self.last_course_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=30, sticky="nsew")
        
        
        
    
    
    def _create_statistics_widget(self):
        self.plot_frame = ctk.CTkFrame(self.stat_bar, corner_radius=20, fg_color="#111111")
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=0)
         
        # Matplotlib-Figur
        fig = Figure(figsize=(6, 4), dpi=100, facecolor="#111111")

        ax = fig.add_subplot(111)

        x = np.linspace(0, 50, 150)
        ax.plot(x, np.sin(x), color="#3B8ED0", linewidth=2)

        # Hintergrund des Diagramms
        ax.set_facecolor("#111111")

        # Achsen anpassen
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#AAAAAA")
        ax.spines["bottom"].set_color("#AAAAAA")

        ax.tick_params(colors="#FFFFFF")
        ax.grid(axis="y", color="#333333", alpha=0.5)

        fig.tight_layout()

        # Canvas in den abgerundeten Frame einsetzen
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()

        canvas_widget = canvas.get_tk_widget()
        canvas_widget.configure(bg="#111111", highlightthickness=0, bd=0)

        canvas_widget.pack(fill="both", expand=True, padx=10, pady=10)
        
                
            
    def _create_inspiration_widget(self):
        try:
            self._orig_inspiration_img = Image.open('./image/winston.jpg').convert("RGBA")
        except Exception:
            # fallback: create empty placeholder
            self._orig_inspiration_img = Image.new("RGBA", (100, 100), self.summary_frame.cget("fg_color"))

        # label that will hold the dynamically resized image
        self.inspiration_image = ctk.CTkLabel(self.inspiration_frame, text="")
        self.inspiration_image.pack(fill="x")

        # update image when frame is resized so it fills x and uses half the frame height
        self.inspiration_frame.bind("<Configure>", self._update_inspiration_image)

        # quote below image
        ctk.CTkLabel(
            self.inspiration_frame,
            text=("Ich weiß nicht, was ich der Welt scheinen mag, \n"
                    "aber mir selbst komme ich nur wie ein Junge vor, der am Meeresufer spielt und sich damit vergnügt, \n"
                    "ein glatteres Kieselsteinchen zu finden."),
            text_color="#808080",
            justify="center",
            font=("Inter", 16, "italic")
        ).pack(padx=10)

    def _update_inspiration_image(self, event=None):
        if not hasattr(self, "_orig_inspiration_img"):
            return

        # determine target size: full width of frame, half height of frame
        if event is not None:
            width = max(1, event.width)
            height = max(1, event.height // 2)
        else:
            width = max(1, self.inspiration_frame.winfo_width())
            height = max(1, self.inspiration_frame.winfo_height() // 2)

        try:
            resample = Image.Resampling.LANCZOS
        except Exception:
            resample = Image.LANCZOS

        img = self._orig_inspiration_img.resize((width, height), resample)

        # create rounded mask
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        radius = 25
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255, corners=[True, True, None, None ])

        # paste onto background (frame color) to avoid transparency issues
        bg = Image.new("RGBA", (width, height), self.summary_frame.cget("fg_color"))
        bg.paste(img, (0, 0), mask)

        # keep reference to avoid GC
        self._inspiration_photo = ImageTk.PhotoImage(bg)
        self.inspiration_image.configure(image=self._inspiration_photo)