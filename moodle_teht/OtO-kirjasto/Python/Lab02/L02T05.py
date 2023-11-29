nimi = input("Anna etunimesi: ")
lause = ""

print("Nimessäsi", nimi, "on", len(nimi), "kirjainta.")

for x in range(len(nimi)):
    lause += nimi[0]

print(lause.upper())