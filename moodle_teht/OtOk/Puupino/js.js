const pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095
var Trees = []
eka = 1
TreesSum = 0
TreesSum2 = 0
var i = 0
A = 0
TreeRandom = 0
document.getElementById("InfoDiv").style.display = "none";


function CalculateA(){
    var Trees = []
    eka = 1
    TreesSum = 0
    TreesSum2 = 0
    var i = 0
    A = 0
    TreeRandom = 0
    Korkeus = Number(prompt("Syötä puupinon Korkeus 'cm'"));
    Leveys = Number(prompt("Syötä puupinon Leveys 'cm'"));
    A = Korkeus * Leveys
    console.log(A + "cm on Pinta-ala")

    ShowGraphic();
    addTrees();
    
}


function addTrees(){
    
    let TreeTrough = 0
    while (TreesSum < A){
    TreeRandom = Math.floor(Math.random() * 30) + 5;
    Trees.push(Math.round(pi * TreeRandom**2))

    TreesSum += Trees.slice(-1)[0] 


    console.log(Trees.slice(-1)[0])
    console.log(TreesSum)
    /*
        if (TreeTrough < Trees.length){
            PuuGraphic()}
    TreeTrough++
    */
}
    
    ViimeNum = Trees.slice(-1)[0]
    TreesSum = TreesSum - ViimeNum
    Trees.pop()
    TreePercent = Math.round((TreesSum/A * 100) * 1000) / 1000
    // alert(A + "cm^2 on Puupinon Pinta-ala ja Puiden Pinta-ala on " + TreesSum + "cm^2")
    //alert("Puita lisätty " + Trees.length)
    // alert("Puut vie "+ Math.round((TreesSum/A * 100) * 100) / 100 +"% tilasta")
    document.getElementById("main1").innerHTML = A + "cm^2 on Puupinon Pinta-ala ja Puiden Pinta-ala on " + TreesSum + "cm^2"
    document.getElementById("main2").innerHTML = "Puita lisätty " + Trees.length
    document.getElementById("main3").innerHTML = "Puut vie "+ TreePercent+"% tilasta"

        document.getElementById("InfoDiv").style.display = "block";
    ShowPieChart();  

}

function ShowPieChart(){
var xValues = ["Puu", "Vapaa-Tila"];
var yValues = [TreePercent, 100 -TreePercent];
var barColors = [
  "brown",
  "#White",
];

new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: false,
      text: "Puu"
    }
  }
});

}
function ShowGraphic(){
    
    
    var div = document.createElement("div");
    div.style.width = Leveys + "px";
        div.style.height =Korkeus + "px";
        div.style.background = "white";
        div.style.zIndex = "1";
        
        div.style.border = "4px solid red";;
        div.style.position = "fixed"

    
       // document.getElementById("main").appendChild(div);
}


/*
function PuuGraphic(){
   
    var PuuDiv = document.createElement("div");
        

        PuuDiv.style.position = "relative";
        PuuDiv.style.width = TreeWidth + "px";
        PuuDiv.style.height = TreeHeight + "px";
        PuuDiv.style.background = "white";
        PuuDiv.style.borderRadius = "1000px";
        PuuDiv.style.zIndex = "2";
        
        
        PuuDiv.style.border = "4px solid red";
        
        TreeHeightoffset += TreeHeight;
     
}
*/

