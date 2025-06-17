# Prime Number Generator: 1 to 250

This Python script checks for **prime numbers** between 1 and 250 using a custom function and writes the results to a text file.

It demonstrates the use of **functions**, **loops**, **conditionals**, **list comprehensions**, and **file handling** — all essential skills for any Python beginner.

---

## What You'll Learn

- How to define and use a function (`is_prime()`)  
- How to check if a number is **prime** using square root optimization  
- How to filter values using **list comprehension**  
- How to write data to a text file (`results.txt`)  
- How to apply algorithmic thinking in real-world tasks

---

## How It Works

1. The `is_prime(n)` function checks whether a number is prime:
   - Returns `False` if `n <= 1`
   - Loops through all numbers from `2` to `√n` using:
     ```python
     for i in range(2, int(n**0.5) + 1)
     ```
   - If `n` is divisible by any of those values (`n % i == 0`), it is **not a prime**

2. All primes between 1 and 250 are collected into a list using:
   ```python
   primes = [str(num) for num in range(1, 251) if is_prime(num)]

3. The result is saved to results.txt using Python file handling.

## Why Square Root?
Instead of checking every number up to n-1, the function only checks up to the square root of n, which is much faster.

Example:  
```python
n = 36  
for i in range(2, int(n**0.5) + 1):
    print(f"Checking if {n} is divisible by {i}: {n % i == 0}")
```
For n = 36, the range is 2 to 6.  
If none of those divide n, it's prime (though 36 is not).  
This technique drastically reduces the number of checks, especially for large numbers.

## Output File: results.txt
Prime numbers between 1 and 250:
2, 3, 5, 7, 11, 13, 17, ..., 241

## Sample Console Output
Done! Prime numbers saved to results.txt.

## Extension Ideas
- Add user input to define a custom range
- Count how many primes were found
- Export results as JSON or CSV for analysis
- Visualize primes using charts

