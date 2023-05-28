"""
5! = 5 * 4 * 3 * 2 * 1 = 120
4! = 4 * 3 * 2 * 1 = 24
"""

def factorial(n):
    if n == 1:
        return 1
    m = factorial(n -1)
    return n * m

print(factorial(4))