luvut = []
määrä = 0
while True:
  luku = input("Anna kokonaisluku (tyhjä lopettaa): ")
  if luku == "":
    break
  try:
    luvut.append(int(luku))
    määrä += 1
  except ValueError:
    print("Virheellinen syöte!")

try:
    f = open("luvut.txt", "w", encoding='utf-8')
    try:
        for i in luvut:
            f.write(str(i) + "\n")
    except Exception as e:
        print("Tiedostoon kirjoittamisessa tapahtui virhe: ", e)
    finally:
        f.close()
except IOError as e:
    print("IO-virhe tapahtui: ", e)
except Exception as e:
    print("Odottamaton virhe tapahtui: ", e)

print("Syötetty 5 lukua: ", määrä)
