def to_binary(n):
    res = 0
    p = 1
    while n > 0:
        d = n % 2
        n = n // 2
        res += d * p
        p *= 10
    return res


def to_decimal(b):
    res = 0
    p = 1
    while b > 0:
        d = b % 10
        b = b // 10
        res += d * p
        p *= 2
    return res


if __name__ == '__main__':
    A = int(input())
    B = int(input())

    C = to_binary(to_decimal(A) + to_decimal(B))
    print(C)
