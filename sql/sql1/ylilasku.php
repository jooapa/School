
<!DOCTYPE html>
<head>
    <style>

    </style>
</head>
<?php

if (isset($_POST['lähetys'])) {
    $tetu = $_POST["arvo"];
}
$servername = "localhost";
$username = "root";
$password = "";
$data = "data";

$conn = new mysqli($servername, $username, $password, $data);

$sql = "SELECT IF(tilausrivitaulu.tilausmaara * tuotetaulu.hinta > $tetu ,asiakastaulu.etunimi, Null) AS etunimi,
IF(tilausrivitaulu.tilausmaara * tuotetaulu.hinta > $tetu ,asiakastaulu.email, Null) AS email
FROM `asiakastaulu`
JOIN tilaustaulu
ON asiakastaulu.id = tilaustaulu.asiakas_id
JOIN tilausrivitaulu
ON tilaustaulu.id = tilausrivitaulu.tilaus_id
JOIN tuotetaulu
ON tuotetaulu.id = tilausrivitaulu.tuote_id
GROUP BY etunimi;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        if ($row["etunimi"] == '') {}
        else{
           echo $row["etunimi"]." Email: ". $row["email"]."<br>";
        }
    }
} else {
    echo "empty Database";
}

$conn->close();
?>

</body>
</html>
