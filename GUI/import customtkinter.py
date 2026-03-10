from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

root = tk.Tk()

# Originalbild laden
img = Image.open("image/test.gif").convert("RGBA")

# Neue leere RGBA-Fläche (Hintergrundfarbe)
bg_color = (255, 255, 255, 255)  # Weiß
new_img = Image.new("RGBA", img.size, bg_color)

# Maske erzeugen
mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

# Originalbild in die neue Fläche einfügen mit Maske
new_img.paste(img, (0,0), mask)

# In Tkinter anzeigen
tk_img = ImageTk.PhotoImage(new_img)
label = tk.Label(root, image=tk_img)
label.pack()

root.mainloop()