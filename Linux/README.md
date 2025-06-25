# Linux Command Line Practice Lab

Welcome to the Linux CLI Practice Lab!  
This guide will help you set up a virtual Linux environment so you can safely explore and practice essential command line skills.

---

## Option 1: Launch an EC2 Instance on AWS

### Step-by-Step Instructions

1. **Log in to your AWS Console**
   - Go to: https://console.aws.amazon.com/

2. **Navigate to EC2**
   - From the Services menu, select **EC2**.

3. **Launch a new instance**
   - Click **Launch Instance**

4. **Configure Instance Details**
   - **Name:** `linux-cli-practice`
   - **Amazon Machine Image (AMI):**
     - Amazon Linux 2 *(recommended for AWS familiarity)*
     - Amazon Linux 2023 *(more up-to-date, stable OS)*
     - Ubuntu 22.04 *(if you're more comfortable with Ubuntu-based distros)*

5. **Instance Type:** `t2.micro or t3.micro` (Free Tier eligible)

6. **Key Pair:**
   - Create or select an existing key pair
   - Download the `.pem` file and keep it safe

7. **Network Settings:**
   - Allow SSH (port 22) from your IP only

8. **Launch the instance**

9. **Connect via SSH**
   ```bash
   chmod 400 your-key.pem
   ssh -i your-key.pem ec2-user@<your-public-ip>      # For Amazon Linux
   ssh -i your-key.pem ubuntu@<your-public-ip>        # For Ubuntu

## Option 2: Here are some ways to run a Linux environment on your local machine:

1. **Install Ubuntu VM using VirtualBox (Windows/macOS/Linux)**  
   - Download and install VirtualBox
   - Download Ubuntu ISO: https://ubuntu.com/download/desktop
   - Create a new VM → Attach ISO → Start → Install Ubuntu

   Open Terminal and start practicing!

2. **Use WSL on Windows (Windows Subsystem for Linux)**  
   - Open PowerShell as Admin and run:
     ```powershell
        wsl --install
      ```
   - Restart your PC when prompted
   - Open Ubuntu from Start Menu and begin using Linux commands

  More info: https://learn.microsoft.com/en-us/windows/wsl/

3. **Use Docker (for advance users)**  
    If you already have Docker Desktop installed:

    ```bash
      docker container run -it amazonlinux:2 /bin/bash     # For Amazon Linux 2
      docker container run -it ubuntu /bin/bash            # For Ubuntu
    ```
    You’ll get an isolated Linux shell instantly.


## Notes
- Don’t forget to terminate your EC2 instance when done to avoid charges.
- Some commands may vary slightly between Amazon Linux and Ubuntu.
- For repeat practice, try creating sample files and directories to manage.