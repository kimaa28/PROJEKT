# Lernportal – Version 1 (Branch: master)

Lokale Desktop-Lernplattform mit **Python, CustomTkinter, HTML und CGI**.

> **Hinweis:** Dies ist die **erste Version**. Die neue Version mit moderner Oberfläche und PDF-Anzeige liegt im Branch **`lerntrack.2.0`**.

---

## Wichtig: Python-Version

Diese Version nutzt **CGI** (das Python-Modul `cgi`). Seit **Python 3.13** ist dieses Modul **deprecated**
(Entfernung geplant in Python 3.15). Dadurch läuft die App nur mit **Python 3.11/3.12** –
in der Regel benötigst du dafür **pyenv** (siehe `GUI/.python-version`).

---

## Features

- Login / Registrierung / Passwort-Reset (lokal, JSON, Passwörter gehasht)
- GUI mit CustomTkinter
- Lernlektionen als lokale HTML-Seiten (HTML-, Python-, Tkinter-, Linux-, CGI-Module)
- CGI-basierte Fragebögen
- Lokaler HTTP-Server
- Fortschritts-Tracking über JSON

---

## Projektstruktur

```
lernportal/
│
├── GUI/                      # CustomTkinter-Anwendung
│   ├── test_dash.py          # Einstiegspunkt (Hauptfenster)
│   ├── login.py              # Login-Ansicht
│   ├── register.py           # Registrierung
│   ├── reset.py              # Passwort-Reset
│   ├── html_class.py         # HTML-Lektionen
│   ├── python_lesson_class.py# Python-Lektionen
│   ├── CGI_class.py          # CGI-Lektionen
│   ├── LINUX_class.py        # Linux-Lektionen
│   ├── Tkinter_class.py      # Tkinter-Lektionen
│   ├── image/                # Icons und Bilder
│   └── index.json / tasks.json
│
├── webseite/html/            # HTML-Lernseiten der Module
│   ├── Lektion1.html – Lektion11.html
│   ├── cgi/ / linux/ / py_l/ / tkinter/
│   └── index.html
│
├── cgi-bin/                  # CGI-Skripte für Fragebögen
│   ├── gear_cgi.py
│   └── redirect.py
│
├── daten/                    # lokale Nutzerdaten
│   └── Passlib.json          # (gitignored, nur lokal)
│
├── index.html
└── README.md
```

---

## Ausführen

1. **Lokalen HTTP-Server mit CGI starten** (Python 3.11/3.12):

   ```bash
   python3 -m http.server --cgi
   ```

2. **GUI starten:**

   ```bash
   python GUI/test_dash.py
   ```

---

## Technologien

- Python 3.11 / 3.12
- CustomTkinter
- HTML / CSS
- CGI (Common Gateway Interface)
- JSON (Datenhaltung)
