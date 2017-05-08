import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = 'Console'
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Copy Translations",
        version = "0.1",
        description = "An app to re-import the most recent translations for styles",
        options = {"build_exe": build_exe_options},
        console = [{'script':'Translation_Main.py'}],
        executables = [Executable("Translation_main.py", base=base)])