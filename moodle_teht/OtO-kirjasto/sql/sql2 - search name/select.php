
<!DOCTYPE html>
<head>
    <style>

    </style>
</head>
<?php

$servername = "localhost";
$username = "root";
$password = "";
$data = "data";

$conn = new mysqli($servername, $username, $password, $data);

$sql = "SELECT * FROM tilaustaulu;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo $row["id"].": ".$row["asiakas_id"]." Email: ". $row["pvm"]."<br>";
    }
} else {
    echo "empty Database";
}

$sql = "SELECT COUNT(*) AS 'rivitid' FROM tilaustaulu;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<br>Rivejä on ".$row["rivitid"]."<br>";
    }
} else {
    echo "empty Database";
}

$conn->close();
?>

</body>
</html>
