"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# pylint: disable=C0103

import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

primes_counter = 2
last_prime = 3
nth_prime_to_find = 10001
n = 3

while primes_counter < nth_prime_to_find:
    n += 2
    if is_prime(n):
        primes_counter += 1
        last_prime = n

print(last_prime)