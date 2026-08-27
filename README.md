# Lernportal – Version 1 (Branch: master)

Local desktop learning platform with **Python, CustomTkinter, HTML and CGI**.

> **Note:** This is the **first version**. The new version with a modern interface and PDF viewer is in the **`lerntrack.2.0`** branch.

---

## Important: Python Version

This version uses **CGI** (the Python `cgi` module). Since **Python 3.13** this module is **deprecated**
(removal planned for Python 3.15). As a result, the app only runs with **Python 3.11/3.12** –
you will usually need **pyenv** for that (see `GUI/.python-version`).

---

## Features

- Login / Registration / Password reset (local, JSON, passwords hashed)
- GUI with CustomTkinter
- Learning lessons as local HTML pages (HTML, Python, Tkinter, Linux, CGI modules)
- CGI-based questionnaires
- Local HTTP server
- Progress tracking via JSON

---

## Project Structure

```
lernportal/
│
├── GUI/                      # CustomTkinter application
│   ├── test_dash.py          # Entry point (main window)
│   ├── login.py              # Login view
│   ├── register.py           # Registration
│   ├── reset.py              # Password reset
│   ├── html_class.py         # HTML lessons
│   ├── python_lesson_class.py# Python lessons
│   ├── CGI_class.py          # CGI lessons
│   ├── LINUX_class.py        # Linux lessons
│   ├── Tkinter_class.py      # Tkinter lessons
│   ├── image/                # Icons and images
│   └── index.json / tasks.json
│
├── webseite/html/            # HTML learning pages of the modules
│   ├── Lektion1.html – Lektion11.html
│   ├── cgi/ / linux/ / py_l/ / tkinter/
│   └── index.html
│
├── cgi-bin/                  # CGI scripts for questionnaires
│   ├── gear_cgi.py
│   └── redirect.py
│
├── daten/                    # local user data
│   └── Passlib.json          # (gitignored, local only)
│
├── index.html
└── README.md
```

---

## Running

1. **Start a local HTTP server with CGI** (Python 3.11/3.12):

   ```bash
   python3 -m http.server --cgi
   ```

2. **Start the GUI:**

   ```bash
   python GUI/test_dash.py
   ```

---

## Technologies

- Python 3.11 / 3.12
- CustomTkinter
- HTML / CSS
- CGI (Common Gateway Interface)
- JSON (data storage)