-- ====== Exercise 4 - SQL Basics 3 ======

-- 1 | Select all products with product categories and include also products without the category. Product name and its category name should be presented in the result set.
--------------------------------------------------
SELECT p.ProductName, c.CategoryName
FROM products p
LEFT JOIN categories c
ON p.CategoryID = c.CategoryID;
--------------------------------------------------

##################################################
-- 2 | Select products that have never been ordered. Include product name in the result set.
--------------------------------------------------
SELECT p.ProductName
FROM products p
LEFT JOIN orderdetails od
ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;
--------------------------------------------------

##################################################
-- 3 | Count how many orders each shipper has delivered. Show shipper name and count in the result set. Use column name shipped_orders for the calculated column.
--------------------------------------------------
SELECT s.ShipperName, COUNT(o.ShipperID) AS shipped_orders
FROM shippers s
LEFT JOIN orders o
ON s.ShipperID = o.ShipperID
GROUP BY s.ShipperName;
--------------------------------------------------

##################################################
-- 4 | List categories with 10 or more products. Show category name and product count in the result set. Order the result set by product count in descending order.
--------------------------------------------------
SELECT c.CategoryName, COUNT(p.ProductID) AS ProductCount
FROM categories c
LEFT JOIN products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
HAVING COUNT(p.ProductID) >= 10
ORDER BY ProductCount DESC;
--------------------------------------------------

##################################################
-- 5 | Calculate how many products each customer have ordered (sum quantities). Use column name total_bought for the calculated column. In addition to this column show customers name in the result set.
--------------------------------------------------
SELECT c.CustomerName, SUM(od.Quantity) AS TotalBought
FROM customers c
LEFT JOIN orders o
ON c.CustomerID = o.CustomerID
LEFT JOIN orderdetails od
ON o.OrderID = od.OrderID
GROUP BY c.CustomerName;
-------------------------------------------------- 

##################################################
-- 6 | List products with price greater or equal than all products with product name starting with letter Q. Include productID, product name and price in the result set. Order the result set by price in descending order.
--------------------------------------------------
SELECT p.ProductID, p.ProductName, p.Price
FROM products p
WHERE p.Price >= ALL (SELECT p2.Price
                      FROM products p2
                      WHERE p2.ProductName LIKE 'Q%')
ORDER BY p.Price DESC;
--------------------------------------------------

##################################################
-- 7 | Use UNION to gather the following customers:
-- 	- Customers coming from Argentina or Brazil
-- 	- Customers who have made at least one order in 17th of August 2023
-- Show customer name in the result set and order the result set by customer name in ascending order.

--------------------------------------------------
SELECT c.CustomerName
FROM customers c
WHERE c.Country = 'Argentina' OR c.Country = 'Brazil'
UNION
SELECT c.CustomerName
FROM customers c
LEFT JOIN orders o
ON c.CustomerID = o.CustomerID
WHERE o.OrderDate = '2023-08-17'
ORDER BY CustomerName ASC;
--------------------------------------------------

##################################################
-- 8 | Calculate the total price (quantity*price) for products in the following orderIDs: 10250, 10260, 10270 and 10280. Use column name total_price for the calculated column. In addition to this column, show product name in the result set.
--------------------------------------------------
SELECT p.ProductName, SUM(od.Quantity * p.Price) AS TotalPrice
FROM products p
LEFT JOIN orderdetails od
ON p.ProductID = od.ProductID
WHERE od.OrderID IN (10250, 10260, 10270, 10280)
GROUP BY p.ProductName;
--------------------------------------------------

##################################################
-- 9 | Use UNION to gather the following suppliers:
-- 	- Suppliers having five or more products
-- 	- Suppliers with postal code length five or less and country is Japan
-- 	- Suppliers offering products in seafood and dairy products categories
-- Show supplier name, contact name and phone number in the result set. Order the result set by supplier name in ascending order.
--------------------------------------------------
SELECT s.SupplierName, s.ContactName, s.Phone
FROM suppliers s
LEFT JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierName
HAVING COUNT(p.ProductID) >= 5
UNION
    SELECT s.SupplierName, s.ContactName, s.Phone
    FROM suppliers s
    WHERE LENGTH(s.PostalCode) <= 5 AND s.Country = 'Japan'
UNION
    SELECT s.SupplierName, s.ContactName, s.Phone
    FROM suppliers s
    LEFT JOIN products p
    ON s.SupplierID = p.SupplierID
    LEFT JOIN categories c
    ON p.CategoryID = c.CategoryID
    WHERE c.CategoryName IN ('Seafood', 'Dairy Products')
ORDER BY SupplierName ASC;

--------------------------------------------------

##################################################
-- 10 | List customers who have bought the most popular product (most sold). Include customer name and quantity in the result set and order the result set by quantity in descending order.
--------------------------------------------------
SELECT c.CustomerName, SUM(od.Quantity) AS Quantity
FROM customers c
LEFT JOIN orders o
ON c.CustomerID = o.CustomerID
LEFT JOIN orderdetails od
ON o.OrderID = od.OrderID
WHERE od.ProductID = (SELECT od2.ProductID
                      FROM orderdetails od2
                      GROUP BY od2.ProductID
                      ORDER BY SUM(od2.Quantity) DESC
                      LIMIT 1)
GROUP BY c.CustomerName
ORDER BY Quantity DESC;
--------------------------------------------------