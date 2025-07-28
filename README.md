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
| ✅ **1. Connect GUI with modules** | Button click → open HTML page and save progress                | 1–2 days       |
| ✅ **2. Create HTML pages**        | Content per module (intro, text formatting, lists, etc.)       | 2–3 days       |
| ✅ **3. Integrate CGI scripts**    | Send and save progress via HTML form                           | 1–2 days       |
| ✅ **4. Improve JSON handling**    | Check progress, avoid duplicates, optionally include timestamp | 1 day          |
| ✅ **5. Dashboard view**           | Show module progress in GUI (green checkmarks, etc.)           | 1–2 days       |
| ✅ **6. Testing & optimization**   | Check for bugs, clean up design                                | 1 day          |

I'm student at a germany university so i can't speak englisch very good. I already learn Html, css and python so i try to make an app and a learn plattform like a site web but all the progress would be save on the app with mein python. people can just acces to the 
lewrn platform with the app.
i choice to add something like tabview, this is bether than tkraise if you already login. in my daschboard i use some button with specifics tabview changer to show some frame. the daschboard muss be an another class then we can import dash_class in haupt_class to manage it.
