nimet = ""
maara = 0

while True:
  luku = str(input("Anna oppilaan nimi: "))
  if luku == "":
    break
  try:
    maara += 1
    nimet += str(luku) + ", " 
  except ValueError:
    print("Virheellinen syöte")

print("Oppilaita:", maara)

nimet = nimet[:-2]
print(nimet)
