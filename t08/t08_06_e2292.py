import sys

sys.setrecursionlimit(100001)

fibs = [0, 1, 1]


def fib(n):
    if n < len(fibs):
        return fibs[n]

    f = fib(n - 1) + fib(n - 2)
    fibs.append(f)
    return f


n = int(input())
for _ in range(n):
    m = int(input())
    print(fib(m))

# print(fibs)
