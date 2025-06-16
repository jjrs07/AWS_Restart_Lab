# Import necessary libraries
# Run these codes in the termnial

import os
import subprocess

# Exercise 1 
print("Exercise 1 - Using os.system to run a command")
os.system("ls")

# Exercise 2 
print("Exercise 2 - Using subprocess.run to run a command")
subprocess.run(["ls"])

# Exercise 3
print("Exercise 3 - Using subprocess.run with two arguments")
subprocess.run(["ls","-l"])

# Exercise 4
print("Exercise 4: Using subprocess.run with three arguments")
subprocess.run(["ls","-l","README.md"])

# Exercise 5
print("Exercise 5: Retrieving system information about the operating system")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Exercise 6
print("Exercise 6: Retrieving system information about a disk space")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])