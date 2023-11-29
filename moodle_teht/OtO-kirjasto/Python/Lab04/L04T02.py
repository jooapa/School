print("Tämä ohjelma laskee sademäärän viikon aikana, jos ei ole sadetta, niin sademäärä on 0.")

sade1 = int(input("Anna Maanantain  sademäärä: "))
sade2 = int(input("Anna Tiistain    sademäärä: "))
sade3 = int(input("Anna Keskiviikon sademäärä: "))
sade4 = int(input("Anna Torstain    sademäärä: "))
sade5 = int(input("Anna Perjantain  sademäärä: "))
sade6 = int(input("Anna Lauantain   sademäärä: "))
sade7 = int(input("Anna Sunnuntain  sademäärä: "))
sum = 0
sum = sade1 + sade2 + sade3 + sade4 + sade5 + sade6 + sade7

print("Sademäärä yhteensä:", sum)