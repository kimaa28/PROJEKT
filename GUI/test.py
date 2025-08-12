import customtkinter as ctk
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageDraw



ctk.set_appearance_mode("light")
class Daschboard:
    def __init__(self):
        self.app = ctk.CTk()
        self.W = 21
        self.H = 25
       

       # windows widh and frame setting
        
        # left frame for Menu and info
        self.left_frame = ctk.CTkFrame(self.app, corner_radius=0, border_width=1, fg_color="#99c0b3")
        self.left_frame.pack(fill="both", side="left")

        # right frame for all tab and specifics information 
        self.right_frame = ctk.CTkFrame(self.app, fg_color="#99c0b3", corner_radius=0)
        self.right_frame.pack(fill="both", side="right", expand="true")
        self.color = ("black", "white")
        # letf frame menu funktion 
        
        # app width setter
        self.app.after(100, self._set_frame_width)
        self._create_image()
        self._rframe_menu()
        self._lframe_menu()

        self._create_canvas()
        
        
        

        self.app.mainloop()

    def _create_image(self):
        self.canva_liste = [ PhotoImage(file=img) for img in ["dash_logo.png","course.png", "profil.png", "setting.png", "logout.png"]]
        # this is just for image path to combinated with pil
        self.first = "screen.png"
        self.second = "second.jpeg"
        self.third = "third.jpeg"
        self.image_list = [self.first, self.second, self.third]
        self.image_index = 0
        self.categories_img = [ ctk.CTkImage(light_image=Image.open(img), size=(40, 40)) for img in ["coding.png", "command.png", "data.png", "linux.png", "commit.png", "security.png"]
]



           

   

    def _set_frame_width(self):
        height_app = self.app.winfo_height()
        width_app= self.app.winfo_width()
        width_l = width_app / 4
        width_r = width_app - width_l
        self.left_frame.configure(width=width_l, height=height_app)
        self.right_frame.configure(width=width_r, height=height_app)

    def _lframe_menu(self):
        self.titel_label = ctk.CTkLabel(self.left_frame, text="<> DEVLEARN", font=("PT serif", 30), text_color= self.color)
        self.titel_label.pack(padx=15, pady=30)

        self.lframe_one = ctk.CTkFrame(self.left_frame, fg_color= self.left_frame.cget("fg_color"))
        self.lframe_one.pack(pady=50, fill="x", padx=15)
        self.menu_list = ["Dashboard", "Courses", "Profil", "Settings"]
        self.button_cmd = [lambda: self.tabs_menu.set("tab-1"), lambda: self.tabs_menu.set("tab-2"), lambda: self.tabs_menu.set("tab-3"), lambda: print("je suisun gros con")]

        for index, (label, cmd) in enumerate(zip(self.menu_list, self.button_cmd)):
            Button = ctk.CTkButton(self.lframe_one, text=label, command=cmd, hover_color="#005f73", corner_radius=20, fg_color=self.left_frame.cget("fg_color"), font=("PT serif", 23), anchor="w", text_color=self.color)
            Button.grid(row=index, column=1, sticky="w", pady=17)


        

        # # left frame  button menu
        
        # #dash button for dashboard tabview pov: i'm tired
        # self.dash_button = ctk.CTkButton(self.lframe_one, text="Dashboard", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command= lambda: self.tabs_menu.set("tab-1"), text_color= self.color)
        # self.dash_button.grid(row=0, column=1, sticky="w", pady=17)
        # # course button for course tabview
        # self.course_button = ctk.CTkButton(self.lframe_one, text="Course", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: self.tabs_menu.set("tab-2"), text_color= self.color, anchor="w")
        # self.course_button.grid(row=1, column=1, sticky="w", pady=17)
        # #profil button for profil tabview
        # self.profil_button = ctk.CTkButton(self.lframe_one, text="Profil", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command=lambda: print("profilbbuttoncliked"), text_color= self.color, anchor="w")
        # self.profil_button.grid(row=2, column=1, sticky="w", pady=17)
        # #profil button for profil tabview
        # self.settings_button = ctk.CTkButton(self.lframe_one, text="settings", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), text_color=self.color, anchor="w")
        # self.settings_button.grid(row=3, column=1, sticky="w", pady=17)
        



        #frame for logout and profil photo
        self.lframe_two = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.lframe_two.pack(side="bottom", pady=20, padx=25, fill="x")
        # button for logout
        self.logout_button = ctk.CTkButton(self.lframe_two, text="logout", font=("PT serif", 23), fg_color= self.lframe_one.cget("fg_color"), command= self.app.quit, text_color=self.color)
        self.logout_button.grid(row=0, column=1, sticky="e", pady=17)
        
       

    def _rframe_menu(self):
        self.tabs_menu = ctk.CTkTabview(master=self.right_frame, anchor="new", corner_radius=0)
        self.tabs_menu.pack(fill="both", expand="true")
        self.tab_1 = self.tabs_menu.add("tab-1")
        self.tab_2 = self.tabs_menu.add("tab-2")
        self.tab_3 = self.tabs_menu.add("tab-3")
        self.tabs_menu.set("tab-1")

        self._widget_dash()
        self._widget_courses()
        self._widget_profil()
        ctk.CTkLabel(self.right_frame, text="© 2025 by jordan kitio zangio", font=("Arial", 15), text_color= self.color).pack()

    # create all widget for my dashboard i choice the funktion this is better andmy code can be beautifull

    def _widget_dash(self):
        # it is difficult to display some informations in a tabview so i need zu mke a firs frame who take the fill = "both" and i can normaly displaying

        self.tab1_frame = ctk.CTkFrame(self.tab_1, fg_color= self.tab_1.cget("fg_color"))
        self.tab1_frame.pack(fill="both", expand="true")

       
        # i don't really no how  i can name this frame i choice random frame it isn't a really random image we just  have 3 image there can automatically switch after a set time, i think switch image is more interssting but we are talking about a  frame

        self.custom_frame = ctk.CTkFrame(self.tab1_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=20, border_width=4)
        self.custom_frame.pack(fill="x", padx=50, pady=40)



        self.welcome_label = ctk.CTkLabel(self.custom_frame, text="Willkommen zurück, jordan!", text_color=self.color, font=("PT serif", 35))
        self.welcome_label.grid(row=0, column=0, pady=20, padx=20, sticky="w")



        # this second frame is for the random frame 
        self.random_image_frame= ctk.CTkFrame(self.custom_frame, border_width=4, width=600, height=500 , fg_color= self.tab1_frame.cget("fg_color"), corner_radius= 30)
        self.random_image_frame.grid(row=1, column=0, padx=30, pady=20)
        
        # frame for learning statistics
        self.scroll = ctk.CTkScrollableFrame(self.custom_frame, corner_radius=20, fg_color=self.random_image_frame.cget("fg_color"), width=300, label_anchor="center", height=350)
        self.scroll.grid(row=1, column=1, padx=40)
        self.mittel_scroll = ctk.CTkScrollableFrame(self.custom_frame, corner_radius=20, fg_color= self.random_image_frame.cget("fg_color"), width=300, label_anchor="center", height=350)
        self.mittel_scroll.grid(row=1, column=2, padx=40)

        

        # title from this frame
        ctk.CTkLabel(self.scroll, text="Learning Statistics", font=("verdana", 20), text_color=self.color, fg_color=self.scroll.cget("fg_color")).grid(row=0, column=0, sticky="w", pady=15, padx=15)
        self.frame_list = ["120h\nlearn Time", "23\nTotal course", "30%\nProgress", "Friend", "Coin", "Level"]

        for i, text in enumerate(self.frame_list, start=1):
            ctk.CTkLabel(self.scroll, width=200,height=70, corner_radius=20, fg_color="#949494", text=text, text_color=self.color).grid(row=i, column=0, padx=20, pady=10)

        #  frame forquick access to course

        self.course_type_frame = ctk.CTkFrame(self.tab1_frame, corner_radius=20,fg_color=self.custom_frame.cget("fg_color"), border_width=4)
        self.course_type_frame.pack(pady=10, padx=50, fill="x")

        ctk.CTkLabel(self.course_type_frame, fg_color=self.course_type_frame.cget("fg_color"), font=("verdana", 20), text="Courses categories").grid(row=0, column=0, sticky="w", pady=20, padx=30)

        self.label_categories = ["Web Development\n11 courses", "Programming\n8 courses", "Backend & Database\n 5 courses", "Operating System\n 5 courses", "Version control\n3 courses", "Cybersecurity Basis\n 4 courses"]
        for index, (img, label_text) in enumerate(zip(self.categories_img, self.label_categories)):
          
            frame = ctk.CTkFrame(self.course_type_frame, corner_radius=25, width=225, height=100, fg_color="#949494")
            frame.grid(row=1, column=index, padx=30, pady=20)

            label = ctk.CTkLabel(frame, text=label_text)
            label.pack(side="right", pady=20, padx=10)

            image_label = ctk.CTkLabel(frame, image=img, text="")
            image_label.pack(side="left", padx=10, pady=20)

        self._load_image(self.first)
        self._start_image_loop()
           
    # all widget on my course tab as a funktion
    def _widget_courses(self):

        self.tab2_frame = ctk.CTkFrame(self.tab_2, fg_color= self.tab1_frame.cget("fg_color"))
        self.tab2_frame.pack(fill="both", expand="true")

        ctk.CTkLabel(self.tab2_frame, text="Courses", font=("Verdana", 40, "bold"), text_color=self.color).pack()

        self.frame_liste = ctk.CTkFrame(self.tab2_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=20, border_color="black", width=800, height=600)
        self.frame_liste.pack(fill="both",expand="true", pady=30)

        self.courses_image = [ ctk.CTkImage(light_image= self.add_rounded_corners(Image.open(img), radius=25), size=(500, 200)) for img in ["html.jpg", "python.webp", "cgi.jpg", "custom_tk.png", "linux_mint.jpg"] ]
        self.courses_titel = ["HTML & CSS Basics", "Python for Beginners", "CGI scripting", "CustomTkinter UI", "Linux Fundamentals"]
        self.courses_about = ["Learn the fundamentals from web development with HTML und CSS", "Dive into programming with python, a versatile language", "Understand server-side programming with CGI", "Build modern dekstop application with customtkinter", "Master the command line and linux operatings system"]
        self.courses_tutor = ["Pierre Giraud", "Graven & GeeksforGeeks", "Prof dr Preuss & Syryakow", "ChatGpt & Customtkinter", "ChatGpt & Herr dr preuss"]  # this musst be a button to the webseite von lehrer
        
        for index, (img, titel, about, tutor) in enumerate(zip(self.courses_image, self.courses_titel, self.courses_about, self.courses_tutor)):
            frame = ctk.CTkFrame(self.frame_liste, height=300, fg_color=None, corner_radius=25, border_width=2)
            self.frame1 = ctk.CTkFrame(frame, fg_color= self.tab1_frame.cget("fg_color"), corner_radius=0)
            label_image = ctk.CTkLabel(self.frame1, image=img, text="")
            frame2 = ctk.CTkFrame(frame, fg_color=None, corner_radius=20)
            frame3 = ctk.CTkFrame(frame2, fg_color=frame2.cget("fg_color"))

            if index % 2 == 0 :
                frame.grid(row=0, column=index//2, pady=20, padx=30)
                self.frame1.pack(fill="both", expand="true")
                frame2.pack(fill="both", expand="true")
                
                label_image.pack(fill="both", expand="true")
                
            else:     
                frame.grid(row=1, column=index//2, pady=20, padx=30)
                self.frame1.pack(fill="both", expand="true")
                frame2.pack(fill="both", expand="true")
                label_image.pack(fill="both", expand="true")

            label_titel = ctk.CTkLabel(frame2, text=titel, text_color=self.color, font=("Arial", 20, "bold"), anchor="w")
            label_titel.pack(padx=10, pady=10)
            label_about = ctk.CTkLabel(frame2, text=about, text_color="#676464", font=("verdana", 13, "italic"), anchor="w")
            label_about.pack(pady=10, padx=10)
            frame3.pack()
            tutot_img = ctk.CTkLabel(frame3, image=ctk.CTkImage(light_image=(Image.open("user.png")), size=(13, 13)), text="")
            tutot_img.grid(row=0, column=0)
            label_tutor = ctk.CTkLabel(frame3, text=tutor, text_color=label_about.cget("text_color"), font=("PT serif", 13, "underline"))
            label_tutor.grid(row=0, column=1, padx=5)
            button_start = ctk.CTkButton(frame2, text="Start Course", text_color="white", fg_color="#005f73")
            button_start.pack(fill="x")

    def _widget_profil(self):
        self.tab3_frame = ctk.CTkFrame(self.tab_3, fg_color= self.tab1_frame.cget("fg_color"))
        self.tab3_frame.pack(fill="both", expand="true")   

        ctk.CTkLabel(self.tab3_frame, text="Profil", text_color=self.color, font=("PT sereif", 35, "bold"), bg_color=self.tab3_frame.cget("fg_color") ).grid(row=0, column=0, sticky="nsew", pady= 40, padx=30) 
        ctk.CTkLabel(self.tab3_frame, text="Profil", text_color=self.color, font=("PT sereif", 35, "bold"), bg_color=self.tab3_frame.cget("fg_color") ).grid(row=0, column=1, sticky="nsew", pady= 40, padx=30) 

        self.profil_img_frm = ctk.CTkFrame(self.tab3_frame, border_color="red", border_width=2)
        self.profil_img_frm.grid(row=1, column=0, sticky="nsew", pady=20, padx=30, columnspan= 10)   
            

    def _create_canvas(self):

        for index, img in enumerate(self.canva_liste):
            if index == 4:
                self.logout_canva = Canvas(self.lframe_two, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
                self.logout_canva.grid(row=0, column=0, sticky="w")
                self.logout_canva.create_image(self.W/2, self.H/2, image= img)
            else:
                canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
                canva.create_image(self.W/2, self.H/2, image=img)
                canva.grid(row=index, column=0, sticky="e", padx=10)

        # # canva for dashboard image
        # self.dash_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        # self.dash_canva.grid(row=0, column=0, sticky="e", padx=10)
        # self.dash_canva.create_image(self.W/2, self.H/2, image= self.dash_logo)
        # # canva for couse image
        # self.course_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        # self.course_canva.grid(row=1, column=0, sticky="e", padx=10)
        # self.course_canva.create_image(self.W/2, self.H/2, image= self.course_logo)
        # # canva for profil 
        # self.profil_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        # self.profil_canva.grid(row=2, column=0, sticky="e", padx=10)
        # self.profil_canva.create_image(self.W/2, self.H/2, image= self.profil)
        # # canva for setting image
        # self.settings_canva = Canvas(self.lframe_one, width=self.W, height= self.H , bg= self.lframe_one.cget("fg_color"), bd=0, highlightthickness=0)
        # self.settings_canva.grid(row=3, column=0, sticky="e", padx=10)
        # self.settings_canva.create_image(self.W/2, self.H/2, image= self.setting)
        # # canva for logout image


        


    
       # i create all image as pil image and the set funktion
    def _load_image(self, path):
        pil_img = Image.open(path).resize((500, 350))
        self.ctk_img = ctk.CTkImage(light_image=self.add_rounded_corners(pil_img, radius=25), size=(600, 400))
        if hasattr(self, "image_label"):
            self.image_label.configure(image=self.ctk_img)
        else:
            self.image_label = ctk.CTkLabel(self.random_image_frame, image=self.ctk_img, text="")
            self.image_label.pack()

    def _start_image_loop(self):
        self.image_index = (self.image_index + 1) % len(self.image_list)
        self._load_image(self.image_list[self.image_index])
        self.app.after(4000, self._start_image_loop)

    def add_rounded_corners(self,image, radius):
        image = image.convert("RGBA")
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, image.size[0], image.size[1]), radius=radius, fill=255)
        image.putalpha(mask)
        return image
   
            
Daschboard()