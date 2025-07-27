from customtkinter import *


def dasch(parent):
    daschboard_frame = CTkFrame(parent, width=1600, height=900, fg_color="#ABC")

    return daschboard_frame

if __name__== "__main__":

    app = CTk()

    frame = dasch(app)
    frame.pack(expand=True)

    app.mainloop()
