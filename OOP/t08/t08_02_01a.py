def generate(x, n):
    a = 1
    for i in range(1, n + 1):
        yield a
        a *= x / i

if __name__ == '__main__':
    for item in generate(3, 10):
        print(item)
