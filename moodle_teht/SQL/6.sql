-- ====== Exercise 6 - SQL Basics 5 ======

-- 1 | Create the following offices:
-- 	- Saint Louis office (address: Palm st 16, postalcode: 63107, city: Saint Louis, manager: Robert King)
-- 	- Springfield office (address: Ohio Ave 3, postalcode: 62702, city: Springfield, manager: Nancy Davolio)
-- 	- Kansas City office (address: Beverly st 80, postalcode: 66204, city: Kansas City, manager: Adam West)
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 2 | Create the following warehouses:
-- 	- Liberty warehouse (address: Grant Ave 400, postalcode: 64068, city: Liberty, surfacearea: 200m2, supplier: New Orleans Cajun Delights)
-- 	- Blue Springs warehouse (address: 1030 SE Forest Ridge Ct, postalcode: 64014, city: Blue Springs, surfacearea: 350m2, supplier: Tasty Roots)
-- 	- Eldon warehouse (address: 800 W Champain St, postalcode: 65026, city: Eldon, surfacearea: 400m2, supplier: New Orleans Cajun Delights)
-- 	- Quincy warehouse (address: 3100 Payson Rd, postalcode: 62305, city: Quincy, surfacearea: 280m2, supplier: Tropical Fruits)
-- 	- Cameron warehouse (address: 650 E Grand Ave, postalcode: 64429, city: Cameron, surfacearea: 310m2, supplier: Bigfoot Breweries)
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 3 | Let's add couple of products into some of previously created warehouses (more specifically into storage shelves inside warehouses). Add the following products:
-- 	- Products in Liberty Warehouse (Grant Ave 400):
-- 		* product: Chang, quantity: 16000, shelf: A7
-- 		* product: Tofu, quantity: 12000, shelf: T8
-- 	- Products in Blue Springs Warehouse (1030 SE Forest Ridge Ct):
-- 		* product: Maxilaku, quantity: 50000, shelf: B5
-- 		* product: Ipoh Coffee, quantity: 35000, shelf: C9
-- 	- Products in Eldon Warehouse (800 W Champain St):
-- 		* product: Sun-Dried Tomatoes, quantity: 95000, shelf: A1
-- 		* product: Almond Milk, quantity: 15000, shelf: Q7
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 4 | Springfield office moves to a new address in Springfield. Do the following changes:
-- 	- address: 1500 Knotts St
-- 	- postalcode: 62703
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 5 | Manager of Kansas City office has left the company and Laura Callahan will be the new manager. Do the update using subquery (tip: get the employeeid for manager column using subquery)!
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 6 | Double the quantity of Tofu and move the product to W8 shelf which has more space for the greater quantity in Liberty Warehouse.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 7 | Create a copy of the storages table. New table should be called storages_backup.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 8 | Copy the data from storages table into storages_backup table.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 9 | The lease for the warehouse in Liberty is coming to an end and the supplier plans to move the products to a larger warehouse in Eldon (Do this same update into the storages_backup table too!). Transfer the Liberty warehouse products to Eldon and remove the Liberty warehouse from the warehouses table.
-- --------------------------------------------------

-- --------------------------------------------------

##################################################
-- 10 | Remove all products from storages table with 0 as a quantity value.
-- --------------------------------------------------

-- --------------------------------------------------