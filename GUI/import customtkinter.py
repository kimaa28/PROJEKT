import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import fitz  # PyMuPDF
from PIL import Image, ImageTk

doc = None
aktuelle_seite = 0
zoom = 1.0
bild_ref = None

def pdf_oeffnen():
    global doc, aktuelle_seite, zoom
    
    pfad = filedialog.askopenfilename(
        filetypes=[("PDF Dateien", "*.pdf")]
    )
    
    if not pfad:
        return
    
    doc = fitz.open(pfad)
    aktuelle_seite = 0
    zoom = 1.0
    
    zeige_seite()

def zeige_seite():
    global bild_ref
    
    if doc is None:
        return
    
    seite = doc[aktuelle_seite]
    
    matrix = fitz.Matrix(zoom, zoom)
    pix = seite.get_pixmap(matrix=matrix)
    
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    bild_ref = ImageTk.PhotoImage(img)
    
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="center", image=bild_ref)
    
    canvas.config(scrollregion=canvas.bbox("all"))
    
    label_seite.config( 
        text=f"Seite {aktuelle_seite + 1}/{len(doc)} | Zoom: {int(zoom*100)}%"
    )

def naechste_seite():
    global aktuelle_seite
    if doc and aktuelle_seite < len(doc) - 1:
        aktuelle_seite += 1
        zeige_seite()

def vorherige_seite():
    global aktuelle_seite
    if doc and aktuelle_seite > 0:
        aktuelle_seite -= 1
        zeige_seite()

# 🔍 Suche
def suchen():
    global aktuelle_seite
    
    if doc is None:
        return
    
    begriff = simpledialog.askstring("Suchen", "Suchbegriff eingeben:")
    
    if not begriff:
        return
    
    for i, seite in enumerate(doc):
        text = seite.get_text()
        if begriff.lower() in text.lower():
            aktuelle_seite = i
            zeige_seite()
            messagebox.showinfo("Gefunden", f"Gefunden auf Seite {i+1}")
            return
    
    messagebox.showinfo("Nicht gefunden", "Begriff nicht gefunden")

# 🔍 Zoom mit STRG + Mausrad
def maus_zoom(event):
    global zoom
    
    if event.state & 0x0004:  # STRG gedrückt
        if event.delta > 0:
            zoom += 0.2
        else:
            if zoom > 0.4:
                zoom -= 0.2
        zeige_seite()
    else:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# ✋ Drag / Pan
def start_pan(event):
    canvas.scan_mark(event.x, event.y)

def pan(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

# Fenster
root = tk.Tk()
root.title("PDF Viewer V3")
root.geometry("1000x750")

# Top-Leiste
frame_top = tk.Frame(root)
frame_top.pack(pady=5)

tk.Button(frame_top, text="📂 Öffnen", command=pdf_oeffnen).grid(row=0, column=0, padx=5)
tk.Button(frame_top, text="⏮️", command=vorherige_seite).grid(row=0, column=1, padx=5)
tk.Button(frame_top, text="⏭️", command=naechste_seite).grid(row=0, column=2, padx=5)
tk.Button(frame_top, text="🔍 Suche", command=suchen).grid(row=0, column=3, padx=5)

label_seite = tk.Label(frame_top, text="Keine PDF geladen")
label_seite.grid(row=0, column=4, padx=10)

# Canvas + Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

canvas = tk.Canvas(frame, cursor="hand2")
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Events
canvas.bind("<MouseWheel>", maus_zoom)
canvas.bind("<ButtonPress-1>", start_pan)
canvas.bind("<B1-Motion>", pan)

# Start
root.mainloop()