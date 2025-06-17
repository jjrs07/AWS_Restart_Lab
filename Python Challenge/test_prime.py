n = 36
# Line 4 of thee prime.py code
# n**0.5 is to get the square root of n
# range(2, int(n**0.5) + 1) generates numbers from 2 to the square root of n
# example for n = 37, it generates numbers from 2 to 6 (inclusive)
for i in range(2, int(n**0.5) + 1):
    print(f"Checking if {n} is divisible by {i}: {n % i == 0}")
