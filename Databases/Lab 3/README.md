# Lab 3: Selecting Data from a Database
In this lab, you'll practice running basic SELECT queries to retrieve data from a MySQL/MariaDB database. You'll use filtering, sorting, column aliases, and aggregate functions to explore the world.country table.

---

## Prerequisites
1. Your EC2 instance with MariaDB is running and accessible.
2. Completed Lab 2

---

## SQL Query Exercises
Run the following SQL Queries one by one in the MariaDB Shell:

```sql
-- Show all available databases
SHOW DATABASES;

-- Select all columns from the country table
SELECT * FROM world.country;

-- Count the number of rows (countries) in the table
SELECT COUNT(*) FROM world.country;

-- Show the columns (schema) of the country table
SHOW COLUMNS FROM world.country;

-- Select specific columns: name, capital, region, surface area, and population
SELECT Name, Capital, Region, SurfaceArea, Population
FROM world.country;

-- Select the same columns but rename SurfaceArea as "Surface Area"
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country;

-- Select and order records by population in ascending order
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
ORDER BY Population;

-- Select and order records by population in descending order (largest first)
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
ORDER BY Population DESC;

-- Filter and show only countries with population greater than 50 million, ordered by population descending
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Population > 50000000 
ORDER BY Population DESC;

-- Filter and show only countries with population between 50 million and 100 million, ordered by population descending
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Population > 50000000 AND Population < 100000000 
ORDER BY Population DESC;

```
