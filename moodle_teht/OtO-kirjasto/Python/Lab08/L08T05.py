import random
def lotto():
    lottorivi = []
    for i in range(7):
        luku = random.randint(1,40)
        while luku in lottorivi: # Katsotaan, ettei luku oo jo listassa
            luku = random.randint(1,40)
        lottorivi.append(luku)
    lottorivi.sort()
    return lottorivi

print("Lottorivi:", lotto())
