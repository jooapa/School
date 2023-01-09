<?php



$servername = "localhost";
$username = "root";
$password = "";
$data = "data";
$conn = new mysqli($servername, $username, $password, $data);
$post1 = true;
if (!empty($_POST['1'])){
    $CustomerId = $_POST["asiakas-id"];
    $sql = "SELECT etunimi, sukunimi, tuotetaulu.tuotenimi
    FROM asiakastaulu
    JOIN tilaustaulu
    ON asiakastaulu.id = tilaustaulu.asiakas_id
    JOIN tilausrivitaulu
    ON tilausrivitaulu.tilaus_id = tilaustaulu.id
    JOIN tuotetaulu
    ON tuotetaulu.id = tilausrivitaulu.tuote_id
    WHERE asiakastaulu.id = $CustomerId;";
    $post1 = true;
}

if (!empty($_POST['2'])) {
    $sql = "SELECT tilaus_id,tilausmaara, tuotetaulu.tuotenimi, tuotetaulu.hinta
    FROM tilausrivitaulu
    JOIN tuotetaulu
    ON tuotetaulu.id = tilausrivitaulu.tuote_id;";
    $post1 = false;
 }

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        if($post1 === true){
            echo $row["etunimi"]." " . $row["sukunimi"]." Email: ". $row["tuotenimi"]."<br>";
        }
        else{
            echo $row["tilaus_id"]." Tuotteiden Määrä: " . $row["tilausmaara"]." Tuotteen Nimi: ". $row["tuotenimi"]." Tuotteen Hinta: ".  $row["hinta"]."<br>";
        }
    }
} else {
    echo "Nothing Found :/";
}
$conn->close();
?>
