# Lab: Inserting, Updating, and Deleting Data in MySQL

In this lab, you'll learn how to work with basic **Data Manipulation Language (DML)** operations such as **INSERT**, **UPDATE**, and **DELETE** in a MySQL database.

# Prerequisites
1. Download the world.sql file to your local if you haven't clone the repositoy.
2. Make sure that your EC2 instance is running and accessible
3. You have the .pem private key file for your EC2 instance.
4. Your security group allows SSH (port 22) from you IP.

scp -i path\to\your-key.pem C:\path\to\localfile.txt ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com:/home/ec2-user/


With only the command prompt (CLI) and minimal setup, the most straightforward way to import a file from your local laptop to an EC2 instance is using **SCP** (Secure Copy Protocol). Here’s how:

### Prerequisites
- Your EC2 instance is running and accessible.
- You have the `.pem` private key file for your EC2 instance.
- Your security group allows SSH (port 22) from your IP.

### Command Example

```bash
scp -i path\to\your-key.pem C:\path\to\localfile.txt ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com:/home/ec2-user/
```

Replace:
- `path\to\your-key.pem` with your private key file path
- `C:\path\to\localfile.txt` with your local file path
- `ec2-user` with the correct username (e.g., `ubuntu` for Ubuntu)
- `ec2-xx-xx-xx-xx.compute-1.amazonaws.com` with your EC2 public DNS

---
Summary:  
- Use `scp` for minimal setup and direct transfer.
- No extra software or AWS CLI configuration is required.

---

## 🗂️ What You'll Learn

✅ How to insert records into a table  
✅ How to update existing data  
✅ How to delete rows safely  
✅ How to verify changes with `SELECT`  
✅ How to import data from an `.sql` file

---

## 🔧 Step-by-Step Instructions

### 1. 🚀 Insert Data into the `world.country` Table

Log in to MySQL and run:

```sql
SELECT * FROM world.country;
```

Insert the following two records:

```sql
INSERT INTO world.country VALUES 
('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Eire','Republic',NULL,1447,'IE');

INSERT INTO world.country VALUES 
('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',NULL,135,'AU');
```

### 2. ✅ Verify the Inserted Records

```sql
SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');
```

---

### 3. 📝 Update Rows in the Table

```sql
-- Set population of all countries to 0
UPDATE world.country SET Population = 0;

-- Set population and surface area to 100
UPDATE world.country SET Population = 100, SurfaceArea = 100;
```

---

### 4. 🗑️ Delete Rows from the Table

Temporarily disable foreign key checks:

```sql
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM world.country;
```

Verify deletion:

```sql
SELECT * FROM world.country;
```

---

### 5. 📂 Import Data Using an SQL File

If you have a file like `world.sql`, you can import it by running:

```bash
mysql -u root --password='yourpassword' < /home/ec2-user/world.sql
```

After import, log in to MySQL and verify:

```sql
SELECT * FROM world.country;
```

---

## 📌 Summary Table

| Operation | Command Example |
|-----------|------------------|
| Insert    | `INSERT INTO world.country ...` |
| Update    | `UPDATE world.country SET ...` |
| Delete    | `DELETE FROM world.country` |
| Import    | `mysql -u root --password=... < file.sql` |

---

> 💡 Tip: Always make a backup before mass updating or deleting rows.