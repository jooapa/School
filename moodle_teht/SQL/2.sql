--====== Exercise 2 - SQL Basics 1 ======

-- 1 | Select employees whose firstname starts with letter A.
--------------------------------------------------
SELECT * FROM `employees` WHERE FirstName LIKE 'A%'
--------------------------------------------------

-- 2 | Select customers who live in London.
--------------------------------------------------
SELECT * FROM `customers` WHERE city = 'London'; 
--------------------------------------------------

-- 3 | Select all different cities from customers table. Remember to remove duplicates!
--------------------------------------------------
SELECT DISTINCT city FROM `customers`;
--------------------------------------------------

-- 4 | Select customers whose postal code starts with number 1 and customerID is between 50 and 70.
--------------------------------------------------
SELECT * FROM `customers` WHERE PostalCode LIKE '1%' AND CustomerID BETWEEN 50 AND 70;
--------------------------------------------------

-- 5 | Select suppliers operating in any of the following countries: Australia, Finland or Japan.
--------------------------------------------------
SELECT * FROM `suppliers` WHERE Country IN ('Australia', 'Finland', 'Japan');
--------------------------------------------------

-- 6 | Select product categories where the word 'bread' is mentioned in the description column. Any wording is acceptable (bread, breads).
--------------------------------------------------
SELECT * FROM `categories` WHERE Description LIKE '%bread%';
--------------------------------------------------

-- 7 | Select products priced over 20 and packed in either cans or boxes. Order the result set by product name in ascending order.
--------------------------------------------------
SELECT * FROM `products` WHERE (Unit LIKE "%box%" OR Unit LIKE "%can%") AND Price > 20 ORDER BY ProductName ASC; 
--------------------------------------------------

-- 8 | Select employees who have been born in 50s or 60s and whose lastname does not start with letters A, B, C or D. Order the result set by employees firstname in descending order.
--------------------------------------------------
SELECT * FROM `employees` WHERE (YEAR(BirthDate) BETWEEN 1950 AND 1960) AND LastName NOT LIKE 'A%' AND LastName NOT LIKE 'B%' AND LastName NOT LIKE 'C%' AND LastName NOT LIKE 'D%' ORDER BY FirstName DESC;
--------------------------------------------------

-- 9 | Select products with missing price. ProductID, ProductName, Unit and Price should be included in the result set. Use alias name Incomplete for the column.
--------------------------------------------------
SELECT ProductID, ProductName, Unit, Price AS Incomplete FROM `products` WHERE Price IS NULL;
--------------------------------------------------

-- 10 | Select products with ProductID in range 50-80. Then show only 10 rows starting from ProductID 60 (included in result set).
--------------------------------------------------
SELECT * FROM `products` WHERE ProductID BETWEEN 50 AND 80 LIMIT 10 OFFSET 10;
--------------------------------------------------
