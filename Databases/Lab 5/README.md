# Lab 5: Working with Functions
In this lab, you will explore built-in MySQL functions that allow you to manipulate, analyze, and transform data. You’ll use aggregate functions like SUM() and AVG(), and string functions like SUBSTRING_INDEX() and LENGTH() to answer practical questions about your dataset.

---
## What You'll Learn
- How to use aggregate functions like SUM(), AVG(), MAX(), MIN(), and COUNT()
- How to apply string functions to extract or transform column values
- How to filter rows using string length and trimming
- How to use DISTINCT to eliminate duplicate values in query results

---
## Prerequisites
1. Your EC2 instance with MariaDB is running and accessible.
2. Completed Lab 4

## SQL Query Exercises
Run the following SQL Queries one by one in the MariaDB Shell:

```sql
-- Show all available databases
SHOW DATABASES;

-- Display all records from the world.country table
SELECT * FROM world.country;

-- Calculate total, average, max, min, and count of population values
SELECT 
    SUM(Population), 
    AVG(Population), 
    MAX(Population), 
    MIN(Population), 
    COUNT(Population) 
FROM world.country;

-- Extract the first word from the Region column (e.g., 'Southern' from 'Southern Europe')
SELECT Region, SUBSTRING_INDEX(Region, " ", 1) 
FROM world.country;

-- Display countries from regions where the first word in the Region column is 'Southern'
SELECT Name, Region 
FROM world.country 
WHERE SUBSTRING_INDEX(Region, " ", 1) = "Southern";

-- Show region names where the trimmed region name length is less than 10 characters
SELECT Region 
FROM world.country 
WHERE LENGTH(TRIM(Region)) < 10;

-- Show only unique region names where length is less than 10 characters
SELECT DISTINCT(Region) 
FROM world.country 
WHERE LENGTH(TRIM(Region)) < 10;
```

## Challenge
Write a query to return rows that have Micronesian/Caribbean as the name in the region column. The output should split the region as Micronesia and Caribbean into two separate columns: one named Region Name 1 and one named Region Name 2.