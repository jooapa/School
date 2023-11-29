nimet = {}
nimiLista = []

f = open("nimet.txt", "r")
try:
    for line in f:
        nimiLista.append(line.strip())
except Exception as e:
    print("Tiedostosta lukemisessa tapahtui virhe: ", e)
finally:
    f.close()


for i in nimiLista:
    if i in nimet: # jos nimi on jo sanakirjassa, i = nimi ja nimet[i] = määrä
        nimet[i] += 1 
    else: 
        nimet[i] = 1

for i in nimet:
    print(str(i) + ":", nimet[i], "kpl")