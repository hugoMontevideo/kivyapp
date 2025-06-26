[app]

title = MyKivyApp
package.name = mykivyapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
entrypoint = main.py
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# SDK/API fixes
android.api = 30
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.build_tools = 30.0.3
android.copy_libs = 1

bootstrap = sdl2
requirements = python3,kivy

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[buildozer]

# build paths (they will be overridden by environment in CI)
build_dir = .buildozer
log_level = 2
warn_on_root = 1
