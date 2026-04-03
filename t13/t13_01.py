def a(filename):
    """a) виведення усіх рядків файла;"""
    f = open(filename)
    for line in f:
        print(line, end="")
    f.close()


def b(filename, size=60):
    """b) виведення рядків, які містять більше 60 символів;"""
    with open("input.txt") as f:
        for line in f:
            if len(line) > size:
                print(len(line), line, end="")

def c(filename):
    """c) підрахунку кількості порожніх рядків;"""
    count = 0
    f = open(filename)
    while True:
        line = f.readline()
        if line == "\n":
            count += 1
        # print(line, end="")
        if line == "":
            break
    f.close()
    print(count)


def d(filename):
    """d) пошуку найдовшого рядка;"""
    max_line = ""
    max_size = 0
    f = open(filename)
    for line in f:
        if len(line) > max_size:
            max_size = len(line)
            max_line = line
    f.close()
    print(max_line)


filename = "input.txt"
# a(filename)
# b(filename, 40)
# c(filename)
d(filename)
