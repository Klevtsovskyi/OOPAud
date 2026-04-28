def A(n):
    a1 = 0
    a2 = 1
    b1 = 1
    b2 = 1
    p = 2
    s = 0
    for k in range(1, n + 1):
        s = s + p / (a1 + b1)
        p *= 2
        b3 = b2 + a2
        a3 = a2 / (k + 2) + a1 * b3
        a1 = a2
        a2 = a3
        b1 = b2
        b2 = b3
    return s


if __name__ == '__main__':
    print(A(10))
