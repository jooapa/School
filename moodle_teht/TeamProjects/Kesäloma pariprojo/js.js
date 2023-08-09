//onclick button id="JooaBtn addEventListener

var jooaBtn = document.getElementById("JooaBtn");
var MikoBtn = document.getElementById("MikoBtn");
var scrollBtn = document.getElementById("ScrollUp");

jooaBtn.addEventListener("click", function(){
    //hide div id="Miko" and show div id="Jooa"
    // document.getElementById("Miko").style.display = "none";
    document.getElementById("jooa").style.display = "block";
    document.getElementById("miko").style.display = "none";
    document.getElementById("hideShow").style.display = "flex";
});

MikoBtn.addEventListener("click", function(){
    //hide div id="Jooa" and show div id="Miko"
    document.getElementById("jooa").style.display = "none";
    document.getElementById("miko").style.display = "block";
    document.getElementById("hideShow").style.display = "flex";
});

scrollBtn.addEventListener("click", function(){
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    });
});