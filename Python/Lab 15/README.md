# Lab: Running Terminal Commands with `os` and `subprocess` in Python

This lab introduces you to **executing shell/terminal commands** from Python using the `os` and `subprocess` modules. You'll run common Linux commands, retrieve system info, and learn the difference between `os.system()` and `subprocess.run()`.

It's a great hands-on intro to **automation**, **DevOps scripting**, and **system administration** using Python!

---

## What You'll Learn

- How to execute terminal commands from Python  
- The difference between `os.system()` and `subprocess.run()`  
- How to pass arguments to system commands (e.g., `ls -l`)  
- How to retrieve system-level info such as active processes and OS details  
- Why `subprocess.run()` is the preferred modern method over `os.system()`

---

## Exercises Covered

| Exercise | Topic/Command                             | Description                                      |
|----------|-------------------------------------------|--------------------------------------------------|
| 1        | `os.system("ls")`                         | Run basic shell command using `os.system()`      |
| 2        | `subprocess.run(["ls"])`                  | Same command using `subprocess.run()`            |
| 3        | `subprocess.run(["ls", "-l"])`            | Add arguments to modify command behavior         |
| 4        | `subprocess.run(["ls", "-l", "README.md"])` | Target a specific file using extended arguments |
| 5        | `subprocess.run(["uname", "-a"])`         | Display full OS and kernel information           |
| 6        | `subprocess.run(["ps", "-x"])`            | Show active processes running on the system      |

---

## Why This Matters

Many real-world automation scripts:
- Deploy applications
- Monitor systems
- Check logs or disk space
- Run backups or cloud CLI tools

All of these rely on shell commands — and Python makes them accessible, scriptable, and powerful.

---

## Notes

- These examples are for **Linux/macOS terminals**  
- On Windows, replace commands like `ls` or `uname` with `dir` or `systeminfo`  
- Always sanitize inputs in production scripts to avoid security risks (e.g., shell injection)

---

> This is your first step into Python-powered DevOps and scripting — turning your code into a tool that can control real systems.

Let the automation begin!
