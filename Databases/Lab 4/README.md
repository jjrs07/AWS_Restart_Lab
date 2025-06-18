# Lab 4: Performing a Conditional Search
In this lab, you will learn how to perform conditional searches using SQL's WHERE, BETWEEN, LIKE, and aggregate functions like SUM(). These are foundational techniques used to extract specific information from large datasets by filtering rows based on numeric or text-based conditions.

## What You'll Learn
- How to filter rows using WHERE, AND, BETWEEN, and LIKE clauses
- How to use SUM() to calculate totals based on conditions
- How to query with partial text matches using LIKE
- Case-insensitive filtering using LOWER()
- Real-world querying practices on structured data

## Prerequisites
1. Your EC2 instance with MariaDB is running and accessible.
2. Completed Lab 3

## SQL Query Exercises
Run the following SQL Queries one by one in the MariaDB Shell:

```sql
-- View all records in the country table
SELECT * FROM world.country;

-- Get countries with a population between 50M and 100M using AND
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE Population >= 50000000 AND Population <= 100000000;

-- Same as above, but using BETWEEN for readability
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE Population BETWEEN 50000000 AND 100000000;

-- Sum of population for regions containing the word "Europe"
SELECT sum(Population) 
FROM world.country 
WHERE Region LIKE "%Europe%";

-- Same as above, but with a column alias for clarity
SELECT sum(Population) AS "Europe Population Total" 
FROM world.country 
WHERE Region LIKE "%Europe%";

-- List countries with "central" in the region name (case-insensitive match)
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE LOWER(Region) LIKE "%central%";

```
---
## Challenge
Write an SQL query to return the sum of the surface area and sum of the population of North America.

