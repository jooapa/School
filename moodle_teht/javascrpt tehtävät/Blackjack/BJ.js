/*
Tee ohjelma jossa käyttäjälle arvotaan kaksi korttia ja tietokone-vastustajalle kaksi korttia. Tämän jälkeen edetään siten, että käyttäjä saa päättää haluaako nostaa lisää kortteja. Hyödynnä korttien nostamisessa funktiota. Tietokone ei nosta lisää kortteja vaan jää lukemaan jonka sai kahdesta ensimmäisestä kortista. Lähemmäs 21 päässyt pelaaja voittaa. Kortteja nostetaan lisää yksi kerrallaan, niin kauan kuin käyttäjä haluaa tai kunnes hänen korttiensa lukema ylittää 21, jolloin hän on hävinnyt. Lopuksi tulostetaan voittaja ja korttien yhteenlasketut lukemat funktiota hyödyntäen esim. seuraavasti:

Voitit! Sinulla on 20, tietokoneella on 18.

tai
Hävisit! Sinulla on 22, tietokoneella on 12.

Saat vähän lisää haastetta, kun teet tehtävän graafisena.
*/
var RandomCard	= undefined
MainCardCount= []

function randomCardfunc(RandomCard){
    var RandomCard = Math.floor(Math.random() * 13) + 1
    return RandomCard;
}

function Start(){

    MainCardCount.push(randomCardfunc(RandomCard))
    document.getElementById("MainCards").innerHTML = MainCardCount

}

function HitCardfunc(){
    randomCardfunc();
    MainCardCount.push(randomCardfunc(RandomCard))
    document.getElementById("MainCards").innerHTML = MainCardCount

}

function HitCard(){
    HitCardfunc();
    console.log(randomCardfunc(RandomCard))
}