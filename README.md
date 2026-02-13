# Lernportal – Offline Learning Platform

A local desktop-based learning platform built with Python, CustomTkinter, HTML, and CGI.
The application provides an offline learning experience with persistent progress tracking using JSON storage.

---

## Features

- User authentication (local JSON-based login system)
- GUI built with CustomTkinter
- Dashboard with module progress tracking
- Local HTML learning pages
- CGI-based questionnaires
- Offline HTTP server
- Persistent user progress tracking

---

## Project Structure

lernportal/
│
├── gui/                  # CustomTkinter GUI Application
│   ├── main.py
│   ├── login.py
│   ├── dashboard.py
│   └── lernmanager.py
│
├── data/                 # Local user & progress data
│   ├── users.json
│   └── progress.json
│
├── webpages/             # HTML learning content
│   ├── html/
│   └── style/
│
├── server/               # Local HTTP server & CGI scripts
│   ├── cgi-bin/
│   ├── start_server.bat
│   └── start_server.sh
│
└── README.md

---

## Architecture

The application follows a modular architecture:

- Separation between GUI, data, and server logic
- Dedicated Dashboard class for tab management
- CustomTkinter TabView for structured navigation
- JSON-based persistence layer
- Local HTTP server with CGI scripts for questionnaires

This separation improves maintainability and scalability.

---

## Technologies Used

- Python 3
- CustomTkinter
- HTML / CSS
- CGI (Common Gateway Interface)
- JSON (data persistence)

---

## How to Run

1. Start the local server:
   - Windows: run `start_server.bat`
   - Linux/macOS: run `start_server.sh`

2. Start the GUI application:
   python gui/main.py

---

## Learning Objectives

This project was built to practice:

- Modular software architecture
- GUI development with CustomTkinter
- Client–server interaction (local HTTP + CGI)
- JSON-based data management
- Separation of concerns in software design
