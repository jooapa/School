arvo1 = int(input("Hypyn pisteet: "))
arvo2 = int(input("Hypyn pisteet: "))
arvo3 = int(input("Hypyn pisteet: "))
arvo4 = int(input("Hypyn pisteet: "))
arvo5 = int(input("Hypyn pisteet: "))

pisteet = [arvo1, arvo2, arvo3, arvo4, arvo5]
pisteet.sort() # sorttaa listan pienimmästä suurimpaan
pisteet.pop(0) # poistaa listan ensimmäisen arvon, eli pienimmän
pisteet.pop(-1) # poistaa listan viimeisen arvon, eli suurimman
print("Pisteet yhteensä:", sum(pisteet))
