class Pelikortti:
    def __init__(self, maa, arvo):
        valid_maa = ['hertta', 'ruutu', 'risti', 'pata']
        if maa not in valid_maa:
            raise ValueError(
                f"Kortin maa pitää olla jokin seuraavista: {valid_maa}"
            )
        if arvo < 2 or arvo > 14:
            raise ValueError("Kortin arvo pitää olla välillä 2-14")
        
        self.maa = maa
        self.arvo = arvo

kortti1 = Pelikortti("pata", 2)
kortti2 = Pelikortti("hertta", 7)
kortti3 = Pelikortti("ruutu", 10)
kortti4 = Pelikortti("risti", 14)
kortti5 = Pelikortti("pata", 9)

print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)
