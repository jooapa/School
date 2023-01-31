
    CREATE TABLE creates a new table.
    INSERT INTO adds a new row to a table.
    SELECT queries data from a table.
    ALTER TABLE changes an existing table.
    UPDATE edits a row in a table.
    DELETE FROM deletes rows from a table.

    
    SELECT is the clause we use every time we want to query information from a database.
    AS renames a column or table.
    DISTINCT return unique values.
    WHERE is a popular command that lets you filter the results of the query based on conditions that you specify.
    LIKE and BETWEEN are special operators.
    AND and OR combines multiple conditions.
    ORDER BY sorts the result.
    LIMIT specifies the maximum number of rows that the query will return.
    CASE creates different outputs.
        END AS 'name'  to change name

        
    COUNT(): count the number of rows
    SUM(): the sum of the values in a column
    MAX()/MIN(): the largest/smallest value
    AVG(): the average of the values in a column
    ROUND(): round the values in the column
    HAVING limit the results of a query based on an aggregate property.

    

    JOIN will combine rows from different tables if the join condition is true.

    LEFT JOIN will return every row in the left table, and if the join condition is not met, NULL values are used to fill in the columns from the right table.

    Primary key is a column that serves a unique identifier for the rows in the table.

    Foreign key is a column that contains the primary key to another table.

    CROSS JOIN lets us combine all rows of one table with all rows of another table.

    UNION stacks one dataset on top of another.

    WITH allows us to define one or more temporary tables that can be used in the final query.





SELECT * FROM asiakastaulu
JOIN tilaustaulu
ON asiakastaulu.id = tilaustaulu.asiakas_id


SELECT * FROM `asiakastaulu`

JOIN tilaustaulu
ON asiakastaulu.id = tilaustaulu.asiakas_id
JOIN tilausrivitaulu
ON tilaustaulu.asiakas_id = tilausrivitaulu.tilaus_id
JOIN tuotetaulu
ON tuotetaulu.id = tilausrivitaulu.tuote_id
WHERE tilausrivitaulu.tilausmaara * tuotetaulu.hinta;





SELECT IF(tilausrivitaulu.tilausmaara * tuotetaulu.hinta > 80 ,asiakastaulu.etunimi, Null),asiakastaulu.email
FROM `asiakastaulu`
JOIN tilaustaulu
ON asiakastaulu.id = tilaustaulu.asiakas_id
JOIN tilausrivitaulu
ON tilaustaulu.id = tilausrivitaulu.tilaus_id
JOIN tuotetaulu
ON tuotetaulu.id = tilausrivitaulu.tuote_id
GROUP BY etunimi;
//____________________________________________________________
"SELECT asiakastaulu.etunimi, asiakastaulu.email,
CASE WHEN tilausrivitaulu.tilausmaara * tuotetaulu.hinta > $tetu THEN '|| Yli $tetu' ELSE NULL END AS 'kokoHinta'
FROM `asiakastaulu`
JOIN tilaustaulu
ON asiakastaulu.id = tilaustaulu.asiakas_id
JOIN tilausrivitaulu
ON tilaustaulu.id = tilausrivitaulu.tilaus_id
JOIN tuotetaulu
ON tuotetaulu.id = tilausrivitaulu.tuote_id
GROUP BY etunimi;"