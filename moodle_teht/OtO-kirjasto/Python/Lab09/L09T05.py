import random

i = 0
writeType = "w"

def kirjoita_tiedostoon(lotto):
    global writeType
    try:
        f = open("lottorivit.txt", writeType, encoding='utf-8')
        try:
            for num in lotto:
                f.write(str(num) + " ")
            f.write("\n")
            writeType = "a"
        except Exception as e:
            print("Tiedostoon kirjoittamisessa tapahtui virhe: ", e)
        finally:
            f.close()
    except IOError as e:
        print("IO-virhe tapahtui: ", e)
    except Exception as e:
        print("Odottamaton virhe tapahtui: ", e)

def arvo_lotto():
    lottoLista = []
    for i in range(7):
        luku = random.randint(0, 40)
        while luku in lottoLista:
            luku = random.randint(0, 40)
        
        lottoLista.append(luku)
        i += 1
    print(lottoLista)
    kirjoita_tiedostoon(lottoLista)


rivit = int(input("Montako riviä halut arpoa: "))
while i < rivit:
    arvo_lotto()
    i += 1
