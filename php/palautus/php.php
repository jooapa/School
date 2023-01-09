<?php


if (isset($_POST['lähetys'])){
$Etunimi = $_POST["etunimi"];
$Sukunimi = $_POST["sukunimi"];
$StuNum = $_POST["stunum"];
//$Email = $_POST["email"];
$TeamNum = $_POST["Team"];
$Course = $_POST["CourseName"];
$Aika = $_POST["Date"];
$Ope = $_POST["Teacher"];

echo "Tiedot: <br>";
echo "Etunimi: " . $Etunimi . "<br>";
echo "Sukunimi: " . $Sukunimi . "<br>";
echo "Opiskelijanumero: " . $StuNum . "<br>";
    $emailAdr = "gr" . $StuNum . "@gradia.fi";
echo "Opiskelija Numeron Sähköposti: " . $emailAdr . "<br>";
echo "Ryhmätunnus: " . $TeamNum . "<br>";
echo "Kurssin Nimi: " . $Course . "<br>";
echo "Ajankohta: " . $Aika . "<br>";
if($Ope === "t1"){
    $Ope = "Jaakko";
}
else if($Ope === "t2"){
    $Ope = "Teppo";
}
else if($Ope === "t3"){
    $Ope = "Juhani";
}
else if($Ope === "t4"){
    $Ope = "Mikko";
}
else if($Ope === "t5"){
    $Ope = "Pete";
}
echo "Opettajasi: " . $Ope . "<br><br>";


$to = $emailAdr;
$subject = "php Viesti!";
$txt = "päivää tässä tietoja sinusta" . "\n" . $Etunimi . "\n" . $Sukunimi . "\n" . $emailAdr . "\n" . $TeamNum . "\n" . $Course . "\n" . $Aika . "\n" . $Ope;
$headers = "From: kdnvkdnvk@gmail.com" . "\n" .
"CC: kdnvkdnvk@gmail.com";

if (mail($to,$subject,$txt,$headers)){
    echo "Email Lähetetty!";
}
else {
    echo "Email:ia ei voitu lähettää";
}



}





?>