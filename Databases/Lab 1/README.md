# Lab 1: Database Table Operations

This lab walks you through creating and managing database tables using SQL scripts.
Each step corresponds to a specific .sql file inside the /sql folder of your project.

---
## Prerequisites
1. You have already provisioned an EC2 instance with MariaDB installed.
2. Insite your EC2 intance, create a necessary SQL files using the touch command.  
Exampe: `touch create_world.sql`
3. Copy the contents of each SQL file from your GitHub repo into the matching file on your EC2 instance.
4. Repeat this process from the rest of the SQL files (e.g. modify_world.sql, challenge1_city.sql, etc.)

## SQL Execution Steps

### Show existing Database   
`SHOW DATABASES;`

### Create world Database   
`CREATE DATABASE world;`

### Create country Table  
`mysql -u root -p < sql/create_world.sql`

### Verify Columns in the country Table  
`SHOW COLUMNS from country`

###  Modify Schema (Rename Column)  
`mysql -u root -p world < sql/modify_world.sql`

###  Challenge 1 – Create city Table  
`mysql -u root -p world < sql/challenge1_city.sql`

### Verify if the City Table is created  
`SHOW TABLES;`

### Challenge 2 – Drop country Table Database  
`mysql -u root -p < sql/challenge2_drop.sql`

---
## Alternative Option
You can also open and execute these SQL files in a MySQL client or GUI tool such as:

- DBeaver
- MySQL Workbench
- phpMyAdmin

This allows step-by-step execution and easier syntax debugging.