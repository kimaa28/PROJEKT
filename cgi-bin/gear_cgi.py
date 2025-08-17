#!/usr/bin/env python3
import os
import json
import cgi, cgitb
import sys

cgitb.enable()

def load_index(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, "r") as datei:
        return json.load(datei)
        
def save_index(pfad, index_data):
    with open(pfad, "w") as datei:
        json.dump(index_data, datei, indent=4)

def site_name(id):
    return f"Lektion{id}"

def redirect_link(id):
    return f"http://127.0.0.1:8000/webseite/html/py_l/Lesson{id}.html"

def redirect_py_link(id):
    return f"http://127.0.0.1:8000/webseite/html/py_l/Lesson{id}.html"




# HTTP Header
print("Content-Type: text/html; charset=utf-8")
print()

# Debug Info HTML Start
print('''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Debug & Weiterleitung</title>
</head>
<body>''')

# DEBUG SECTION

path = "progress.json"

# Prüfe ob JSON existiert
if os.path.exists(path):
    try:
        with open(path, "r") as f:
            content = f.read()
    except Exception as e:
        pass
else:
    pass

# Form Daten
form = cgi.FieldStorage()
index_raw = form.getvalue("Index")

index = index_raw or 1
try:
    index = int(index)
except ValueError as e:
    index = 3

# JSON laden
json_change = load_index(path)

# Prüfe JSON Struktur
if "Done" not in json_change:
    json_change["Done"] = []

if "Current" not in json_change:
    json_change["Current"] = []


# Logik
try:
    if index - 1 in json_change["Done"]:
        json_change["Current"] = index
        save_index(path, json_change)
    else:
        json_change["Done"].append(index-1)
        json_change["Current"] = index
        save_index(path, json_change)
    
    
except Exception as e:
    print(f"<p><strong>❌ Fehler in Logik:</strong> {e}</p>")

# Redirect Link
redirect_url = redirect_link(index)

print("<h3>🚀 Weiterleitung: </h3>")
print(f'<p>Falls nicht automatisch weitergeleitet: <a href="{redirect_url}">Hier klicken</a></p>')

# Auto-redirect nach 3 Sekunden
print(f'''
<script>
    setTimeout(function() {{
        window.location.href = "{redirect_url}";
    }}, 2000);
</script> 
<p><em>Automatische Weiterleitung in 3 Sekunden..{os.getcwd()}.</em></p>
''')

print("</body></html>")