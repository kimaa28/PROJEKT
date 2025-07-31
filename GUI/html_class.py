
class my_class:
    def __init__(self, titel_lesson, text1, code, beschreibung, img, next_anw, btn_lst, btn_nxt, index):
        self.titel_lesson = titel_lesson
        self.text1 = text1
        self.code = code
        self.beacreibung = beschreibung
        self.img = img
        self.next_anw = next_anw
        self.btn_lst = btn_lst
        self.btn_nxt = btn_nxt
        self.index = index




my_class(
    "Lektion 1: Was ist HTML?",
    """
HTML steht für Hypertext Markup Language und bildet das Grundgerüst jeder Webseite.
Es beschreibt, wie Inhalte strukturiert werden sollen. HTML ist keine Programmiersprache, 
sondern eine textbasierte Sprache, die es ermöglicht, Text, Bilder, Links, Tabellen und mehr
auf Webseiten darzustellen.
HTML wurde in den 1990ern entwickelt, um wissenschaftliche Dokumente im Internet verlinkbar zu machen.
Heute ist es ein zentraler Bestandteil des World Wide Web und wird weltweit verwendet.
Jede HTML-Seite besteht aus sogenannten Tags (z. B. &#x3C;p&#x3E;, &#x3C;h1&#x3E;, &#x3C;img&#x3E;), die Inhalte strukturieren.
Das Ziel von HTML ist es, die Bedeutung und Funktion des Inhalts zu definieren, nicht sein Aussehen.
    """,
    """&#x3C;html&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;Meine erste HTML-Seite&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Willkommen!&#x3C;/h1&#x3E;
    &#x3C;p&#x3E;Dies ist ein einfacher Absatz.&#x3C;/p&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
In diesem Beispiel beginnt die Datei mit einem &#x3C;html&#x3E;-Element, das alles umfasst.
Der &#x3C;head&#x3E;-Teil enthält den Titel der Seite (sichtbar im Browser-Tab),
und im &#x3C;body&#x3E; steht alles, was der Benutzer direkt sieht. Jede HTML-Seite sollte mit &#x3C;!DOCTYPE html&#x3E; starten,
um dem Browser zu sagen, dass es sich um ein HTML5-Dokument handelt.
    """,
    "code1.png",
    "In der nächsten Lektion geht es um den Aufbau einer HTML-Seite.",
    "Zurück zur Startseite",
    "Weiter zu Lektion 2",
    1
),

my_class(
    "Lektion 2: Grundstruktur von HTML",
    """
Die Grundstruktur jeder HTML-Seite beginnt mit <!DOCTYPE html>, gefolgt von einem <html>-Element.
Innerhalb dieses Elements befinden sich zwei wichtige Teile: &#x3C;head&#x3E; und &#x3C;body&#x3E;.
Im &#x3C;head&#x3E;-Teil stehen Metadaten, z. B. der Titel, Zeichencodierung oder Stylesheets.
Im &#x3C;body&#x3E; steht der sichtbare Inhalt wie Texte, Bilder, Tabellen oder Formulare.
Diese Trennung sorgt für Ordnung und bessere Wartbarkeit.
Der &#x3C;head&#x3E;-Bereich ist wie das Fundament eines Hauses - unsichtbar, aber essentiell.
Hier werden wichtige Informationen für Browser und Suchmaschinen hinterlegt.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;meta charset=&#x22;UTF-8&#x22;&#x3E;
    &#x3C;meta name=&#x22;viewport&#x22; content=&#x22;width=device-width, initial-scale=1.0&#x22;&#x3E;
    &#x3C;title&#x3E;Meine strukturierte Seite&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Haupt&#xFC;berschrift&#x3C;/h1&#x3E;
    &#x3C;p&#x3E;Dies ist der sichtbare Inhalt der Webseite.&#x3C;/p&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Der DOCTYPE-Tag zeigt dem Browser, dass es sich um HTML5 handelt.
Das lang-Attribut hilft Screenreadern und Suchmaschinen bei der Spracherkennung.
Meta-Tags definieren Zeichencodierung und Responsive-Verhalten.
Der viewport-Tag ist besonders wichtig für mobile Geräte.
    """,
    "code2.png",
    "Als Nächstes lernst du, wie man Text mit Überschriften und Absätzen gliedert.",
    "Zurück zu Lektion 1",
    "Weiter zu Lektion 3",
    2
),

my_class(
    "Lektion 3: Überschriften und Absätze",
    """
HTML bietet sechs verschiedene Überschriftenebenen von &#x3C;h1&#x3E; bis &#x3C;h6&#x3E;.
<h1> ist die wichtigste Überschrift, &#x3C;h6&#x3E; die unwichtigste.
Diese Hierarchie hilft nicht nur bei der visuellen Gliederung, sondern auch bei der
Suchmaschinenoptimierung und der Barrierefreiheit.
Absätze werden mit &#x3C;p&#x3E;-Tags erstellt und sollten thematisch zusammengehörige Inhalte gruppieren.
Zwischen Absätzen entstehen automatisch Abstände, die das Lesen erleichtern.
Eine gute Überschriftenstruktur ist wie ein Inhaltsverzeichnis - sie zeigt die Hierarchie des Inhalts.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;&#xDC;berschriften und Abs&#xE4;tze&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Hauptthema der Seite&#x3C;/h1&#x3E;
    &#x3C;p&#x3E;Dies ist ein einleitender Absatz zum Hauptthema.&#x3C;/p&#x3E;
    
    &#x3C;h2&#x3E;Erstes Unterthema&#x3C;/h2&#x3E;
    &#x3C;p&#x3E;Hier wird das erste Unterthema behandelt.&#x3C;/p&#x3E;
    
    &#x3C;h3&#x3E;Detailpunkt&#x3C;/h3&#x3E;
    &#x3C;p&#x3E;Spezifische Details zu diesem Punkt.&#x3C;/p&#x3E;
    
    &#x3C;h2&#x3E;Zweites Unterthema&#x3C;/h2&#x3E;
    &#x3C;p&#x3E;Ein weiterer wichtiger Bereich wird hier besprochen.&#x3C;/p&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Die Überschriften bilden eine logische Hierarchie: H1 für den Haupttitel,
H2 für Hauptkapitel, H3 für Unterkapitel usw.
Niemals sollte eine Überschriftenebene übersprungen werden (z.B. von H2 direkt zu H4).
Jeder Absatz behandelt idealerweise nur einen Gedanken oder eine Idee.
    """,
    "code3.png",
    "In der nächsten Lektion lernst du verschiedene Textformatierungen kennen.",  
    "Zurück zu Lektion 2",
    "Weiter zu Lektion 4",
    3
),

my_class(
    "Lektion 4: Textformatierung",
    """
HTML bietet verschiedene Tags zur Textformatierung, die sowohl visuelle als auch semantische Bedeutung haben.
&#x3C;strong&#x3E; macht Text fett und betont seine Wichtigkeit, während &#x3C;em&#x3E; Text kursiv macht und Betonung anzeigt.
&#x3C;b&#x3E; und &#x3C;i&#x3E; sind rein visuelle Tags ohne semantische Bedeutung.
Weitere nützliche Tags sind &#x3C;mark&#x3E; für Hervorhebungen, &#x3C;small&#x3E; für Kleingedrucktes,
&#x3C;del&#x3E;für durchgestrichenen Text und &#x3C;ins&#x3E; für eingefügten Text.
Die semantischen Tags sind wichtig für Screenreader und Suchmaschinen.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;Textformatierung&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Verschiedene Textformatierungen&#x3C;/h1&#x3E;
    
    &#x3C;p&#x3E;Dieser Text enth&#xE4;lt &#x3C;strong&#x3E;wichtige Informationen&#x3C;/strong&#x3E; und 
    &#x3C;em&#x3E;betonte Passagen&#x3C;/em&#x3E;.&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;Hier ist &#x3C;mark&#x3E;hervorgehobener Text&#x3C;/mark&#x3E; zu sehen.&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;&#x3C;small&#x3E;Dies ist kleingedruckter Text f&#xFC;r Zusatzinformationen.&#x3C;/small&#x3E;&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;Der alte Preis war &#x3C;del&#x3E;50&#x20AC;&#x3C;/del&#x3E;, jetzt nur &#x3C;ins&#x3E;35&#x20AC;&#x3C;/ins&#x3E;!&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;Die chemische Formel f&#xFC;r Wasser ist H&#x3C;sub&#x3E;2&#x3C;/sub&#x3E;O.&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;Einstein&#x27;s ber&#xFC;hmte Formel: E=mc&#x3C;sup&#x3E;2&#x3C;/sup&#x3E;&#x3C;/p&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
<strong> und &#x3C;em&#x3E; haben semantische Bedeutung und werden von Screenreadern unterschiedlich vorgelesen.
<mark> hebt Text hervor, als wäre er mit einem Textmarker markiert.
<sub> und &#x3C;sup&#x3E; erstellen tiefgestellten bzw. hochgestellten Text für Formeln.
&#x3C;del&#x3E; und &#x3C;ins&#x3E; zeigen Änderungen in Dokumenten an.
Diese Tags können auch kombiniert werden für komplexere Formatierungen.
    """,
    "code4.png",
    "Als Nächstes erfährst du, wie Links und Navigation funktionieren.",
    "Zurück zu Lektion 3", 
    "Weiter zu Lektion 5",
    4
),

my_class(
    "Lektion 5: Links und Navigation",
    """
Links sind das Herzstück des World Wide Web und werden mit dem &#x3C;a&#x3E;-Tag erstellt.
Das href-Attribut gibt das Ziel des Links an - das kann eine andere Webseite,
eine E-Mail-Adresse, eine Telefonnummer oder ein Anker innerhalb der Seite sein.
Links können absolut (komplette URL) oder relativ (bezogen auf die aktuelle Seite) sein.
Das target-Attribut bestimmt, wo der Link geöffnet wird.
title-Attribute bieten zusätzliche Informationen beim Hovern über den Link.
Gute Linktexte sind beschreibend und aussagekräftig für die Barrierefreiheit.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;Links und Navigation&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Verschiedene Arten von Links&#x3C;/h1&#x3E;
    
    &#x3C;nav&#x3E;
        &#x3C;a href=&#x22;#abschnitt1&#x22;&#x3E;Sprung zu Abschnitt 1&#x3C;/a&#x3E; |
        &#x3C;a href=&#x22;#abschnitt2&#x22;&#x3E;Sprung zu Abschnitt 2&#x3C;/a&#x3E;
    &#x3C;/nav&#x3E;
    
    &#x3C;p&#x3E;&#x3C;a href=&#x22;https://www.example.com&#x22; target=&#x22;_blank&#x22; 
       title=&#x22;&#xD6;ffnet externe Seite&#x22;&#x3E;Externe Webseite&#x3C;/a&#x3E;&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;&#x3C;a href=&#x22;mailto:info@example.com&#x22;&#x3E;E-Mail senden&#x3C;/a&#x3E;&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;&#x3C;a href=&#x22;tel:+49123456789&#x22;&#x3E;Anrufen&#x3C;/a&#x3E;&#x3C;/p&#x3E;
    
    &#x3C;p&#x3E;&#x3C;a href=&#x22;../andere-seite.html&#x22;&#x3E;Relative Verlinkung&#x3C;/a&#x3E;&#x3C;/p&#x3E;
    
    &#x3C;h2 id=&#x22;abschnitt1&#x22;&#x3E;Abschnitt 1&#x3C;/h2&#x3E;
    &#x3C;p&#x3E;Inhalt des ersten Abschnitts...&#x3C;/p&#x3E;
    
    &#x3C;h2 id=&#x22;abschnitt2&#x22;&#x3E;Abschnitt 2&#x3C;/h2&#x3E;
    &#x3C;p&#x3E;Inhalt des zweiten Abschnitts...&#x3C;/p&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Das &#x3C;nav&#x3E;-Element kennzeichnet Navigationsbereiche für bessere Semantik.
target="_blank" öffnet Links in einem neuen Tab/Fenster.
Anker-Links (#) springen zu Elementen mit entsprechender ID auf derselben Seite.
mailto: und tel: Links öffnen E-Mail-Programme bzw. Telefon-Apps.
Relative Links sind praktisch für interne Seitenstrukturen.
    """,
    "code5.png",
    "In der nächsten Lektion lernst du, wie Bilder in Webseiten eingebunden werden.",
    "Zurück zu Lektion 4",
    "Weiter zu Lektion 6", 
    5
),

my_class(
    "Lektion 6: Bilder einbinden",
    """
Bilder werden mit dem &#x3C;img&#x3E;-Tag eingebunden und sind selbstschließende Elemente.
Das src-Attribut gibt den Pfad zum Bild an, alt-Attribut beschreibt das Bild für Screenreader.
Immer ein alt-Attribut verwenden - es ist essentiell für die Barrierefreiheit!
width und height können die Bildgröße kontrollieren, aber CSS ist dafür besser geeignet.
Das title-Attribut zeigt einen Tooltip beim Hovern an.
Moderne Webseiten nutzen oft das <picture>-Element für responsive Bilder.
Bildformate wie WebP bieten bessere Kompression als klassische JPG/PNG.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;Bilder einbinden&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Verschiedene Arten der Bildeinbindung&#x3C;/h1&#x3E;
    
    &#x3C;h2&#x3E;Einfaches Bild&#x3C;/h2&#x3E;
    &#x3C;img src=&#x22;landschaft.jpg&#x22; alt=&#x22;Sch&#xF6;ne Berglandschaft bei Sonnenuntergang&#x22; 
         title=&#x22;Foto aus den Alpen&#x22;&#x3E;
    
    &#x3C;h2&#x3E;Bild mit Gr&#xF6;&#xDF;enangabe&#x3C;/h2&#x3E;
    &#x3C;img src=&#x22;logo.png&#x22; alt=&#x22;Firmenlogo&#x22; width=&#x22;200&#x22; height=&#x22;100&#x22;&#x3E;
    
    &#x3C;h2&#x3E;Responsive Bild mit Picture-Element&#x3C;/h2&#x3E;
    &#x3C;picture&#x3E;
        &#x3C;source srcset=&#x22;bild-gross.webp&#x22; media=&#x22;(min-width: 800px)&#x22;&#x3E;
        &#x3C;source srcset=&#x22;bild-mittel.webp&#x22; media=&#x22;(min-width: 400px)&#x22;&#x3E;
        &#x3C;img src=&#x22;bild-klein.jpg&#x22; alt=&#x22;Produktfoto eines Smartphones&#x22;&#x3E;
    &#x3C;/picture&#x3E;
    
    &#x3C;h2&#x3E;Bild als Link&#x3C;/h2&#x3E;
    &#x3C;a href=&#x22;grosses-bild.jpg&#x22;&#x3E;
        &#x3C;img src=&#x22;thumbnail.jpg&#x22; alt=&#x22;Klicken f&#xFC;r gr&#xF6;&#xDF;ere Ansicht&#x22;&#x3E;
    &#x3C;/a&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Das alt-Attribut ist nicht optional - es macht Bilder für sehbehinderte Menschen zugänglich.
Bei dekorativen Bildern kann alt="" (leer) verwendet werden.
Das &#x3C;picture&#x3E;-Element lädt je nach Bildschirmgröße unterschiedliche Bilder.
srcset ermöglicht die Bereitstellung verschiedener Bildauflösungen.
Bilder in Links werden automatisch mit einem blauen Rahmen versehen (kann per CSS entfernt werden).
    """,
    "code6.png",
    "Als Nächstes lernst du, wie Listen zur Strukturierung von Inhalten verwendet werden.",
    "Zurück zu Lektion 5",
    "Weiter zu Lektion 7",
    6
),

my_class(
    "Lektion 7: Listen erstellen",
    """
HTML bietet drei Haupttypen von Listen: geordnete Listen (&#x3C;ol&#x3E;), ungeordnete Listen (&#x3C;ul&#x3E;) 
und Beschreibungslisten (&#x3C;dl&#x3E;).
Geordnete Listen verwenden Nummerierung, ungeordnete Listen verwenden Aufz&#xE4;hlungszeichen.
Jeder Listeneintrag wird mit &#x3C;li&#x3E; erstellt.
Listen k&#xF6;nnen verschachtelt werden f&#xFC;r hierarchische Strukturen.
Beschreibungslisten bestehen aus Begriffen (&#x3C;dt&#x3E;) und Beschreibungen (&#x3C;dd&#x3E;).
Listen sind semantisch wichtig und helfen bei der Strukturierung von Inhalten.
CSS kann das Aussehen von Listen vollst&#xE4;ndig anpassen.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;Listen in HTML&#x3C;/title&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Verschiedene Listentypen&#x3C;/h1&#x3E;
    
    &#x3C;h2&#x3E;Ungeordnete Liste (Aufz&#xE4;hlung)&#x3C;/h2&#x3E;
    &#x3C;ul&#x3E;
        &#x3C;li&#x3E;&#xC4;pfel&#x3C;/li&#x3E;
        &#x3C;li&#x3E;Bananen&#x3C;/li&#x3E;
        &#x3C;li&#x3E;Orangen&#x3C;/li&#x3E;
    &#x3C;/ul&#x3E;
    
    &#x3C;h2&#x3E;Geordnete Liste (Nummerierung)&#x3C;/h2&#x3E;
    &#x3C;ol&#x3E;
        &#x3C;li&#x3E;HTML lernen&#x3C;/li&#x3E;
        &#x3C;li&#x3E;CSS verstehen&#x3C;/li&#x3E;
        &#x3C;li&#x3E;JavaScript &#xFC;ben&#x3C;/li&#x3E;
    &#x3C;/ol&#x3E;
    
    &#x3C;h2&#x3E;Verschachtelte Liste&#x3C;/h2&#x3E;
    &#x3C;ul&#x3E;
        &#x3C;li&#x3E;Frontend-Technologien
            &#x3C;ul&#x3E;
                &#x3C;li&#x3E;HTML&#x3C;/li&#x3E;
                &#x3C;li&#x3E;CSS&#x3C;/li&#x3E;
                &#x3C;li&#x3E;JavaScript&#x3C;/li&#x3E;
            &#x3C;/ul&#x3E;
        &#x3C;/li&#x3E;
        &#x3C;li&#x3E;Backend-Technologien
            &#x3C;ol&#x3E;
                &#x3C;li&#x3E;PHP&#x3C;/li&#x3E;
                &#x3C;li&#x3E;Python&#x3C;/li&#x3E;
                &#x3C;li&#x3E;Node.js&#x3C;/li&#x3E;
            &#x3C;/ol&#x3E;
        &#x3C;/li&#x3E;
    &#x3C;/ul&#x3E;
    
    &#x3C;h2&#x3E;Beschreibungsliste&#x3C;/h2&#x3E;
    &#x3C;dl&#x3E;
        &#x3C;dt&#x3E;HTML&#x3C;/dt&#x3E;
        &#x3C;dd&#x3E;Hypertext Markup Language - strukturiert Webinhalte&#x3C;/dd&#x3E;
        
        &#x3C;dt&#x3E;CSS&#x3C;/dt&#x3E;
        &#x3C;dd&#x3E;Cascading Style Sheets - gestaltet das Aussehen&#x3C;/dd&#x3E;
    &#x3C;/dl&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
&#x3C;ul&#x3E; f&#xFC;r Listen ohne bestimmte Reihenfolge (Shopping-Listen, Features).
&#x3C;ol&#x3E; f&#xFC;r Listen mit wichtiger Reihenfolge (Anleitungen, Rankings).
Verschachtelte Listen erstellen Hierarchien durch Listen innerhalb von &#x3C;li&#x3E;-Elementen.
&#x3C;dl&#x3E;, &#x3C;dt&#x3E; und &#x3C;dd&#x3E; sind perfekt f&#xFC;r Glossare und Definitionen.
Listen k&#xF6;nnen mit CSS-Eigenschaften wie list-style-type angepasst werden.
    """,
    "code7.png",
    "In der nächsten Lektion lernst du die Grundlagen von CSS kennen.",
    "Zurück zu Lektion 6",
    "Weiter zu Lektion 8",
    7
),

my_class(
    "Lektion 8: Einführung in CSS",
    """
CSS (Cascading Style Sheets) ist die Sprache, die das Aussehen von HTML-Elementen bestimmt.
Während HTML die Struktur definiert, definiert CSS das Design: Farben, Schriftarten,
Abstände, Layout und Animationen.
CSS folgt dem Prinzip der Trennung von Inhalt und Darstellung.
Es gibt drei Möglichkeiten, CSS einzubinden: inline, internal oder external.
CSS-Regeln bestehen aus Selektoren und Deklarationsblöcken.
Das Cascading-Prinzip bestimmt, welche Stile bei Konflikten angewendet werden.
CSS macht Webseiten erst richtig schön und benutzerfreundlich.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;CSS Grundlagen&#x3C;/title&#x3E;
    &#x3C;style&#x3E;
        /* Internal CSS */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 2px solid #3498db;
        }
        
        .highlight {
            background-color: #f39c12;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
        }
        
        #special-text {
            font-size: 18px;
            font-weight: bold;
            color: #e74c3c;
        }
    &#x3C;/style&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;Willkommen zu CSS!&#x3C;/h1&#x3E;
    
    &#x3C;p&#x3E;Dies ist ein normaler Absatz.&#x3C;/p&#x3E;
    
    &#x3C;p class=&#x22;highlight&#x22;&#x3E;Dieser Text hat eine besondere Hervorhebung.&#x3C;/p&#x3E;
    
    &#x3C;p id=&#x22;special-text&#x22;&#x3E;Dieser Text hat eine eindeutige ID.&#x3C;/p&#x3E;
    
    &#x3C;p style=&#x22;color: green; font-style: italic;&#x22;&#x3E;
        Dieser Text verwendet Inline-CSS.
    &#x3C;/p&#x3E;
    
    &#x3C;div&#x3E;
        &#x3C;h2&#x3E;CSS-Eigenschaften&#x3C;/h2&#x3E;
        &#x3C;ul&#x3E;
            &#x3C;li&#x3E;Farben (color, background-color)&#x3C;/li&#x3E;
            &#x3C;li&#x3E;Schriftarten (font-family, font-size)&#x3C;/li&#x3E;
            &#x3C;li&#x3E;Abst&#xE4;nde (margin, padding)&#x3C;/li&#x3E;
            &#x3C;li&#x3E;Rahmen (border)&#x3C;/li&#x3E;
        &#x3C;/ul&#x3E;
    &#x3C;/div&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Selektoren bestimmen, welche Elemente gestylt werden: Elementname (h1), Klasse (.highlight), ID (#special-text).
Deklarationen bestehen aus Eigenschaft und Wert, getrennt durch einen Doppelpunkt.
Internal CSS steht im &#x3C;style&#x3E;-Tag im <head>, External CSS in separaten .css-Dateien.
Inline-CSS hat die höchste Priorität, sollte aber sparsam verwendet werden.
Die Kaskadierung löst Konflikte zwischen verschiedenen CSS-Regeln.
    """,
    "code8.png",
    "In der nächsten Lektion vertiefst du dein Wissen über CSS-Selektoren.",
    "Zurück zu Lektion 7",
    "Weiter zu Lektion 9",
    8
),

my_class(
    "Lektion 9: CSS-Selektoren und Eigenschaften",
    """
CSS-Selektoren sind das Herzstück von CSS - sie bestimmen, welche HTML-Elemente gestylt werden.
Es gibt verschiedene Arten: Element-Selektoren, Klassen-Selektoren, ID-Selektoren,
Attribut-Selektoren und Pseudo-Selektoren.
Kombinatoren ermöglichen komplexe Auswahlen: Nachfahren, Kinder, Geschwister.
Wichtige CSS-Eigenschaften umfassen Farben, Typografie, Box-Model und Positionierung.
Die Spezifität bestimmt, welche Regeln bei Konflikten angewendet werden.
Moderne CSS bietet auch erweiterte Selektoren wie :nth-child() und :not().
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;CSS-Selektoren&#x3C;/title&#x3E;
    &#x3C;style&#x3E;
        /* Element-Selektor */
        p {
            line-height: 1.6;
            color: #333;
        }
        
        /* Klassen-Selektor */
        .info-box {
            background-color: #e8f4fd;
            border-left: 4px solid #2196F3;
            padding: 15px;
            margin: 10px 0;
        }
        
        /* ID-Selektor */
        #main-title {
            color: #1976D2;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Nachfahren-Selektor */
        .article p {
            text-indent: 20px;
        }
        
        /* Pseudo-Selektoren */
        a:hover {
            color: #FF5722;
            text-decoration: underline;
        }
        
        li:first-child {
            font-weight: bold;
        }
        
        /* Attribut-Selektor */
        input[type=&#x22;text&#x22;] {
            border: 2px solid #4CAF50;
            padding: 8px;
            border-radius: 4px;
        }
        
        /* Kombinator - direktes Kind */
        nav &#x3E; ul {
            list-style: none;
            padding: 0;
        }
    &#x3C;/style&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1 id=&#x22;main-title&#x22;&#x3E;CSS-Selektoren Demo&#x3C;/h1&#x3E;
    
    &#x3C;div class=&#x22;info-box&#x22;&#x3E;
        &#x3C;p&#x3E;Diese Box verwendet den Klassen-Selektor .info-box&#x3C;/p&#x3E;
    &#x3C;/div&#x3E;
    
    &#x3C;nav&#x3E;
        &#x3C;ul&#x3E;
            &#x3C;li&#x3E;&#x3C;a href=&#x22;#home&#x22;&#x3E;Startseite&#x3C;/a&#x3E;&#x3C;/li&#x3E;
            &#x3C;li&#x3E;&#x3C;a href=&#x22;#about&#x22;&#x3E;&#xDC;ber uns&#x3C;/a&#x3E;&#x3C;/li&#x3E;
            &#x3C;li&#x3E;&#x3C;a href=&#x22;#contact&#x22;&#x3E;Kontakt&#x3C;/a&#x3E;&#x3C;/li&#x3E;
        &#x3C;/ul&#x3E;
    &#x3C;/nav&#x3E;
    
    &#x3C;article class=&#x22;article&#x22;&#x3E;
        &#x3C;h2&#x3E;Artikel mit spezieller Formatierung&#x3C;/h2&#x3E;
        &#x3C;p&#x3E;Dieser Absatz hat einen Einzug durch den Nachfahren-Selektor.&#x3C;/p&#x3E;
        &#x3C;p&#x3E;Auch dieser Absatz ist betroffen.&#x3C;/p&#x3E;
    &#x3C;/article&#x3E;
    
    &#x3C;form&#x3E;
        &#x3C;label&#x3E;Name: &#x3C;input type=&#x22;text&#x22; placeholder=&#x22;Ihr Name&#x22;&#x3E;&#x3C;/label&#x3E;
        &#x3C;label&#x3E;E-Mail: &#x3C;input type=&#x22;email&#x22; placeholder=&#x22;ihre@email.de&#x22;&#x3E;&#x3C;/label&#x3E;
    &#x3C;/form&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Element-Selektoren stylen alle Elemente eines Typs (p, h1, div).
Klassen-Selektoren (.klassenname) können mehrfach verwendet werden.
ID-Selektoren (#idname) sollten nur einmal pro Seite verwendet werden.
Pseudo-Selektoren wie :hover reagieren auf Benutzerinteraktionen.
Kombinatoren wie > (direktes Kind) und Leerzeichen (Nachfahre) ermöglichen präzise Auswahlen.
Spezifität: inline > ID > Klasse > Element.
    """,
    "code9.png",
    "In der nächsten Lektion lernst du das CSS Box-Model kennen.",
    "Zurück zu Lektion 8",
    "Weiter zu Lektion 10",
    9
),

my_class(
    "Lektion 10: CSS Box-Model und Layout",
    """
Das CSS Box-Model ist fundamental für das Verständnis von Layout und Spacing.
Jedes HTML-Element ist eine rechteckige Box mit vier Bereichen:
Content (Inhalt), Padding (Innenabstand), Border (Rahmen) und Margin (Außenabstand).
Die Gesamtbreite eines Elements berechnet sich aus width + padding + border + margin.
box-sizing: border-box ändert dieses Verhalten und macht Layouts einfacher.
Display-Eigenschaften (block, inline, inline-block, flex, grid) kontrollieren das Layout-Verhalten.
Moderne Layout-Methoden wie Flexbox und CSS Grid revolutionieren das Webdesign.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;title&#x3E;CSS Box-Model&#x3C;/title&#x3E;
    &#x3C;style&#x3E;
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .box-example {
            width: 300px;
            padding: 20px;
            border: 5px solid #3498db;
            margin: 20px auto;
            background-color: #ecf0f1;
            text-align: center;
        }
        
        .container {
            display: flex;
            gap: 20px;
            margin: 30px 0;
        }
        
        .flex-item {
            flex: 1;
            padding: 15px;
            background-color: #2ecc71;
            color: white;
            text-align: center;
            border-radius: 5px;
        }
        
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .grid-item {
            padding: 20px;
            background-color: #e74c3c;
            color: white;
            text-align: center;
            border-radius: 5px;
        }
        
        .inline-demo span {
            background-color: #f39c12;
            padding: 5px 10px;
            margin: 5px;
            border: 2px solid #d68910;
        }
        
        .block-demo div {
            background-color: #9b59b6;
            color: white;
            padding: 10px;
            margin: 10px 0;
            width: 200px;
        }
    &#x3C;/style&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;h1&#x3E;CSS Box-Model und Layout&#x3C;/h1&#x3E;
    
    &#x3C;h2&#x3E;Box-Model Beispiel&#x3C;/h2&#x3E;
    &#x3C;div class=&#x22;box-example&#x22;&#x3E;
        Diese Box hat 20px Padding, 5px Border und 20px Margin
    &#x3C;/div&#x3E;
    
    &#x3C;h2&#x3E;Flexbox Layout&#x3C;/h2&#x3E;
    &#x3C;div class=&#x22;container&#x22;&#x3E;
        &#x3C;div class=&#x22;flex-item&#x22;&#x3E;Element 1&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;flex-item&#x22;&#x3E;Element 2&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;flex-item&#x22;&#x3E;Element 3&#x3C;/div&#x3E;
    &#x3C;/div&#x3E;
    
    &#x3C;h2&#x3E;CSS Grid Layout&#x3C;/h2&#x3E;
    &#x3C;div class=&#x22;grid-container&#x22;&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 1&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 2&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 3&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 4&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 5&#x3C;/div&#x3E;
        &#x3C;div class=&#x22;grid-item&#x22;&#x3E;Grid 6&#x3C;/div&#x3E;
    &#x3C;/div&#x3E;
    
    &#x3C;h2&#x3E;Display-Eigenschaften&#x3C;/h2&#x3E;
    
    &#x3C;h3&#x3E;Inline-Elemente&#x3C;/h3&#x3E;
    &#x3C;div class=&#x22;inline-demo&#x22;&#x3E;
        &#x3C;span&#x3E;Inline 1&#x3C;/span&#x3E;
        &#x3C;span&#x3E;Inline 2&#x3C;/span&#x3E;
        &#x3C;span&#x3E;Inline 3&#x3C;/span&#x3E;
    &#x3C;/div&#x3E;
    
    &#x3C;h3&#x3E;Block-Elemente&#x3C;/h3&#x3E;
    &#x3C;div class=&#x22;block-demo&#x22;&#x3E;
        &#x3C;div&#x3E;Block 1&#x3C;/div&#x3E;
        &#x3C;div&#x3E;Block 2&#x3C;/div&#x3E;
        &#x3C;div&#x3E;Block 3&#x3C;/div&#x3E;
    &#x3C;/div&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
box-sizing: border-box macht width/height-Berechnungen vorhersagbarer.
Flexbox ist ideal für eindimensionale Layouts (Reihen oder Spalten).
CSS Grid eignet sich perfekt für zweidimensionale Layouts.
display: block nimmt die ganze Breite ein, display: inline nur den benötigten Platz.
margin: auto zentriert Block-Elemente horizontal.
gap-Eigenschaft erstellt Abstände zwischen Flex- oder Grid-Items.
    """,
    "code10.png",
    "In der letzten Lektion lernst du responsive Design und erweiterte CSS-Techniken.",
    "Zurück zu Lektion 9",
    "Weiter zu Lektion 11",
    10
),

my_class(
    "Lektion 11: Responsive Design und erweiterte CSS-Techniken",
    """
Responsive Design sorgt dafür, dass Webseiten auf allen Geräten gut aussehen und funktionieren.  
Media Queries ermöglichen verschiedene CSS-Regeln für verschiedene Bildschirmgrößen.
Mobile-First Ansatz: Zuerst für kleine Bildschirme designen, dann für größere erweitern.
Relative Einheiten wie %, em, rem und vw/vh passen sich an verschiedene Bildschirmgrößen an.
CSS-Variablen (Custom Properties) machen Stylesheets wartbarer und konsistenter.
Moderne CSS-Features wie Transitions, Transforms und Animationen verbessern die Benutzererfahrung.
Flexbox und Grid sind die Grundlagen für responsive Layouts.
Progressive Enhancement: Grundfunktionalität für alle, erweiterte Features für moderne Browser.
    """,
    """&#x3C;!DOCTYPE html&#x3E;
&#x3C;html lang=&#x22;de&#x22;&#x3E;
&#x3C;head&#x3E;
    &#x3C;meta charset=&#x22;UTF-8&#x22;&#x3E;
    &#x3C;meta name=&#x22;viewport&#x22; content=&#x22;width=device-width, initial-scale=1.0&#x22;&#x3E;
    &#x3C;title&#x3E;Responsive Design&#x3C;/title&#x3E;
    &#x3C;style&#x3E;
        :root {
            --primary-color: #3498db;
            --secondary-color: #2ecc71;
            --accent-color: #e74c3c;
            --text-color: #2c3e50;
            --bg-color: #ecf0f1;
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: &#x27;Segoe UI&#x27;, Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        h1 {
            margin: 0;
            font-size: clamp(1.5rem, 4vw, 3rem);
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .card h3 {
            color: var(--primary-color);
            margin-top: 0;
        }
        
        .responsive-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
        }
        
        .button {
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        
        .button:hover {
            background: #c0392b;
        }
        
        /* Mobile First - Standard Styles f&#xFC;r mobile Ger&#xE4;te */
        .flex-container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        /* Tablet Styles */
        @media screen and (min-width: 768px) {
            .flex-container {
                flex-direction: row;
                align-items: center;
            }
            
            .container {
                padding: 0 40px;
            }
        }
        
        /* Desktop Styles */
        @media screen and (min-width: 1024px) {
            body {
                font-size: 1.1rem;
            }
            
            .grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        /* Large Desktop */
        @media screen and (min-width: 1400px) {
            .container {
                max-width: 1400px;
            }
        }
        
        /* Animation */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animate {
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {
            :root {
                --text-color: #ecf0f1;
                --bg-color: #2c3e50;
            }
            
            .card {
                background: #34495e;
                color: #ecf0f1;
            }
        }
    &#x3C;/style&#x3E;
&#x3C;/head&#x3E;
&#x3C;body&#x3E;
    &#x3C;header&#x3E;
        &#x3C;div class=&#x22;container&#x22;&#x3E;
            &#x3C;h1 class=&#x22;animate&#x22;&#x3E;Responsive Webdesign&#x3C;/h1&#x3E;
            &#x3C;p&#x3E;Eine Webseite f&#xFC;r alle Ger&#xE4;te&#x3C;/p&#x3E;
        &#x3C;/div&#x3E;
    &#x3C;/header&#x3E;
    
    &#x3C;main class=&#x22;container&#x22;&#x3E;
        &#x3C;section class=&#x22;flex-container animate&#x22;&#x3E;
            &#x3C;div&#x3E;
                &#x3C;h2&#x3E;Mobile First Ansatz&#x3C;/h2&#x3E;
                &#x3C;p&#x3E;Diese Seite wurde zuerst f&#xFC;r mobile Ger&#xE4;te entwickelt und dann f&#xFC;r gr&#xF6;&#xDF;ere Bildschirme erweitert.&#x3C;/p&#x3E;
                &#x3C;a href=&#x22;#&#x22; class=&#x22;button&#x22;&#x3E;Mehr erfahren&#x3C;/a&#x3E;
            &#x3C;/div&#x3E;
            &#x3C;div&#x3E;
                &#x3C;img src=&#x22;https://picsum.photos/400/300&#x22; alt=&#x22;Responsive Design Beispiel&#x22; class=&#x22;responsive-image&#x22;&#x3E;
            &#x3C;/div&#x3E;
        &#x3C;/section&#x3E;
        
        &#x3C;section class=&#x22;grid&#x22;&#x3E;
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;Media Queries&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;Verschiedene CSS-Regeln f&#xFC;r verschiedene Bildschirmgr&#xF6;&#xDF;en. Ab 768px wird das Layout zweispaltig, ab 1024px dreispaltig.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
            
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;Flexible Einheiten&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;Verwendung von %, em, rem und Viewport-Einheiten (vw, vh) statt festen Pixelwerten f&#xFC;r bessere Skalierbarkeit.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
            
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;CSS-Variablen&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;Custom Properties erm&#xF6;glichen konsistente Farben und Werte im gesamten Stylesheet und einfache Wartung.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
            
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;Grid &#x26; Flexbox&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;Moderne Layout-Methoden, die automatisch responsive Verhalten bieten ohne komplexe Media Queries.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
            
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;Animationen&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;CSS-Transitions und Keyframe-Animationen verbessern die Benutzererfahrung ohne JavaScript.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
            
            &#x3C;div class=&#x22;card animate&#x22;&#x3E;
                &#x3C;h3&#x3E;Dark Mode&#x3C;/h3&#x3E;
                &#x3C;p&#x3E;Unterst&#xFC;tzung f&#xFC;r das System-Farbschema des Benutzers mit prefers-color-scheme Media Query.&#x3C;/p&#x3E;
            &#x3C;/div&#x3E;
        &#x3C;/section&#x3E;
    &#x3C;/main&#x3E;
    
    &#x3C;script&#x3E;
        // Progressive Enhancement: Animation nur wenn JavaScript verf&#xFC;gbar
        document.addEventListener(&#x27;DOMContentLoaded&#x27;, function() {
            const cards = document.querySelectorAll(&#x27;.card&#x27;);
            
            const observer = new IntersectionObserver((entries) =&#x3E; {
                entries.forEach(entry =&#x3E; {
                    if (entry.isIntersecting) {
                        entry.target.style.animationDelay = Math.random() * 0.3 + &#x27;s&#x27;;
                        entry.target.classList.add(&#x27;animate&#x27;);
                    }
                });
            });
            
            cards.forEach(card =&#x3E; observer.observe(card));
        });
    &#x3C;/script&#x3E;
&#x3C;/body&#x3E;
&#x3C;/html&#x3E;""",
    """
Mobile-First bedeutet: Basis-Styling für mobile Geräte, dann Media Queries für größere Bildschirme.
clamp(min, preferred, max) ermöglicht flüssige Typografie zwischen verschiedenen Bildschirmgrößen.
CSS-Variablen (--variable-name) können mit var(--variable-name) verwendet werden.
auto-fit und minmax() in CSS Grid erstellen automatisch responsive Spalten.
prefers-color-scheme erkennt die Systemeinstellung für helle/dunkle Themes.
Intersection Observer API lädt Animationen nur bei Bedarf für bessere Performance.
Progressive Enhancement: Grundfunktionen ohne JavaScript, Verbesserungen mit JavaScript.
    """,
    "code11.png",
    "Herzlichen Glückwunsch! Du hast alle HTML- und CSS-Grundlagen erfolgreich durchlaufen.",
    "Zurück zu Lektion 10",
    "Zurück zur Startseite",
    11
)