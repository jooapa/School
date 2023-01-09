
<?php


$i = 0;
$j = 0;
$num = 0;
if ($_POST['lähetys']) {
  $numero = intval($_POST["numero"]);
}
while($i < $numero){ //column's
  $j = 0;
  while($j <= $i){ // rows acc to outer loop
    
    echo $num. "  ";
    $j++;
  }
  
  $i++;
  $num +=  1; //kasvaa numero
  echo "<br>";
}
?>