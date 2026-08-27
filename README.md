# Lerntrack 2.0 – Version 2 (Branch: lerntrack.2.0)

Completely redesigned learning app with **Python, CustomTkinter and PyMuPDF**.

> **Note:** This is the **second version** with a new design and PDF viewing.
> The older, CGI/HTML-based version is in the **`master`** branch.

---

## Why Version 2?

Version 1 used **CGI + HTML**. Since **Python 3.13** the `cgi` module is **deprecated**,
which means the old version only runs with pyenv (Python ≤ 3.12). Version 2:

- drops CGI → runs directly with **Python 3.13** (see `GUI/.python-version`)
- offers a more modern interface with sidebar navigation
- displays learning material **directly as PDF in the app** – upload a file and view it again at any time

---

## Features

- New GUI with sidebar navigation (Dashboard, Courses, Progress, Settings, Support)
- **PDF viewer** directly in the app (PyMuPDF): upload files, flip through pages, zoom
- **ZIP tools** (compress / extract files)
- **Knowledge database** (personalities of science)
- Dashboard and statistics with **matplotlib**
- Login / Registration / Password reset (local, JSON, passwords hashed)
- Progress tracking via JSON

---

## Project Structure

```
lernportal/
│
├── GUI/                      # CustomTkinter application
│   ├── main.py               # Entry point
│   ├── main_app.py           # App framework with sidebar navigation
│   ├── daschboard.py         # Dashboard (statistics, quote)
│   ├── dashboard.py          # New dashboard
│   ├── courses.py            # Courses
│   ├── settings.py           # Settings (design done, variables still open)
│   ├── statistik.py          # Statistics (matplotlib)
│   ├── fitzpdf.py            # PDF viewer
│   ├── show_pdf.py           # PDF viewer (variant)
│   ├── wissen_dict.py        # Knowledge database
│   ├── zipfile.py            # ZIP tools
│   ├── login.py              # Login view
│   ├── register.py           # Registration
│   ├── reset.py              # Password reset
│   ├── html_class.py / python_lesson_class.py
│   ├── CGI_class.py / LINUX_class.py / Tkinter_class.py
│   ├── image/                # Icons and images
│   └── index.json / tasks.json
│
├── webseite/html/            # (still present) HTML learning pages
├── cgi-bin/                  # (still present) CGI scripts
│
├── daten/                    # local user data
│   └── Passlib.json          # (gitignored, local only)
│
└── README.md
```

---

## Running

```bash
pip install customtkinter pymupdf matplotlib pillow
python GUI/main.py
```

---

## Technologies

- Python 3.13
- CustomTkinter
- PyMuPDF (fitz)
- matplotlib
- Pillow / PIL
- JSON (data storage)

---

## Status

Version 2 is **still in progress**:

- ✅ App framework with sidebar navigation
- ✅ Dashboard, Courses, Statistics (design + layout)
- ✅ PDF viewer and file tools
- 🔧 Settings: layout done, variables not yet connected