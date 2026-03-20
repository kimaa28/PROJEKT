# 📚 Lernportal (Python + CustomTkinter)

Ein lokales Lernportal, entwickelt mit Python und CustomTkinter.
Die Anwendung kombiniert eine Desktop-GUI mit HTML-Inhalten und speichert den Lernfortschritt der Nutzer lokal über JSON-Dateien.

👉 Ziel des Projekts ist es, eine einfache und flexible Lernumgebung zu schaffen, die ohne externe Server oder Datenbanken funktioniert.

---

## 🚀 Features

* 🔐 Login-System (lokal über JSON)
* 🖥️ GUI mit CustomTkinter (Dashboard + Navigation)
* 📄 Integration von HTML-Lernseiten
* 📊 Fortschritts-Tracking pro Benutzer
* ⚙️ Lokaler HTTP-Server mit Python (inkl. CGI-Skripte)
* 🧠 Quiz / Fragebögen über CGI
* 💾 Speicherung aller Daten lokal (keine Cloud)

---

## 🧱 Projektstruktur

```
lernportal/
├── gui/              # GUI (CustomTkinter)
├── data/             # JSON Daten (User + Fortschritt)
├── webseite/         # HTML Lerninhalte  aber wird in der neue version entfernt
├── cgi-bin/           # Lokaler Server + CGI aber wird in der neue version entfernt
└── README.md
```

---

## 🧠 Technischer Ansatz

Das Projekt kombiniert mehrere Technologien:

* **Frontend (GUI):** CustomTkinter
* **Web-Inhalte:** HTML + CSS
* **Backend (lokal):** Python
* **Daten:** JSON (kein Datenbank-System)
* **Server:** Python HTTP Server (früher mit CGI)

👉 Der Nutzer greift ausschließlich über die Desktop-App auf Inhalte zu.

---

## ⚠️ Hinweis zu CGI

Die ursprüngliche Version nutzte **CGI mit dem Python HTTP Server**.
Da CGI ab Python 3.13 entfernt wurde, wird dieser Teil aktuell überarbeitet.

➡️ Alternative Ansätze (in Planung):

* Umstieg auf lokale API (z. B. Flask)
* Direkte Verarbeitung in Python ohne CGI

---

## 🆕 Aktuelle Erweiterung (in Entwicklung)

Neue Features in einer separaten Branch:

📄 **PDF-Kursverwaltung**

* Upload von PDF-Lernmaterialien
* Lokale Speicherung
* Schnelles Wiederfinden von Kursen
* Integration in das Dashboard

👉 Ziel: Lernportal mehr wie eine echte Lernplattform machen

## 💡 Motivation

Dieses Projekt wurde entwickelt, um praktische Erfahrungen in folgenden Bereichen zu sammeln:

* Python-Anwendungsentwicklung
* GUI-Design
* Systemstrukturierung
* Arbeiten mit lokalen Daten
* Kombination von Desktop + Web-Technologien

---

## 🔗 Author

Jordan Kitio Zangio
Informatik-Student (2. Semester)
GitHub: https://github.com/kimaa28
