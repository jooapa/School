<?php
$nimesi = $_POST["name"];
$palkkasi = $_POST["tuntipalkka"];
$verosi = $_POST["veroPros"];
$netto = (1 - ($verosi/100)) * $palkkasi;

echo "Nimesi on ".$nimesi;
echo "<br>Bruttopalkkasi on ".$palkkasi;
echo "<br>Nettopalkkasi on ".$netto;
?> 