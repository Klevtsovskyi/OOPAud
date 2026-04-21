def a(n):
    p = 2
    for i in range(2,n+1):
        p = (1 + 1/i**2)*p
    return p

if __name__ == '__main__':
    print(a(2))