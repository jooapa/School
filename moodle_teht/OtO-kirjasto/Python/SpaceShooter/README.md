<img src="img/title.png" width="100%" height="100%">

## PELI

Peli on ylhäältä päin kuvattu 2d peli, jossa kontrolloit WASD:illa ja osoitat asetta hiirillä. Pelaaja kääntyy hiiren cursoria päin ja painamalla LMOUSE, ammut panoksen hiiren suuntaan.

## GAME LOOP

Ekan kerran kun pääset peliin voit valita vain yhden levelin kolmesta levelistä. Kolikkoja pelaajalla on 0 ja power-uppeja ei ole
Kun pääset leveliin vihollisia alkaa tulla sivuilta, ja sinun pitää tappaa viholliset ennen kuin ne osuu pelaajaan, josta pelaaja menettää elämän.
Levelit toimivat roundi systeemillä. Eli leveli alkaa on round 1, sitten kun vihollisia ei ole enään, alkaa round 2. Joka roundilla viholliset tulevat enemmän agreessivisemmiksi eli pystyy liikkuaan nopeammin tai jos on ase niin ampuu nopeammin.

## Aseet

Aseita on 3 erilaista, joita voi päivittää kolikoilla. Aseet ovat räkä ase, ja kakku sinko. Aseita voi päivittää kolikoilla, joka tekee aseista tehokkaampia.

### Räkä ase

Räkä ase on perus ase, joka ampuu yhden panoksen kerrallaan. Panos on nopea ja tekee vähän vahinkoa.

| Räkä-ase   | Vahinko | Tulenopeus (s) | Latausaika (s) | Lippaan koko   | Hinta |
|------------|---------|----------------|----------------|----------------|-------|
| MK1        | 20      | 0.5            | 5              | 10             | -     |
| MK2        | 30      | 0.4            | 4              | 20             | 50    |
| MK3        | 40      | 0.3            | 3              | 30             | 100   |
| MK4        | 50      | 0.2            | 2              | 40             | 150   |
| MK5        | 60      | 0.1            | 1              | 50             | 200   |

### Kakku sinko

Kakku sinko ampuu yhden ison kakun, joka tekee paljon vahinkoa, mutta on hidas ja ampuu vain yhden kerrallaan.
Aseita voi päivittää kolikoilla, joka tekee aseista tehokkaampia.

| Kakku-sinko | Vahinko | Tulenopeus (s) | Latausaika (s) | Lippaan koko   | Hinta |
|-------------|---------|----------------|----------------|----------------|-------|
| MK1         | 50      | 2.0            | 5              | 3              | -     |
| MK2         | 60      | 1.8            | 4.5            | 4              | 50    |
| MK3         | 70      | 1.6            | 4              | 5              | 100   |
| MK4         | 80      | 1.4            | 3.5            | 6              | 150   |
| MK5         | 90      | 1.2            | 3              | 7              | 200   |

# Testiraportti

## Kakku singon sijaiti väärässä paikassa**

Päivämäärä: [16.12.2023]

### Ongelman Kuvaus

Ongelmana oli, että ammuttaessa vihollista kakku singolla ja lisättäessä räjähdysanimaatio, animaatio tapahtui väärässä paikassa. Alkuperäinen koodi sijoitti räjähdyksen koordinaatit vihollisen keskelle, mutta räjähdyksen kuva alkoi silti (0,0)-kohdasta, mikä johti epätoivottuun sijaintiin.

### Ratkaisuvaiheet

1. **Räjähdyksen sijainti:**
   - Alkuperäinen koodi:

     ```python
     enemy_x = _enemy_.get_x() - _enemy_.rect.width / 2
     enemy_y = _enemy_.get_y() - _enemy_.rect.height / 2
     explosions.append(Explosion(enemy_x, enemy_y, 200))
     ```

   - Ongelma: Räjähdys tapahtui vihollisen keskellä, mutta sen räjähdyskuva alkoi silti (0,0)-kohdasta, mutta nyt se (0,0)-kohta oli vihollisen keskellä.
   - Ratkaisu: Muutin Explosion-luokassa koordinaatteja seuraavasti:

     ```python
     self.x = x - radius
     self.y = y - radius
     ```

   - Tämä korjasi ongelman, ja räjähdys tapahtui nyt oikeassa paikassa suhteessa viholliseen, mutta oli siitä vielä vähän vinossa.
   - Pitimyös muuttaa niin, että räjähdys ei tapahtunut vihollisen keskellä, vaan panoksen keskellä, joka johti seuraavaan ongelmaan, (Ongelma oli läsnä jo ennen tätä muutosta, mutta se ei ollut niin huomattava.)

2. **Panoksen sijainti:**
   - Alkuperäinen koodi:

     ```python
     bullet_x = bullet.get_x() - bullet_x.rect.width / 2
     bullet_y = bullet.get_y() - bullet_y.rect.height / 2
     explosions.append(Explosion(bullet_x, bullet_y, 200))
     ```

   - Ongelma: Panoksen räjähdys tapahtui panoksen keskellä, joka jhti että räjähdyksen nolla-piste alkoi keskeltä panosta.
   - Ratkaisu: Käytin suoraan panoksen nollapistettä Explosion-luokassa:

     ```python
     explosions.append(Explosion(bullet.get_x(), bullet.get_y(), 200))
     ```
