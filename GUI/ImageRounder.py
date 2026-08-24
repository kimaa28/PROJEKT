import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def rounded_image(image:str, parent_color, i_size:tuple):
	img = Image.open(image).resize(i_size)
	new_img = Image.new("RGBA", img.size, parent_color)
	mask = Image.new("L", i_size, 0)
	draw = ImageDraw.Draw(mask)
	draw.ellipse((0, 0, i_size[0], i_size[1]), fill=255, outline=False)
	new_img.paste(img, (0,0), mask)
	tk_img = ImageTk.PhotoImage(new_img)            
	return tk_img