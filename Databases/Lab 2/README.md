# Lab 2: Inserting, Updating, and Deleting Data in MySQL

In this lab, you'll learn how to work with basic **Data Manipulation Language (DML)** operations such as **INSERT**, **UPDATE**, and **DELETE** in a MySQL database.

---
## What You'll Learn
- How to insert new records into a MySQL table using INSERT
- How to update existing records using the UPDATE statement
- How to delete records using DELETE
- How to disable foreign key checks to allow deletion in related tables
- How to import data using .sql files via the terminal
- How to verify inserted, updated, or deleted records using SELECT queries
- How to securely transfer SQL files to EC2 using scp

---

## Prerequisites
1. Make sure the **world.sql** file is available in your local machine.  
(If you haven't cloned the repositoy yet, download the file manually)
2. Your EC2 instance with MariaDB is running and accessible.
3. You have the .pem private key file to SSH into your EC2 instance.
4. Your EC2 security group allows SSH access (port 22) from your IP address.

---

## Transfer world.sql to EC2
Use SCP to upload the SQL file from your local machine to your EC2 instance.

```bash
scp -i C:\AWS\keypair.pem C:\AWS\world.sql ec2-user@< EC2-Public-IP >:/home/ec2-user/
```
Replace < EC2-Public-IP > with your actual EC2 public IP address. 

---
## Insert Data into the world.country
Note: Make sure the country table exists. If not, re-run the table creation script from Lab 1.

`mysql -u root -p < sql/insert.sql`

---

## Verify the Inserted Records
`SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');`

---

## Update Rows in the Table

```sql
-- Set population of all countries to 0
UPDATE world.country SET Population = 0;

-- Set population and surface area to 100
UPDATE world.country SET Population = 100, SurfaceArea = 100;
```

---

## Delete Records from the Table
Temporarily disable foreign key checks:

```sql
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM world.country;
```

## Verify deletion:

```sql
SELECT * FROM world.country;
```

---

### Import Data Using an SQL File

If you have a `world.sql`, you can import it by running:

```bash
mysql -u root --password='yourpassword' < /home/ec2-user/world.sql
```

After import, log in to MySQL and verify:

```sql
SELECT * FROM world.country;
```

---

## Summary Table

| Operation | Command Example |
|-----------|------------------|
| Insert    | `INSERT INTO world.country ...` |
| Update    | `UPDATE world.country SET ...` |
| Delete    | `DELETE FROM world.country` |
| Import    | `mysql -u root --password=... < file.sql` |

---

> 💡 Tip: Always make a backup before mass updating or deleting rows.