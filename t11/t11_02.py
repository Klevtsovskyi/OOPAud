def a(n):
    s = 0
    for k in range(1, n+1):
        print(s)
        s = s + k
    return s


def b(n):
    s=1
    a=1
    for k in range(2,n+1):
        a=((1-k)/k)*a
        s=s+a
    return s


if __name__ == '__main__':
    print(b(2))
