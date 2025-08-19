# Tkinter Courses (Lessons 1-5)
class my_class:
    def __init__(self, titel_lesson, body, code, img, next_anw, btn_lst, btn_nxt, index):
        self.titel_lesson = titel_lesson
        self.body = body
        self.code = code
        self.img = img
        self.next_anw = next_anw
        self.btn_lst = btn_lst
        self.btn_nxt = btn_nxt
        self.index = index



lektion1 = my_class("Lektion 1: Einführung in Tkinter", 
"""Tkinter ist Pythons Standard-GUI-Bibliothek und kommt bereits mit jeder Python-Installation mit. GUI steht für "Graphical User Interface" - also grafische Benutzeroberfläche. Mit Tkinter kannst du Desktop-Anwendungen mit Fenstern, Buttons, Textfeldern und anderen grafischen Elementen erstellen.

Tkinter basiert auf dem Tk-Framework, das ursprünglich für die Programmiersprache Tcl entwickelt wurde. Es ist plattformübergreifend und funktioniert auf Windows, macOS und Linux.

Der große Vorteil von Tkinter ist seine Einfachheit - du brauchst keine zusätzlichen Bibliotheken zu installieren. Es ist perfekt für Anfänger und kleine bis mittlere Projekte geeignet.

In diesem ersten Beispiel erstellst du ein einfaches Fenster mit einem Label. Das Tk()-Objekt erstellt das Hauptfenster, title() setzt den Titel, geometry() bestimmt die Größe, und mainloop() startet die GUI-Ereignisschleife.

Jede GUI-Anwendung braucht diese mainloop() am Ende - sie wartet auf Benutzerinteraktionen wie Mausklicks oder Tasteneingaben und hält das Fenster offen.
""", 
"""
import tkinter as tk # or just from tkinter import * if you just working on tkinter

# Hauptfenster erstellen
root = tk.Tk()
root.title("Mein erstes Tkinter-Fenster")
root.geometry("400x300")

# Ein Label hinzufügen
label = tk.Label(root, text="Willkommen bei Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# GUI starten
root.mainloop()
""", "tkinter1.png", "In der nächsten Lektion lernst du verschiedene Widgets kennen.", "Zurück zur Startseite", "Weiter zu Lektion 2", 1)

lektion2 = my_class("Lektion 2: Grundlegende Widgets", 
"""
Widgets sind die Bausteine jeder GUI-Anwendung. Tkinter bietet viele verschiedene Widget-Typen für unterschiedliche Zwecke.

Label zeigt Text oder Bilder an - perfekt für Beschriftungen und Informationen. Button erstellt klickbare Schaltflächen für Benutzerinteraktionen. Entry ermöglicht einzeilige Texteingaben, während Text mehrzeilige Texteingaben erlaubt.

Jedes Widget hat Eigenschaften (Optionen) die sein Aussehen und Verhalten bestimmen. 'text' setzt den anzuzeigenden Text, 'font' bestimmt Schriftart und -größe, 'fg' und 'bg' setzen Vorder- und Hintergrundfarbe.

Die pack()-Methode ist eine der drei Layout-Manager in Tkinter. Sie ordnet Widgets automatisch im Fenster an. Der Parameter 'pady' fügt vertikalen Abstand hinzu, 'padx' horizontalen Abstand.

Das command-Parameter bei Buttons verbindet eine Funktion mit dem Klick-Ereignis. Wenn der Button geklickt wird, wird die angegebene Funktion ausgeführt.
""", 
"""
import tkinter as tk

def button_clicked():
    text = entry.get()
    label_result.config(text=f"Du hast eingegeben: {text}")

root = tk.Tk()
root.title("Tkinter Widgets")
root.geometry("400x300")

# Verschiedene Widgets
label = tk.Label(root, text="Gib etwas ein:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Klick mich!", command=button_clicked, 
                  font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="green")
label_result.pack(pady=10)

root.mainloop()
""", "tkinter2.png", "In der nächsten Lektion lernst du Layout-Management kennen.", "Zurück zu Lektion 1", "Weiter zu Lektion 3", 2)

lektion3 = my_class("Lektion 3: Layout-Management", """
Layout-Manager bestimmen, wie Widgets in einem Fenster angeordnet werden. Tkinter bietet drei Hauptmethoden: pack(), grid() und place().

pack() ist der einfachste Layout-Manager. Er ordnet Widgets nacheinander an - standardmäßig von oben nach unten. Mit 'side' kannst du die Richtung ändern: tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT. 'fill' lässt Widgets den verfügbaren Platz ausfüllen.

grid() verwendet ein Raster-System mit Zeilen und Spalten - wie eine Tabelle. Das ist sehr flexibel für komplexe Layouts. 'row' und 'column' bestimmen die Position, 'sticky' die Ausrichtung innerhalb der Zelle.

place() gibt dir absolute Kontrolle über die Position mit x/y-Koordinaten oder relativen Positionen. Es wird seltener verwendet, da es bei Fenstergrößenänderungen Probleme geben kann.

Wichtig: Verwende niemals pack() und grid() im gleichen Container - das führt zu Konflikten! Du kannst aber verschiedene Layout-Manager in verschiedenen Frames kombinieren.
""", 
"""
import tkinter as tk

root = tk.Tk()
root.title("Layout-Management")
root.geometry("500x400")

# Frame für pack()-Beispiel
pack_frame = tk.Frame(root, bg="lightgray", relief="raised", bd=2)
pack_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

tk.Label(pack_frame, text="Pack Layout", font=("Arial", 14, "bold")).pack(pady=5)
tk.Button(pack_frame, text="Oben", bg="red").pack(pady=2)
tk.Button(pack_frame, text="Mitte", bg="green").pack(pady=2)
tk.Button(pack_frame, text="Unten", bg="blue").pack(pady=2)

# Frame für grid()-Beispiel
grid_frame = tk.Frame(root, bg="white", relief="raised", bd=2)
grid_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

tk.Label(grid_frame, text="Grid Layout", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=5)

for i in range(3):
    for j in range(3):
        tk.Button(grid_frame, text=f"{i},{j}", width=8).grid(row=i+1, column=j, padx=2, pady=2)

root.mainloop()
""", "tkinter3.png", "In der nächsten Lektion lernst du Event-Handling kennen.", "Zurück zu Lektion 2", "Weiter zu Lektion 4", 3)

lektion4 = my_class("Lektion 4: Event-Handling und Callbacks", 
"""
Events sind Ereignisse wie Mausklicks, Tasteneingaben oder Fensterereignisse. Event-Handling ermöglicht es deiner Anwendung, auf Benutzerinteraktionen zu reagieren.

Callbacks sind Funktionen, die aufgerufen werden, wenn ein bestimmtes Event auftritt. Bei Buttons verwendest du den 'command'-Parameter für Click-Events. Für komplexere Events nutzt du die bind()-Methode.

Die bind()-Methode verbindet Events mit Callback-Funktionen. Häufige Events sind: '<Button-1>' (linker Mausklick), '<Key>' (Tastendruck), '<Return>' (Enter-Taste), '<FocusIn>' (Widget erhält Fokus).

Event-Objekte enthalten Informationen über das aufgetretene Ereignis. Bei Tastatur-Events findest du in event.keysym die gedrückte Taste, bei Maus-Events event.x und event.y die Koordinaten.

Lambda-Funktionen sind praktisch für einfache Callbacks. Statt eine separate Funktion zu definieren, kannst du mit lambda eine Mini-Funktion direkt im command-Parameter erstellen.
""", 
"""
import tkinter as tk

def on_button_click():
    output.insert(tk.END, "Button wurde geklickt!\\n")

def on_key_press(event):
    output.insert(tk.END, f"Taste gedrückt: {event.keysym}\\n")

def on_mouse_click(event):
    output.insert(tk.END, f"Mausklick bei ({event.x}, {event.y})\\n")

def clear_output():
    output.delete(1.0, tk.END)

root = tk.Tk()
root.title("Event-Handling")
root.geometry("500x400")

# Button für Click-Event
button = tk.Button(root, text="Klick mich!", command=on_button_click,
                  font=("Arial", 12), bg="lightblue")
button.pack(pady=10)

# Entry für Tastatur-Events
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)
entry.bind('<Key>', on_key_press)
entry.focus_set()  # Fokus setzen

# Frame für Maus-Events
mouse_frame = tk.Frame(root, bg="lightyellow", width=200, height=100)
mouse_frame.pack(pady=10)
mouse_frame.bind('<Button-1>', on_mouse_click)

# Text-Widget für Ausgabe
output = tk.Text(root, height=8, font=("Arial", 10))
output.pack(pady=10, fill=tk.BOTH, expand=True)

# Clear-Button mit Lambda
tk.Button(root, text="Löschen", command=lambda: clear_output(),
          bg="lightcoral").pack(pady=5)

root.mainloop()
""", "tkinter4.png", "In der nächsten Lektion lernst du Menüs und Dialoge kennen.", "Zurück zu Lektion 3", "Weiter zu Lektion 5", 4)

lektion5 = my_class("Lektion 5: Menüs und Dialoge", 
"""
Menüs geben deiner Anwendung ein professionelles Aussehen und bieten einfachen Zugang zu Funktionen. Tkinter bietet verschiedene Arten von Menüs: Menüleisten, Popup-Menüs und Untermenüs.

Eine Menüleiste wird mit Menu(root) erstellt und mit root.config(menu=menubar) am Fenster befestigt. add_cascade() fügt Hauptmenüs hinzu, add_command() einzelne Menüeinträge, add_separator() Trennlinien.

Dialoge sind spezielle Fenster für Benutzerinteraktionen. tkinter.messagebox bietet vorgefertigte Dialoge: showinfo() für Informationen, showwarning() für Warnungen, showerror() für Fehler, askquestion() für Ja/Nein-Fragen.

tkinter.filedialog ermöglicht Datei-Operationen: askopenfilename() öffnet einen Dialog zur Dateiauswahl, asksaveasfilename() zum Speichern. Du kannst Dateitypen mit filetypes=[("Text", "*.txt")] einschränken.

tkinter.simpledialog bietet einfache Eingabedialoge: askstring() für Text, askinteger() für Zahlen, askfloat() für Dezimalzahlen. Diese geben den eingegebenen Wert zurück oder None bei Abbruch.
""", 
"""
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

def show_info():
    messagebox.showinfo("Information", "Das ist eine Informationsmeldung!")

def show_warning():
    messagebox.showwarning("Warnung", "Das ist eine Warnung!")

def ask_question():
    result = messagebox.askquestion("Frage", "Möchtest du fortfahren?")
    status_label.config(text=f"Antwort: {result}")

def open_file():
    filename = filedialog.askopenfilename(
        title="Datei öffnen",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        status_label.config(text=f"Gewählte Datei: {filename}")

def save_file():
    filename = filedialog.asksaveasfilename(
        title="Datei speichern",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        status_label.config(text=f"Speichern als: {filename}")

def ask_name():
    name = simpledialog.askstring("Eingabe", "Wie heißt du?")
    if name:
        status_label.config(text=f"Hallo, {name}!")

root = tk.Tk()
root.title("Menüs und Dialoge")
root.geometry("600x400")

# Menüleiste erstellen
menubar = tk.Menu(root)
root.config(menu=menubar)

# Datei-Menü
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_command(label="Speichern", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=root.quit)

# Hilfe-Menü
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Hilfe", menu=help_menu)
help_menu.add_command(label="Info", command=show_info)

# Buttons für verschiedene Dialoge
tk.Button(root, text="Information anzeigen", command=show_info,
          font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Warnung anzeigen", command=show_warning,
          font=("Arial", 12)).pack(pady=5)

tk.Button(root, text="Frage stellen", command=ask_question,
          font=("Arial", 12)).pack(pady=5)

tk.Button(root, text="Name eingeben", command=ask_name,
          font=("Arial", 12)).pack(pady=5)

# Status-Label
status_label = tk.Label(root, text="Bereit...", font=("Arial", 12),
                       fg="blue", wraplength=500)
status_label.pack(pady=20, fill=tk.X)

root.mainloop()
""", "tkinter5.png", "In der nächsten Lektion wechseln wir zu CustomTkinter.", "Zurück zu Lektion 4", "Weiter zu Lektion 6", 5)

# CustomTkinter Courses (Lessons 6+)

lektion6 = my_class("Lektion 6: Einführung in CustomTkinter", 
"""
CustomTkinter ist eine moderne Alternative zu Tkinter, die ein zeitgemäßes und ansprechendes Design bietet. Es erweitert Tkinter um moderne UI-Elemente mit Dark/Light-Themes, abgerundeten Ecken und schöneren Animationen.

Der große Vorteil von CustomTkinter ist das professionelle Aussehen ohne viel zusätzlichen Aufwand. Während Standard-Tkinter oft veraltet aussieht, bietet CustomTkinter eine moderne Optik, die heutigen Design-Standards entspricht.

CustomTkinter muss separat installiert werden: pip install customtkinter. Es ist vollständig kompatibel mit Tkinter-Code, du kannst also bestehende Tkinter-Anwendungen leicht umstellen.

Die wichtigsten Neuerungen sind: CTk() statt Tk() für das Hauptfenster, CTkLabel, CTkButton etc. statt den Standard-Widgets, automatische Theme-Unterstützung (Dark/Light), und schönere Standard-Farben und Schriftarten.

CustomTkinter unterstützt moderne Farbschemata und Appearance-Modi. Du kannst zwischen "dark", "light" und "system" (folgt Systemeinstellung) wählen. Das macht deine Anwendung automatisch benutzerfreundlicher.
""", 
"""
import customtkinter as ctk

# Appearance-Modus und Farbthema setzen
ctk.set_appearance_mode("dark")  # "dark" oder "light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Hauptfenster erstellen
root = ctk.CTk()
root.title("Meine erste CustomTkinter-App")
root.geometry("500x350")

# Titel-Label
title_label = ctk.CTkLabel(root, 
                          text="Willkommen bei CustomTkinter!",
                          font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=20)

# Beschreibungs-Label
desc_label = ctk.CTkLabel(root,
                         text="CustomTkinter bietet moderne, schöne GUI-Elemente\\n"
                              "mit Dark/Light-Theme-Unterstützung.",
                         font=ctk.CTkFont(size=14))
desc_label.pack(pady=10)

# Moderne Buttons
button1 = ctk.CTkButton(root, text="Moderner Button", 
                       font=ctk.CTkFont(size=14))
button1.pack(pady=10)

button2 = ctk.CTkButton(root, text="Anderer Stil", 
                       fg_color="green", hover_color="darkgreen")
button2.pack(pady=5)

# Theme-Wechsel Button
def toggle_theme():
    current_mode = ctk.get_appearance_mode()
    new_mode = "light" if current_mode == "dark" else "dark"
    ctk.set_appearance_mode(new_mode)

theme_button = ctk.CTkButton(root, text="Theme wechseln", 
                           command=toggle_theme,
                           fg_color="orange", hover_color="darkorange")
theme_button.pack(pady=20)

root.mainloop()
""", "customtkinter1.png", "In der nächsten Lektion lernst du moderne CustomTkinter-Widgets kennen.", "Zurück zu Lektion 5", "Weiter zu Lektion 7", 6)

lektion7 = my_class("Lektion 7: Moderne Widgets in CustomTkinter", 
"""
CustomTkinter bietet viele verbesserte Widgets, die nicht nur schöner aussehen, sondern auch mehr Funktionen bieten als ihre Tkinter-Gegenstücke.

CTkEntry bietet moderne Texteingabefelder mit Placeholder-Text, abgerundeten Ecken und schönen Fokus-Animationen. Der placeholder_text wird automatisch angezeigt, wenn das Feld leer ist.

CTkTextbox ersetzt das alte Text-Widget und bietet bessere Darstellung mit modernerm Scrollbar-Design. Es unterstützt alle bekannten Text-Operationen mit verbesserter Optik.

CTkCheckBox und CTkRadioButton haben moderne Designs mit schöneren Animationen. CTkSwitch ist eine moderne Alternative zu Checkboxes für An/Aus-Optionen.

CTkProgressBar zeigt Fortschritte mit schönen, animierten Balken an. CTkSlider bietet moderne Schieberegler mit besserer Bedienbarkeit als Scale-Widgets.

Alle Widgets unterstützen die Theme-Farben automatisch und passen sich dem gewählten Appearance-Modus an. Du kannst aber auch individuelle Farben mit fg_color, text_color etc. setzen.
""", 
"""
import customtkinter as ctk
from tkinter import StringVar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Moderne CustomTkinter Widgets")
root.geometry("600x700")

# Titel
title = ctk.CTkLabel(root, text="Moderne Widget-Sammlung", 
                    font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=20)

# Entry mit Placeholder
entry = ctk.CTkEntry(root, placeholder_text="Gib hier etwas ein...",
                    width=300, font=ctk.CTkFont(size=14))
entry.pack(pady=10)

# Textbox
textbox = ctk.CTkTextbox(root, width=400, height=100)
textbox.pack(pady=10)
textbox.insert("0.0", "Das ist eine moderne Textbox.\\n"
                      "Sie unterstützt mehrzeiligen Text\\n"
                      "und hat schöne Scrollbars.")

# Checkboxes und Switch
checkbox_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(root, text="Moderne Checkbox", 
                          variable=checkbox_var)
checkbox.pack(pady=5)

switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(root, text="Modern Switch", 
                      variable=switch_var)
switch.pack(pady=5)

# Radio Buttons
radio_var = ctk.StringVar(value="option1")
radio1 = ctk.CTkRadioButton(root, text="Option 1", 
                           variable=radio_var, value="option1")
radio1.pack(pady=2)

radio2 = ctk.CTkRadioButton(root, text="Option 2", 
                           variable=radio_var, value="option2")
radio2.pack(pady=2)

# Progress Bar
progress = ctk.CTkProgressBar(root, width=300)
progress.pack(pady=15)
progress.set(0.7)  # 70%

# Slider
def slider_callback(value):
    progress.set(value)
    slider_label.configure(text=f"Wert: {value:.2f}")

slider = ctk.CTkSlider(root, from_=0, to=1, 
                      command=slider_callback, width=300)
slider.pack(pady=5)
slider.set(0.7)

slider_label = ctk.CTkLabel(root, text="Wert: 0.70")
slider_label.pack(pady=5)

# Optionsmenu
option_menu = ctk.CTkOptionMenu(root, 
                               values=["Option 1", "Option 2", "Option 3"],
                               width=200)
option_menu.pack(pady=15)

root.mainloop()
""", "customtkinter2.png", "In der nächsten Lektion lernst du Frames und Layout in CustomTkinter kennen.", "Zurück zu Lektion 6", "Weiter zu Lektion 8", 7)

lektion8 = my_class("Lektion 8: Frames und erweiterte Layouts", 
"""
CTkFrame ist das moderne Gegenstück zu Tkinters Frame-Widget und bietet viel mehr Gestaltungsmöglichkeiten. Du kannst Rahmenfarben, Eckenradius und verschiedene visuelle Effekte einstellen.

CTkScrollableFrame ist eine einzigartige Neuerung in CustomTkinter - ein Frame mit automatischen Scrollbars. Das ist perfekt für Inhalte, die größer als das verfügbare Fenster sind, ohne manuell Scrollbars programmieren zu müssen.

CTkTabview ermöglicht es, verschiedene Ansichten in Tabs zu organisieren - wie Browser-Tabs. Du kannst mit add() neue Tabs hinzufügen und dann Widgets in jeden Tab mit tab("Tabname").

Das Layout-System funktioniert genauso wie in Tkinter - du kannst pack(), grid() und place() verwenden. CustomTkinter-Widgets haben aber bessere Standard-Paddings und Abstände.

Corner_radius bestimmt, wie abgerundet die Ecken der Widgets sind. border_width setzt die Rahmendicke, fg_color die Hintergrundfarbe. Diese Parameter geben dir viel Kontrolle über das Aussehen.
""", 
"""
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Frames und erweiterte Layouts")
root.geometry("800x600")

# Hauptframe mit unterschiedlichen Bereichen
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Titel
title = ctk.CTkLabel(main_frame, text="Layout-Demo", 
                    font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=20)

# Tabview für verschiedene Bereiche
tabview = ctk.CTkTabview(main_frame, width=700, height=400)
tabview.pack(pady=20, padx=20)

# Tab 1: Normale Widgets
tab1 = tabview.add("Widgets")
ctk.CTkLabel(tab1, text="Normale Widget-Sammlung", 
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

widget_frame = ctk.CTkFrame(tab1, fg_color="transparent")
widget_frame.pack(fill="x", padx=20, pady=10)

ctk.CTkEntry(widget_frame, placeholder_text="Eingabefeld").pack(pady=5)
ctk.CTkButton(widget_frame, text="Button").pack(pady=5)
ctk.CTkCheckBox(widget_frame, text="Checkbox").pack(pady=5)

# Tab 2: Scrollbarer Bereich
tab2 = tabview.add("Scrollbar")
ctk.CTkLabel(tab2, text="Scrollbarer Inhalt", 
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

# Scrollbares Frame
scrollable_frame = ctk.CTkScrollableFrame(tab2, width=600, height=250)
scrollable_frame.pack(pady=10, padx=20)

# Viele Widgets zum Scrollen hinzufügen
for i in range(20):
    frame_item = ctk.CTkFrame(scrollable_frame)
    frame_item.pack(fill="x", pady=5, padx=5)
    
    ctk.CTkLabel(frame_item, text=f"Element {i+1}").pack(side="left", padx=10, pady=10)
    ctk.CTkButton(frame_item, text=f"Button {i+1}", width=100).pack(side="right", padx=10, pady=5)

# Tab 3: Grid Layout
tab3 = tabview.add("Grid Layout")
ctk.CTkLabel(tab3, text="Grid-basiertes Layout", 
            font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

grid_frame = ctk.CTkFrame(tab3, fg_color="transparent")
grid_frame.pack(pady=20)

# Grid mit verschiedenen Widgets
colors = ["red", "green", "blue", "orange", "purple", "pink"]
for i in range(2):
    for j in range(3):
        btn = ctk.CTkButton(grid_frame, text=f"{i},{j}", 
                           fg_color=colors[i*3 + j],
                           width=120, height=60)
        btn.grid(row=i, column=j, padx=10, pady=10)

root.mainloop()
""", "customtkinter3.png", "In der nächsten Lektion lernst du spezielle CustomTkinter-Features kennen.", "Zurück zu Lektion 7", "Weiter zu Lektion 9", 8)

lektion9 = my_class("Lektion 9: Spezielle CustomTkinter-Features", 
"""
CustomTkinter bietet einige einzigartige Features, die in Standard-Tkinter nicht verfügbar sind. Diese machen deine Anwendungen professioneller und benutzerfreundlicher.

CTkToplevel erstellt moderne popup-Fenster mit den gleichen Styling-Optionen wie das Hauptfenster. Anders als Tkinters Toplevel unterstützt es automatisch die Theme-Einstellungen.

Die Scaling-Funktion ist besonders nützlich für verschiedene Bildschirmgrößen und DPI-Einstellungen. Mit set_widget_scaling() kannst du die Größe aller Widgets proportional anpassen - perfekt für High-DPI-Displays.

Font-Handling ist in CustomTkinter deutlich verbessert. CTkFont bietet einfache Gewichts- und Größeneinstellungen mit automatischer Theme-Anpassung. Du kannst auch System-Schriftarten und eigene Schriftarten laden.

Color-Management ist flexibler - du kannst eigene Farbthemen erstellen oder einzelne Widgets mit benutzerdefinierten Farben versehen. Transparenz wird ebenfalls unterstützt.

Die bind()-Methoden funktionieren genauso wie in Tkinter, aber CustomTkinter fügt zusätzliche Events für Hover-Effekte und Theme-Änderungen hinzu.
""", 
"""
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AdvancedApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Erweiterte CustomTkinter-Features")
        self.root.geometry("700x500")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Titel mit benutzerdefinierten Fonts
        title_font = ctk.CTkFont(family="Arial", size=28, weight="bold")
        title = ctk.CTkLabel(self.root, text="Erweiterte Features", font=title_font)
        title.pack(pady=20)
        
        # Frame für Controls
        control_frame = ctk.CTkFrame(self.root)
        control_frame.pack(pady=20, padx=40, fill="x")
        
        # Scaling Controls
        ctk.CTkLabel(control_frame, text="UI-Skalierung:", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        scaling_frame = ctk.CTkFrame(control_frame, fg_color="transparent")
        scaling_frame.pack(pady=5)
        
        def change_scaling(value):
            ctk.set_widget_scaling(value)
            
        scaling_slider = ctk.CTkSlider(scaling_frame, from_=0.8, to=1.5,
                                     command=change_scaling, width=200)
        scaling_slider.set(1.0)
        scaling_slider.pack(side="left", padx=5)
        
        self.scaling_label = ctk.CTkLabel(scaling_frame, text="100%")
        self.scaling_label.pack(side="left", padx=10)
        
        # Theme Controls
        theme_frame = ctk.CTkFrame(control_frame, fg_color="transparent")
        theme_frame.pack(pady=10, fill="x")
        
        ctk.CTkLabel(theme_frame, text="Appearance:", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        appearance_menu = ctk.CTkOptionMenu(theme_frame, 
                                           values=["dark", "light", "system"],
                                           command=self.change_appearance)
        appearance_menu.pack(pady=5)
        
        # Color Theme Controls
        ctk.CTkLabel(theme_frame, text="Farbthema:", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        color_menu = ctk.CTkOptionMenu(theme_frame,
                                      values=["blue", "green", "dark-blue"],
                                      command=self.change_color_theme)
        color_menu.pack(pady=5)
        
        # Demo Widgets mit besonderen Features
        demo_frame = ctk.CTkFrame(self.root)
        demo_frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        # Hover-Effekt Button
        hover_button = ctk.CTkButton(demo_frame, text="Hover-Effekt", 
                                   fg_color="purple", hover_color="magenta")
        hover_button.pack(pady=10)
        
        # Popup-Fenster Button
        popup_button = ctk.CTkButton(demo_frame, text="Popup öffnen", 
                                   command=self.open_popup)
        popup_button.pack(pady=10)
        
        # Transparente Elemente
        transparent_frame = ctk.CTkFrame(demo_frame, fg_color="transparent")
        transparent_frame.pack(pady=10, fill="x")
        
        ctk.CTkLabel(transparent_frame, text="Transparenter Frame-Hintergrund").pack()
        
    def change_appearance(self, mode):
        ctk.set_appearance_mode(mode)
        
    def change_color_theme(self, theme):
        ctk.set_default_color_theme(theme)
        # Neustart der App für Theme-Änderung
        self.root.destroy()
        app = AdvancedApp()
        app.run()
        
    def open_popup(self):
        popup = ctk.CTkToplevel(self.root)
        popup.title("Popup-Fenster")
        popup.geometry("400x300")
        popup.transient(self.root)  # Bleibt über Hauptfenster
        
        ctk.CTkLabel(popup, text="Das ist ein modernes Popup!", 
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        
        # Popup-spezifische Widgets
        entry = ctk.CTkEntry(popup, placeholder_text="Eingabe im Popup...")
        entry.pack(pady=10)
        
        def close_popup():
            value = entry.get()
            if value:
                print(f"Eingabe aus Popup: {value}")
            popup.destroy()
            
        ctk.CTkButton(popup, text="Schließen", command=close_popup).pack(pady=20)
        
        # Popup zentrieren
        popup.grab_set()  # Modal machen
        
    def run(self):
        self.root.mainloop()

# App starten
if __name__ == "__main__":
    app = AdvancedApp()
    app.run()
""", "customtkinter4.png", "In der nächsten Lektion lernst du die Integration von Bildern und Icons.", "Zurück zu Lektion 8", "Weiter zu Lektion 10", 9)

lektion10 = my_class("Lektion 10: Bilder, Icons und Multimedia", 
"""
CustomTkinter bietet erweiterte Möglichkeiten für die Integration von Bildern und Icons in deine Anwendungen. CTkImage ist eine mächtige Klasse, die automatische Skalierung und Theme-Anpassungen unterstützt.

CTkImage kann sowohl Light- als auch Dark-Mode-Versionen von Bildern verwalten. Du kannst verschiedene Bilder für verschiedene Themes bereitstellen, und CustomTkinter wechselt automatisch zwischen ihnen.

Die size-Parameter von CTkImage bestimmen die Anzeigegröße unabhängig von der ursprünglichen Bildgröße. Das ist perfekt für konsistente Icon-Größen in deiner Anwendung.

PIL (Pillow) wird für die Bildverarbeitung verwendet. Du kannst Bilder laden, skalieren, drehen und andere Transformationen durchführen, bevor du sie in CTkImage verwendest.

Icons lassen sich einfach zu Buttons, Labels und anderen Widgets hinzufügen. Der image-Parameter zeigt nur das Bild an, compound bestimmt, wie Text und Bild kombiniert werden.

CustomTkinter unterstützt die meisten Bildformate: PNG, JPEG, GIF, BMP. PNG wird empfohlen für Icons wegen der Transparenz-Unterstützung.
""", 
"""
import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ImageApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Bilder und Icons in CustomTkinter")
        self.root.geometry("800x600")
        
        self.create_images()
        self.create_widgets()
        
    def create_images(self):
        # Erstelle einfache Bilder programmatisch (da wir keine echten Dateien haben)
        # In einer echten App würdest du Image.open("pfad/zum/bild.png") verwenden
        
        # Beispiel für programmatisch erstellte Icons
        self.home_icon = self.create_colored_image(32, 32, "blue")
        self.settings_icon = self.create_colored_image(32, 32, "green") 
        self.info_icon = self.create_colored_image(32, 32, "orange")
        
        # Größeres Bild
        self.large_image = self.create_colored_image(200, 150, "purple")
        
    def create_colored_image(self, width, height, color):
        ""Erstellt ein einfarbiges Bild als Beispiel""
        # In einer echten App: return ctk.CTkImage(Image.open("pfad.png"), size=(width, height))
        img = Image.new("RGB", (width, height), color)
        return ctk.CTkImage(img, size=(width, height))
        
    def create_widgets(self):
        # Titel
        title = ctk.CTkLabel(self.root, text="Bilder und Icons Demo",
                           font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=20)
        
        # Icon-Buttons in einem Frame
        icon_frame = ctk.CTkFrame(self.root)
        icon_frame.pack(pady=20)
        
        ctk.CTkLabel(icon_frame, text="Icon-Buttons:",
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        
        button_frame = ctk.CTkFrame(icon_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        
        # Buttons mit Icons
        home_btn = ctk.CTkButton(button_frame, text="Home", 
                               image=self.home_icon, compound="left",
                               command=lambda: self.show_message("Home geklickt!"))
        home_btn.pack(side="left", padx=10)
        
        settings_btn = ctk.CTkButton(button_frame, text="Einstellungen",
                                   image=self.settings_icon, compound="left",
                                   command=lambda: self.show_message("Einstellungen geklickt!"))
        settings_btn.pack(side="left", padx=10)
        
        info_btn = ctk.CTkButton(button_frame, text="Info",
                               image=self.info_icon, compound="left",
                               command=lambda: self.show_message("Info geklickt!"))
        info_btn.pack(side="left", padx=10)
        
        # Nur-Icon Button
        icon_only_btn = ctk.CTkButton(button_frame, text="", 
                                    image=self.settings_icon,
                                    width=50, height=50)
        icon_only_btn.pack(side="left", padx=10)
        
        # Label mit Bild
        image_frame = ctk.CTkFrame(self.root)
        image_frame.pack(pady=20)
        
        ctk.CTkLabel(image_frame, text="Bild-Label:",
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        
        image_label = ctk.CTkLabel(image_frame, text="", image=self.large_image)
        image_label.pack(pady=10)
        
        # Text mit Bild kombiniert
        combined_frame = ctk.CTkFrame(self.root)
        combined_frame.pack(pady=20, fill="x", padx=40)
        
        ctk.CTkLabel(combined_frame, text="Kombinierte Text-Bild-Labels:",
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        
        # Verschiedene compound-Modi
        compound_frame = ctk.CTkFrame(combined_frame, fg_color="transparent")
        compound_frame.pack(pady=10)
        
        compounds = [("left", "Icon links"), ("right", "Icon rechts"), 
                    ("top", "Icon oben"), ("bottom", "Icon unten")]
        
        for i, (compound, text) in enumerate(compounds):
            label = ctk.CTkLabel(compound_frame, text=text, 
                               image=self.info_icon, compound=compound,
                               font=ctk.CTkFont(size=12))
            label.grid(row=i//2, column=i%2, padx=20, pady=10)
            
        # Bildgrößen-Kontrolle
        control_frame = ctk.CTkFrame(self.root)
        control_frame.pack(pady=20)
        
        ctk.CTkLabel(control_frame, text="Bildgröße anpassen:",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        def change_image_size(value):
            size = int(value)
            new_image = self.create_colored_image(size, size, "red")
            size_label.configure(image=new_image)
            size_info.configure(text=f"Größe: {size}x{size} px")
            
        size_slider = ctk.CTkSlider(control_frame, from_=32, to=128,
                                  command=change_image_size)
        size_slider.set(64)
        size_slider.pack(pady=10)
        
        self.size_image = self.create_colored_image(64, 64, "red")
        size_label = ctk.CTkLabel(control_frame, text="", image=self.size_image)
        size_label.pack(pady=5)
        
        size_info = ctk.CTkLabel(control_frame, text="Größe: 64x64 px")
        size_info.pack(pady=5)
        
        # Status-Label für Button-Feedback
        self.status_label = ctk.CTkLabel(self.root, text="Bereit...",
                                       text_color="gray")
        self.status_label.pack(pady=10)
        
    def show_message(self, message):
        self.status_label.configure(text=message, text_color="green")
        self.root.after(2000, lambda: self.status_label.configure(
            text="Bereit...", text_color="gray"))
        
    def run(self):
        self.root.mainloop()

# App starten
if __name__ == "__main__":
    app = ImageApp()
    app.run()
""", "customtkinter5.png", "In der nächsten Lektion lernst du eine komplette Anwendung zu erstellen.", "Zurück zu Lektion 9", "Weiter zu Lektion 11", 10)

lektion11 = my_class("Lektion 11: Komplette CustomTkinter-Anwendung", 
"""
In dieser finalen Lektion erstellen wir eine vollständige CustomTkinter-Anwendung, die alle gelernten Konzepte kombiniert. Wir bauen einen modernen Task-Manager mit verschiedenen Funktionen.

Die Anwendung demonstriert professionelle Strukturierung mit separaten Klassen für verschiedene Komponenten. Das macht den Code wartbarer und erweiterbarer.

Wir verwenden alle wichtigen CustomTkinter-Features: moderne Widgets, Tabs, Scrolling, Dialoge, Theme-Unterstützung und Event-Handling. Das zeigt, wie man eine echte Desktop-Anwendung entwickelt.

Die Anwendung speichert Daten in einer einfachen JSON-Datei (in einer echten App würdest du eine Datenbank verwenden). Das zeigt Persistenz und Datenmanagement.

Error-Handling und User-Feedback sind wichtige Aspekte professioneller Anwendungen. Wir zeigen, wie man Fehler abfängt und dem Benutzer klare Rückmeldungen gibt.

Die modulare Struktur erlaubt einfache Erweiterungen. Du könntest weitere Features wie Kategorien, Deadlines, Prioritäten oder Export-Funktionen hinzufügen.
""", 
"""
import customtkinter as ctk
import json
import os
from datetime import datetime
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TaskManager:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("ModernTask - Task Manager")
        self.root.geometry("900x700")
        self.root.minsize(700, 500)
        
        # Datenfile
        self.data_file = "tasks.json"
        self.tasks = self.load_tasks()
        
        self.setup_ui()
        self.refresh_task_list()
        
    def load_tasks(self):
        ""Lädt Tasks aus JSON-Datei""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
            return []
            
    def save_tasks(self):
        ""Speichert Tasks in JSON-Datei""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False
            
    def setup_ui(self):
        # Header
        header_frame = ctk.CTkFrame(self.root, height=80)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(header_frame, text="🚀 ModernTask Manager",
                                 font=ctk.CTkFont(size=28, weight="bold"))
        title_label.pack(side="left", padx=20, pady=20)
        
        # Stats
        self.stats_label = ctk.CTkLabel(header_frame, text="",
                                      font=ctk.CTkFont(size=14))
        self.stats_label.pack(side="right", padx=20, pady=20)
        
        # Main Container
        main_container = ctk.CTkFrame(self.root)
        main_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Sidebar für Eingabe
        sidebar = ctk.CTkFrame(main_container, width=300)
        sidebar.pack(side="left", fill="y", padx=(0, 10))
        sidebar.pack_propagate(False)
        
        # Task-Eingabe Bereich
        input_frame = ctk.CTkFrame(sidebar)
        input_frame.pack(fill="x", padx=15, pady=15)
        
        ctk.CTkLabel(input_frame, text="✏️ Neue Aufgabe",
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(15, 10))
        
        self.task_entry = ctk.CTkEntry(input_frame, placeholder_text="Aufgabe eingeben...",
                                     font=ctk.CTkFont(size=14), height=40)
        self.task_entry.pack(fill="x", padx=15, pady=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        self.desc_entry = ctk.CTkTextbox(input_frame, height=80,
                                       font=ctk.CTkFont(size=12))
        self.desc_entry.pack(fill="x", padx=15, pady=5)
        self.desc_entry.insert("0.0", "Beschreibung (optional)...")
        
        # Priorität
        priority_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        priority_frame.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkLabel(priority_frame, text="Priorität:").pack(side="left")
        self.priority_var = ctk.StringVar(value="Normal")
        priority_menu = ctk.CTkOptionMenu(priority_frame, variable=self.priority_var,
                                        values=["Niedrig", "Normal", "Hoch", "Urgent"])
        priority_menu.pack(side="right")
        
        # Buttons
        button_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=15, pady=15)
        
        add_btn = ctk.CTkButton(button_frame, text="➕ Hinzufügen",
                              command=self.add_task, height=35,
                              font=ctk.CTkFont(size=14, weight="bold"))
        add_btn.pack(fill="x", pady=2)
        
        clear_btn = ctk.CTkButton(button_frame, text="🗑️ Alle löschen",
                                command=self.clear_all_tasks,
                                fg_color="red", hover_color="darkred",
                                height=35)
        clear_btn.pack(fill="x", pady=2)
        
        # Filter-Bereich
        filter_frame = ctk.CTkFrame(sidebar)
        filter_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        ctk.CTkLabel(filter_frame, text="🔍 Filter",
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(15, 10))
        
        self.filter_var = ctk.StringVar(value="Alle")
        filter_menu = ctk.CTkOptionMenu(filter_frame, variable=self.filter_var,
                                      values=["Alle", "Offen", "Erledigt"],
                                      command=self.filter_tasks)
        filter_menu.pack(padx=15, pady=(0, 15))
        
        # Task-Liste Bereich
        list_frame = ctk.CTkFrame(main_container)
        list_frame.pack(side="right", fill="both", expand=True)
        
        list_header = ctk.CTkFrame(list_frame, height=50)
        list_header.pack(fill="x", padx=15, pady=(15, 5))
        list_header.pack_propagate(False)
        
        ctk.CTkLabel(list_header, text="📋 Aufgaben-Liste",
                    font=ctk.CTkFont(size=18, weight="bold")).pack(side="left", pady=15)
        
        # Scrollbare Task-Liste
        self.task_list_frame = ctk.CTkScrollableFrame(list_frame, height=400)
        self.task_list_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warnung", "Bitte gib eine Aufgabe ein!")
            return
            
        desc_text = self.desc_entry.get("0.0", "end-1c").strip()
        if desc_text == "Beschreibung (optional)...":
            desc_text = ""
            
        new_task = {
            "id": len(self.tasks) + 1,
            "text": task_text,
            "description": desc_text,
            "priority": self.priority_var.get(),
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        
        # Eingabefelder leeren
        self.task_entry.delete(0, "end")
        self.desc_entry.delete("0.0", "end")
        self.desc_entry.insert("0.0", "Beschreibung (optional)...")
        
        self.refresh_task_list()
        
    def toggle_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                break
        self.save_tasks()
        self.refresh_task_list()
        
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        self.refresh_task_list()
        
    def clear_all_tasks(self):
        if messagebox.askyesno("Bestätigung", "Wirklich alle Aufgaben löschen?"):
            self.tasks = []
            self.save_tasks()
            self.refresh_task_list()
            
    def filter_tasks(self, filter_value):
        self.refresh_task_list()
        
    def refresh_task_list(self):
        # Alte Widgets löschen
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
            
        # Filter anwenden
        filter_value = self.filter_var.get()
        filtered_tasks = self.tasks
        
        if filter_value == "Offen":
            filtered_tasks = [t for t in self.tasks if not t["completed"]]
        elif filter_value == "Erledigt":
            filtered_tasks = [t for t in self.tasks if t["completed"]]
            
        # Prioritäts-Sortierung
        priority_order = {"Urgent": 0, "Hoch": 1, "Normal": 2, "Niedrig": 3}
        filtered_tasks.sort(key=lambda x: (x["completed"], priority_order.get(x["priority"], 2)))
        
        # Tasks anzeigen
        for task in filtered_tasks:
            self.create_task_widget(task)
            
        # Stats aktualisieren
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        self.stats_label.configure(text=f"📊 {completed}/{total} erledigt")
        
        if not filtered_tasks:
            empty_label = ctk.CTkLabel(self.task_list_frame, 
                                     text="🎉 Keine Aufgaben gefunden!",
                                     font=ctk.CTkFont(size=16),
                                     text_color="gray")
            empty_label.pack(pady=50)
            
    def create_task_widget(self, task):
        # Task-Container
        task_frame = ctk.CTkFrame(self.task_list_frame)
        task_frame.pack(fill="x", pady=5, padx=5)
        
        # Checkbox und Text
        left_frame = ctk.CTkFrame(task_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Checkbox
        checkbox_var = ctk.BooleanVar(value=task["completed"])
        checkbox = ctk.CTkCheckBox(left_frame, text="", variable=checkbox_var,
                                 command=lambda: self.toggle_task(task["id"]))
        checkbox.pack(side="left")
        
        # Text-Bereich
        text_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True, padx=(10, 0))
        
        # Prioritäts-Farben
        priority_colors = {
            "Urgent": "red", "Hoch": "orange", "Normal": "blue", "Niedrig": "green"
        }
        
        task_text = task["text"]
        if task["completed"]:
            task_text = f"✓ {task_text}"
            text_color = "gray"
        else:
            text_color = priority_colors.get(task["priority"], "white")
            
        title_label = ctk.CTkLabel(text_frame, text=task_text,
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 text_color=text_color, anchor="w")
        title_label.pack(fill="x")
        
        if task["description"]:
            desc_label = ctk.CTkLabel(text_frame, text=task["description"],
                                    font=ctk.CTkFont(size=11),
                                    text_color="gray", anchor="w")
            desc_label.pack(fill="x")
            
        # Info-Zeile
        info_text = f"{task['priority']} • {task['created']}"
        info_label = ctk.CTkLabel(text_frame, text=info_text,
                                font=ctk.CTkFont(size=10),
                                text_color="darkgray", anchor="w")
        info_label.pack(fill="x")
        
        # Delete-Button
        delete_btn = ctk.CTkButton(task_frame, text="🗑️", width=40,
                                 command=lambda: self.delete_task(task["id"]),
                                 fg_color="transparent", text_color="red",
                                 hover_color="darkred")
        delete_btn.pack(side="right", padx=10)
        
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

# App starten
if __name__ == "__main__":
    app = TaskManager()
    app.run()
""", "customtkinter6.png", "Gratulation! Du hast alle Lektionen abgeschlossen.", "Zurück zu Lektion 10", "Kurs abgeschlossen!", 11)


tkinter_class = [lektion1, lektion2, lektion3, lektion4, lektion5, lektion6, lektion7, lektion8, lektion9, lektion10, lektion11]