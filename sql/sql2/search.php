
<!DOCTYPE html>
<head>
    <style>

    </style>
</head>
<?php
$sukunimi = "";
$etunimi = "";
if ($_POST['lähetysEtu']) {
    $sukunimi = $_POST["nimi"];
    $etunimi = $_POST["etunimi"];
}

$servername = "localhost";
$username = "root";
$password = "";
$data = "data";
$conn = new mysqli($servername, $username, $password, $data);

    $sql = "SELECT * FROM asiakastaulu WHERE sukunimi LIKE '$sukunimi%' AND  etunimi LIKE '$etunimi%';";


$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo $row["etunimi"]." " . $row["sukunimi"]." Email: ". $row["email"]." Osoite: ". $row["osoite"]. " Postinumero: ". $row["postinumero"]." Paikkakunta: ". $row["paikkakunta"]."<br>";
    }
} else {
    echo "Nothing Found :/";
}
$conn->close();
?>
</body>
</html>
