import re

kilvet = []

def kilpi_vai_ei(kilpi):
    if re.match(r"[A-Z]{3}-[0-9]{3}", kilpi):
        return True
    else:
        return False
    
while True:
    try:
        nimi = str(input("Kirjoita Rekisterinumero: "))

        if nimi == "" or nimi == " ":
            break
        else:
            if kilpi_vai_ei(nimi):
              kilvet.append(nimi)
            else:
              print("Virheellinen rekisterinumero!")
              continue
            continue
    except ValueError:
        print("Virheellinen syöte!")
        continue
    
kilvet.sort()
print("Rekisterinumerot:")
print(", ".join(kilvet))
