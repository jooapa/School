<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mustat Renkaat</title>

    <style>   
            @font-face {
            font-family: Font;
            src: url(RacingSansOne-Regular.ttf)
        }   

        * {
            font-family: Font;
        }  
        @keyframes logo-scale {
            0% {
                transform: (0px,-200px)
            }
            100% {
                transform: translate(0px,0px)
            }
        }
        html{
            scroll-behavior: smooth;
        }
        body{ /*bodyn css*/
            color: aliceblue;
            background: rgb(1,35,38);
            overflow-x: hidden;
            height: 100vw ;
            width: 100vw;
            margin: 0;
        } 
        div{
            display: block;
        } 
        #logo-img{
            animation: 2s cubic-bezier(.24,.76,0,1.14) 0.01s 1 logo-scale;/*tämä aloittaa logo-animaation, heti kuin sivu on ladattu*/
            width: 100vw;
            height: 50vw;
            min-width: 100vw;
        }
        .container-pre-logo{  /*Tämä sisältää napit*/
            background-color: #012840;   
            width: 100vw;
            height: 360px; 
            min-width: 100vw; 
            min-width: 100vw;  
        }
        .container-contain{/*Grid: napeille*/
            display: grid;
            grid-template: 1fr 1fr / auto;
            row-gap: 20px;
            justify-items: center;
            align-items: center;
            transform: translate(0px,50px);
        }
        .text1{/*MAINOS TEXTI!!*/
            text-align: center;
        }
        .text2{ /*SQL MITÄÄN EI LÖYTYNYT teksti*/ 
            text-shadow: 0px 0px 20px #000000;
            text-align: center;
        }
        #button-grid-1, #button-grid-2{/*container-contain:Nappien css* button-grid-1 == search options button-grid-2 == MEISTÄ button*/
            transition: 1s cubic-bezier(.21,1.29,.4,.99);
            color: aliceblue;
            background-color: #0123266d;
            padding: 8px;
            font-size: 24px;
            width: 100vw;
            margin: 0px;
            border: 2px solid #00000055;
            position: static;
        }
        #button-grid-1:hover, #button-grid-2:hover{/*container-contain:Nappien hover css*/
            transition: 1s cubic-bezier(.21,1.29,.4,.99);
            background-color: #012326bf;
            padding-top: 12px;
        }
        #button-grid-1:active, #button-grid-2:active{/*container-contain: kun painetaan Nappia css*/
            transition: 1s cubic-bezier(.21,1.29,.4,.99);
            background-color: #012326;
            padding-top: 20px;
        }

        #button-grid-2{
            position: absolute;
            top: 242px;
        }
        input, select{
            appearance: auto;
            user-select: none;
            white-space: pre;
            align-items: flex-start;
            text-align: center;
            cursor: default;
            box-sizing: border-box;
            background-color: buttonface;
            color: buttontext;
            padding: 1px 6px;
            border-width: 2px;
            border-style: outset;
            border-color: buttonborder;
            border-image: initial;
        }
        select{
            color: aliceblue;
            background-color: #01232683;
            width: 100vw;
            font-size: 24px;
            height: 35px;
        }

        .imageDiv-overlay{/*gradiantti logosta --> kuvaan*/
            position: absolute;
            background: linear-gradient(180deg, rgba(1,35,38,1) 0%, rgba(1, 40, 64, 0) 100%); 
            width: 100vw;
            height: 200px;
        }
        .image-grid{/*Tämä sisältää kaiken tähän mennessä koodia*/
            width: 100vw;
            display: grid;
            grid-template: auto / 1fr 1fr;
            justify-items: center;
            gap: 40px;
            margin-top: 40px;
        }
        img{ /*kuvien css*/
            height: 400px; 
            width: auto;
            border-radius: 10px;
        }
        .meista-container{ /*meistä kohtan parent*/
            
            background-color: #012326;
            filter: brightness(0.9);
        }
        #headertext{
            font-size: 24px;
            
        }
        .meista{ /*Yritykset tiedot div: css*/
            display: flex;
            width: 100vw;
            height: fit-content;
            text-align: center;
            margin-top: 105px;
            flex-direction: column;
            justify-content: center;
            align-content: center;
            flex-wrap: wrap;
            gap: 30px;
        }

        .karttakuva-div{/*Karttakuva div: css*/
            background-color: #012326;
            filter: brightness(0.8);
            display: flex;
            position: inherit;
            justify-content: center;
            width: 100vw;
        }
        #karttakuva{/*img karttakuvan id*/
            transition: 1s cubic-bezier(.25,.86,0,1.36);
            height: auto;
            width: 90vw;
            margin-bottom: 150px;
            margin-top: 100px;
            box-shadow: 0px 0px 0px #ffffff;
        }
        #karttakuva:hover{
            box-shadow: 0px 0px 5px #ffffff;
        }
        #karttakuva:active{
            box-shadow: 0px 0px 10px #ffffff;
        }
        .gridimg{
            width: 400px;
            height: auto;
        }
        @media only screen and (max-width: 1000px) { /*media säännöt*/
            img{
                height: 500px;
            }
            .image-grid{
            grid-template: revert;
            }
           
            .meista{
                align-items: center;
                flex-direction: column;
                flex-wrap: wrap;
            }
        }
        @media only screen and (min-width: 1750px) {
            .image-grid{
            grid-template: auto / 1fr 1fr 1fr 1fr;

            }
            .meista{
                gap: 50px;
                flex-direction: row;
            }
            
        }
        @media only screen and (max-width: 550px) {
            .gridimg{
                width: 90vw;
                height: auto;
                object-fit: cover;
                object-position: center;
            }
        }
        footer{
            display: block;
            background: linear-gradient(180deg, rgb(0 28 30) 0%, rgba(2,48,89,1) 71%);
            width: 100vw;
            height: 100px;
            
        }
        #footerh2{
            position: relative;
            font-family: 'Roboto', sans-serif;
            font-weight: lighter;
            text-align: center;
            margin: 0;
            bottom: -70px;
            font-size: 14px;
            padding: 0;
        }
        .SQL-grid{ /*SQL grid mihin tulee tuotteen */
            display: grid;
            background-color: #012840;
            background: linear-gradient(0deg, rgb(0 28 30) 0%, rgba(2,48,89,1) 71%);
            grid-template-columns: 1fr;
            gap: 15px;
            justify-items: center;
        }
        @media only screen and (min-width: 800px) {
            .SQL-grid{
                grid-template-columns: 1fr 1fr;
            }
        }
        @media only screen and (min-width: 1000px) {
            .SQL-grid{
                grid-template-columns: 1fr 1fr 1fr;
            }
        }
        @media only screen and (min-width: 1400px) {
            .SQL-grid{
                grid-template-columns: 1fr 1fr 1fr 1fr;
            }
        }
        @media only screen and (min-width: 1600px) {
            .SQL-grid{
                grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
            }
        }
        @media only screen and (min-width: 2000px) {
            .SQL-grid{
                grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
            }
        }
        .product{
            position: relative;
            height: 300px;
            width: 300px;
            background-color: #000000;
            border-radius: 20px;
        }
        .product h2,.product h1 {
            text-align: left;
            margin-left: 15px;
        }
        .hintadiv{
            position: relative;
            width: fit-content;
            height: fit-content;
            background-color: green;
            padding-left: 5px;
            padding-right: 5px;
            border-radius: 3px;
            right: -160px;
            bottom: 55px;
        }
        #hinta{
            color: #ffffff;
            font-size: 32px;
        }
        .Searchdiv h1{
            background-color: #0123266d;
            margin: 0;
            width: 100vw;
        }
    </style>
</head>
<body>
    <img id="logo-img" src="RengasKuvat/logo_dark.svg"> 
    <div class="imageDiv-overlay">
    </div>
    <div class="imageDiv">
        <img src="RengasKuvat/arseny-togulev-xTXIAVRI3rA-unsplash.jpg" style="width: 100vw;height: auto;">
        <div class="container-pre-logo">
            <div class="container-contain">
                <div class="Searchdiv">
                    <form method="POST"> <!--Renkaiden haku formi -->
                        <input id="button-grid-1" type="text" name="tiretext">
                        <select name="TireCompany">
                            <option value="">Kaikki Yritykset</option>
                            <option value="Nokian">Nokian</option>
                            <option value="Kumho">Kumho</option>
                            <option value="Hankook">Hankook</option>
                        </select>
                        <select name="TireType">
                            <option value="">Kaikki Tyypit</option>
                            <option value="Kesä">Kesä</option>
                            <option value="Talvi">Talvi</option>
                            <option value="Kitka">Kitka</option>
                          </select>
                        <select name="TireSize">
                            <option value="">Kaikki Koot</option>
                            <option value="165/55-14">165/55-14</option>
                            <option value="165/65-14">165/65-14</option>
                            <option value="165/55-15">165/55-15</option>
                            <option value="175/65-15">175/65-15</option>
                            <option value="185/65-15">185/65-15</option>
                            <option value="205/65-16">205/65-16</option>
                            <option value="175/65-14">175/65-14</option>
                            <option value="185/65-14">185/65-14</option>
                            <option value="235/65-17">235/65-17</option>
                            <option value="235/60-18">235/60-18</option>
                            <option value="195/65-15">195/65-15</option>
                            <option value="225/55-18">225/55-18</option>
                            <option value="235/60-17">235/60-17</option>
                            <option value="255/50-19">255/50-19</option>
                            <option value="205/55-16">205/55-16</option>
                            <option value="185/55-15">185/55-15</option>
                            <option value="195/55-15">195/55-15</option>
                          </select>
                        <select name="Sort">
                            <option value="Hinta">Lajittele Hinnan mukaan:</option>
                            <option value="Merkki">Lajittele Merkin mukaan:</option>
                        <select>
                        
                        <input id="button-grid-1" type="submit" value="Hae Renkaita" name="haetires">
                    </form>
                </div>
                <button onclick="location.href='#meista-id'" id="button-grid-2">MEISTÄ</button> <!--Klikkauksen jälkeen tämä vie #meista-id diviin-->
            </div>
        </div>
        
            
        <div class="SQL-grid">
            <?php
            if (isset($_POST['haetires'])) {
                    $TireText = $_POST["tiretext"]; //ottaa formista tiedot muuttujaan
                    $TireCompany = $_POST["TireCompany"]; //ottaa formista tiedot muuttujaan
                    $TireType = $_POST["TireType"];
                    $TireSize = $_POST["TireSize"];
                    $Sort = $_POST["Sort"];
                    if($TireCompany == ""){$TireCompany = "";} //Tämä muuttaa muuttajat eri SQL Lauseiseen, filtteröintia varten
                        else{$TireCompany = "WHERE Merkki ='$TireCompany'";}

                    if($TireType == ""){$TireType = "";}
                        else if($TireCompany == ""){$TireType = "WHERE Tyyppi ='$TireType'";}
                        else{$TireType = "AND Tyyppi ='$TireType'";}
                        
                        
                    if($TireSize == ""){$TireSize = "";}
                        else if($TireCompany == "" and $TireType == ""){$TireSize = " WHERE Koko = '$TireSize'";}
                        else if($TireCompany != "" and $TireType == ""){$TireSize = " AND Koko = '$TireSize'";}
                        else if($TireCompany != "" and $TireType != ""){$TireSize = " AND Koko = '$TireSize'";}

                         
                    if ($TireText == "") {
                        $TireText == "";
                    } 
                        if($TireText != ""){
                            if($TireCompany == "" && $TireSize == "" && $TireType == ""){
                                $TireText = "WHERE Malli LIKE '%$TireText%'";
                            }
                            else if($TireCompany != "" || $TireSize != "" || $TireType != ""){
                                $TireText = "AND Malli LIKE '%$TireText%'";
                            }
                        }
                    
                    
                    $servername = "localhost"; //etsii tietokannan
                    $username = "root";
                    $password = "";
                    $data = "renkaat";
                    $conn = new mysqli($servername, $username, $password, $data);
                    $sql = "SELECT * FROM renkaat $TireCompany $TireType $TireSize $TireText ORDER BY $Sort";//SQL lause
                    $result = $conn->query($sql);
                    if ($result->num_rows > 0) {
                        while($row = $result->fetch_assoc()) { //Tämä laittaa rivit HTML:llään                            
                            echo "<div class='product'>
                            <h1>" . $row["Merkki"] . "</h1>
                            <h2>" . $row["Malli"] . "</h2>
                            <h2>" . $row["Tyyppi"] . "</h2>
                            <h2>" . $row["Koko"] . "</h2>
                            <h2>" . $row["Saldo"] . "</h2>
                            
                            <div class='hintadiv' <h1 id='hinta'>" . $row["Hinta"] . "€</h1></div></div>";
                        }
                    } else {
                        echo "</div><div class='text2'>
                        <h1>MITÄÄN EI LÖYTYNYT</h1>
                        </div>";
                    }
                    //echo"</table>";
                    $conn->close();
                }
                ?>
        </div>
        <div class="text1">
            <h1>KORJAAMME SINUN AUTON</h1>
            <h1>NOPEIN AUTOKORJAAMO SUOMESSA</h1>
            <h1>100% TAKUU</h1>
        </div>
    </div>
    <div class="image-grid">
        
        <div class="image-grid-1">
            <img class="gridimg" src="RengasKuvat/pexels-andrea-piacquadio-3807649.jpg">
        </div>
        <div class="image-grid-2">
            <img class="gridimg" src="RengasKuvat/Alpine.jpeg">
        </div>
        <div class="image-grid-3">
            <img class="gridimg" src="RengasKuvat/tekton-O_ufcLVTAYw-unsplash.jpg">
        </div>
        <div class="image-grid-4">
            <img class="gridimg" src="RengasKuvat/jairph-7pT4LWfORS0-unsplash.jpg">
        </div>
    </div>
    
    <div class="meista-container" id="meista-id">
        <div class="text1" id="headertext">
            <h1>MEISTÄ</h1>
        </div>
        <div class="meista">
            <div class="meista-1">
                <h1 style="text-align: center;">LÖYDÄT MEIDÄT</h1>
                <h2>Kosteenkatu 1, 86300 Oulainen</h2>
            </div>
            <div class="meista-2">
                <h1>PUHELIN</h1>
                <h2>040-7128158</h2>
            </div>
            <div class="meista-3">
                <h1>EMAIL</h1>
                <h2>myyntimies@mustatrenkaat.net</h2>
            </div>
        </div>
        
    </div>
    <div class="karttakuva-div">
        <img id="karttakuva" src="RengasKuvat/MUSTATrenkaat_Karttakuva.jfif">
    </div>
    <footer>
        <h2 id="footerh2">© 1999-2023 Mustapään Auto Oy. Kaikki Oikeudet Pidätetään</h2>
    </footer>
        <script src="js.js"></script>
</body>
</html>
