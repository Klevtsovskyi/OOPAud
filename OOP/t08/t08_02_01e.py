import math


def generate(x, eps):
    a = 1
    s = 1
    i = 1
    while abs(a) > eps:
        yield s
        a *= x / i
        s += a
        i += 1

if __name__ == '__main__':
    for item in generate(2, 0.1):
        print(item)

    print()
    print(math.e**2)

