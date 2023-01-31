
laakevoima = 0
laakesaatu = -1
suurin = 0
laakecompare = 0
yhteensa = 0;
smaara = 0
ateksti = "Annos, kunnes yli <br> suosituksen"
laakekaytetty = 0

const laakemuisti = []

function laakemaara() {
    if (smaara == null || smaara == ""){
        alert("Sinun pitää ensin lisätä Suositusmäärä!");
        return;
    }
    var laakesaatu = (prompt("Lisää Lääkkeenmäärä"));
    console.log(laakesaatu + " tämä")
    
    if(laakesaatu == null || laakesaatu == "") {
        alert("Sinun pitää lisätä numero!");
        return;
    }
    laakemuisti.push(laakesaatu);
    
    var lm = [...laakemuisti]
    
    console.log(laakemuisti.length + " lenght")
    console.log(laakemuisti.length-2 + " ds")
   
    lm.sort(function(a, b){return a-b});
    

    var biggest = lm[lm.length-1]
    
    let text = "";
    for (let i = 0; i < laakemuisti.length; i++) {
        text += "Lääkettä annettu: " + laakemuisti[i] + "<br>";
    }
    yhteensa = 0
    for (let i = 0; i < laakemuisti.length; i++) {
        yhteensa += Number(laakemuisti[i]) ;
    }
    
    if ([laakemuisti.length] > 1){
        
        if (laakemuisti[laakemuisti.length-2] < laakemuisti[laakemuisti.length-1]){
            document.getElementById("tuloslaake").innerHTML = "Suurempi kuin edellinen";
        }
                else if (laakemuisti[laakemuisti.length-2] > laakemuisti[laakemuisti.length-1]){
                    document.getElementById("tuloslaake").innerHTML = "Pienempi kuin edellinen"; 
                }
                        else if (text == text){ 
                            document.getElementById("tuloslaake").innerHTML = "Sama kuin edellinen"; 
                        }
        

    }

    console.log("plussa: " + yhteensa)
    console.log(biggest)

    let yhteys = smaara - yhteensa
    
    if(yhteys == 0){
        ateksti = "Annosmäärä on saavutettu"
        ateksti = "<span style='color:green'>" + ateksti + "</span>"
    }
    else if (yhteys < 0){
        ateksti = "Annosmäärä ylitetty"
        ateksti = "<span style='color:red'>" + ateksti + "</span>"
        yhteys = yhteys * -1
    }
    laakekaytetty += 1; 

    console.log(laakemuisti)
    console.log(laakesaatu)
    console.log(laakekaytetty + " lääkekäytetty")
    document.getElementById("Lääkelista").innerHTML = text;
    document.getElementById("suurin").innerHTML = biggest;
    document.getElementById("jäljellä").innerHTML =yhteys;
    document.getElementById("annosteksti").innerHTML = ateksti;
    document.getElementById("laakek").innerHTML = laakekaytetty;
}

function suositusmaara(){
    smaara = prompt("Lisää Suositusmäärä");

    
    if(smaara == null || smaara == "") {
            alert("Sinun pitää lisätä numero!");
            return;

            
    }
    document.getElementById("suositus").innerHTML =smaara;
}


