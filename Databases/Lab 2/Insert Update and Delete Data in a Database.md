# Insert data into a table

`SELECT * FROM world.country`

```sql
--Insert 2 data in the world.country table
INSERT INTO world.country VALUES ('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Eire','Republic',NULL,1447,'IE');

INSERT INTO world.country VALUES ('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.
00,392911.00,'Australia','Constitutional Monarchy, Federation',NULL,135,'AU');

--Verify if the 2 rows are inserted
SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');

--Update rows in a table
UPDATE world.country SET Population = 0;
UPDATE world.country SET Population = 100, SurfaceArea = 100;


--Delete rows from a table
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM world.country;

SELECT * FROM world.country
```

## Import data using an SQL file

Go to the path where the world.sql file is located

Ex. /home/ec2-user/

Run this command below to insert data to the Country table

`mysql -u root --password= 'yourpassword' < /home/world.sql

Connect to MySQL database and verify if the data was inserted.



