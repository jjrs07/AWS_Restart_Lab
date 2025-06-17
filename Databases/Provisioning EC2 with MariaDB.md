# Provisioning EC2 with MariaDB using User Data

This guide walks you through creating an Amazon EC2 instance with **MariaDB** pre-installed using **User Data scripts**, and how to securely access the MariaDB server from your terminal.

---

## What You'll Learn

- Launch an EC2 instance with a MariaDB setup  
- Use EC2 User Data to automate package installation  
- Connect to your EC2 via SSH  
- Access and secure your MariaDB database  

---

## Step 1: Create EC2 with User Data Script

When launching your EC2 instance (Amazon Linux 2 or Ubuntu), add the following in the **User Data** field under **Advanced Details**:

### User Data Script (Amazon Linux 2)

```bash
#!/bin/bash
yum update -y
amazon-linux-extras install -y mariadb10.5
yum install -y mariadb-server
systemctl start mariadb
systemctl enable mariadb
```

### User Data Script (Ubuntu)

```bash
#!/bin/bash
apt update -y
apt install -y mariadb-server
systemctl start mariadb
systemctl enable mariadb
```

### Make sure to:
Select a security group that allows inbound SSH (port 22) access
Use a key pair for later SSH login

## Step 2: Connect to EC2 via SSH
Once the instance is running:

`ssh -i your-key.pem ec2-user@<EC2-Public-IP>`   # Amazon Linux

### or

`ssh -i your-key.pem ubuntu@<EC2-Public-IP>`     # Ubuntu

Replace your-key.pem with your actual key pair and `<EC2-Public-IP>` with your instance’s public IP address.

## Step 3: Access MariaDB on the EC2
Once connected via SSH:

```bash
sudo systemctl status mariadb   # Check if MariaDB is running
sudo mysql                      # Access the MariaDB shell
```
You can now run standard SQL commands, and proceed to the labs for detailed instructions

```sql
SHOW DATABASES;
CREATE DATABASE testdb;
```

🔒 Optional: Secure Your MariaDB Installation
```sql
sudo mysql_secure_installation
```

This will let you:  
Set a root password  
Remove anonymous users  
Disallow root remote login
Remove test databases

## Summary
| Step | Description                     |
|------|---------------------------------|
| 1    | Launch EC2 with User Data       |
| 2    | Connect using SSH               |
| 3    | Access MariaDB with `sudo mysql` |
| 4    | (Optional) Secure MariaDB setup |
