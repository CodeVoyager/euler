"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Brute force
"""

a = 0
b = 0
c = 0
s = 1000
result = ()
found = False

for a in range(1, s // 3):
    for b in range(a, s // 2):
        c = s - a - b
        if a ** 2 + b ** 2 == c ** 2:
            result = (a, b, c)
            found = True
            break
    if found:
        break

print(result, result[0] * result[1] * result[2])