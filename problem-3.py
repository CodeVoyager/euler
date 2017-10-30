"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

n = 600851475143

while n % 2 == 0:
    n /= 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        n /= i
    if n == 1:
        break

print(i)