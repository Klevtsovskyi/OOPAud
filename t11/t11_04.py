def a(n):
    f = 1
    for _ in range(n - 1):
        print(f)
        f = 1 + 1 / f
    return f


def b(n):
    f = 2
    for _ in range(n - 1):
        print(f)
        f = 2 + 1 / f
    return f - 1


if __name__ == '__main__':
    print(b(10))
