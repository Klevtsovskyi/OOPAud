class Equation:

    INF = float("inf")

    def __init__(self, b: float, c: float):
        self._b = b
        self._c = c

    def __str__(self):
        return f"{self._b} x + {self._c} = 0"

    def __repr__(self):
        return str(self)

    def show(self):
        print(self)

    def solve(self) -> set[float] | float:
        if self._b == 0:
            if self._c == 0:
                return self.INF
            else:
                return set()
        else:
            return {-self._c / self._b}


if __name__ == '__main__':
    eq = Equation(-5, 3)
    eq.show()
    print(eq.solve())
    eq = Equation(0, 5)
    eq.show()
    print(eq.solve())
    eq = Equation(0, 0)
    eq.show()
    print(eq.solve())
