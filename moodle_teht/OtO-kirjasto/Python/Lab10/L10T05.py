import ctypes
import os
import platform

# Tarkistetaan onko käyttäjä admin
try:
  is_admin = os.getuid() == 0
except AttributeError:
  is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if is_admin:
  print("Olet admin")
else:
  print("Et ole admin")
  exit()

# Tarkistetaan käyttöjärjestelmä ja asetetaan polku
if platform.system() == 'Windows':
  path = "C:\\"
elif platform.system() == 'Linux':
  path = "/home/"
elif platform.system() == 'Darwin':
  path = "/Users/"
else:
  print("Tuntematon käyttöjärjestelmä")
  exit()

f = open(path + "ayho.txt", "w")
f.write("Aapo\n")