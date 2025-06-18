# Lab: Inserting, Updating, and Deleting Data in MySQL

In this lab, you'll learn how to work with basic **Data Manipulation Language (DML)** operations such as **INSERT**, **UPDATE**, and **DELETE** in a MySQL database.

# Prerequisites
1. Download the world.sql file to your local if you haven't clone the repositoy.
2. Make sure that your EC2 instance is running and accessible
3. You have the .pem private key file for your EC2 instance.
4. Your security group allows SSH (port 22) from you IP.

Use SCP to import file from your local desktop/laptop to EC2 instance

### Command Example
scp -i C:\AWS\keypair.pem C:\AWS\world.sql ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com:/home/ec2-user/

### Insert Data into the world.country Table
NOTE: Ensure that the country table exist, if now run again the create table country script from Lab 1.

`mysql -u root -p < sql/insert.sql`

### Verify the Inserted Records
`SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');`


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