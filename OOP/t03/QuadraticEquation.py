from Equation import Equation


class QuadraticEquation(Equation):

    def __init__(self, a: float, b: float, c:float):
        super().__init__(b, c)
        self._a = a

    def __str__(self):
        return f"{self._a} x^2 + {super().__str__()}"

    def solve(self) -> set[float] | float:
        if self._a == 0:
            return super().solve()
        else:
            d = self._b ** 2 - 4 * self._a * self._c
            if d < 0:
                return set()
            elif d == 0:
                return {-self._b / (2 * self._a)}
            else:
                return {
                    (-self._b - d ** 0.5) / (2 * self._a),
                    (-self._b + d ** 0.5) / (2 * self._a)
                }


if __name__ == '__main__':
    eq = QuadraticEquation(1, -4, 2)
    eq.show()
    print(eq.solve())
