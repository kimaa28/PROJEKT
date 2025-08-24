import sys, os

base = os.path.dirname(__file__)
cgi_path = os.path.join(base, "cgi-bin")
print("Base:", base)
print("CGI Path:", cgi_path)
print("Sys Path:", sys.path)

sys.path.insert(0, cgi_path)

try:
    import gear_cgi
    print("Import erfolgreich!")
except ModuleNotFoundError as e:
    print("Fehler:", e)
