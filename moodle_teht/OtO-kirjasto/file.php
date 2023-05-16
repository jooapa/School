<?php
/*
function prompt($prompt_msg){
    echo("<script type='text/javascript'> var answer = prompt('.$prompt_msg.'); </script>");

    $answer = "<script type='text/javascript'> document.write(answer); </script>";
    return($answer);
}
function prompt1($prompt_msg1){
    echo("<script type='text/javascript'> var answer1 = Number(prompt('$prompt_msg1')); </script>");

    $answer1 = "<script type='text/javascript'> document.write(answer1); </script>";
    return($answer1);
}
function prompt2($prompt_msg2){
    echo("<script type='text/javascript'> var answer2 = prompt('.$prompt_msg2.'); </script>");

    $answer2 = "<script type='text/javascript'> document.write(answer2); </script>";
    return($answer2);
}


$prompt_msg = "Syötä Nimesi tähän!";
$name_msg = prompt($prompt_msg);
$name = "Nimesi on ".$name_msg.".";

$vero_msg = prompt1(intval($prompt_msg1));
$vero = "<p>Veroprosenttisi on $vero_msg.% </p>";
$veroInt = $prompt_msg1;

$Netto = 100- $vero_msg;

$prompt_msg2 = "Syötä Kuukautispalkkasi!";
$kkpalkka_msg= prompt2($prompt_msg2);
$kkpalkka = "<p>Kuukautispalkkasi on ".$kkpalkka_msg."€ </p>";

$Netto = 100 - $vero_msg; 
echo $name;
echo $vero;
echo $kkpalkka;
echo "<p>Bruttopalkkasi on $kkpalkka_msg </p>";
echo "<p>Nettopalkkasi on $veroInt </p>";
echo "brutto palkkasi on $kkpalkka";

/*
?>
