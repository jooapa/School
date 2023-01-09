
<!DOCTYPE html>
<?php

if (isset($_POST['lähetys'])) {
    $tetu = $_POST["etunimi"];
    $tsuku = $_POST["sukunimi"];
    $temail = $_POST["email"];
    $tosoite = $_POST["osoite"];
    $tposti = $_POST["posti"];
    $tkunta = $_POST["kunta"];
}
$servername = "localhost";
$username = "root";
$password = "";
$data = "data";

$conn = new mysqli($servername, $username, $password, $data);
$sql = "SELECT * FROM asiakastaulu";
$result = $conn->query($sql);



$sql = "INSERT INTO `asiakastaulu` (etunimi, sukunimi, email, osoite, postinumero, paikkakunta) 
VALUES ('$tetu', '$tsuku', '$temail', '$tosoite', '$tposti', '$tkunta')";
$result = $conn->query($sql);

$sql = "SELECT * FROM asiakastaulu";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["etunimi"]." " . $row["sukunimi"]." Email: ". $row["email"]." Osoite: ". $row["osoite"]. " Postinumero: ". $row["postinumero"]." Paikkakunta: ". $row["paikkakunta"]."<br>";
    }
} else {
    echo "empty Database";
}

$conn->close();
?>

</body>
</html>
