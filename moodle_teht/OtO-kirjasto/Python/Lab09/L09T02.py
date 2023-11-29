sukunimet = []

f = open("sukunimet.txt", "r")
try:
    for line in f:
        sukunimet.append(line.strip())
except Exception as e:
    print("Tiedostosta lukemisessa tapahtui virhe: ", e)
finally:
    f.close()

print("Sukunimet: ")
print(sukunimet)
print(sorted(sukunimet))