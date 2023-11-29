kaverit = []
while True:
    try:
        nimi = str(input("Kaverisi nimi: "))

        if nimi != "" and nimi != " ":
            kaverit.append(nimi)

        if len(kaverit) == 10:
            print("Kaverilistasi on täynnä!")
            break
    except ValueError:
        print("Virheellinen syöte!")
        continue

print("Kaverilistasi:")
print(", ".join(kaverit))

kaverit.reverse()
print(", ".join(kaverit))
