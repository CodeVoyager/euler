"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def even_fib():
    prev = 0
    curr = 1
    while True:
        curr, prev = prev + curr, curr
        if curr % 2 == 0:
            yield curr

def fib_sum(treshold):
    s = 0
    for i in even_fib():
        if i > treshold:
            break
        s += i
    return s

print(fib_sum(4000000))
