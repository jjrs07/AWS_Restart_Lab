## Database Table Operations

To run each part of this lab, use the corresponding SQL files in the `/sql` (example folder) folder.

# Prerequisites
1. Ensure that you already provisioned an EC2 instance with Maria DB installed.
2. Create SQL files in your EC2 example `touch create_world.sql`
3. Copy the content of the create_world.sql on GitHub to the created file in Linux.
4. Do the same in othere SQL files
5. Login to MySQL database and execute the commands below.

### Show existing Database
`SHOW DATABASES;`

### Create World Database 
`CREATE DATABASE world;`

### Create Table country
`mysql -u root -p < sql/create_world.sql`

### Verify Columns in the Country Table
`SHOW COLUMNS from country`

### Modify Schema
`mysql -u root -p world < sql/modify_world.sql`

### Challenge 1 – Create city Table
`mysql -u root -p world < sql/challenge1_city.sql`

### Verify if the City Table is created
`SHOW TABLES;`

### Challenge 2 – Drop country Table Database
`mysql -u root -p < sql/challenge2_drop.sql`

NOTE: You can also open these SQL files inside a MySQL client or GUI like DBeaver, MySQL Workbench, or phpMyAdmin for step-by-step execution.