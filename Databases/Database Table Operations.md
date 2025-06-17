# Database Table Operations
## Connect to the database

`mysql -u root --password`

`mysql> show databases;`

```sql
--Create database
CREATE DATABASE world;

--Verify world database is created
SHOW DATABASES;

--Create table
CREATE TABLE world.country (
  `Code` CHAR(3) NOT NULL DEFAULT '',
  `Name` CHAR(52) NOT NULL DEFAULT '',
  `Conitinent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South  America') NOT NULL DEFAULT 'Asia',
  `Region` CHAR(26) NOT NULL DEFAULT '',
  `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` SMALLINT(6) DEFAULT NULL,
  `Population` INT(11) NOT NULL DEFAULT '0',
  `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
  `GNP` FLOAT(10,2) DEFAULT NULL,
  `GNPOld` FLOAT(10,2) DEFAULT NULL,
  `LocalName` CHAR(45) NOT NULL DEFAULT '',
  `GovernmentForm` CHAR(45) NOT NULL DEFAULT '',
  `HeadOfState` CHAR(60) DEFAULT NULL,
  `Capital` INT(11) DEFAULT NULL,
  `Code2` CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
);

--Connect to world database
USE world;

--List available tables
SHOW TABLES;

--List all the columns on a table
SHOW COLUMNS FROM world.country;

--Alter the table' schema
ALTER TABLE world.country
RENAME COLUMN Conitinent TO Continent;

--Verify Changes
SHOW COLUMNS FROM world.country;
```

## Challenge 1
Create a table named city and add two columns named Name and Region. Both columns should use the CHAR data type.

```sql
CREATE TABLE world.city 
(
 Name CHAR(52), 
 Region CHAR(26));
```

Delete a database and tables

`DROP TABLE world.city;

## Challenge 2
Write a query to drop the country table

```sql
SHOW TABLES;

DROP DATABASE world;

SHOW DATABASES;
```