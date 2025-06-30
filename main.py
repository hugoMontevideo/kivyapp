from kivy.app import App
from kivy.uix.label import Label
from plyer import gps
from kivy.utils import platform
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
request_permissions([Permission.ACCESS_FINE_LOCATION])


class GpsApp(App):
    def build(self):
        self.label = Label(text="En attente de la position GPS...")
        if platform == "android":
            try:
                gps.configure(on_location=self.on_location, on_status=self.on_status)
                gps.start(minTime=1000, minDistance=1)
            except NotImplementedError:
                self.label.text = "GPS non disponible sur cette plateforme"
        else:
            self.label.text = "GPS uniquement sur Android"
        return self.label

    def on_location(self, **kwargs):
        lat = kwargs.get('lat', 'N/A')
        lon = kwargs.get('lon', 'N/A')
        self.label.text = f"Latitude: {lat}\nLongitude: {lon}"

    def on_status(self, stype, status):
        self.label.text = f"[{stype}] {status}"


if __name__ == '__main__':
    GpsApp().run()


