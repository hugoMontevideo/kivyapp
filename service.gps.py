from plyer import gps

def start():
    try:
        gps.configure(on_location=on_location, on_status=on_status)
        gps.start(minTime=1000, minDistance=1)
    except NotImplementedError:
        print("Le GPS n'est pas disponible sur cette plateforme.")

def on_location(**kwargs):
    print("Localisation reçue depuis le service GPS :", kwargs)

def on_status(stype, status):
    print(f"Statut du service GPS : [{stype}] {status}")
