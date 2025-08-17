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


def redirect_link(id, lesson):
    if lesson == "py":
        return f"http://127.0.0.1:8000/webseite/html/py_l/Lesson{id}.html"
    elif lesson == "html":
        return f"http://127.0.0.1:8000/webseite/html/Lektion{id}.html"


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


# Form Daten
form = cgi.FieldStorage()
index_html = form.getvalue("index")
index_p = form.getvalue("index_p")

if not index_html:
    index = index_p # if you start the programm on the terminal you will see an error but no panics it is normal because the don't have the value index fron formular but if you want you cant set (or 1) zu fix the error i don't it because i don't need an another json in my cgi folder
    redirect_url = redirect_link(index, "py")
else:
    index = index_html 
    redirect_url = redirect_link(index, "html")

try:
    index = int(index)
except ValueError as e:
    index = 1

# JSON laden
json_change = load_index(path)

# Prüfe JSON Struktur
if "Done" not in json_change:
    json_change["Done"] = {"html": [], "python": []}

if "Current" not in json_change:
    json_change["Current"] = {"None": 0}

# Logik
try:
    if not index_html:
        if index - 1 in json_change["Done"]["python"]:
            json_change["Current"] = {"python": f"lektion{index}"}
            save_index(path, json_change)
        else:
            json_change["Done"]["python"].append(index)
            json_change["Current"] = {"python": f"lektion{index}"}
            json_change["Done"]["python"].sort()
            save_index(path, json_change)
    else:
        if index - 1 in json_change["Done"]["html"]:
            json_change["Current"] = {"html": f"lektion{index}"}
            save_index(path, json_change)
        else:
            json_change["Done"]["html"].append(index)
            json_change["Current"] = {"html": f"lektion{index}"}
            json_change["Done"]["html"].sort()
            save_index(path, json_change)

except Exception as e:
    pass      # TODO i can ameliorate the struktur and the raise error 

# Redirect Link just for some browser who don't redirekt

print("<h3>🚀 Weiterleitung: </h3>")
print(f'<p>Falls nicht automatisch weitergeleitet: <a href="{redirect_url}">Hier klicken</a></p>')

# Auto-redirect nach 3 Sekunden
print(f'''
<script>
    setTimeout(function() {{
        window.location.href = "{redirect_url}";
    }}, 3000);
</script> 
<p><em>Automatische Weiterleitung in 3 Sekunden...</em></p>
''')

print("</body></html>")