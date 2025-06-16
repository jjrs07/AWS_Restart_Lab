def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find prime numbers between 1 and 250
primes = [str(num) for num in range(1, 251) if is_prime(num)]

# Write to results.txt
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    file.write(", ".join(primes))

print("Done! Prime numbers saved to results.txt.")
