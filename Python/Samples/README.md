# Lab: Tools and Templates for Python Development

This guide introduces two essential tools — **Pylint** and **Pytest** — to help you write clean, reliable, and maintainable Python code. These tools assist with **code styling** and **automated testing**.

---

##  What You'll Learn

- How to use `pylint` to check and fix code formatting issues  
- How to use `pytest` to write and run logic tests  
- How to install both tools using `pip`  
- How to run them from the terminal using command-line syntax

---

## Code Style Checking with Pylint

`pylint` checks Python files for:
- Indentation and formatting errors
- Naming conventions
- Unused variables and imports
- Best practice suggestions

### To Install:
```bash
pip install pylint
```

### To Run:
```bash
pylint conditionals.py
# or
python -m pylint conditionals.py
```

## Logic Testing with Pytest

`pytest` allows you to:  
- Write test cases to validate code logic
- Ensure changes don't break existing functionality
- Automate test execution

### To Install:
`pip install pytest`

### To Run:
```bash
pytest conditionals.py
# or
python -m pytest conditionals.py
```

These tools help you build confidence in your code by catching bugs early and enforcing clean, professional formatting.

Keep testing and refining!