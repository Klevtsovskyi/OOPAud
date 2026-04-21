def a(n):
    f = 1
    for _ in range(n - 1):
        print(f)
        f = 1 + 1 / f
    return f


if __name__ == '__main__':
    print(a(10))
