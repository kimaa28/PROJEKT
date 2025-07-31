
import os


class my_class:
    def __init__(self, value1, value2, id):
        self.value1 = value1
        self.value2 = value2
        self.id = id




lektion1 = my_class("Lektion1", "je suis un con qui ne sait pas coder et utilise l'IA comme un debile", 1)
lektion2 = my_class("Lektion2", "je sais coder et je n'utilise l'IA que pour des fonctions repetitives specifiques", 2)
lektion3 = my_class("lektion 3", "je ne sia pas encore ce qui vas dans cette case ou frame mais bon ca m'es egal bitch", 3)
les = [lektion1, lektion2, lektion3]
liste = {key: wert for key, wert in enumerate(les, start=1)}

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

html_content = """
<!DOCTYPE html>
<html>
<head><title>Meine Seite</title></head>
<body>
<h1>Willkomme!</h1>
<p>Dies ist eine automatisch erstellte HTML-Datei.</p>
</body>
</html>
"""
def html(titel, id):
    return f"""
<!DOCTYPE html>
<html>
<head>{titel}</title></head>
<body>
<h1> {titel}</h1>
<p>Dies ist eine automatisch erstellte HTML-Datei.</p>
<p> je <a href="user{id-1}.html">suis</a> un <a href="user{id+1}.html"> con</a> </p>
</body>
</html>
"""
def html_file(id):
     return f"user{id}.html"

for ele in les:
     create_html_file("html", html_file(ele.id), html(ele.value1, ele.id))