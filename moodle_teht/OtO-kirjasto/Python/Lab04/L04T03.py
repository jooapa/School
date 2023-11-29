kokoSumma = 0
maara = 0

while True:
  luku = input("Anna luku: ")
  if luku == "":
    break
  try:
    maara += 1
    kokoSumma += int(luku)
  except ValueError:
    print("Virheellinen syöte!")

print("Lukuja annettu:", maara)
print("Lukujen summa:", kokoSumma)
