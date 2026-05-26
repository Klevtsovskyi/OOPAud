def A(n):
    S=0
    for i in range(1, n+1):
        S = S + 1/i
        yield S

if __name__ == '__main__':
    for item in A(5):
        print(item)


