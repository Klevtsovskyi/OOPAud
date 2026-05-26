def product(n):
    a0 = a1 = 1
    a2 = 3
    p2 = 2
    p3 = 1
    pr = 1
    for _ in range(n + 1):
        pr *= a0/p3
        a3 = a0 + a1/p2
        p2 *= 2
        p3 *= 3
        a0 = a1
        a1 = a2
        a2 = a3
        yield pr

if __name__ == '__main__':
    for item in product(5):
        print(item)




