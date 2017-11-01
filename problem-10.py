"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

n = 2000000
ns = [True] * n
s = 0

ns[0] = False
ns[1] = False

for i in range(2, int(math.sqrt(n) + 1)):
    if ns[i]:
        pointer = i + i
        while pointer < n:
            ns[pointer] = False
            pointer += i

for i in range(0, n):
    if ns[i]:
        s += i

print(s)
