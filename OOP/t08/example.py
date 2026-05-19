import random


def generate(a, b):
    while True:
        yield random.random() * (b - a) + a


if __name__ == '__main__':
    random.seed(42)
    i = 0
    for item in generate(10, 100):
        print(item)
        i += 1
        if i > 10:
            break
