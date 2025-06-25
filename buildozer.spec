[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (used for naming your app's Java package)
package.domain = org.example

# (str) Source code where your main.py is
source.dir = .

# (str) Application versioning
version = 0.1

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Entry point
entrypoint = main.py

# (list) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Supported android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android NDK API
android.ndk_api = 21

# (bool) Copy the necessary libs
android.copy_libs = 1

# (str) Bootstrap to use (sdl2 is the default and best)
bootstrap = sdl2

# (str) List of requirements (comma separated)
requirements = python3,kivy

# (str) Application icon
icon.filename = %(source.dir)s/icon.png

# (str) Presplash screen
presplash.filename = %(source.dir)s/presplash.png


[buildozer]

# (str) Path to the Android SDK
# android.sdk_path =

# (str) Path to the Android NDK
# android.ndk_path =

# (str) Path to the Android's adb tool
# android.adb_path =

# (str) Path to your Android SDK's tools/bin folder
# android.sdk_path =

# (str) Path to the debug keystore
# android.debug_keystore =

# (str) Directory where buildozer stores everything
build_dir = .buildozer

# (str) Log level (1 = error only, 2 = normal output, 3 = verbose output)
log_level = 2

# (bool) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
