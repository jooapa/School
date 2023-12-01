maara = 0
pisinNimi = ""

f = open("nimet.txt", "r")
try:
    for line in f:
        if len(line.strip()) > len(pisinNimi):
            pisinNimi = line.strip()
        maara += 1
except Exception as e:
    print("Tiedostosta lukemisessa tapahtui virhe: ", e)
finally:
    f.close()


print("Nimiä löytyi:", maara)
print("Pisin nimion :", pisinNimi)