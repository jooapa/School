<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mustat Renkaat</title>
    <body>
        
    <?php
    $usernameErr = $emailErr = $phoneErr = $addressErr = "";
        

    if (isset($_POST['submit'])){
        $username2   = $_POST['username'];
        $password2   = $_POST['password'];
        $email      = $_POST['email'];
        $phone      = $_POST['phone'];
        $address    = $_POST['address'];
        $hashed_password = password_hash($password2, PASSWORD_ARGON2I);


        $username = test_input($_POST["username"]);
        // check if name only contains letters and whitespace
        if (!preg_match("/^[a-zA-Z-' ]*$/",$username)) {
        $usernameErr = "Käyttäjänimessä ei saa olla /^[a-zA-Z-' ]*$/";
        header("Refresh:0");
        }

        if (empty($_POST["email"])) {
            $emailErr = "Email is required";
        } else {
        $email = test_input($_POST["email"]);
        // check if e-mail address is well-formed
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $usernameErr = "Käyttäjänimessä ei saa olla /^[a-zA-Z-' ]*$/";
                header("Refresh:0");
        }
    }


        $servername = "localhost"; //etsii tietokannan
        $username = "root";
        $password = "";
        $data = "renkaat";
        $conn = new mysqli($servername, $username, $password, $data);
        $sql = "INSERT INTO tilit (username, password, email, puh, kotiosoite)
        VALUES ('$username2', '$hashed_password', '$email', '$phone', '$address')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        //echo"</table>";
        $conn->close();

        
        var_dump($password . "<br>");
        

        var_dump($hashed_password);

    }

    if (isset($_POST['LogIn'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

        if(password_verify($password, $hashed_password))
        { // Mikäli salassana oikein
        echo " lol";
        } // Else, Mikäli salasana ei täsmää palataan login ikkunaan
    }
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
        }
?>
    SIGN UP<br>
    <form method="POST">
        Käyttäjänimi:<br>
        <input type="text" name="username" id="username-id"> <span class="error"> <?php echo $usernameErr;?></span>
        <br>
        Email:<br>
        <input type="text" name="email" id="email-id">
        <br>
        Puhelinnumero:<br>
        <input type="text" name="phone" id="phone-id">
        <br>
        Kotiosoite:<br>
        <input type="text" name="address" id="address-id">
        <br>
        Salasana:<br>
        <input type="password" name="password" id="password-id">
        <br>
        <input type="submit" value="Sign Up" name="submit">
    </form>
    LOG IN<br>
    <form method="POST">
        Käyttäjänimi:<br>
        <input type="text" name="username" id="username-id">
        <br>
        Salasana<br>
        <input type="password" name="password" id="password-id">
        <br>
        <input type="submit" value="Log In" name="LogIn">
    </form>

    </body>
</html>