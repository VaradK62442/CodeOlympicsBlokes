from math import floor

# n = input()
# s = input()

def f(b, n):
    if n < b:
        return n
    return f(b, floor(n/b)) + (n % b)

def find_b(n, s):
    found = False
    b = 2
    while b <= n:
        print(b)
        if s == f(b, n):
            return b
        b += 1
    return -1

print(find_b(100000000000, 1))