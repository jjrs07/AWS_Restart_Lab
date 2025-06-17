## Database Table Operations

To run each part of this lab, use the corresponding SQL files in the `/sql` folder.

### Show existing Database
`SHOW DATABASES;`

### Create World Database 
`CREATE DATABASE world;`

### Create Table country
`mysql -u root -p < sql/create_world.sql`

### Modify Schema
`mysql -u root -p world < sql/modify_world.sql`

### Challenge 1 – Create/Delete city Table
`mysql -u root -p world < sql/challenge1_city.sql`

### Challenge 2 – Drop country Table Database
`mysql -u root -p < sql/challenge2_drop.sql`

NOTE: You can also open these SQL files inside a MySQL client or GUI like DBeaver, MySQL Workbench, or phpMyAdmin for step-by-step execution.