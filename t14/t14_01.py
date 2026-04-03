"""
14.1. Знайти площу трикутника за трьома сторонами 𝑎,𝑏,𝑐. Оформити
перевірку вхідних даних (що трикутник з такими сторонами 𝑎,𝑏,𝑐
існує) за допомогою оператора assert.
"""

def square(a, b, c):
    assert a + b > c and a + c > b and b + c > a, "Такий трикутник не існує!"

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


if __name__ == '__main__':
    a, b, c = [int(x) for x in input().split()]
    print(square(a, b, c))
