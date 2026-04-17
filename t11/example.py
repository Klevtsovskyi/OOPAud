def f(n):
    """Рекурсія"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)


def ff(n):
    """Рекурентне"""
    f0 = 0
    f1 = 1
    for _ in range(n):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f0


if __name__ == '__main__':
    print(f(10))
    print(ff(10))
