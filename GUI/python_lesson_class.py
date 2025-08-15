class my_class:
    def __init__(self, titel_lesson, body, code, img, next_anw, btn_lst, btn_nxt, index):
        self.titel_lesson = titel_lesson
        self.body = body
        self.code = code
        self.img = img
        self.next_anw = next_anw
        self.btn_lst = btn_lst
        self.btn_nxt = btn_nxt
        self.index = index


lesson1 =my_class(
    "Lektion 1: Was ist Python?",
    """
Python ist eine der beliebtesten Programmiersprachen der Welt und wurde 1991 von Guido van Rossum entwickelt.
Der Name stammt übrigens von der britischen Komikertruppe "Monty Python" - nicht von der Schlange!

Python zeichnet sich durch seine einfache, lesbare Syntax aus. Während andere Programmiersprachen
oft komplizierte Klammern und Semikolons verwenden, setzt Python auf Einrückungen und klare Struktur.
Das macht Python besonders anfängerfreundlich.

Python ist eine interpretierte Sprache, das bedeutet, du kannst Code direkt ausführen ohne ihn vorher
zu kompilieren. Python wird in vielen Bereichen eingesetzt: Webentwicklung, Datenanalyse, 
Künstliche Intelligenz, Automatisierung und wissenschaftliche Berechnungen.

In diesem ersten Beispiel siehst du ein klassisches "Hello World" Programm. Die print()-Funktion
gibt Text auf dem Bildschirm aus. Beachte, wie einfach und lesbar Python-Code ist - du kannst
wahrscheinlich schon verstehen, was passiert, ohne Programmiervorerfahrung zu haben!

Python verwendet Anführungszeichen (einfach oder doppelt) um Text (Strings) zu kennzeichnen.
Kommentare beginnst du mit dem #-Symbol - alles dahinter wird ignoriert und dient nur als Notiz.
    """,
    """# Mein erstes Python-Programm
print("Hallo Welt!")
print("Willkommen bei Python!")

# Dies ist ein Kommentar
print("Python ist großartig!")  # Kommentar am Ende der Zeile""",
    "python1.png",
    "In der nächsten Lektion lernst du Variablen und Datentypen kennen.",
    "Zurück zur Startseite",
    "Weiter zu Lektion 2",
    1
)

lesson2 = my_class(
    "Lektion 2: Variablen und Datentypen",
    """
Variablen sind wie Behälter, in denen du Daten speichern kannst. In Python musst du Variablen
nicht vorher deklarieren - du weist ihnen einfach einen Wert zu und Python erkennt automatisch
den Datentyp.

Python hat verschiedene grundlegende Datentypen:
- Strings (str): Text in Anführungszeichen
- Integers (int): Ganze Zahlen wie 42, -17, 0
- Floats (float): Dezimalzahlen wie 3.14, -2.5
- Booleans (bool): Wahrheitswerte True oder False

Du kannst Variablennamen fast frei wählen, aber sie sollten aussagekräftig sein und keine
Leerzeichen enthalten. Verwende Unterstriche für mehrere Wörter wie "mein_name".

Mit der type()-Funktion kannst du herausfinden, welchen Datentyp eine Variable hat.
Python konvertiert Datentypen automatisch wenn möglich - zum Beispiel wenn du eine 
Zahl mit einem String kombinierst.

Die f-String Syntax (f"...") ist eine moderne Art, Variablen in Text einzufügen.
Du schreibst die Variable in geschweifte Klammern {} innerhalb des Strings.
    """,
    """# Verschiedene Datentypen
name = "Anna"              # String
alter = 25                 # Integer  
groesse = 1.75             # Float
ist_student = True         # Boolean

# Ausgabe mit f-Strings
print(f"Name: {name}")
print(f"Alter: {alter}")
print(f"Größe: {groesse}m")
print(f"Student: {ist_student}")

# Datentypen anzeigen
print(f"Typ von name: {type(name)}")
print(f"Typ von alter: {type(alter)}")

# Variablen ändern
alter = 26
print(f"Neues Alter: {alter}")""",
    "python2.png",
    "Als Nächstes lernst du grundlegende Operatoren kennen.",
    "Zurück zu Lektion 1", 
    "Weiter zu Lektion 3",
    2
)

lesson3 = my_class(
    "Lektion 3: Grundlegende Operatoren",
    """
Operatoren sind Symbole, die Berechnungen und Vergleiche durchführen. Python bietet
verschiedene Arten von Operatoren für unterschiedliche Zwecke.

Arithmetische Operatoren führen mathematische Berechnungen durch:
+ (Addition), - (Subtraktion), * (Multiplikation), / (Division)
// (Ganzzahldivision), % (Modulo - Rest einer Division), ** (Potenz)

Vergleichsoperatoren vergleichen Werte und geben True oder False zurück:
== (gleich), != (nicht gleich), < (kleiner), > (größer), <= (kleiner gleich), >= (größer gleich)

Logische Operatoren verknüpfen Bedingungen:
and (und), or (oder), not (nicht)

Die Operator-Priorität in Python folgt mathematischen Regeln: Klammern zuerst, dann
Potenzen, dann Multiplikation/Division, zuletzt Addition/Subtraktion.

String-Operatoren ermöglichen das Verknüpfen und Wiederholen von Text.
Du kannst Strings mit + zusammenfügen oder mit * wiederholen.
    """,
    """# Arithmetische Operatoren
a = 10
b = 3

print(f"{a} + {b} = {a + b}")       # Addition
print(f"{a} - {b} = {a - b}")       # Subtraktion  
print(f"{a} * {b} = {a * b}")       # Multiplikation
print(f"{a} / {b} = {a / b}")       # Division
print(f"{a} // {b} = {a // b}")     # Ganzzahldivision
print(f"{a} % {b} = {a % b}")       # Modulo
print(f"{a} ** {b} = {a ** b}")     # Potenz

# Vergleichsoperatoren
x = 5
y = 8
print(f"{x} == {y}: {x == y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")

# String-Operatoren
vorname = "Max"
nachname = "Mustermann" 
vollname = vorname + " " + nachname
print(f"Vollname: {vollname}")
print("Ha" * 3)  # Ausgabe: HaHaHa""",
    "python3.png",
    "In der nächsten Lektion lernst du, wie du Eingaben vom Benutzer entgegennimmst.",
    "Zurück zu Lektion 2",
    "Weiter zu Lektion 4",
    3
)

lesson4 = my_class(
    "Lektion 4: Eingabe und Ausgabe",
    """
Die input()-Funktion ermöglicht es, Daten vom Benutzer einzulesen. Das Programm wartet,
bis der Benutzer etwas eingibt und Enter drückt. Wichtig: input() gibt immer einen String zurück!

Wenn du Zahlen einlesen möchtest, musst du sie mit int() oder float() konvertieren.
int() wandelt in ganze Zahlen um, float() in Dezimalzahlen.

Die print()-Funktion hat viele nützliche Parameter:
- sep: bestimmt das Trennzeichen zwischen mehreren Werten
- end: bestimmt, was am Ende gedruckt wird (standardmäßig ein Zeilenumbruch)

Du kannst auch formatierte Ausgaben mit verschiedenen Methoden erstellen:
- f-Strings: f"Text {variable}"  
- .format(): "Text {}".format(variable)
- % formatting: "Text %s" % variable (älter)

Für Zahlen kannst du die Anzahl der Dezimalstellen kontrollieren mit :.2f für 2 Stellen.
Mit try/except kannst du Fehler abfangen, wenn der Benutzer keine gültige Zahl eingibt.
    """,
    """# Einfache Eingabe
name = input("Wie heißt du? ")
print(f"Hallo {name}!")

# Zahlen einlesen
alter_str = input("Wie alt bist du? ")
alter = int(alter_str)  # String zu Integer konvertieren
print(f"Du bist {alter} Jahre alt.")

# Direktkonvertierung
groesse = float(input("Deine Größe in Metern: "))
print(f"Du bist {groesse:.2f}m groß.")

# Berechnungen mit Eingaben
zahl1 = int(input("Erste Zahl: "))
zahl2 = int(input("Zweite Zahl: "))
summe = zahl1 + zahl2
print(f"{zahl1} + {zahl2} = {summe}")

# Formatierte Ausgabe
preis = 49.99
print(f"Preis: {preis:.2f}€")
print("Name:", name, "Alter:", alter, sep=" - ")
print("Ende", end="!\n")""",
    "python4.png",
    "Als Nächstes lernst du bedingte Anweisungen mit if-else kennen.",
    "Zurück zu Lektion 3",
    "Weiter zu Lektion 5",
    4
)

lesson5 = my_class(
    "Lektion 5: Bedingte Anweisungen (if-else)",
    """
Bedingte Anweisungen ermöglichen es deinem Programm, Entscheidungen zu treffen.
Mit if, elif und else kannst du verschiedene Codeblöcke je nach Bedingung ausführen.

Die Syntax ist einfach:
- if Bedingung: führt Code aus, wenn Bedingung True ist
- elif Bedingung: (else if) prüft weitere Bedingungen  
- else: führt Code aus, wenn alle Bedingungen False sind

Wichtig in Python: Die Einrückung bestimmt, welcher Code zum if-Block gehört!
Verwende 4 Leerzeichen oder einen Tab für jede Einrückungsebene.

Du kannst Bedingungen mit logischen Operatoren kombinieren:
- and: beide Bedingungen müssen True sein
- or: mindestens eine Bedingung muss True sein
- not: kehrt True/False um

Vergleiche können mit Zahlen, Strings und anderen Datentypen durchgeführt werden.
Bei Strings wird alphabetisch verglichen. Du kannst auch prüfen, ob ein Wert
in einer Liste enthalten ist mit dem in-Operator.
    """,
    """# Einfache if-else Anweisung
alter = int(input("Dein Alter: "))

if alter >= 18:
    print("Du bist volljährig!")
else:
    print("Du bist noch minderjährig.")

# Mehrere Bedingungen mit elif
note = int(input("Deine Note (1-6): "))

if note == 1:
    print("Sehr gut!")
elif note == 2:
    print("Gut!")
elif note == 3:
    print("Befriedigend!")
elif note == 4:
    print("Ausreichend!")
elif note == 5:
    print("Mangelhaft!")
elif note == 6:
    print("Ungenügend!")
else:
    print("Ungültige Note!")

# Logische Operatoren
temperatur = float(input("Temperatur in °C: "))
regen = input("Regnet es? (ja/nein): ").lower()

if temperatur > 20 and regen == "nein":
    print("Perfektes Wetter für einen Spaziergang!")
elif temperatur > 20 or regen == "nein":
    print("Das Wetter ist okay.")
else:
    print("Lieber drinnen bleiben...")""",
    "python5.png",
    "In der nächsten Lektion lernst du Schleifen kennen - for und while.",
    "Zurück zu Lektion 4",
    "Weiter zu Lektion 6",
    5
)

lesson6 = my_class(
    "Lektion 6: Schleifen (for und while)",
    """
Schleifen ermöglichen es, Code mehrfach auszuführen. Python bietet zwei Haupttypen:
for-Schleifen und while-Schleifen.

For-Schleifen verwendest du, wenn du weißt, wie oft der Code ausgeführt werden soll.
Die range()-Funktion erzeugt eine Zahlenfolge:
- range(5): 0, 1, 2, 3, 4
- range(1, 6): 1, 2, 3, 4, 5  
- range(0, 10, 2): 0, 2, 4, 6, 8 (mit Schrittweite)

While-Schleifen laufen, solange eine Bedingung True ist. Achte darauf, dass sich die
Bedingung irgendwann ändert, sonst entsteht eine Endlosschleife!

Nützliche Schleifenbefehle:
- break: beendet die Schleife sofort
- continue: überspringt den Rest der aktuellen Iteration
- else bei Schleifen: wird ausgeführt, wenn die Schleife normal beendet wurde (nicht mit break)

Verschachtelte Schleifen sind Schleifen innerhalb von Schleifen - nützlich für
Tabellen oder komplexere Muster.
    """,
    """# For-Schleife mit range()
print("Zählen von 1 bis 5:")
for i in range(1, 6):
    print(f"Zahl: {i}")

# For-Schleife über Strings
wort = "Python"
for buchstabe in wort:
    print(f"Buchstabe: {buchstabe}")

# While-Schleife
zahl = 1
print("\nWhile-Schleife - Verdopplung:")
while zahl <= 100:
    print(zahl)
    zahl = zahl * 2

# Benutzereingabe mit while
while True:
    eingabe = input("Gib 'quit' ein zum Beenden: ")
    if eingabe.lower() == 'quit':
        print("Auf Wiedersehen!")
        break
    print(f"Du hast eingegeben: {eingabe}")

# Verschachtelte Schleifen - Multiplikationstabelle
print("\n3x3 Multiplikationstabelle:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Leerzeile nach jeder Reihe""",
    "python6.png", 
    "Als Nächstes lernst du Listen kennen - eine wichtige Datenstruktur.",
    "Zurück zu Lektion 5",
    "Weiter zu Lektion 7",
    6
)

lesson7 = my_class(
    "Lektion 7: Listen",
    """
Listen sind eine der wichtigsten Datenstrukturen in Python. Sie speichern mehrere Werte
in einer geordneten Reihenfolge und können verschiedene Datentypen enthalten.

Listen erstellst du mit eckigen Klammern: [1, 2, 3] oder ["a", "b", "c"]
Du kannst auch eine leere Liste erstellen: [] oder list()

Wichtige Eigenschaften von Listen:
- Indizierung: Das erste Element hat Index 0, das zweite Index 1, usw.
- Negative Indizes: -1 ist das letzte Element, -2 das vorletzte
- Veränderbar: Du kannst Elemente hinzufügen, entfernen oder ändern
- Slicing: Du kannst Teile der Liste mit [start:end] extrahieren

Nützliche Listen-Methoden:
- append(): fügt am Ende hinzu
- insert(): fügt an bestimmter Position hinzu  
- remove(): entfernt erstes Vorkommen eines Wertes
- pop(): entfernt und gibt Element an Index zurück
- len(): gibt Anzahl der Elemente zurück
- sort(): sortiert die Liste

Du kannst über Listen mit for-Schleifen iterieren oder mit enumerate() 
sowohl Index als auch Wert erhalten.
    """,
    """# Liste erstellen
fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]
zahlen = [1, 3, 5, 7, 9]
gemischt = ["Hallo", 42, 3.14, True]

print("Früchte:", fruechte)
print("Erstes Element:", fruechte[0])
print("Letztes Element:", fruechte[-1])

# Liste ändern
fruechte[1] = "Mango"  # Banane durch Mango ersetzen
print("Nach Änderung:", fruechte)

# Elemente hinzufügen
fruechte.append("Traube")
fruechte.insert(1, "Erdbeere")
print("Nach Hinzufügen:", fruechte)

# Elemente entfernen
fruechte.remove("Kiwi")
letztes = fruechte.pop()
print(f"Nach Entfernen: {fruechte}")
print(f"Letztes Element war: {letztes}")

# Über Liste iterieren
print("\nAlle Früchte:")
for i, frucht in enumerate(fruechte):
    print(f"{i+1}. {frucht}")

# Listen-Operationen
print(f"Anzahl Elemente: {len(fruechte)}")
zahlen.sort()
print(f"Sortierte Zahlen: {zahlen}")""",
    "python7.png",
    "In der nächsten Lektion lernst du Dictionaries kennen - Datenstrukturen mit Schlüssel-Wert-Paaren.",
    "Zurück zu Lektion 6", 
    "Weiter zu Lektion 8",
    7
)

lesson8 = my_class(
    "Lektion 8: Dictionaries (Wörterbücher)",
    """
Dictionaries sind Sammlungen von Schlüssel-Wert-Paaren. Während Listen über Indizes
zugreifen, verwendest du bei Dictionaries Schlüssel um auf Werte zuzugreifen.

Du erstellst ein Dictionary mit geschweiften Klammern: {"schlüssel": "wert"}
Jeder Schlüssel muss eindeutig sein und kann ein String, eine Zahl oder ein Tupel sein.
Werte können beliebige Datentypen sein.

Vorteile von Dictionaries:
- Schneller Zugriff über Schlüssel (auch bei großen Datenmengen)
- Logische Struktur für zusammengehörige Daten
- Flexible Erweiterung um neue Schlüssel-Wert-Paare

Wichtige Dictionary-Methoden:
- keys(): gibt alle Schlüssel zurück
- values(): gibt alle Werte zurück  
- items(): gibt Schlüssel-Wert-Paare zurück
- get(): sicherer Zugriff mit Standardwert
- pop(): entfernt und gibt Wert zurück
- update(): fügt mehrere Paare hinzu

Du kannst prüfen, ob ein Schlüssel existiert mit dem in-Operator.
For-Schleifen über Dictionaries iterieren standardmäßig über die Schlüssel.
    """,
    """# Dictionary erstellen
person = {
    "name": "Anna Schmidt",
    "alter": 28,
    "stadt": "Berlin",
    "beruf": "Programmiererin"
}

print("Person:", person)
print("Name:", person["name"])
print("Alter:", person["alter"])

# Sicherer Zugriff mit get()
email = person.get("email", "Keine E-Mail vorhanden")
print("E-Mail:", email)

# Werte ändern und hinzufügen
person["alter"] = 29
person["email"] = "anna@example.com"
print("Nach Änderung:", person)

# Mehrere Werte hinzufügen
person.update({
    "telefon": "0123456789",
    "verheiratet": False
})

# Über Dictionary iterieren
print("\nAlle Informationen:")
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")

# Nur Schlüssel oder Werte
print("\nAlle Schlüssel:", list(person.keys()))
print("Alle Werte:", list(person.values()))

# Verschachtelte Dictionaries
studenten = {
    "Anna": {"note": 1, "fach": "Informatik"},
    "Max": {"note": 2, "fach": "Mathematik"}
}

print(f"\nAnnas Note: {studenten['Anna']['note']}")""",
    "python8.png",
    "Als Nächstes lernst du, wie du eigene Funktionen erstellst.",
    "Zurück zu Lektion 7",
    "Weiter zu Lektion 9", 
    8
)

lesson9 = my_class( "Lektion 9: Funktionen definieren",
"""
Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen.
Sie helfen dabei, Code zu organisieren und Wiederholungen zu vermeiden.

Eine Funktion definierst du mit dem def-Schlüsselwort, gefolgt vom Funktionsnamen
und Parametern in Klammern. Der Code der Funktion wird eingerückt.

Funktionen können:
- Parameter entgegennehmen (Eingabewerte)
- Werte mit return zurückgeben
- Ohne Parameter oder return-Wert existieren
- Standardwerte für Parameter haben
- Variable Anzahl von Parametern akzeptieren

Wichtige Konzepte:
- Lokale Variablen existieren nur innerhalb der Funktion
- Globale Variablen sind überall verfügbar  
- return beendet die Funktion und gibt einen Wert zurück
- Ohne return gibt eine Funktion None zurück

Docstrings (dreifache Anführungszeichen) dokumentieren, was eine Funktion tut.
Das ist wichtig für die Lesbarkeit und Wartung des Codes.

Funktionen machen deinen Code modularer, testbarer und einfacher zu verstehen.
    """,
    """# Einfache Funktion ohne Parameter
def begruessung():
    "Gibt eine Begrüßung aus."
    print("Hallo! Willkommen bei Python!")

# Funktion mit Parametern
def begruesse_person(name, alter):
    "Begrüßt eine Person mit Namen und Alter."
    print(f"Hallo {name}! Du bist {alter} Jahre alt.")

# Funktion mit Rückgabewert  
def addiere(a, b):
    "Addiert zwei Zahlen und gibt das Ergebnis zurück."
    ergebnis = a + b
    return ergebnis

# Funktion mit Standardwerten
def stelle_vor(name, alter=0, stadt="Unbekannt"):
    "Stellt eine Person vor mit optionalen Parametern."
    return f"Ich bin {name}, {alter} Jahre alt und komme aus {stadt}."

# Funktionen aufrufen
begruessung()
begruesse_person("Max", 25)

summe = addiere(10, 20)
print(f"10 + 20 = {summe}")

# Mit Standardwerten
print(stelle_vor("Anna"))
print(stelle_vor("Bob", 30))  
print(stelle_vor("Clara", 25, "Hamburg"))

# Funktion für Berechnungen
def kreisflaeche(radius):
    "Berechnet die Fläche eines Kreises."
    pi = 3.14159
    flaeche = pi * radius ** 2
    return flaeche

radius = float(input("Radius des Kreises: "))
flaeche = kreisflaeche(radius)
print(f"Fläche: {flaeche:.2f}")""",
    "python9.png",
    "In der nächsten Lektion lernst du den Umgang mit Dateien.",
    "Zurück zu Lektion 8",
    "Weiter zu Lektion 10",
    9
)

lesson10 = my_class(
    "Lektion 10: Dateien lesen und schreiben",
"""
Das Arbeiten mit Dateien ist in Python sehr einfach. Du kannst Textdateien lesen,
schreiben und verändern. Dies ist nützlich für Datenspeicherung, Konfigurationsdateien
oder das Verarbeiten von Datenmengen.

Die open()-Funktion öffnet Dateien in verschiedenen Modi:
- 'r': Lesen (read) - Standardmodus
- 'w': Schreiben (write) - überschreibt die Datei
- 'a': Anhängen (append) - fügt am Ende hinzu
- 'r+': Lesen und Schreiben

Wichtig: Verwende immer with open() - das stellt sicher, dass die Datei
automatisch geschlossen wird, auch wenn ein Fehler auftritt.

Methoden zum Lesen:
- read(): liest die gesamte Datei
- readline(): liest eine Zeile
- readlines(): liest alle Zeilen in eine Liste

Methoden zum Schreiben:
- write(): schreibt einen String
- writelines(): schreibt eine Liste von Strings

Bei Dateipfaden achte auf das Betriebssystem: Windows verwendet Backslashes r"(\\)",
Linux und Mac verwenden Forward slashes r"(/)". Python akzeptiert beide.
"""
,
"""# Datei schreiben
dateiname = "meine_datei.txt"

# Text in Datei schreiben
with open(dateiname, 'w', encoding='utf-8') as datei:
    datei.write("Hallo Welt!\n")
    datei.write("Das ist meine erste Datei.\n")
    datei.write("Python macht Spaß!")

print(f"Datei '{dateiname}' wurde erstellt.")

# Datei lesen
with open(dateiname, 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print("Dateiinhalt:")
    print(inhalt)

# Datei zeilenweise lesen
print("\nZeilenweise lesen:")
with open(dateiname, 'r', encoding='utf-8') as datei:
    for nummer, zeile in enumerate(datei, 1):
        print(f"Zeile {nummer}: {zeile.strip()}")

# Text anhängen
with open(dateiname, 'a', encoding='utf-8') as datei:
    datei.write("\nNeue Zeile hinzugefügt!")

# Liste in Datei schreiben
einkaufsliste = ["Äpfel", "Bananen", "Brot", "Milch"]
with open("einkauf.txt", 'w', encoding='utf-8') as datei:
    for artikel in einkaufsliste:
        datei.write(f"- {artikel}\n")

# Datei existiert prüfen
import os
if os.path.exists("einkauf.txt"):
    print("Einkaufsliste wurde erstellt!")""",
    "python10.png",
    "Als Nächstes lernst du den Umgang mit Fehlern und Exceptions.",
    "Zurück zu Lektion 9",
    "Weiter zu Lektion 11",
    10
)

lesson11 = my_class(
    "Lektion 11: Fehlerbehandlung (try-except)",
    """
Fehler gehören zur Programmierung dazu. Python bietet mit try-except eine elegante
Möglichkeit, Fehler abzufangen und zu behandeln, ohne dass das Programm abstürzt.

Die Grundstruktur:
- try: Code, der einen Fehler verursachen könnte
- except: Was passiert, wenn ein Fehler auftritt
- else: Code, der ausgeführt wird, wenn kein Fehler auftritt  
- finally: Code, der immer ausgeführt wird

Häufige Fehlertypen:
- ValueError: falsche Datentyp-Konvertierung
- TypeError: falsche Datentypen für Operationen
- FileNotFoundError: Datei nicht gefunden
- KeyError: Schlüssel in Dictionary nicht vorhanden
- IndexError: Index außerhalb des Bereichs
- ZeroDivisionError: Division durch Null

Du kannst spezifische Fehler abfangen oder alle mit einem allgemeinen except.
Mit raise kannst du eigene Fehler auslösen.

Die Fehlerbehandlung macht deine Programme robuster und benutzerfreundlicher.
Statt mysteriösen Fehlermeldungen bekommen Benutzer verständliche Hinweise.
    """,
    """# Einfache Fehlerbehandlung
while True:
    try:
        zahl = int(input("Gib eine Zahl ein: "))
        ergebnis = 100 / zahl
        print(f"100 / {zahl} = {ergebnis}")
        break
    except ValueError:
        print("Das war keine gültige Zahl! Versuche es nochmal.")
    except ZeroDivisionError:
        print("Division durch Null ist nicht möglich!")

# Mehrere Fehlertypen behandeln
def datei_lesen(dateiname):
    try:
        with open(dateiname, 'r') as datei:
            return datei.read()
    except FileNotFoundError:
        return f"Fehler: Datei '{dateiname}' nicht gefunden."
    except PermissionError:
        return f"Fehler: Keine Berechtigung für '{dateiname}'."
    except Exception as e:
        return f"Unerwarteter Fehler: {e}"

# Try-except-else-finally
def sichere_division(a, b):
    try:
        ergebnis = a / b
    except ZeroDivisionError:
        print("Warnung: Division durch Null!")
        return None
    except TypeError:
        print("Fehler: Ungültige Datentypen für Division!")
        return None
    else:
        print("Division erfolgreich!")
        return ergebnis
    finally:
        print("Division-Vorgang abgeschlossen.")

# Beispiele
print(sichere_division(10, 2))
print(sichere_division(10, 0))
print(sichere_division("10", 2))

# Eigene Fehler auslösen
def validiere_alter(alter):
    if alter < 0:
        raise ValueError("Alter kann nicht negativ sein!")
    if alter > 150:
        raise ValueError("Alter scheint unrealistisch hoch!")
    return True

try:
    alter = int(input("Dein Alter: "))
    validiere_alter(alter)
    print("Alter ist gültig!")
except ValueError as e:
    print(f"Fehler: {e}")""",
    "python11.png",
    "In der nächsten Lektion lernst du Module und Bibliotheken kennen.",
    "Zurück zu Lektion 10",
    "Weiter zu Lektion 12",
    11
)

lesson12 = my_class(
    "Lektion 12: Module und Bibliotheken",
    """
Module sind Python-Dateien, die Code enthalten, den du in anderen Programmen verwenden kannst.
Python hat viele eingebaute Module, und du kannst auch eigene erstellen oder externe installieren.

Wichtige eingebaute Module:
- math: mathematische Funktionen
- random: Zufallszahlen und -auswahlen
- datetime: Datum und Zeit
- os: Betriebssystem-Funktionen
- json: JSON-Datenverarbeitung

Module importierst du mit:
- import modulname: importiert das ganze Modul
- from modulname import funktion: importiert nur bestimmte Funktionen
- import modulname as alias: gibt dem Modul einen anderen Namen

Externe Bibliotheken installierst du mit pip (Python Package Installer):
pip install bibliotheksname

Eigene Module erstellst du, indem du Python-Code in eine .py-Datei schreibst.
Diese Datei kannst du dann in anderen Programmen importieren.

Die Python Standard Library enthält über 200 Module für fast jeden Zweck.
Das macht Python so vielseitig - für die meisten Aufgaben gibt es bereits
fertige Lösungen, die du einfach importieren kannst.
    """,
    """# Math-Modul für mathematische Funktionen
import math

print(f"Pi: {math.pi}")
print(f"Quadratwurzel von 16: {math.sqrt(16)}")
print(f"2 hoch 8: {math.pow(2, 8)}")
print(f"Fakultät von 5: {math.factorial(5)}")

# Random-Modul für Zufallszahlen
import random

print(f"\nZufallszahl 1-10: {random.randint(1, 10)}")
print(f"Zufallszahl 0-1: {random.random()}")

farben = ["rot", "grün", "blau", "gelb"]
print(f"Zufällige Farbe: {random.choice(farben)}")

# Datetime für Datum und Zeit
from datetime import datetime, date

heute = date.today()
jetzt = datetime.now()

print(f"\nHeute: {heute}")
print(f"Jetzt: {jetzt.strftime('%H:%M:%S')}")
print(f"Jahr: {heute.year}, Monat: {heute.month}")

# OS-Modul für Systemfunktionen
import os

print(f"\nAktueller Ordner: {os.getcwd()}")
print(f"Dateien im Ordner: {os.listdir('.')}")

# JSON für Datenverarbeitung
import json

daten = {
    "name": "Max",
    "alter": 25,
    "hobbys": ["Lesen", "Sport", "Kochen"]
}

json_string = json.dumps(daten, ensure_ascii=False, indent=2)
print(f"\nJSON-Daten:\n{json_string}")""",
    "python12.png",
    "Als Nächstes lernst du Klassen und objektorientierte Programmierung kennen.",
    "Zurück zu Lektion 11",
    "Weiter zu Lektion 13",
    12
)

lesson13 = my_class(
    "Lektion 13: Klassen und Objekte (OOP)",
    """
Objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das Code in
Klassen und Objekte organisiert. Eine Klasse ist wie eine Bauplan, ein Objekt ist
eine konkrete Instanz dieser Klasse.

Grundkonzepte der OOP:
- Klasse: Vorlage/Bauplan für Objekte
- Objekt: konkrete Instanz einer Klasse
- Attribute: Eigenschaften eines Objekts (Variablen)
- Methoden: Funktionen, die zu einer Klasse gehören

Die __init__-Methode ist der Konstruktor - sie wird aufgerufen, wenn ein neues
Objekt erstellt wird. Der erste Parameter ist immer self (Verweis auf das Objekt selbst).

Vorteile von OOP:
- Kapselung: Daten und Funktionen gehören zusammen
- Wiederverwendbarkeit: Klassen können mehrfach verwendet werden
- Wartbarkeit: Code ist besser organisiert
- Vererbung: neue Klassen basierend auf bestehenden erstellen

Python ist vollständig objektorientiert - sogar einfache Datentypen wie int und str
sind Objekte mit Methoden. Mit dir(objekt) siehst du alle verfügbaren Methoden.
    """,
    """# Einfache Klasse definieren
class Person:
    def __init__(self, name, alter):
        "Konstruktor - wird beim Erstellen eines Objekts aufgerufen."
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        "Methode zur Vorstellung der Person."
        return f"Hallo, ich bin {self.name} und {self.alter} Jahre alt."
    
    def geburtstag(self):
        "Erhöht das Alter um 1."
        self.alter += 1
        print(f"{self.name} ist jetzt {self.alter} Jahre alt!")

# Objekte erstellen (Instanziierung)
person1 = Person("Anna", 25)
person2 = Person("Max", 30)

# Methoden aufrufen
print(person1.vorstellen())
print(person2.vorstellen())

# Attribute direkt zugreifen
print(f"{person1.name} ist {person1.alter} Jahre alt")

person1.geburtstag()

# Klasse mit mehr Funktionalität
class BankKonto:
    def __init__(self, kontoinhaber, kontostand=0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand
        self.transaktionen = []
    
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            self.transaktionen.append(f"Einzahlung: +{betrag}€")
            print(f"{betrag}€ eingezahlt. Neuer Kontostand: {self.kontostand}€")
        else:
            print("Einzahlungsbetrag muss positiv sein!")
    
    def abheben(self, betrag):
        if betrag > 0 and betrag <= self.kontostand:
            self.kontostand -= betrag
            self.transaktionen.append(f"Abhebung: -{betrag}€")
            print(f"{betrag}€ abgehoben. Neuer Kontostand: {self.kontostand}€")
        else:
            print("Ungültiger Abhebungsbetrag!")
    
    def kontoauszug(self):
        print(f"\nKonto von {self.kontoinhaber}")
        print(f"Aktueller Kontostand: {self.kontostand}€")
        print("Letzte Transaktionen:")
        for transaktion in self.transaktionen[-5:]:  # Letzte 5
            print(f"  {transaktion}")

# Bankkonto verwenden
konto = BankKonto("Anna Schmidt", 1000)
konto.einzahlen(500)
konto.abheben(200)
konto.kontoauszug()""",
    "python13.png",
    "In der nächsten Lektion lernst du Vererbung und erweiterte OOP-Konzepte.",
    "Zurück zu Lektion 12",
    "Weiter zu Lektion 14",
    13
)

lesson14 = my_class(
    "Lektion 14: Vererbung und erweiterte OOP",
    """
Vererbung ermöglicht es, neue Klassen basierend auf bestehenden zu erstellen.
Die neue Klasse (Kindklasse) erbt alle Attribute und Methoden der Elternklasse
und kann zusätzliche hinzufügen oder bestehende überschreiben.

Wichtige Konzepte:
- Elternklasse (Basisklasse, Superklasse): die ursprüngliche Klasse
- Kindklasse (abgeleitete Klasse): erbt von der Elternklasse
- super(): Zugriff auf Methoden der Elternklasse
- Überschreiben: Kindklasse definiert Methode der Elternklasse neu

Weitere OOP-Konzepte:
- Polymorphismus: gleiche Methode, unterschiedliches Verhalten
- Kapselung: private Attribute mit _ oder __
- Klassenvariablen: Variablen, die für alle Objekte einer Klasse gleich sind
- Klassenmethoden: Methoden, die auf die Klasse, nicht auf Objekte wirken

Multiple Vererbung ist möglich (von mehreren Klassen erben), sollte aber
sparsam verwendet werden. Python verwendet Method Resolution Order (MRO)
um zu bestimmen, welche Methode aufgerufen wird.

Vererbung fördert Code-Wiederverwendung und ermöglicht elegante, hierarchische
Programmstrukturen.
    """,
    """# Elternklasse
class Fahrzeug:
    def __init__(self, marke, modell, jahr):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.kilometer = 0
    
    def info(self):
        return f"{self.marke} {self.modell} ({self.jahr})"
    
    def fahren(self, km):
        self.kilometer += km
        print(f"Gefahren: {km} km. Gesamt: {self.kilometer} km")

# Kindklasse erbt von Fahrzeug
class Auto(Fahrzeug):
    def __init__(self, marke, modell, jahr, tueren):
        super().__init__(marke, modell, jahr)  # Eltern-Konstruktor aufrufen
        self.tueren = tueren
    
    def info(self):
        # Methode der Elternklasse überschreiben
        basis_info = super().info()
        return f"{basis_info} - {self.tueren} Türen"
    
    def hupen(self):
        print("Beep beep! 🚗")

# Weitere Kindklasse
class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, jahr, hubraum):
        super().__init__(marke, modell, jahr)
        self.hubraum = hubraum
    
    def info(self):
        basis_info = super().info()
        return f"{basis_info} - {self.hubraum}ccm"
    
    def wheelie(self):
        print("Wheelie! 🏍️")

# Objekte erstellen und verwenden
auto = Auto("BMW", "X3", 2020, 5)
motorrad = Motorrad("Honda", "CBR", 2021, 600)

print(auto.info())
print(motorrad.info())

auto.fahren(100)
auto.hupen()

motorrad.fahren(50)
motorrad.wheelie()

# Polymorphismus - gleiche Methode, unterschiedliches Verhalten
fahrzeuge = [auto, motorrad]

print("\nAlle Fahrzeuge:")
for fahrzeug in fahrzeuge:
    print(fahrzeug.info())  # Jedes Objekt verwendet seine eigene info()-Methode

# Klassen-Variable und -Methode
class Tier:
    anzahl_tiere = 0  # Klassenvariable
    
    def __init__(self, name, art):
        self.name = name
        self.art = art
        Tier.anzahl_tiere += 1
    
    @classmethod
    def get_anzahl(cls):
        return cls.anzahl_tiere

hund = Tier("Bello", "Hund")
katze = Tier("Mimi", "Katze")
print(f"Anzahl Tiere: {Tier.get_anzahl()}")""",
    "python14.png",
    "In der letzten Lektion lernst du erweiterte Python-Konzepte und Best Practices.",
    "Zurück zu Lektion 13",
    "Weiter zu Lektion 15",
    14
)

lesson15 = my_class(
    "Lektion 15: Erweiterte Konzepte und Best Practices",
    """
In dieser letzten Lektion lernst du wichtige erweiterte Python-Konzepte und Best Practices
für sauberen, professionellen Code.

List Comprehensions sind eine kompakte Art, Listen zu erstellen:
[ausdruck for element in iterable if bedingung]

Lambda-Funktionen sind kleine, anonyme Funktionen für einfache Operationen.
Sie werden oft mit map(), filter() und sorted() verwendet.

Generators erzeugen Werte on-demand und sparen Speicher bei großen Datenmengen.
Sie verwenden yield statt return.

Wichtige Best Practices:
- Aussagekräftige Variablen- und Funktionsnamen verwenden
- Code kommentieren und dokumentieren
- Funktionen kurz und fokussiert halten (eine Aufgabe pro Funktion)
- Konstanten in GROSSBUCHSTABEN schreiben
- PEP 8 Stil-Richtlinien befolgen (Leerzeichen, Zeilenlänge, etc.)

Debugging-Tipps:
- print()-Statements für einfaches Debugging
- Debugger verwenden für komplexere Probleme
- Exception-Handling für robuste Programme

Python-Ökosystem:
- PyPI (Python Package Index) für externe Bibliotheken
- Virtual Environments für Projekt-isolierte Abhängigkeiten
- IDEs wie PyCharm, VS Code oder Jupyter Notebooks

Herzlichen Glückwunsch! Du hast die Python-Grundlagen gemeistert!
    """,
    """# List Comprehensions
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditionelle Methode
quadrate_alt = []
for zahl in zahlen:
    if zahl % 2 == 0:
        quadrate_alt.append(zahl ** 2)

# Mit List Comprehension
quadrate_neu = [zahl ** 2 for zahl in zahlen if zahl % 2 == 0]
print("Quadrate gerader Zahlen:", quadrate_neu)

# Verschachtelte List Comprehensions
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplikationstabelle:", matrix)

# Lambda-Funktionen
# Normale Funktion
def verdoppeln(x):
    return x * 2

# Als Lambda
lambda_verdoppeln = lambda x: x * 2

print("Verdoppeln von 5:", lambda_verdoppeln(5))

# Lambda mit map(), filter(), sorted()
namen = ["Anna", "Bob", "Clara", "David"]
grosse_namen = list(map(lambda name: name.upper(), namen))
print("Große Namen:", grosse_namen)

lange_namen = list(filter(lambda name: len(name) > 3, namen))
print("Lange Namen:", lange_namen)

# Generator-Funktionen
def fibonacci_generator(n):
    "Generator für Fibonacci-Zahlen."
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Erste 10 Fibonacci-Zahlen:", list(fibonacci_generator(10)))

# Decorator-Beispiel
def zeitenmessung(func):
    "Decorator zur Zeitmessung von Funktionen."
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        ergebnis = func(*args, **kwargs)
        ende = time.time()
        print(f"{func.__name__} dauerte {ende-start:.4f} Sekunden")
        return ergebnis
    return wrapper

@zeitenmessung
def langsame_funktion():
    "Eine Funktion, die etwas Zeit braucht."
    import time
    time.sleep(1)
    return "Fertig!"

# Context Manager (with-Statement)
class DateiManager:
    def __init__(self, dateiname, modus):
        self.dateiname = dateiname
        self.modus = modus
    
    def __enter__(self):
        self.datei = open(self.dateiname, self.modus)
        return self.datei
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.datei.close()

# Verwendung
# with DateiManager("test.txt", "w") as f:
#     f.write("Test mit Context Manager")

# Best Practice Beispiele
KONSTANTE = 42  # Konstanten in Großbuchstaben

def berechne_kreisflaeche(radius):
    
    "Berechnet die Fläche eines Kreises."
    
   " Args:"
       " radius (float): Der Radius des Kreises"
        
    "Returns:"
        "float: Die Fläche des Kreises"
    
    import math
    return math.pi * radius ** 2

print("Kreisfläche (r=5):", berechne_kreisflaeche(5))
langsame_funktion()""",
    "python15.png",
    "Herzlichen Glückwunsch! Du hast alle Python-Grundlagen erfolgreich durchlaufen!",
    "Zurück zu Lektion 14",
    "Zurück zur Startseite",
 
    15
) 

python_liste = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9,lesson10, lesson11, lesson12, lesson13, lesson14, lesson15]