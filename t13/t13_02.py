def read_numbers(filename):
    f = open(filename)
    numbers = []
    for line in f:
        numbers += [float(x) for x in line.split()]
    f.close()
    return numbers


def a(filename):
    """a) сума компонент файла;"""
    numbers = read_numbers(filename)
    return sum(numbers)


def d(filename):
    """d) найбільший із значень компонент файла;"""
    numbers = read_numbers(filename)
    return max(numbers)


filename = "numbers.txt"
print(a(filename))
print(d(filename))
