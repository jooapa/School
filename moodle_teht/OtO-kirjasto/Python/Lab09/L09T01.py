import os

sukunimet = []
sukunimi1 = ""
sukunimi2 = ""
sukunimi3 = ""

while True:
  try:
    if sukunimi1 == "":
      sukunimi1 = str(input("Anna sukunimi: "))
    if sukunimi2 == "":  
      sukunimi2 = str(input("Anna sukunimi: "))
    if sukunimi3 == "":
      sukunimi3 = str(input("Anna sukunimi: "))

    if sukunimi1 != "" and sukunimi2 != "" and sukunimi3 != "":
      sukunimet.append(sukunimi1)
      sukunimet.append(sukunimi2)
      sukunimet.append(sukunimi3)
      break
  except ValueError:
      print("Virheellinen syöte!")

# onko tiedosto olemassa
if os.path.isfile("sukunimet.txt"):
    print("Tiedosto on jo olemassa!")
    input("y/n haluatko poistaa tiedoston? ja luoda uuden? ")
    if input == "n":
        exit()

# kirjoitetaan tiedostoon sukunimet
try:
    f = open("sukunimet.txt", "w", encoding='utf-8')
    try:
        for i in sukunimet:
            print(i)
            f.write(i + "\n")
    except Exception as e:
        print("Tiedostoon kirjoittamisessa tapahtui virhe: ", e)
    finally:
        f.close()
except IOError as e:
    print("IO-virhe tapahtui: ", e)
except Exception as e:
    print("Odottamaton virhe tapahtui: ", e)
