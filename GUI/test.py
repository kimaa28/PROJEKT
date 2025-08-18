import customtkinter as ctk
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageDraw
import random as rd



ctk.set_appearance_mode("light")
class Daschboard:
    def __init__(self):
        self.app = ctk.CTk()
        self.color = ("black", "white")
        self.app.title("Devlearn")

        
         # left frame for Menu and info
        self.left_frame = ctk.CTkFrame(self.app, corner_radius=0, border_width=1, fg_color="#99c0b3")
        self.left_frame.pack(fill="both", side="left")

        # right frame for all tab and specifics information 
        self.right_frame = ctk.CTkFrame(self.app, fg_color="#99c0b3", corner_radius=0)
        self.right_frame.pack(fill="both", side="right", expand="true")
        

        self.app.after(100, self._set_frame_width)
        self._create_image()
        self._rframe_menu()
        self._lframe_menu()
        self._create_canvas()
        
        
        

        self.app.mainloop()



    # i create all image on this funktion or fast all, we have some image the are local managed
    def _create_image(self):
        # width ans height for canva
        self.W = 25
        self.H = 25
        self.canva_liste = [ PhotoImage(file=img) for img in ["dash_logo.png","course.png", "profil.png", "settings.png", "logout.png"]]
        # this is just for image path to combinated with pil
        self.first = "first.jpeg"
        self.second = "second.webp"
        self.third = "third.webp"
        self.fourth = "fourth.jpg"
        self.image_list = [self.first, self.second, self.third, self.fourth]
        self.image_index = rd.randrange(len(self.image_list))
        self.categories_img = [ ctk.CTkImage(light_image=Image.open(img), size=(40, 40)) for img in ["coding.png", "command.png", "data.png", "linux.png", "commit.png", "security.png"] ]
        self.titel_img = ctk.CTkImage(light_image=Image.open("dev.png"), size=(30, 30))


    # set the widht of my tho frame 
    def _set_frame_width(self):
        height_app = self.app.winfo_height()
        width_app= self.app.winfo_width()
        width_l = width_app / 4
        width_r = width_app - width_l
        self.left_frame.configure(width=width_l, height=height_app)
        self.right_frame.configure(width=width_r, height=height_app)


    # create the left frame or frame menu for the legend
    def _lframe_menu(self):
        frame = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        frame.pack(pady=10, padx=20, fill="x")
        self.label_img =  ctk.CTkLabel(frame, image=self.titel_img, text="", anchor="s")
        self.label_img.grid(row=0, column=0, pady=10, sticky="s")
        self.titel_label = ctk.CTkLabel(frame, text="DevLearn", font=("DM Sans", 20), text_color= self.color, anchor="s")
        self.titel_label.grid(row=0, column=1, padx=10)

        # TODO: i would make an image from users with his name on this frame
        self.img_frame = ctk.CTkFrame(self.left_frame, fg_color="#CBA", height=100, corner_radius=20)
        self.img_frame.pack(fill="x", padx=20, pady=10)

        # the left frame for all button to another tabs
        self.lframe_one = ctk.CTkFrame(self.left_frame, fg_color= self.left_frame.cget("fg_color"))
        self.lframe_one.pack(pady=30, fill="x", padx=15)

        #list of label from button
        # TODO: i would make a better settings tab, this can include many parameter like color setter, notifications enable and disable or text_ height
        self.menu_list = ["Dashboard", "Courses", "Profil", "Settings"]

        # list of command button
        self.button_cmd = [lambda: self.tabs_menu.set("tab-1"), lambda: self.tabs_menu.set("tab-2"), lambda: self.tabs_menu.set("tab-3"), lambda: print("not yet available")]

        # Button creation
        # this small commbination from enumerate and zip make the same think like 10 code line or more
        for index, (label, cmd) in enumerate(zip(self.menu_list, self.button_cmd)):
            Button = ctk.CTkButton(self.lframe_one, text=label, command=cmd, hover_color="#005f73", corner_radius=20, fg_color=self.left_frame.cget("fg_color"), font=("DM Sans", 18), anchor="w", text_color=self.color)
            Button.grid(row=index, column=1, sticky="w", pady=17)

        
        
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
        


        #frame for logout
        self.lframe_two = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.lframe_two.pack(side="bottom", pady=20, padx=25, fill="x")
        # button for logout
        self.logout_button = ctk.CTkButton(self.lframe_two, text="Logout", font=("DM Sans", 18), fg_color= self.lframe_one.cget("fg_color"), command= self.app.quit, text_color=self.color)
        self.logout_button.grid(row=0, column=1, sticky="e", pady=10)
        
       
    # create all tabs for all menu 
    def _rframe_menu(self):
        
        self.tabs_menu = ctk.CTkTabview(master=self.right_frame, anchor="nsew", corner_radius=0)
        self.tabs_menu.pack(fill="both", expand="true")
        self.tab_1 = self.tabs_menu.add("tab-1")
        self.tab_2 = self.tabs_menu.add("tab-2")
        self.tab_3 = self.tabs_menu.add("tab-3")
        self.tabs_menu.set("tab-1")

        self._widget_dash()
        self._widget_courses()
        self._widget_profil()

        ctk.CTkLabel(self.right_frame, text="© 2025 by jordan kitio zangio", font=("Arial", 15), text_color= self.color).pack()


    # dashboard tab
    def _widget_dash(self):
        
        # it is difficult to display some informations in a tabview so i need zu make a firt frame who take the fill = "both" and i can normaly displaying
        self.tab1_frame = ctk.CTkFrame(self.tab_1, fg_color= self.tab_1.cget("fg_color"))
        self.tab1_frame.pack(fill="both", expand="true")
        
        # frame 
        self.custom_frame = ctk.CTkFrame(self.tab1_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=20)
        self.custom_frame.pack(fill="x", padx=20, pady=20)

        self.welcome_label = ctk.CTkLabel(self.custom_frame, text="Willkommen zurück, jordan!", text_color=self.color, font=("PT serif", 35))
        self.welcome_label.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # this second frame is for the random image
        self.random_image_frame= ctk.CTkFrame(self.custom_frame, border_width=4, width=600, height=500 , fg_color= self.tab1_frame.cget("fg_color"), corner_radius= 30)
        self.random_image_frame.grid(row=1, column=0, padx=20, pady=20)
        
        # frame for learning statistics
        # TODO: make a responsive relation with label and information from this learnings statistics to the webseite
        self.scroll = ctk.CTkScrollableFrame(self.custom_frame, corner_radius=20, fg_color=self.random_image_frame.cget("fg_color"), width=300, label_anchor="center", height=350, border_width=2, )
        self.scroll.grid(row=1, column=1, padx=40)
        # frame for todo or focus of the learning or next journey
        self.mittel_scroll = ctk.CTkScrollableFrame(self.custom_frame, corner_radius=20, fg_color= self.random_image_frame.cget("fg_color"), width=300, label_anchor="center", height=350, border_width=3)
        self.mittel_scroll.grid(row=1, column=2, padx=40)

        
        # TODO: an explicite description from every quick access course and a button 
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

        self._load_image(rd.choice(self.image_list))
        self._start_image_loop()
        
        
           
    # all widget from my course tab
    def _widget_courses(self):

        # TODO: make the name of tutor like a button to the webpage from this one
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
            

    # tab for course
    def _widget_profil(self):
         
        #TODO: creste a neu tab to modified some personal information and more this can be trhought the click on edit be done, and add some variable to schwith button whose can hve consequenses
        self.tab3_frame = ctk.CTkFrame(self.tab_3, fg_color= self.tab1_frame.cget("fg_color"))
        self.tab3_frame.pack(fill="both", expand="true")   

        self.titel_frame = ctk.CTkFrame(self.tab3_frame, fg_color=self.tab1_frame.cget("fg_color"))
        self.titel_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(self.titel_frame, text="Profil", text_color=self.color, font=("PT sereif", 35), bg_color=self.tab3_frame.cget("fg_color") ).grid(row=0, column=0, sticky="nsew", pady= 10) 

        self.photo_frame = ctk.CTkFrame(self.tab3_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=20, height=250, border_width=2, border_color= "#8F8484")
        self.photo_frame.pack(fill="x", padx=20, pady=20)
        ctk.CTkLabel(self.photo_frame, text="i put the user image on this frame later").pack(padx=20, pady=100)
        self.account_settings = ["Edit profile", "Change passwort", "Delete Account"]

        self.account_frame = ctk.CTkFrame(self.tab3_frame, fg_color=self.tab1_frame.cget("fg_color"), border_color=self.photo_frame.cget("border_color"), border_width=2, corner_radius=20)
        self.account_frame.pack(fill="x", padx=20, pady=20)
        self.titel_account = ctk.CTkFrame(self.account_frame, fg_color=self.tab1_frame.cget("fg_color"))
        self.titel_account.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(self.titel_account, text="Account settings", text_color=self.color, font=("Arial",  15, "bold")).pack(side="left", padx=10, pady=10)

        for index, ele in enumerate(self.account_settings, start=1):
            frame = ctk.CTkFrame(self.account_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=10, border_color=self.photo_frame.cget("border_color"), border_width=1)
            frame.pack(fill="x", padx=20, pady=10)
            label = ctk.CTkLabel(frame, text=ele, text_color=self.color, font=("verdana", 10), fg_color=frame.cget("fg_color"))
            label.pack(side="left", padx=10, pady=10)

        # notifications frame
        self.notif_list = ["Email notification", "In-app notifications", "App uptdate"]
        self.notification_frame = ctk.CTkFrame(self.tab3_frame, fg_color=self.tab1_frame.cget("fg_color"), border_color=self.photo_frame.cget("border_color"), border_width=2, corner_radius=20)
        self.notification_frame.pack(fill="x", padx=20, pady=20)
        self.titel_notif = ctk.CTkFrame(self.notification_frame, fg_color=self.tab1_frame.cget("fg_color"))
        self.titel_notif.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(self.titel_notif, text="Notifications Preferences", text_color=self.color, font=("Arial",  15, "bold")).pack(side="left", padx=10, pady=10)

        for index, ele in enumerate(self.notif_list):
            frame = ctk.CTkFrame(self.notification_frame, fg_color=self.tab1_frame.cget("fg_color"), corner_radius=10, border_color=self.photo_frame.cget("border_color"), border_width=1)
            frame.pack(fill="x", padx=20, pady=10)
            label = ctk.CTkLabel(frame, text=ele, text_color=self.color, font=("verdana", 10), fg_color=frame.cget("fg_color"))
            label.pack(side="left", padx=10, pady=10)
            if index ==  0 or index == 1:

                switch =ctk.CTkSwitch(frame, onvalue="on", offvalue="off", text="", width=45, height=35, switch_width=35, progress_color=self.right_frame.cget("fg_color"), button_color="#5C8790", button_hover_color="#343232", fg_color="#343232")
                switch.pack(side="right", padx=10, pady=10)

            
            else:
                pass
   
    # crestion of canva 
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