"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math

def is_palindrome(n):
    _n = str(n)
    _len = len(_n)
    for i in range(0, math.ceil(_len / 2)):
        if _n[i] != _n[_len - 1 - i]:
            return False
    return True

n = 0
a = 999

for i in range(a, a - 100, -1):
    for j in range(a, a - 100, -1):
        if is_palindrome(i * j) and i * j > n:
            n = i * j
print(n)