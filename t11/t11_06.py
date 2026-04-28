def det(n):
    a1 = 2
    a2 = 1
    for _ in range(n - 1):
        a3 = 2 * a2 - 3 * a1
        a1 = a2
        a2 = a3
    return a1


if __name__ == '__main__':
    print(det(10))