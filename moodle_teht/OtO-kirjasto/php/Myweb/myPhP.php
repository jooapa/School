<DOCTYPW html>
    <head>
    <title>redirect comberbutch</title>
    </head>
    <body>
    <h2>Redirecting..</h2>
<?php
$username = $_POST["username"];
$password = $_POST["password"];
$hash = '$2y$10$dH3pytshyJRKvOHoRejR.epGRkTnTc37XAmXP2PNrZ5VaUsCupfAq';
$verify = password_verify($password, $hash);

if ($verify) {
    if ($username != 'jooadmin'){
	    echo 'Something went Wrong :/';
    }
    else{
        echo "Hello jooapa!!";
        header("Location: index.html");
        echo ('if not working click <a href="http://jakonpelto.jypatipt.com/index.html?change=2">here</a>');
        exit(); 
           
    }
    return;
    
} else {
	echo 'Incorrect Password!';
    header("Location: http://jakonpelto.jypatipt.com?change=1");
    echo ('if not working click <a href="http://jakonpelto.jypatipt.com/index.html?change=1">here</a>');
    exit();
    
}   

?>