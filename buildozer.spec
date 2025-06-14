[app]
title = BasitKivyApp
package.name = basitkivyapp
package.domain = org.deneme
source.dir = .
source.include_exts = py,kv,png,jpg,txt,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = INTERNET
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.arch = armeabi-v7a,arm64-v8a
debug = 1
