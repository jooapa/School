<img src="img/title.png" width="100%" height="100%">

# SUUNNITELMA
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

#### Päivitykset
| Räkä-ase | Damage | Fire Rate (s) | Reload Time (s) | Magazine Size | Cost |
|----------|--------|---------------|-----------------|---------------|------|
| MK1      | 20     | 0.5           | 5               | 10            | -    |
| MK2      | 30     | 0.4           | 4               | 20            | 50   |
| MK3      | 40     | 0.3           | 3               | 30            | 100  |
| MK4      | 50     | 0.2           | 2               | 40            | 150  |
| MK5      | 60     | 0.1           | 1               | 50            | 200  |

### Kakku sinko
Kakku sinko ampuu yhden ison kakun, joka tekee paljon vahinkoa, mutta on hidas ja ampuu vain yhden kerrallaan.
Aseita voi päivittää kolikoilla, joka tekee aseista tehokkaampia.

#### Päivitykset
| Kakku-sinko | Damage | Fire Rate (s) | Reload Time (s) | Magazine Size | Cost |
|-------------|--------|---------------|-----------------|---------------|------|
| MK1         | 50     | 2.0           | 5               | 3             | -    |
| MK2         | 60     | 1.8           | 4.5             | 4             | 50   |
| MK3         | 70     | 1.6           | 4               | 5             | 100  |
| MK4         | 80     | 1.4           | 3.5             | 6             | 150  |
| MK5         | 90     | 1.2           | 3               | 7             | 200  |

# Testiraportti
