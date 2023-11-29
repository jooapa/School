arvosanat = []
montakoArvosanaa = 0
while True:
    arvosana = input("Kirjoita arvosana: 0-5: ")

    if arvosana == "":
        break
    try:
        arvosana = int(arvosana)
    except ValueError:
        print("Virheellinen syöte!")
        continue

    if arvosana < 0 or arvosana > 5:
        print("Virheellinen arvosana!")
        continue
    else:
        arvosanat.append(arvosana)
        montakoArvosanaa += 1
        continue

print("Arvosanoja annettu:", montakoArvosanaa)
print("Arvosanojen keskiarvo:", sum(arvosanat) / len(arvosanat))
