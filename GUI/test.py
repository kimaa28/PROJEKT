import customtkinter as ctk
from tkinter import PhotoImage, Canvas




ctk.set_appearance_mode("light")
class Daschboard:
    def __init__(self):
        self.app = ctk.CTk()
        self.W = 21
        self.H = 25
       

       # windows widh and frame setting
        
        # left frame for Menu and info
        self.left_frame = ctk.CTkFrame(self.app, corner_radius=0, border_width=1, fg_color="#CDCDCD")
        self.left_frame.pack(fill="both", side="left")

        # right frame for all tab and specifics information 
        self.right_frame = ctk.CTkFrame(self.app, fg_color="#CDCDCD", corner_radius=0)
        self.right_frame.pack(fill="both", side="right", expand="true")
        self.color = ("black", "white")
        # letf frame menu funktion 
        self._lframe_menu()

        # app width setter
        self.app.after(100, self._set_frame_width)
        self._create_image()
        self._rframe_menu()
        self._create_canvas()
        

        self.app.mainloop()

    def _create_image(self):
        self.dash_logo = PhotoImage(file="dash_logo.png")
        self.course_logo = PhotoImage(file="course.png")
        self.profil = PhotoImage(file="profil.png")
        self.setting = PhotoImage(file="setting.png")
        self.logout = PhotoImage(file="logout.png")


    def _set_frame_width(self):
        height_app = self.app.winfo_height()
        width_app= self.app.winfo_width()
        width_l = width_app // 4
        width_r = width_app - width_l
        self.left_frame.configure(width=width_l, height=height_app)
        self.right_frame.configure(width=width_r, height=height_app)

    def _lframe_menu(self):
        self.titel_label = ctk.CTkLabel(self.left_frame, text="<> DEVLEARN", font=("PT serif", 30), text_color= self.color)
        self.titel_label.pack(padx=15, pady=30)

        # left frame  button menu
        self.lframe_one = ctk.CTkFrame(self.left_frame, fg_color= self.left_frame.cget("fg_color"))
        self.lframe_one.pack(pady=50, fill="x", padx=15)
        #dash button for dashboard tabview pov: i'm tired
        self.dash_button = ctk.CTkButton(self.lframe_one, text="Dashboard", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("dashboard cliked"), text_color= self.color)
        self.dash_button.grid(row=0, column=1, sticky="w", pady=17)
        # course button for course tabview
        self.course_button = ctk.CTkButton(self.lframe_one, text="Course", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("coursebbuttoncliked"), text_color= self.color)
        self.course_button.grid(row=1, column=1, sticky="w", pady=17)
        #profil button for profil tabview
        self.profil_button = ctk.CTkButton(self.lframe_one, text="Profil", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("profilbbuttoncliked"), text_color= self.color)
        self.profil_button.grid(row=2, column=1, sticky="w", pady=17)
        #profil button for profil tabview
        self.settings_button = ctk.CTkButton(self.lframe_one, text="settings", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("settingsbbuttoncliked"), text_color=self.color)
        self.settings_button.grid(row=3, column=1, sticky="w", pady=17)
        
        #frame for logout and profil photo
        self.lframe_two = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.lframe_two.pack(side="bottom", pady=20, padx=25, fill="x")
        # button for logout
        self.logout_button = ctk.CTkButton(self.lframe_two, text="logout", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("logoutbbuttoncliked"), text_color=self.color)
        self.logout_button.grid(row=0, column=0, sticky="e", pady=17)
        
       

    def _rframe_menu(self):
        self.tabs_menu = ctk.CTkTabview(master=self.right_frame, anchor="new", corner_radius=0)
        self.tabs_menu.pack(fill="both", expand="true")
        self.tab_1 = self.tabs_menu.add("tab-1")
        self.tab_2 = self.tabs_menu.add("tab-2")
        self.tabs_menu.set("tab-1")

        self._widget_dash()
        ctk.CTkLabel(self.right_frame, text="© 2025 by jordan kitio zangio", font=("Arial", 15), text_color= self.color).pack()

    # create all widget for my dashboard i choice the funktion this is better andmy code caan be beautifull

    def _widget_dash(self):
        # it is difficult to display some informations in a tabview so i need zu mke a firs frame who take the fill = "both" and i can normaly displaying

        self.tab1_frame = ctk.CTkFrame(self.tab_1, fg_color= self.tab_1.cget("fg_color"))
        self.tab1_frame.pack(fill="both", expand="true")

        self.welcome_label = ctk.CTkLabel(self.tab1_frame, text="Willkommen zurück, jordan!", text_color=self.color, font=("PT serif", 35))
        self.welcome_label.pack()

        # i don't really no how  i can name this frame i choice random frame it isn't a really random image we just  have 3 image there can automatically switch after a set time, i think switch image is more interssting but we are talking about a  frame

        self.custom_frame = ctk.CTkFrame(self.tab1_frame, fg_color="#D6D4D4", corner_radius=20, border_width=2)
        self.custom_frame.pack(fill="x", padx=20, pady=40)

        ctk.CTkLabel(self.custom_frame, text="Your Learning Journey", font=("PT serif", 20), text_color=self.color).pack(pady=20, padx=20)


        # this second frame is for the random frame 
        self.random_image = ctk.CTkFrame(self.custom_frame, width=300, height=200, border_width=0, fg_color=None )
        self.random_image.pack(fill="x", pady=10, padx=50)

        


    def _create_canvas(self):
        # canva for dashboard image
        self.dash_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        self.dash_canva.grid(row=0, column=0, sticky="e", padx=10)
        self.dash_canva.create_image(self.W/2, self.H/2, image= self.dash_logo)
        # canva for couse image
        self.course_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        self.course_canva.grid(row=1, column=0, sticky="e", padx=10)
        self.course_canva.create_image(self.W/2, self.H/2, image= self.course_logo)
        # canva for profil 
        self.profil_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        self.profil_canva.grid(row=2, column=0, sticky="e", padx=10)
        self.profil_canva.create_image(self.W/2, self.H/2, image= self.profil)
        # canva for setting image
        self.settings_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        self.settings_canva.grid(row=3, column=0, sticky="e", padx=10)
        self.settings_canva.create_image(self.W/2, self.H/2, image= self.setting)
        # canva for logout image
        self.logout_canva = Canvas(self.lframe_two, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        self.logout_canva.grid(row=0, column=0, sticky="w")
        self.logout_canva.create_image(self.W/2, self.H/2, image= self.logout)
       
        class my_random_canva:
            def __init__(self, parent,  image):
                self.Wid = 500
                self.hei = 300
                self.image = image
                self.random_canva = Canvas(parent, width= self.Wid, height= self.hei, bd=0)
                
                self.random_canva.pack()

            def _get_image(self):
                return self.image
            
            def _set_image(self, neue_image):
                self.image = neue_image
                self.random_canva.itemconfig(self.image_id, image=self.image)

            
Daschboard()