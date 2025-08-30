from html_class import html_list
from python_lesson_class import python_class
from CGI_class import cgi_class
from LINUX_class import linux_class
from Tkinter_class import tkinter_class
import os




def create_html_file(directory, filename, content):
    # Stelle sicher, dass der Ordner existiert
    os.makedirs(directory, exist_ok=True)

    # Erstelle den vollständigen Pfad zur Datei
    filepath = os.path.join(directory, filename)
    

    # Schreibe den Inhalt in die HTML-Datei
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath  # Optional, falls du den Pfad später brauchst


   
def html(titel ,haupttitel, body, code, beschreibung,img_1, img_2, anw, preview, next, index):
    return f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titel}</title>
    <style>
        body {{
            font-family: PT 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif, sans-serif;
            margin: 0;
            padding: 20px;
        }}

        #back_to {{
            margin-top: 20px;
            font-family: Arial, sans-serif;
            width: 1200px; /* i would make a root to defined all this value */
            width: 50%;
            margin: 0 auto;
            padding: 20px;
        }}

        #Zurück{{
            text-decoration: none;
            margin: auto;        /* i would make a root to defined all this value */
            color: #000000;
            border-radius: 10px;
            font-size: 20px; 
            padding: 10px;
        }}
        #Zurück:hover {{
            color: #7daa8c;
            background-color: #f0f0f0;
            transition: 0.3s;
        }}
        #content {{
            /* i would make a root to defined all this value */
            padding-left: 20px;
           
            padding-bottom: 10px;
        }}
        #section1 {{
            width: 50%; /* i would make a root to defined all this value */
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow:0 4px 5px rgba(0, 0, 0, 0.3);
            border-radius: 10px;
        }}
        #content1 {{
            margin: 20px;
            padding: 40px;
            background-color: #b2c0b815;
            border-radius: 20px;
            display: flex;   
            white-space: pre-wrap;      /* Zeilen werden umbrochen */
            word-wrap: break-word;      /* Lange Wörter umbrechen */     

        }}
        #img {{
            text-align: center;
            margin: 20px;
            background-color: #d3d3d381;
            border-radius: 20px;
        }}
        .anw {{
            margin-left: 20px;
            padding: 10px;
            
        
        }}
        #buttons {{
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            padding: 20px;
        }}
        #display1 {{
            text-decoration: none;
            color: #7d7272;
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            background-color: #f0f0f0;
        }}
        #display1:hover {{
            color: #111513;
            background-color: #e0e0e0;
        }}
        #display2 {{
            text-decoration: none;
            color: #ffffff;
            font-size: 20px;
            padding: 10px;
            border-radius: 10px;
            transition: background-color 0.3s, color 0.3s;
            background-color: #242424;
        }}
        #display2:hover {{
            color: #ffffff;
            background-color: #2a72b6;
        }}
        #text{{
            font-size:23px;
        }}
        #anw1{{
         font-size:18px;
        }}
    </style>
</head>
<body>
    <div id="back_to">
    <p> <a> ⇦ Zurück zum Kurs</a></p>
    </div>
    <section id="section1">
        <div id="content">
            <h1>{haupttitel}</h1>
                <p id="text">{body}</p>
        </div>

        <div id="content1">
            <pre style=" white-space: pre-wrap;
            word-wrap: break-word;">{code}</pre>
        </div>
        <div class="anw">
            <p>Bildbeschreibung des beispiel:</p>
            <p>{beschreibung}</p>
        </div>
        <div id="img">
            <img src="{img_1}" alt="Placeholder Image" style="width:100%; height:auto; border-radius:10px;">
            <img src="{img_2}" alt="Placeholder Image" style="width:100%; height:auto; border-radius:10px;">
          
        </div>
        <div class="anw">
            <p id="anw1">{anw}</p>
        </div>

       <form action="../../cgi-bin/gear_cgi.py" method="post" id="buttons">
            <input type="hidden" name="user" id="userField">
            <button type="submit" name="index" value="{index - 1}" id="display1">{preview}</button>
            <button type="submit" name="index" value="{index + 1}" id="display2">{next}</button>
        </form>


        <script>
        // URL-Parameter auslesen
            const params = new URLSearchParams(window.location.search);
            const user = params.get("user");

            // falls user vorhanden, in das versteckte Feld einfügen
            if (user) {{
                document.getElementById("userField").value = user;
            }}
        </script>

    </section>
</body>
</html>
"""
titel_list = [titel.titel_lesson for titel in html_list]


def site_name(id):
    return f"""Lektion{id}.html"""

# create all html courses
for index, (titel, ele) in enumerate(zip(titel_list, html_list)):
    create_html_file("../webseite/html", site_name(ele.index), html(titel, ele.titel_lesson, ele.body, ele.code, ele.beschreibung,ele.img[0], ele.img[1], ele.next_anw, site_name(ele.index-1), site_name(ele.index+1), ele.index ))

#python modul for python courses
def courses(titel ,haupttitel, body, code,img_1, anw, preview, next, id, index):
    return f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titel}</title>
    <style>
        body {{
            font-family: PT 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif, sans-serif;
            margin: 0;
            padding: 20px;
        }}

        #back_to {{
            margin-top: 20px;
            font-family: Arial, sans-serif;
            width: 1200px; /* i would make a root to defined all this value */
            width: 50%;
            margin: 0 auto;
            padding: 20px;
        }}

        #Zurück{{
            text-decoration: none;
            margin: auto;        /* i would make a root to defined all this value */
            color: #000000;
            border-radius: 10px;
            font-size: 20px; 
            padding: 10px;
        }}
        #Zurück:hover {{
            color: #7daa8c;
            background-color: #f0f0f0;
            transition: 0.3s;
        }}
        #content {{
            /* i would make a root to defined all this value */
            padding-left: 20px;
           
            padding-bottom: 10px;
        }}
        #section1 {{
            width: 50%; /* i would make a root to defined all this value */
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow:0 4px 5px rgba(0, 0, 0, 0.3);
            border-radius: 10px;
        }}
        #content1 {{
            margin: 20px;
            padding: 40px;
            background-color: #b2c0b815;
            border-radius: 20px;
            display: flex;   
            white-space: pre-wrap;      /* Zeilen werden umbrochen */
            word-wrap: break-word;      /* Lange Wörter umbrechen */     

        }}
        #img {{
            text-align: center;
            margin: 20px;
            background-color: #d3d3d381;
            border-radius: 20px;
        }}
        .anw {{
            margin-left: 20px;
            padding: 10px;
            
        
        }}
        #buttons {{
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            padding: 20px;
        }}
        #display1 {{
            text-decoration: none;
            color: #7d7272;
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            background-color: #f0f0f0;
        }}
        #display1:hover {{
            color: #111513;
            background-color: #e0e0e0;
        }}
        #display2 {{
            text-decoration: none;
            color: #ffffff;
            font-size: 20px;
            padding: 10px;
            border-radius: 10px;
            transition: background-color 0.3s, color 0.3s;
            background-color: #242424;
        }}
        #display2:hover {{
            color: #ffffff;
            background-color: #2a72b6;
        }}
        #text{{
            font-size: 23px;
         }}
        #anw1{{
         font-size:20px;
        }}
    </style>
</head>
<body>
    <div id="back_to">
    <p> <a> ⇦ Zurück zum Kurs</a></p>
    </div>
    <section id="section1">
        <div id="content">
            <h1>{haupttitel}</h1>
                <p id="text">{body}</p>
        </div>

        <div id="content1">
            <p id="anw1">{code}</p>

        </div>
        <div class="anw">
            <p>Bildbeschreibung des beispiel:</p>
            <p></p>
        </div>
        
        <div id="img">
            <img src="{img_1}" alt="Placeholder Image" style="width:100%; height:auto; border-radius:10px;">
          
        </div>
        <div class="anw">
            <p >{anw}</p>
        </div>

       
        <form action="../../../cgi-bin/gear_cgi.py" method="post" id="buttons">
            <input type="hidden" name="user" id="userField">
            <button type="submit" name={id} value="{index - 1}" id="display1">{preview}</button>
            <button type="submit" name={id} value="{index + 1}" id="display2">{next}</button>
        </form>

        <script>
        // URL-Parameter auslesen
            const params = new URLSearchParams(window.location.search);
            const user = params.get("user");

            // falls user vorhanden, in das versteckte Feld einfügen
            if (user) {{
                document.getElementById("userField").value = user;
            }}
        </script>
    </section>
</body>
</html>
"""

def courses_site_name(id):
    return f"""Lesson{id}.html"""

  #neue in dex
  #destination
  # titel list

courses_dict = {
    "python": {
            "id": "index_p",
            "pfad": "../webseite/html/py_l",
            "titel": [titel.titel_lesson for titel in python_class],
            "class": python_class
               },
    "CGI": {
            "id": "index_c",
            "pfad": "../webseite/html/cgi",
            "titel": [titel.titel_lesson for titel in cgi_class],
            "class": cgi_class
    },
    "Linux": {
            "id": "index_l",
            "pfad": "../webseite/html/linux",
            "titel": [titel.titel_lesson for titel in linux_class],
            "class": linux_class
    },
    "Tkinter":{
            "id": "index_t",
            "pfad": "../webseite/html/tkinter",
            "titel": [titel.titel_lesson for titel in tkinter_class],
            "class": tkinter_class
    }

}

for key, value in courses_dict.items():
    for index, (titel, ele) in enumerate(zip(value["titel"], value["class"])):
        create_html_file( value["pfad"], courses_site_name(ele.index), courses(titel, ele.titel_lesson, ele.body, ele.code, ele.img, ele.next_anw, courses_site_name(ele.index-1), courses_site_name(ele.index+1), value["id"],ele.index))
# i am proud of me, just one line to resume 3 workingshours 