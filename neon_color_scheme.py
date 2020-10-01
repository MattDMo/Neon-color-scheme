import sublime

from package_control import events


package_name = "Neon Color Scheme"

def plugin_loaded():
    if events.install(package_name):
        print("%s successfully installed!" % events.install(package_name))
    elif events.post_upgrade(package_name):
        settings = sublime.load_settings("Preferences.sublime-settings")
        color_scheme = settings.get("color_scheme")
        if color_scheme == "Packages/Neon Color Scheme/Neon.tmTheme":
            settings.set("color_scheme", "Packages/Neon Color Scheme/Neon.sublime-color-scheme")
            sublime.save_settings("Preferences.sublime-settings")
            print("Successfully changed color_scheme!")
