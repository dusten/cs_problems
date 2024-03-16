#!/usr/bin/python3

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Invalid input! Please enter a positive number.")
    else:
        factors = prime_factors(number)
        print(f"The prime factors of {number} are: {factors}")
