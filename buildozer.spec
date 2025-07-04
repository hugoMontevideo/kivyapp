[app]

title = MyKivyAppgit
package.name = mykivyapp
package.domain = org.example   

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
entrypoint = main.py
orientation = portrait
fullscreen = 1

android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET
#android.features = android.hardware.location.gps
android.services=gps

# Forcer les versions compatibles
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_path = /home/runner/android-ndk-r25b
android.build_tools = 30.0.3
android.accept_sdk_license = true
android.copy_libs = 1

bootstrap = sdl2
requirements = python3,kivy,hostpython3,setuptools,python-for-android==2024.1.21,plyer

# icon.filename = %(source.dir)s/icon.png #add later
# presplash.filename = %(source.dir)s/presplash.png #add later

[buildozer]
build_dir = .buildozer
log_level = 2
warn_on_root = 1