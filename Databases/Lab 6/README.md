# Lab 6: Organizing Data
In this lab, you will explore ways to group, aggregate, and rank data in SQL using clauses like GROUP BY, and advanced features such as window functions (OVER, PARTITION BY, and RANK()). This is useful for performing regional comparisons, cumulative totals, and ranking records within a group.

---

## What You'll Learn
- How to sort and filter data using ORDER BY
- How to use GROUP BY to summarize data by category
- How to calculate running totals using window functions
- How to assign rankings to rows within a group using RANK()
- How to combine PARTITION BY with window functions for per-group analysis

---
## Prerequisites
1. Your EC2 instance with MariaDB is running and accessible.
2. Completed Lab 5

---
## SQL Query Execises
Run the following SQL Queries one by one in the MariaDB Shell:

```sql
-- Show all available databases
SHOW DATABASES;

-- Display all records from the world.country table
SELECT * FROM world.country;

-- List countries in the 'Australia and New Zealand' region, sorted by population (largest to smallest)
SELECT Region, Name, Population 
FROM world.country 
WHERE Region = 'Australia and New Zealand' 
ORDER BY Population DESC;

-- Show total population for the region 'Australia and New Zealand' using GROUP BY
SELECT Region, SUM(Population) 
FROM world.country 
WHERE Region = 'Australia and New Zealand' 
GROUP BY Region 
ORDER BY SUM(Population) DESC;

-- Calculate a running total of population per region using a window function
SELECT 
    Region, 
    Name, 
    Population, 
    SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total' 
FROM world.country 
WHERE Region = 'Australia and New Zealand';

-- Calculate running total and assign population rank per country within each region
SELECT 
    Region, 
    Name, 
    Population, 
    SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total', 
    RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS 'Ranked' 
FROM world.country 
WHERE Region = 'Australia and New Zealand';

```
---
## Challenge
Write a query to rank the countries in each region by their population from the largest to smallest.