[app]
title = MonApp
package.name = monapp
package.domain = org.monorganisation
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
