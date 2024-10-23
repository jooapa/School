-- ====== Exercise 5 - SQL Basics 4 ======

-- 1 | Create a new table called offices with the following columns:
--     - OfficeID (primary key)
--     - OfficeName
--     - Address
--     - PostalCode
--     - City

-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 2 | Create a connection between offices and employees tables. Each employee can have one office attached (this should be an optional field). Use the following foreign key options:
--     - UPDATE CASCADE
--     - DELETE NO ACTION
-- Important: If you get an error (code 1452), run the following command for the current session before connection creation:
--     - SET FOREIGN_KEY_CHECKS=0;
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 3 | Now do the following modifications to offices table:
-- 	- Add automatic counter for the OfficeID column so that new value will be generated automatically each time new data is inserted.
-- 	- Add a new column: manager (use data type int)
-- 	- Create another connection between offices and employees tables so that each office will have one employee working as a manager.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 4 | Create input validation check using TRIGGER to offices table. OfficeName field value should not begin with a word office (for example, officenorth should not be accepted while northoffice will be accepted).
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 5 | Create a new table called warehouses with the following columns:
-- 	- WarehouseID (primary key, numerical value with auto increment feature)
-- 	- Address
-- 	- PostalCode
-- 	- City
-- 	- SurfaceArea (number with one decimal in square meters)
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 6 | Connect warehouses table to suppliers table. Each supplier can have many warehouses for supplies, but each warehouse can only be used by one supplier. Use the same foreign key options as previously:
--     - UPDATE CASCADE
--     - DELETE NO ACTION
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 7 | Add the following columns to warehouses table:
-- 	- LastUpdated (automatic datetime value when new data is inserted or existing data is updated)
-- 	- AdditionalInfo (should store large amount of text data)
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 8 | Create a table called storages. Suppliers will store the following information about products into this table:
-- 	- StorageID (integer with auto increment feature)
-- 	- Shelf (shelf identifier, ie. A1, A2 etc.)
-- 	- Quantity (number of product units that have been stored)
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 9 | Connect the storages table with products and warehouses tables. One row in storages table will tell how many units of what product is stored in which warehouse (and of course the specific location in that warehouse created earlier with shelf identifier). Use a primary key column StorageID for this table with integer data type and auto increment feature.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 10 | Create input validation check using TRIGGER to storages table. The following two conditions should be check before data is inserted:
-- 	- Quantity cannot be negative and cannot exceed the value of 5000000.
-- 	- Shelf identifiers must be in format XY where X can only be a letter in range A-Z inclusive and Y a number in range 0-9 inclusive (for example, AX1 should not be accepted).
-- --------------------------------------------------

-- --------------------------------------------------