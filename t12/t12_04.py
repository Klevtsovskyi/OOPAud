def scrt(x, eps):
    x1=x/2
    x0=0
    while abs(x0-x1)>eps:
        x2=0.5*(x1+x/x1)
        x0=x1
        x1=x2
    return x1


def sqrt(x, eps):
    x1=x/2
    while abs(x1**2 - x)>eps:
        x1=0.5*(x1+x/x1)
    return x1


if __name__ == '__main__':
    x=5
    eps=0.01
    print (scrt(x, eps))
    print (sqrt(x, eps))
    print(x**0.5)
