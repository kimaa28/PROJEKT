import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

# --- Funktionen ---

# 1️⃣ Dateien zippen
def dateien_zippen():
    dateien = filedialog.askopenfilenames(title="Dateien auswählen")
    if not dateien:
        return
    
    ziel = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("ZIP Dateien", "*.zip")]
    )
    if not ziel:
        return
    
    try:
        with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
            for datei in dateien:
                z.write(datei, os.path.basename(datei))
        messagebox.showinfo("Fertig", "Dateien wurden komprimiert!")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

# 2️⃣ Ordner zippen
def ordner_zippen():
    ordner = filedialog.askdirectory(title="Ordner auswählen")
    if not ordner:
        return
    
    ziel = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("ZIP Dateien", "*.zip")]
    )
    if not ziel:
        return
    
    try:
        with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(ordner):
                for file in files:
                    pfad = os.path.join(root, file)
                    z.write(pfad, os.path.relpath(pfad, ordner))
        messagebox.showinfo("Fertig", f"Ordner {ordner} wurde komprimiert!")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

# 3️⃣ ZIP entpacken
def zip_entpacken():
    pfad = filedialog.askopenfilename(
        title="ZIP Datei auswählen",
        filetypes=[("ZIP Dateien", "*.zip")]
    )
    if not pfad:
        return
    
    ziel = filedialog.askdirectory(title="Entpacken nach Ordner")
    if not ziel:
        return
    
    try:
        with zipfile.ZipFile(pfad, "r") as z:
            z.extractall(ziel)
        messagebox.showinfo("Fertig", f"ZIP-Datei wurde nach {ziel} entpackt!")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

# 4️⃣ Drag & Drop ZIP → automatisch entpacken
def drag_drop(event):
    pfad = event.data
    if pfad.endswith(".zip"):
        ziel = filedialog.askdirectory(title=f"Entpacken {os.path.basename(pfad)} nach")
        if not ziel:
            return
        try:
            with zipfile.ZipFile(pfad, "r") as z:
                z.extractall(ziel)
            messagebox.showinfo("Fertig", f"{os.path.basename(pfad)} entpackt!")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

# --- GUI ---

root = tk.Tk()
root.title("Zip-Manager")
root.geometry("600x200")

frame_top = tk.Frame(root)
frame_top.pack(pady=20)

tk.Button(frame_top, text="📦 Dateien zippen", command=dateien_zippen).grid(row=0, column=0, padx=5)
tk.Button(frame_top, text="📁 Ordner zippen", command=ordner_zippen).grid(row=0, column=1, padx=5)
tk.Button(frame_top, text="📤 ZIP entpacken", command=zip_entpacken).grid(row=0, column=2, padx=5)

# Drag & Drop Unterstützung (Windows / Mac)
try:
    import tkinterdnd2 as tkdnd
    root = tkdnd.TkinterDnD.Tk()
    canvas = tk.Canvas(root, width=600, height=100, bg="lightgray")
    canvas.pack(pady=20)
    canvas.create_text(300, 50, text="ZIP hierher ziehen → automatisch entpacken", font=("Arial", 14))
    canvas.drop_target_register(tkdnd.DND_FILES)
    canvas.dnd_bind('<<Drop>>', drag_drop)
except ImportError:
    label = tk.Label(root, text="Drag & Drop nicht verfügbar (Installiere tkinterdnd2)")
    label.pack(pady=20)

root.mainloop()