<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel= stylesheet href="style.css">
    <link rel="icon" href="logo/FAVICON.png">
    <title>Tuottajamarket - Shop</title>
</head>
<body>
    <!-- HEADER -->
    <header>
        <div id="header-content">
            <div id="header-logo">
                <a href="index.php">
                    <img src="logo/OFFICIAL LOGO.png" alt="logo" class="logo">
                </a>
            </div>
            <div id="header-search">
                <div id="cart-div">
                    <a href="cart.php">
                        <img src="img/cart.png" alt="cart" class="cart">
                    </a>
                </div>
                <div id="search-button">
                    <a href="index.php">
                        <button>Etusivu</button>
                    </a>
                </div>
            </div>
        </div>
    </header>
    
    <!-- CONTENT -->
    <div id="shop">
        <div id="shop-content">
            <div id="intro-text">
                <h5>Verkkokauppa</h5>
            </div>
            <div id="info-input">
                <form method="POST">
                    <input type="text" placeholder="Etsi Tuotteita"> 
                    <br/>
                    <label class="container"> Kaikki
                        <input type="checkbox" checked="checked">
                        <span class="checkmark"></span>
                    </label>
                    <br/>
                    <label class="container"> Liha
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container"> Kala
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container"> Viljatuotteet
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container"> Marjat
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container"> Juustot
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container"> Muut Tuotteet
                        <input type="checkbox">
                        <span class="checkmark"></span>
                    </label>
                    <br/>
                </form>
            </div>
            <br/><br/><br/><br/>
            <div id="products">
            <?php
                // get database credentials
                $servername = "localhost";
                $username = "taitaja_2633";
                $password = "Vss449#uo"; // Edit: Can't do anything with this
                $data = "taitaja_2633";

                // try to connect to database
                try {
                    $conn = new PDO("mysql:host=$servername;dbname=$data", $username, $password);
                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                    $sql = "SELECT p.producer_id, p.category_id, p.name AS 
                                    product_name, p.prize, p.description, c.id, c.name AS 
                                    category_name
                        FROM products p
                        INNER JOIN categories c
                        ON p.category_id = c.id";

                    $result = $conn->query($sql);

                    // append data to divs
                    while($row = $result->fetch(PDO::FETCH_ASSOC)) {
                        echo "<div class='product'>";
                        echo "<div class='product-text'>";
                        echo $row['product_name'];
                        echo "</div>";
                        echo "<div class='product-type'>";
                        echo $row['category_name'];
                        echo "</div>";
                        echo "<div class='info'>";
                        echo $row['description'];
                        echo "</div>";
                        echo "<div class='price'>";
                        echo "<div class='product-price'>";
                        echo $row['prize'] . "€";
                        echo "</div>";
                        echo "<button class='add-to-cart'>Lisää ostoskoriin</button>";
                        echo "</div>";
                        echo "</div>";
                    }
                } catch(PDOException $e) {
                    echo "Connection failed: " . $e->getMessage();
                }
            ?>
            </div>
        </div>
    </div>
    
    <br/><br/><br/>
    <!-- FOOTER -->
    <footer>
        <h5>© TAITAJAT 2024</h5>
        <h3>Jooa Akonpelto</h3>
        <h3>Gradia</h3>
    </footer>
</body>
</html>
