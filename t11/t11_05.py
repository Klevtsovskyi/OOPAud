def f(n):
    t0 = 0
    t1 = 0
    t2 = 1
    for _ in range(n):
        t3 = t2 + t1 + t0
        t0 = t1
        t1 = t2
        t2 = t3
    return t0


if __name__ == '__main__':
    print(f(10))
