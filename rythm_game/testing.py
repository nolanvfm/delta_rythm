import importlib
import os

liste = []

for filename in os.listdir("Map"):
    if filename != "Music" and filename != "template.py" and filename != "__pycache__":
        a = importlib.import_module("."+filename[:len(filename)-3], "Map")
        liste.append(a.Constructor())