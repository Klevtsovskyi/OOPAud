import math


def taylor_sin(x, eps):
    s = x
    a = x
    k = 1
    while abs(a) > eps:
        k += 1
        a *= - x * x / (2 * k - 1) / (2 * k - 2)
        s += a
    return s


def taylor_cos(x, eps):
    s = 1
    a = 1
    k = 0
    while abs(a) > eps:
        k += 1
        a *= - x**2 / (2*k) / (2*k - 1)
        s += a
    return s


if __name__ == '__main__':
    x = math.pi / 6
    eps = 0.0001
    print(taylor_cos(x, eps))
    print(math.cos(x))

