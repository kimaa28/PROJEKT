import json, os


def load_passwort(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, "r") as datei:
        return json.load(datei)
    
def save_passwort(pfad, passwort):
    with open(pfad, "w") as datei:
        json.dump(passwort, datei, indent=4)


load_passwort("index.json")




save_passwort("index.json", load_passwort("index.json") + 1)
index = load_passwort("index.json")
print(index)