
document.getElementById("restart").style.visibility = "hidden";
Kierros = 0
NoppaLuku1 = 0
NoppaLuku2 = 0
CombNum = 0

function Throw(){
    document.getElementById("nappi").style.visibility = "visible";
   Kierros += 1
   console.log(Kierros)

    RandoNum();
    document.getElementById("luku1").innerHTML = NoppaLuku1;
    document.getElementById("luku2").innerHTML = NoppaLuku2;

   if(Kierros == 5){
    document.getElementById("nappi").style.visibility = "hidden";
    document.getElementById("restart").style.visibility = "visible";
    console.log("Kierros")
    Kierros = 0
   }
   else{
    document.getElementById("restart").style.visibility = "hidden";
   }


   CombNum += NoppaLuku1 + NoppaLuku2



       document.getElementById("yht").innerHTML = "Noppien yhteenlaskettu summa " + CombNum


}

function RandoNum(){

    NoppaLuku1 = Math.floor(Math.random() * 6) + 1;
    NoppaLuku2 = Math.floor(Math.random() * 6) + 1;
   


    NoppaLuku2
}

function Restart(){
    CombNum = 0
    Throw();
}
