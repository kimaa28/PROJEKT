lernportal/
│
├── gui/                           # CustomTkinter GUI App
│   ├── main.py                    # Entry point of the app
│   ├── login.py                   # Login window
│   ├── dashboard.py               # Homepage after login
│   └── lernmanager.py             # Course management, topics, progress
│
├── data/                          # Local user data and learning progress
│   ├── users.json                 # User login credentials
│   └── progress.json              # Progress per user
│
├── webpages/                      # Local HTML content
│   ├── html/
│   │   └── intro.html             # First learning page
│   └── style/
│       └── style.css              # Stylesheet for HTML pages
│
├── server/                        # Local HTTP + CGI scripts
│   ├── cgi-bin/
│   │   ├── questionnaire.py       # CGI quiz/questionnaire
│   │   ├── help.py                # CGI contact form or similar
│   │   └── __init__.py            # Optional (for testing)
│   │
│   ├── python-portable/           # (Optional) Portable Python (e.g. WinPython)
│   │   └── python.exe             # Portable interpreter
│   │
│   ├── start_server.bat           # Start server on Windows
│   └── start_server.sh            # Start server on Linux/macOS
│
├── README.md                      # Project description
└── .gitignore                     # (optional for Git)


| Task                              | Description                                                    | Estimated Time |
| --------------------------------- | -------------------------------------------------------------- | -------------- |
| ✅ **1. Connect GUI with modules** | Button click → open HTML page and save progress                | 10 days       |
| ✅ **2. Create HTML pages**        | Content per module (intro, text formatting, lists, etc.)       | 2–3 days       |
| ✅ **3. Integrate CGI scripts**    | Send and save progress via HTML form                           | 1–2 days       |
| ✅ **4. Improve JSON handling**    | Check progress, avoid duplicates, optionally include timestamp | 1 day          |
| ✅ **5. Dashboard view**           | Show module progress in GUI (green checkmarks, etc.)           | 10 days       |
| ✅ **6. Testing & optimization**   | Check for bugs, clean up design                                | 6 day          |

I'm a student at a university in Germany, so I can't speak English very well. I've already learned HTML, CSS, and Python, and now I'm trying to build an app and a learning platform—something like a website—but all progress will be saved locally in the app using my Json file. Users can only access the learning platform through the app.

I chose to use something like a TabView because it's better than tkraise once the user is logged in. In my dashboard, I use buttons that switch between specific tabs or frames. The dashboard should be a separate class so we can import the Dashboard class into the main class to manage it.
