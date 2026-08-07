# Lerntrack 2.0 – Version 2 (Branch: lerntrack.2.0)

Komplett neu gestaltete Lern-App mit **Python, CustomTkinter und PyMuPDF**.

> **Hinweis:** Dies ist die **zweite Version** mit neuem Design und PDF-Anzeige.
> Die ältere, CGI/HTML-basierte Version liegt im Branch **`master`**.

---

## Warum Version 2?

Version 1 nutzte **CGI + HTML**. Seit **Python 3.13** ist das `cgi`-Modul **deprecated**,
wodurch die alte Version nur noch mit pyenv (Python ≤ 3.12) läuft. Version 2:

- verzichtet auf CGI → läuft direkt mit **Python 3.13** (siehe `GUI/.python-version`)
- bietet eine modernere Oberfläche mit Sidebar-Navigation
- zeigt Lernmaterial **direkt als PDF in der App** an – Datei hochladen und jederzeit wieder ansehen

---

## Features

- Neue GUI mit Sidebar-Navigation (Dashboard, Courses, Progress, Settings, Support)
- **PDF-Viewer** direkt in der App (PyMuPDF): Datei hochladen, Seiten blättern, zoomen
- **ZIP-Tools** (Dateien packen / entpacken)
- **Wissens-Datenbank** (Persönlichkeiten der Wissenschaft)
- Dashboard und Statistiken mit **matplotlib**
- Login / Registrierung / Passwort-Reset (lokal, JSON, Passwörter gehasht)
- Fortschritts-Tracking über JSON

---

## Projektstruktur

```
lernportal/
│
├── GUI/                      # CustomTkinter-Anwendung
│   ├── main.py               # Einstiegspunkt
│   ├── main_app.py           # App-Gerüst mit Sidebar-Navigation
│   ├── daschboard.py         # Dashboard (Statistik, Zitat)
│   ├── dashboard.py          # Neues Dashboard
│   ├── courses.py            # Kurse
│   ├── settings.py           # Einstellungen (Design fertig, Variablen noch offen)
│   ├── statistik.py          # Statistiken (matplotlib)
│   ├── fitzpdf.py            # PDF-Viewer
│   ├── show_pdf.py           # PDF-Viewer (Variante)
│   ├── wissen_dict.py        # Wissens-Datenbank
│   ├── zipfile.py            # ZIP-Tools
│   ├── login.py              # Login-Ansicht
│   ├── register.py           # Registrierung
│   ├── reset.py              # Passwort-Reset
│   ├── html_class.py / python_lesson_class.py
│   ├── CGI_class.py / LINUX_class.py / Tkinter_class.py
│   ├── image/                # Icons und Bilder
│   └── index.json / tasks.json
│
├── webseite/html/            # (noch vorhanden) HTML-Lernseiten
├── cgi-bin/                  # (noch vorhanden) CGI-Skripte
│
├── daten/                    # lokale Nutzerdaten
│   └── Passlib.json          # (gitignored, nur lokal)
│
└── README.md
```

---

## Ausführen

```bash
pip install customtkinter pymupdf matplotlib pillow
python GUI/main.py
```

---

## Technologien

- Python 3.13
- CustomTkinter
- PyMuPDF (fitz)
- matplotlib
- Pillow / PIL
- JSON (Datenhaltung)

---

## Status

Version 2 ist **noch in Arbeit**:

- ✅ App-Gerüst mit Sidebar-Navigation
- ✅ Dashboard, Courses, Statistik (Design + Layout)
- ✅ PDF-Viewer und Datei-Tools
- 🔧 Settings: Layout fertig, Variablen noch nicht angebunden
