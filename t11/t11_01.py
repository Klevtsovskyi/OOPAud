def a(x, n):
    xk = x
    for k in range(1, n):
        print(xk)
        xk = x * k / (k + 1) * xk
    return xk


def b(x, n):
    xk = 1
    for k in range(0,n):
        print(xk)
        xk = -(x**2 * xk) / ((2*k+1) * (2*k+2))
    return xk


if __name__ == '__main__':
    print(b(2, 10))
