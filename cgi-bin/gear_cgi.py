#!/usr/bin/env python3
import os
import json
import cgi, cgitb
import sys

#TODO manage the json for all user

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
index_h = form.getvalue("index")
index_p = form.getvalue("index_p")
index_t = form.getvalue("index_t")
index_c = form.getvalue("index_c")
index_l = form.getvalue("index_l")

index_list = {
    0: index_h,
    1 : index_p,
    2 : index_t,
    3 : index_c,
    4 : index_l
}
for key, value in index_list.items():
    if value:
        index = value
        if value == index:
            try:
                index = int(index)
            except ValueError as e:
                index = 1
            link_list = [f"http://127.0.0.1:8000/webseite/html/Lektion{index}.html", f"http://127.0.0.1:8000/webseite/html/py_l/Lesson{index}.html", f"http://127.0.0.1:8000/webseite/html/tkinter/Lesson{index}.html",f"http://127.0.0.1:8000/webseite/html/cgi/Lesson{index}.html",f"http://127.0.0.1:8000/webseite/html/linux/Lesson{index}.html"]
            redirect_url = link_list[key]



# JSON laden
json_change = load_index(path)

# Prüfe JSON Struktur
if "Done" not in json_change:
    json_change["Done"] = {"html": [], "python": [], "tkinter": [], "cgi": [], "linux": []}

if "Current" not in json_change:
    json_change["Current"] = {"None": 0}

# Logik
try:
    for key, value in {"html": index_h,"python": index_p,"tkinter": index_t,"cgi": index_c,"linux": index_l}:
        if value :
            if index -1 in json_change["Done"][key]:
                json_change["Current"] = {key : f"lektion{index}"}
                save_index(path, json_change)
            else:
                json_change["Done"][key].append(index - 1)
                json_change["Current"] = {key: f"lektion{index}"}
                json_change["Done"][key].sort()
                save_index(path, json_change)
except Exception as e:
    pass 

# try:
#     if not index_h:
#         if index - 1 in json_change["Done"]["python"]:
#             json_change["Current"] = {"python": f"lektion{index}"}
#             save_index(path, json_change)
#         else:
#             json_change["Done"]["python"].append(index)
#             json_change["Current"] = {"python": f"lektion{index}"}
#             json_change["Done"]["python"].sort()
#             save_index(path, json_change)
#     else:
#         if index - 1 in json_change["Done"]["html"]:
#             json_change["Current"] = {"html": f"lektion{index}"}
#             save_index(path, json_change)
#         else:
#             json_change["Done"]["html"].append(index)
#             json_change["Current"] = {"html": f"lektion{index}"}
#             json_change["Done"]["html"].sort()
#             save_index(path, json_change)

     # TODO i can ameliorate the struktur and the raise error 

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