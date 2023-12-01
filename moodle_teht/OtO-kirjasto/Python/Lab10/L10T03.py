class account:
    def __init__(self):
        self.saldo = 2000

    def withdraw(self, saldo):
        saldo = abs(saldo)
        if self.saldo < saldo:
            print("Ei tarpeeksi rahaa! Sinulla on ", self.saldo, "€ tilillä.")
            return False
        else:
            self.saldo -= saldo
            print("Rahaa nostettu: ", saldo)
            return True
    def add(self, saldo):
        saldo = abs(saldo)
        self.saldo += saldo
        print("Rahaa lisätty:  ", saldo)
        return True


while True:
    try:
        miskaTili = account()
        while True:
            try:
                print("Saldo:", miskaTili.saldo , "€")
                print("1. Nosta rahaa")
                print("2. Lisää rahaa")
                print("3. Lopeta")
                valinta = int(input("Valitse: "))
                if valinta == 1:
                    miskaTili.withdraw(int(input("Kuinka paljon nostetaan? ")))
                elif valinta == 2:
                    miskaTili.add(int(input("Kuinka paljon lisätään? ")))
                elif valinta == 3:
                    exit()
            except ValueError:
                print("Virheellinen syöte!")
    except Exception as e:
        print("Odottamaton virhe tapahtui: ", e)
