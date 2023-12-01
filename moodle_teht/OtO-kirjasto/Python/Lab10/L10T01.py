import datetime

def kerro3(age):
    if age < 1:
        return "baby"
    elif age <= 13:
        return "child"
    elif age <= 20:
        return "teen"
    elif age < 65:
        return "adult"
    elif age >= 65:
        return "senior"


syntymavuosi = 0
thisYear = datetime.date.today().year

while True:
    try:
        syntymavuosi = int(input("Kerro syntymävuotesi: "))

        if len(str(syntymavuosi)) != 4:
            continue
        else:
            if syntymavuosi > thisYear:
                continue
            else:
                break
    except ValueError:
        print("syntymävuosi pitäisi olla")

print(kerro3(thisYear - syntymavuosi))